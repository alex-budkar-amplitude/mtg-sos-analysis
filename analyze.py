#!/usr/bin/env python3
"""
Analyze Secrets of Strixhaven (SOS) card data.
Produces report.md with breakdowns by color and rarity.
Covers: creatures, removal, combat tricks, mana curve.
"""

import json
import os
import re
from collections import defaultdict

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
REPORT_PATH = os.path.join(os.path.dirname(__file__), "report.md")
INDEX_PATH = os.path.join(os.path.dirname(__file__), "index.md")

COLOR_NAMES = {"W": "White", "U": "Blue", "B": "Black", "R": "Red", "G": "Green"}
COLOR_SHORT = {
    "W": "W",
    "U": "U",
    "B": "B",
    "R": "R",
    "G": "G",
    "Multicolor": "MC",
    "Colorless": "NC",
}
COLOR_ORDER = ["W", "U", "B", "R", "G", "Multicolor", "Colorless"]
RARITY_ORDER = ["common", "uncommon", "rare", "mythic"]
RARITY_SHORT = {"common": "C", "uncommon": "U", "rare": "R", "mythic": "M"}
RARITY_DISPLAY = {
    "common": "Common",
    "uncommon": "Uncommon",
    "rare": "Rare",
    "mythic": "Mythic",
}

# Keywords to track on creatures
TRACKED_KEYWORDS = [
    "flying",
    "trample",
    "vigilance",
    "lifelink",
    "deathtouch",
    "first strike",
    "double strike",
    "menace",
    "reach",
    "haste",
    "ward",
    "hexproof",
    "indestructible",
    "flash",
    "defender",
]


# ── Helpers ──────────────────────────────────────────────────────────────


BASIC_LAND_NAMES = {"Plains", "Island", "Swamp", "Mountain", "Forest"}


def is_standard_basic(card):
    """Return True for the five standard basic lands (not Snow, Wastes, etc.)."""
    return card.get("name") in BASIC_LAND_NAMES and "Basic Land" in card.get(
        "type_line", ""
    )


def load_cards():
    path = os.path.join(DATA_DIR, "all_cards.json")
    with open(path) as f:
        all_cards = json.load(f)
    return [c for c in all_cards if not is_standard_basic(c)]


def card_color_bucket(card):
    """Assign card to a color bucket."""
    colors = card.get("colors", [])
    if not colors:
        # Check color_identity for lands etc.
        ci = card.get("color_identity", [])
        if not ci:
            return "Colorless"
        if len(ci) > 1:
            return "Multicolor"
        return ci[0]
    if len(colors) > 1:
        return "Multicolor"
    return colors[0]


def get_oracle_text(card):
    """Get combined oracle text, handling double-faced cards."""
    ot = card.get("oracle_text", "")
    if not ot and "card_faces" in card:
        parts = []
        for face in card["card_faces"]:
            parts.append(face.get("oracle_text", ""))
        ot = "\n".join(parts)
    return ot.lower()


def get_type_line(card):
    tl = card.get("type_line", "")
    if not tl and "card_faces" in card:
        parts = [f.get("type_line", "") for f in card["card_faces"]]
        tl = " // ".join(parts)
    return tl


def get_power_toughness(card):
    """Return (power, toughness) as floats if creature, else None."""
    p = card.get("power")
    t = card.get("toughness")
    if p is None and "card_faces" in card:
        for face in card["card_faces"]:
            if face.get("power"):
                p = face["power"]
                t = face["toughness"]
                break
    if p is None:
        return None
    try:
        return (float(p), float(t))
    except (ValueError, TypeError):
        # Handle * or X
        return None


def get_pt_display(card):
    """Return P/T as a display string like '2/3', '*/4', or '-' for non-creatures."""
    p = card.get("power")
    t = card.get("toughness")
    if p is None and "card_faces" in card:
        for face in card["card_faces"]:
            if face.get("power") is not None:
                p = face["power"]
                t = face["toughness"]
                break
    if p is None:
        return "-"
    return f"{p}/{t}"


def is_type(card, card_type):
    """Check if card has a given type (handles DFCs)."""
    tl = get_type_line(card)
    return card_type.lower() in tl.lower()


def get_cmc(card):
    return card.get("cmc", 0)


def get_scryfall_uri(card):
    """Get the Scryfall page URL (strip utm params)."""
    uri = card.get("scryfall_uri", "")
    if "?" in uri:
        uri = uri.split("?")[0]
    return uri


def get_image_url(card):
    """Get the normal-size card image URL."""
    imgs = card.get("image_uris", {})
    return imgs.get("normal", "")


def card_link(name, scryfall_uri, image_url):
    """Return HTML for a card name that links to Scryfall with hover image preview."""
    if not scryfall_uri:
        return name
    # Escape quotes in name for HTML attributes
    safe_name = name.replace('"', "&quot;")
    if image_url:
        return (
            f'<a href="{scryfall_uri}" class="card-link" target="_blank">'
            f"{name}"
            f'<span class="card-preview"><img src="{image_url}" alt="{safe_name}"></span>'
            f"</a>"
        )
    return f'<a href="{scryfall_uri}" target="_blank">{name}</a>'


# CSS + JS for hover card previews
HOVER_CSS = """\
<style>
.card-link {
  text-decoration: none;
  border-bottom: 1px dotted #888;
  color: inherit;
  white-space: nowrap;
}
.card-link:hover {
  color: #1a6baa;
}
/* Hidden inline span -- the image is positioned by JS */
.card-preview {
  display: none;
}
#card-hover-img {
  display: none;
  position: fixed;
  z-index: 10000;
  pointer-events: none;
  width: 244px;
  height: auto;
  border-radius: 10px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.4);
}
/* Dark mode adjustments */
@media (prefers-color-scheme: dark) {
  .card-link {
    border-bottom-color: #666;
  }
  .card-link:hover {
    color: #6db3f2;
  }
  #card-hover-img {
    box-shadow: 0 4px 20px rgba(0,0,0,0.7);
  }
}
</style>

<img id="card-hover-img" src="" alt="">

<script>
(function() {
  var img = document.getElementById('card-hover-img');
  document.addEventListener('mouseover', function(e) {
    var link = e.target.closest('.card-link');
    if (!link) return;
    var preview = link.querySelector('.card-preview img');
    if (!preview) return;
    img.src = preview.src;
    img.style.display = 'block';
  });
  document.addEventListener('mouseout', function(e) {
    var link = e.target.closest('.card-link');
    if (link) {
      img.style.display = 'none';
      img.src = '';
    }
  });
  document.addEventListener('mousemove', function(e) {
    if (img.style.display !== 'block') return;
    var x = e.clientX + 16;
    var y = e.clientY - 180;
    // Keep within viewport
    if (x + 260 > window.innerWidth) x = e.clientX - 260;
    if (y < 4) y = 4;
    if (y + 340 > window.innerHeight) y = window.innerHeight - 344;
    img.style.left = x + 'px';
    img.style.top = y + 'px';
  });
})();
</script>
"""


# ── Creature ability detection ────────────────────────────────────────────

EVASION_KEYWORDS = [
    "flying",
    "menace",
    "trample",
    "skulk",
    "shadow",
    "fear",
    "intimidate",
]


def has_evasion(d):
    """Check if creature has evasion keywords or 'can't be blocked'."""
    kws = d["keywords"]
    if any(k in kws for k in EVASION_KEYWORDS):
        return True
    if "can't be blocked" in d["oracle_text"]:
        return True
    return False


def get_evasion_types(d):
    """Return list of evasion types this creature has."""
    types = [k.title() for k in EVASION_KEYWORDS if k in d["keywords"]]
    if "can't be blocked" in d["oracle_text"]:
        types.append("Unblockable")
    return types


def has_etb(d):
    """Check if creature has an enters-the-battlefield trigger."""
    ot = d["oracle_text"]
    return bool(re.search(r"when (this creature|it) enters", ot) or "enters, " in ot)


def get_etb_summary(d):
    """Extract a short ETB effect summary."""
    ot = d["card"].get("oracle_text", "") or ""
    if "card_faces" in d["card"] and not ot:
        ot = "\n".join(f.get("oracle_text", "") for f in d["card"]["card_faces"])
    for line in ot.split("\n"):
        if "enters" in line.lower() or "enter" in line.lower():
            # Trim the "When this creature enters, " prefix for brevity
            short = re.sub(r"^.*?enters,?\s*", "", line, flags=re.IGNORECASE)
            return short[:90].replace("|", "/")
    return ""


def is_mana_producer(d):
    """Check if creature produces mana."""
    ot = d["oracle_text"]
    return bool(re.search(r"add \{", ot) or "add one mana" in ot)


def get_keyword_display(d):
    """Return a short comma-separated list of notable keywords."""
    kws = d["keywords"]
    notable = [
        k.title()
        for k in [
            "flying",
            "trample",
            "vigilance",
            "lifelink",
            "deathtouch",
            "first strike",
            "double strike",
            "menace",
            "reach",
            "haste",
            "ward",
            "hexproof",
            "indestructible",
            "flash",
            "defender",
        ]
        if k in kws
    ]
    return ", ".join(notable) if notable else "-"


# ── Classification ───────────────────────────────────────────────────────


def _categorize_generic(cat):
    """Map a detailed removal/burn category to its generic form for summary tables."""
    if cat.startswith("Damage:"):
        return "Damage"
    if cat.startswith("Burn:"):
        return "Burn"
    if re.match(r"^-\d+/-\d+$", cat):
        return "-X/-X"
    if cat.startswith("Board Wipe"):
        return "Board Wipe"
    return cat


def classify_removal_and_burn(card):
    """Classify a card as removal and/or burn.

    Returns (removal_cats, burn_cats) -- each a list of detailed category strings.
    Removal = can remove/interact with creatures/permanents.
    Burn = deals damage to players/opponents only (not creatures).
    """
    ot = get_oracle_text(card)
    tl = get_type_line(card)
    removal = []
    burn = []

    # ── Destroy ──
    if re.search(r"destroy target (creature|permanent|nonland permanent)", ot):
        if re.search(
            r"destroy target (creature|permanent|nonland permanent) (with|that|an opponent|if)",
            ot,
        ):
            removal.append("Conditional Destroy")
        else:
            removal.append("Destroy")

    # ── Board wipe ──
    wipe_debuff = re.search(r"all creatures get (-\d+/-\d+)", ot)
    has_destroy_all = re.search(r"destroy all creatures", ot)
    if has_destroy_all and wipe_debuff:
        removal.append(f"Board Wipe / {wipe_debuff.group(1)}")
    elif has_destroy_all:
        removal.append("Board Wipe")
    elif wipe_debuff:
        removal.append(f"Board Wipe ({wipe_debuff.group(1)})")

    # ── Exile ──
    # Blink (exile + return immediately or end of turn) is NOT removal.
    # Exile until source leaves the battlefield IS removal.
    # Permanent exile IS removal.
    is_blink = bool(
        re.search(
            r"exile.*(target|another|up to one).*(creature|permanent).*return (that|it|the exiled|those)",
            ot,
            re.DOTALL,
        )
    )
    is_exile_until_leaves = bool(re.search(r"exile.*until .* leaves", ot))
    if re.search(r"exile target (creature|permanent|nonland permanent)", ot):
        if is_exile_until_leaves:
            removal.append("Exile (until leaves)")
        elif not is_blink:
            removal.append("Exile")

    # ── Damage ──
    # Targets that can hit creatures/permanents
    creature_targets = r"(target creature|any target|each creature|target creature or planeswalker|up to one target creature)"
    # Targets that only hit players
    player_targets = r"(each opponent|target (opponent|player))"

    dmg_creature = re.findall(r"deals? (\d+) damage to " + creature_targets, ot)
    dmg_player = re.findall(r"deals? (\d+) damage to " + player_targets, ot)
    dmg_equal = re.search(r"deals? damage equal to", ot)
    dmg_x = re.search(r"deals? x damage to " + creature_targets, ot)
    dmg_x_player = re.search(r"deals? x damage to " + player_targets, ot)
    # "deals N damage to target" (plain "target" = any target = can hit creatures)
    dmg_plain_target = re.findall(
        r"deals? (\d+) damage to (target\b|up to one target\b)", ot
    )

    # Creature-hitting damage -> removal
    creature_vals = [int(m[0]) for m in dmg_creature] + [
        int(m[0]) for m in dmg_plain_target
    ]
    if creature_vals:
        removal.append(f"Damage: {max(creature_vals)}")
    elif dmg_equal:
        if re.search(r"deals? damage equal to its power", ot):
            removal.append("Damage: P")
        else:
            removal.append("Damage: X")
    elif dmg_x:
        removal.append("Damage: X")

    # Player-only damage -> burn (only if no creature damage was found)
    if dmg_player and not creature_vals and not dmg_equal and not dmg_x:
        player_vals = [int(m[0]) for m in dmg_player]
        burn.append(f"Burn: {max(player_vals)}")
    elif dmg_x_player and not creature_vals and not dmg_equal and not dmg_x:
        burn.append("Burn: X")

    # ── Fight / Bite ──
    if re.search(r"fights? (up to one )?target", ot) or re.search(
        r"fights? another target", ot
    ):
        removal.append("Fight")
    if re.search(r"deals damage equal to its power to (up to one )?target", ot):
        removal.append("Bite")

    # ── -X/-X ──
    debuff_targeted = re.search(r"target creature.*?gets? (-\d+/-\d+)", ot)
    debuff_all = re.search(r"all creatures get (-\d+/-\d+)", ot)
    if debuff_all:
        if not any(c.startswith("Board Wipe") for c in removal):
            removal.append(f"{debuff_all.group(1)}")
    elif debuff_targeted:
        removal.append(f"{debuff_targeted.group(1)}")

    # ── Bounce ──
    if re.search(
        r"return target (creature|nonland permanent|permanent).*(to (its|their) owner'?s hand|top.*(library|deck))",
        ot,
    ):
        removal.append("Bounce")
    if re.search(r"owner puts it on .*(top|bottom).*library", ot):
        removal.append("Bounce (Library)")

    # ── Edict ──
    if re.search(r"(each opponent|target (opponent|player)) sacrifices", ot):
        removal.append("Edict")
    if re.search(r"exiles? a creature.*they control", ot):
        removal.append("Edict")

    # ── Tap/Stun ──
    if re.search(r"tap target creature.*stun counter", ot) or re.search(
        r"put .* stun counter", ot
    ):
        if re.search(r"target creature", ot) or re.search(
            r"target (nonland )?permanent", ot
        ):
            removal.append("Tap/Stun")

    # ── Counter ──
    if re.search(r"counter target (spell|creature spell|instant|sorcery)", ot):
        removal.append("Counter")

    return (list(set(removal)), list(set(burn)))


def classify_combat_trick(card):
    """Classify as combat trick. Returns list of trick categories or []."""
    ot = get_oracle_text(card)
    tl = get_type_line(card)
    categories = []

    # ── Blink (any speed -- creature ETB, instant, sorcery) ──
    # Exile + return immediately or at end of turn. NOT exile-until-leaves.
    is_blink = bool(
        re.search(
            r"exile.*(target|another|up to one).*(creature|permanent).*return (that|it|the exiled|those)",
            ot,
            re.DOTALL,
        )
    )
    is_exile_until_leaves = bool(re.search(r"exile.*until .* leaves", ot))
    if is_blink and not is_exile_until_leaves:
        categories.append("Blink")

    # ── Instant-speed tricks (require instant or flash) ──
    is_instant = "instant" in tl.lower()
    has_flash = "flash" in card.get("keywords", []) or "flash" in ot

    if is_instant or has_flash:
        # Power/toughness buff
        if re.search(r"gets? \+\d+/\+\d+", ot) or re.search(
            r"each get \+\d+/\+\d+", ot
        ):
            if re.search(r"target creature.*(gets?|each get) \+", ot):
                categories.append("P/T Buff")
            elif re.search(r"creatures you control (each )?get \+", ot):
                categories.append("P/T Buff (Team)")
            elif re.search(r"target creatures you control each get \+", ot):
                categories.append("P/T Buff (Team)")

        # +1/+1 counters at instant speed
        if re.search(r"put .* \+1/\+1 counter", ot) and is_instant:
            categories.append("Counters")

        # Keyword grant
        for kw in [
            "indestructible",
            "hexproof",
            "first strike",
            "double strike",
            "trample",
            "flying",
            "lifelink",
            "protection from",
        ]:
            if re.search(rf"gains? {kw}", ot):
                categories.append(f"Grants {kw.title()}")

        # Protection / save
        if re.search(r"gains? hexproof", ot) or re.search(r"gains? indestructible", ot):
            if "Protection" not in categories:
                categories.append("Protection")

        # Falter
        if re.search(r"can't block", ot):
            categories.append("Falter")

    return list(set(categories))


# ── Report Building ──────────────────────────────────────────────────────


def build_report(cards):
    lines = []
    w = lines.append

    w(HOVER_CSS)
    w("")
    w("# Secrets of Strixhaven (SOS) -- Set Analysis")
    w("")
    w(f"**Total unique cards:** {len(cards)}")
    w(f"**Release date:** April 24, 2026")
    w(f"**Source:** Scryfall API (`e:sos`)")
    w("")
    w("*Hover over card names to preview the card image. Click to open on Scryfall.*")
    w("")

    # Pre-classify all cards
    card_data = []
    for c in cards:
        color = card_color_bucket(c)
        rarity = c.get("rarity", "unknown")
        tl = get_type_line(c)
        ot = get_oracle_text(c)
        removal_cats, burn_cats = classify_removal_and_burn(c)
        trick_cats = classify_combat_trick(c)
        pt = get_power_toughness(c)
        cmc = get_cmc(c)

        scryfall_uri = get_scryfall_uri(c)
        image_url = get_image_url(c)
        name = c.get("name", "?")
        linked_name = card_link(name, scryfall_uri, image_url)
        pt_display = get_pt_display(c)

        card_data.append(
            {
                "card": c,
                "name": name,
                "linked_name": linked_name,
                "pt_display": pt_display,
                "color": color,
                "rarity": rarity,
                "type_line": tl,
                "oracle_text": ot,
                "is_creature": is_type(c, "creature"),
                "is_instant": is_type(c, "instant"),
                "is_sorcery": is_type(c, "sorcery"),
                "is_enchantment": is_type(c, "enchantment"),
                "is_artifact": is_type(c, "artifact"),
                "is_planeswalker": is_type(c, "planeswalker"),
                "is_land": is_type(c, "land"),
                "removal_cats": removal_cats,
                "burn_cats": burn_cats,
                "trick_cats": trick_cats,
                "pt": pt,
                "cmc": cmc,
                "keywords": [kw.lower() for kw in c.get("keywords", [])],
                "mana_cost": c.get("mana_cost", ""),
            }
        )

    # ── SECTION 1: Overview ──────────────────────────────────────────
    w("---")
    w("## 1. Set Overview")
    w("")

    # Precompute per-color and per-rarity subsets
    by_color = {c: [d for d in card_data if d["color"] == c] for c in COLOR_ORDER}
    by_rarity = {r: [d for d in card_data if d["rarity"] == r] for r in RARITY_ORDER}
    col_hdr = [COLOR_SHORT[c] for c in COLOR_ORDER]

    # By color -- transposed: types as rows, colors as columns
    w("### Card Count by Color")
    w("")
    w("| Type | " + " | ".join(col_hdr) + " |")
    w("|------|" + "|".join("---" for _ in COLOR_ORDER) + "|")
    type_checks = [
        ("Total", lambda d: True),
        ("Creatures", lambda d: d["is_creature"]),
        ("Instants", lambda d: d["is_instant"]),
        ("Sorceries", lambda d: d["is_sorcery"]),
        ("Enchantments", lambda d: d["is_enchantment"]),
        ("Artifacts", lambda d: d["is_artifact"]),
        ("Planeswalkers", lambda d: d["is_planeswalker"]),
        ("Lands", lambda d: d["is_land"]),
    ]
    for label, pred in type_checks:
        counts = [str(sum(1 for d in by_color[c] if pred(d))) for c in COLOR_ORDER]
        w(f"| {label} | " + " | ".join(counts) + " |")
    w("")

    # By rarity -- transposed: types as rows, rarities as columns
    w("### Card Count by Rarity")
    w("")
    rar_hdr = [RARITY_SHORT[r] for r in RARITY_ORDER]
    w("| Type | " + " | ".join(rar_hdr) + " |")
    w("|------|" + "|".join("---" for _ in RARITY_ORDER) + "|")
    for label, pred in type_checks:
        counts = [str(sum(1 for d in by_rarity[r] if pred(d))) for r in RARITY_ORDER]
        w(f"| {label} | " + " | ".join(counts) + " |")
    w("")

    # Color x Rarity matrix
    w("### Color x Rarity Matrix")
    w("")
    w("| Color | " + " | ".join(rar_hdr) + " | Total |")
    w("|-------|" + "|".join("---" for _ in RARITY_ORDER) + "|-------|")
    for color in COLOR_ORDER:
        cshort = COLOR_SHORT[color]
        counts = []
        for rarity in RARITY_ORDER:
            cnt = sum(
                1 for d in card_data if d["color"] == color and d["rarity"] == rarity
            )
            counts.append(str(cnt))
        total = len(by_color[color])
        w(f"| {cshort} | " + " | ".join(counts) + f" | {total} |")
    w("")

    # ── SECTION 2: Mana Curve ────────────────────────────────────────
    w("---")
    w("## 2. Mana Curve")
    w("")

    # Helper: get nonland cards per group
    def cmc_count(subset, cmc_val):
        if cmc_val < 8:
            return sum(1 for d in subset if int(d["cmc"]) == cmc_val)
        return sum(1 for d in subset if int(d["cmc"]) >= 8)

    cmc_labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8+"]
    cmc_vals = list(range(9))

    # By color -- transposed: CMC as rows, colors as columns
    w("### By Color")
    w("")
    nonland_by_color = {
        c: [d for d in by_color[c] if not d["is_land"]] for c in COLOR_ORDER
    }
    w("| CMC | " + " | ".join(col_hdr) + " |")
    w("|-----|" + "|".join("---" for _ in COLOR_ORDER) + "|")
    for i, label in zip(cmc_vals, cmc_labels):
        counts = [str(cmc_count(nonland_by_color[c], i)) for c in COLOR_ORDER]
        w(f"| {label} | " + " | ".join(counts) + " |")
    # Avg row
    avgs = []
    for c in COLOR_ORDER:
        s = nonland_by_color[c]
        avgs.append(f"{sum(d['cmc'] for d in s) / len(s):.1f}" if s else "-")
    w(f"| **Avg** | " + " | ".join(avgs) + " |")
    w("")

    # By rarity -- transposed: CMC as rows, rarities as columns
    w("### By Rarity")
    w("")
    nonland_by_rar = {
        r: [d for d in by_rarity[r] if not d["is_land"]] for r in RARITY_ORDER
    }
    w("| CMC | " + " | ".join(rar_hdr) + " |")
    w("|-----|" + "|".join("---" for _ in RARITY_ORDER) + "|")
    for i, label in zip(cmc_vals, cmc_labels):
        counts = [str(cmc_count(nonland_by_rar[r], i)) for r in RARITY_ORDER]
        w(f"| {label} | " + " | ".join(counts) + " |")
    avgs = []
    for r in RARITY_ORDER:
        s = nonland_by_rar[r]
        avgs.append(f"{sum(d['cmc'] for d in s) / len(s):.1f}" if s else "-")
    w(f"| **Avg** | " + " | ".join(avgs) + " |")
    w("")

    # ── SECTION 3: Creatures ─────────────────────────────────────────
    w("---")
    w("## 3. Creature Analysis")
    w("")

    all_creatures = [d for d in card_data if d["is_creature"]]
    creatures_by_color = {
        c: [d for d in all_creatures if d["color"] == c] for c in COLOR_ORDER
    }
    creatures_by_rar = {
        r: [d for d in all_creatures if d["rarity"] == r] for r in RARITY_ORDER
    }

    # ── 3.1 Stats summary ──
    w("### Creature Stats by Color")
    w("")
    w("| Color | Count | Avg P | Avg T | Avg CMC | Evasion | ETB | Keywords |")
    w("|-------|-------|-------|-------|---------|---------|-----|----------|")
    for color in COLOR_ORDER:
        creatures = creatures_by_color[color]
        if not creatures:
            continue
        cshort = COLOR_SHORT[color]
        pts = [d["pt"] for d in creatures if d["pt"]]
        avg_p = sum(p for p, t in pts) / len(pts) if pts else 0
        avg_t = sum(t for p, t in pts) / len(pts) if pts else 0
        avg_cmc = sum(d["cmc"] for d in creatures) / len(creatures)
        n_evasion = sum(1 for d in creatures if has_evasion(d))
        n_etb = sum(1 for d in creatures if has_etb(d))
        with_kw = sum(1 for d in creatures if d["keywords"])
        w(
            f"| {cshort} | {len(creatures)} | {avg_p:.1f} | {avg_t:.1f} | {avg_cmc:.1f} | {n_evasion} | {n_etb} | {with_kw} |"
        )
    w("")

    w("### Creature Stats by Rarity")
    w("")
    w("| Rarity | Count | Avg P | Avg T | Avg CMC | Evasion | ETB |")
    w("|--------|-------|-------|-------|---------|---------|-----|")
    for rarity in RARITY_ORDER:
        creatures = creatures_by_rar[rarity]
        if not creatures:
            continue
        rname = RARITY_SHORT[rarity]
        pts = [d["pt"] for d in creatures if d["pt"]]
        avg_p = sum(p for p, t in pts) / len(pts) if pts else 0
        avg_t = sum(t for p, t in pts) / len(pts) if pts else 0
        avg_cmc = sum(d["cmc"] for d in creatures) / len(creatures)
        n_evasion = sum(1 for d in creatures if has_evasion(d))
        n_etb = sum(1 for d in creatures if has_etb(d))
        w(
            f"| {rname} | {len(creatures)} | {avg_p:.1f} | {avg_t:.1f} | {avg_cmc:.1f} | {n_evasion} | {n_etb} |"
        )
    w("")

    # ── 3.2 Creature mana curve ──
    w("### Creature Mana Curve by Color")
    w("")
    cmc_labels = ["0", "1", "2", "3", "4", "5", "6", "7+"]
    cmc_vals = list(range(8))

    def cmc_bucket(cmc_val, subset):
        if cmc_val < 7:
            return sum(1 for d in subset if int(d["cmc"]) == cmc_val)
        return sum(1 for d in subset if int(d["cmc"]) >= 7)

    w("| CMC | " + " | ".join(col_hdr) + " |")
    w("|-----|" + "|".join("---" for _ in COLOR_ORDER) + "|")
    for i, label in zip(cmc_vals, cmc_labels):
        counts = [str(cmc_bucket(i, creatures_by_color[c])) for c in COLOR_ORDER]
        w(f"| {label} | " + " | ".join(counts) + " |")
    w("")

    # ── 3.3 Keyword Frequency ──
    w("### Keyword Frequency (Creatures)")
    w("")
    w("| Keyword | Total | " + " | ".join(col_hdr) + " |")
    w("|---------|-------|" + "|".join("---" for _ in COLOR_ORDER) + "|")
    for kw in TRACKED_KEYWORDS:
        counts = []
        total = 0
        for color in COLOR_ORDER:
            creatures = creatures_by_color[color]
            cnt = sum(
                1 for d in creatures if kw in d["keywords"] or kw in d["oracle_text"]
            )
            counts.append(str(cnt))
            total += cnt
        if total == 0:
            continue
        w(f"| {kw.title()} | {total} | " + " | ".join(counts) + " |")
    w("")

    # ── 3.4 Full Creature List by Color ──
    w("### Full Creature List by Color")
    w("")
    for color in COLOR_ORDER:
        subset = creatures_by_color[color]
        if not subset:
            continue
        cname = COLOR_NAMES.get(color, color) if color in COLOR_NAMES else color
        w(f"#### {cname}")
        w("")
        w("| Card | P/T | CMC | Rarity | Keywords |")
        w("|------|-----|-----|--------|----------|")
        for d in sorted(subset, key=lambda x: (x["cmc"], x["name"])):
            rarity_char = d["rarity"][0].upper()
            kws = get_keyword_display(d)
            w(
                f"| {d['linked_name']} | {d['pt_display']} | {d['cmc']:.0f} | {rarity_char} | {kws} |"
            )
        w("")

    # ── 3.5 Evasion Creatures ──
    w("### Evasion Creatures")
    w("")
    w("*Creatures with flying, menace, trample, or that can't be blocked.*")
    w("")
    evasion_creatures = [d for d in all_creatures if has_evasion(d)]
    for color in COLOR_ORDER:
        subset = [d for d in evasion_creatures if d["color"] == color]
        if not subset:
            continue
        cname = COLOR_NAMES.get(color, color) if color in COLOR_NAMES else color
        w(f"#### {cname}")
        w("")
        w("| Card | P/T | CMC | Rarity | Evasion |")
        w("|------|-----|-----|--------|---------|")
        for d in sorted(subset, key=lambda x: x["cmc"]):
            rarity_char = d["rarity"][0].upper()
            ev = ", ".join(get_evasion_types(d))
            w(
                f"| {d['linked_name']} | {d['pt_display']} | {d['cmc']:.0f} | {rarity_char} | {ev} |"
            )
        w("")

    # ── 3.6 ETB Creatures ──
    w("### ETB Creatures (Enters-the-Battlefield)")
    w("")
    w("*Creatures with enters-the-battlefield triggers -- key for limited value.*")
    w("")
    etb_creatures = [d for d in all_creatures if has_etb(d)]
    for color in COLOR_ORDER:
        subset = [d for d in etb_creatures if d["color"] == color]
        if not subset:
            continue
        cname = COLOR_NAMES.get(color, color) if color in COLOR_NAMES else color
        w(f"#### {cname}")
        w("")
        w("| Card | P/T | CMC | Rarity | ETB Effect |")
        w("|------|-----|-----|--------|------------|")
        for d in sorted(subset, key=lambda x: x["cmc"]):
            rarity_char = d["rarity"][0].upper()
            etb_eff = get_etb_summary(d)
            w(
                f"| {d['linked_name']} | {d['pt_display']} | {d['cmc']:.0f} | {rarity_char} | {etb_eff} |"
            )
        w("")

    # ── 3.7 Mana Creatures ──
    mana_creatures = [d for d in all_creatures if is_mana_producer(d)]
    if mana_creatures:
        w("### Mana Creatures")
        w("")
        w("*Creatures that produce mana -- enable splashing and ramp.*")
        w("")
        w("| Card | P/T | Color | CMC | Rarity |")
        w("|------|-----|-------|-----|--------|")
        for d in sorted(mana_creatures, key=lambda x: x["cmc"]):
            cshort = COLOR_SHORT.get(d["color"], d["color"])
            rarity_char = d["rarity"][0].upper()
            w(
                f"| {d['linked_name']} | {d['pt_display']} | {cshort} | {d['cmc']:.0f} | {rarity_char} |"
            )
        w("")

    # ── Helper: short type abbreviation ──
    def short_type(d):
        parts = []
        for t in [
            "Instant",
            "Sorcery",
            "Creature",
            "Enchantment",
            "Artifact",
            "Planeswalker",
        ]:
            if t.lower() in d["type_line"].lower():
                parts.append(t[:4])
        return "/".join(parts)

    # ── Helper: effect summary for tricks ──
    def effect_summary(d):
        ot = d["oracle_text"]
        for line in ot.split("\n"):
            if any(
                pat in line
                for pat in [
                    "gets +",
                    "get +",
                    "gains ",
                    "+1/+1 counter",
                    "can't block",
                    "hexproof",
                    "indestructible",
                ]
            ):
                clean = line.strip().lstrip("• ").replace("|", "/").replace("\n", " ")
                return clean[:80]
        # Fallback: flatten entire text, strip newlines
        flat = ot.replace("\n", " ").replace("|", "/")
        return flat[:80]

    # ── SECTION 4: Removal ───────────────────────────────────────────
    w("---")
    w("## 4. Removal Spells")
    w("")

    removal_cards = [d for d in card_data if d["removal_cats"]]

    # Generic categories for summary tables
    generic_rem_cats = sorted(
        set(
            _categorize_generic(cat) for d in removal_cards for cat in d["removal_cats"]
        )
    )
    rem_by_color = {
        c: [d for d in removal_cards if d["color"] == c] for c in COLOR_ORDER
    }
    rem_by_rar = {
        r: [d for d in removal_cards if d["rarity"] == r] for r in RARITY_ORDER
    }

    # Summary by color -- generic categories
    w("### Removal Count by Color")
    w("")
    w("| Category | " + " | ".join(col_hdr) + " |")
    w("|----------|" + "|".join("---" for _ in COLOR_ORDER) + "|")
    w(
        "| **Total** | "
        + " | ".join(str(len(rem_by_color[c])) for c in COLOR_ORDER)
        + " |"
    )
    for gcat in generic_rem_cats:
        counts = [
            str(
                sum(
                    1
                    for d in rem_by_color[c]
                    for cat in d["removal_cats"]
                    if _categorize_generic(cat) == gcat
                )
            )
            for c in COLOR_ORDER
        ]
        w(f"| {gcat} | " + " | ".join(counts) + " |")
    w("")

    # Summary by rarity -- generic categories
    w("### Removal Count by Rarity")
    w("")
    w("| Category | " + " | ".join(rar_hdr) + " |")
    w("|----------|" + "|".join("---" for _ in RARITY_ORDER) + "|")
    w(
        "| **Total** | "
        + " | ".join(str(len(rem_by_rar[r])) for r in RARITY_ORDER)
        + " |"
    )
    for gcat in generic_rem_cats:
        counts = [
            str(
                sum(
                    1
                    for d in rem_by_rar[r]
                    for cat in d["removal_cats"]
                    if _categorize_generic(cat) == gcat
                )
            )
            for r in RARITY_ORDER
        ]
        w(f"| {gcat} | " + " | ".join(counts) + " |")
    w("")

    # Full removal list -- per color, with detailed categories
    w("### Full Removal List by Color")
    w("")
    for color in COLOR_ORDER:
        subset = [d for d in removal_cards if d["color"] == color]
        if not subset:
            continue
        cname = COLOR_NAMES.get(color, color) if color in COLOR_NAMES else color
        w(f"#### {cname}")
        w("")
        w("| Card | P/T | Rarity | CMC | Type | Categories |")
        w("|------|-----|--------|-----|------|------------|")
        for d in sorted(subset, key=lambda x: x["cmc"]):
            cats = ", ".join(d["removal_cats"])
            rarity_char = d["rarity"][0].upper()
            w(
                f"| {d['linked_name']} | {d['pt_display']} | {rarity_char} | {d['cmc']:.0f} | {short_type(d)} | {cats} |"
            )
        w("")

    # ── SECTION 5: Burn ──────────────────────────────────────────────
    w("---")
    w("## 5. Burn (Player-Only Damage)")
    w("")
    w("*Cards that deal damage to opponents only -- cannot remove creatures.*")
    w("")

    burn_cards = [d for d in card_data if d["burn_cats"]]

    if burn_cards:
        w("| Card | P/T | Color | Rarity | CMC | Type | Categories |")
        w("|------|-----|-------|--------|-----|------|------------|")
        for d in sorted(
            burn_cards,
            key=lambda x: (
                COLOR_ORDER.index(x["color"]) if x["color"] in COLOR_ORDER else 99,
                x["cmc"],
            ),
        ):
            cshort = COLOR_SHORT.get(d["color"], d["color"])
            cats = ", ".join(d["burn_cats"])
            rarity_char = d["rarity"][0].upper()
            w(
                f"| {d['linked_name']} | {d['pt_display']} | {cshort} | {rarity_char} | {d['cmc']:.0f} | {short_type(d)} | {cats} |"
            )
        w("")

    # ── SECTION 6: Combat Tricks ─────────────────────────────────────
    w("---")
    w("## 6. Combat Tricks")
    w("")

    trick_cards = [d for d in card_data if d["trick_cats"]]

    # Generic categories for summary
    generic_trick_cats = sorted(
        set(cat for d in trick_cards for cat in d["trick_cats"])
    )
    trick_by_color = {
        c: [d for d in trick_cards if d["color"] == c] for c in COLOR_ORDER
    }
    trick_by_rar = {
        r: [d for d in trick_cards if d["rarity"] == r] for r in RARITY_ORDER
    }

    # Summary by color
    w("### Combat Trick Count by Color")
    w("")
    if generic_trick_cats:
        active_colors = [c for c in COLOR_ORDER if trick_by_color[c]]
        active_hdr = [COLOR_SHORT[c] for c in active_colors]
        w("| Category | " + " | ".join(active_hdr) + " |")
        w("|----------|" + "|".join("---" for _ in active_colors) + "|")
        w(
            "| **Total** | "
            + " | ".join(str(len(trick_by_color[c])) for c in active_colors)
            + " |"
        )
        for cat in generic_trick_cats:
            counts = [
                str(sum(1 for d in trick_by_color[c] if cat in d["trick_cats"]))
                for c in active_colors
            ]
            w(f"| {cat} | " + " | ".join(counts) + " |")
        w("")

    # Summary by rarity
    w("### Combat Trick Count by Rarity")
    w("")
    if generic_trick_cats:
        active_rars = [r for r in RARITY_ORDER if trick_by_rar[r]]
        active_rhdr = [RARITY_SHORT[r] for r in active_rars]
        w("| Category | " + " | ".join(active_rhdr) + " |")
        w("|----------|" + "|".join("---" for _ in active_rars) + "|")
        w(
            "| **Total** | "
            + " | ".join(str(len(trick_by_rar[r])) for r in active_rars)
            + " |"
        )
        for cat in generic_trick_cats:
            counts = [
                str(sum(1 for d in trick_by_rar[r] if cat in d["trick_cats"]))
                for r in active_rars
            ]
            w(f"| {cat} | " + " | ".join(counts) + " |")
        w("")

    # Full combat tricks list -- per color sub-tables
    w("### Full Combat Tricks List by Color")
    w("")
    for color in COLOR_ORDER:
        subset = [d for d in trick_cards if d["color"] == color]
        if not subset:
            continue
        cname = COLOR_NAMES.get(color, color) if color in COLOR_NAMES else color
        w(f"#### {cname}")
        w("")
        w("| Card | P/T | Rarity | CMC | Categories | Effect Summary |")
        w("|------|-----|--------|-----|------------|----------------|")
        for d in sorted(subset, key=lambda x: x["cmc"]):
            cats = ", ".join(d["trick_cats"])
            rarity_char = d["rarity"][0].upper()
            w(
                f"| {d['linked_name']} | {d['pt_display']} | {rarity_char} | {d['cmc']:.0f} | {cats} | {effect_summary(d)} |"
            )
        w("")

    # ── SECTION 7: Notable Cycles & Mechanics ────────────────────────
    w("---")
    w("## 7. Set Mechanics")
    w("")

    # Detect mechanics from keywords
    mechanics = defaultdict(int)
    mechanic_examples = defaultdict(list)
    mechanic_keywords = [
        "flashback",
        "paradigm",
        "infusion",
        "converge",
        "ward",
        "surveil",
        "magecraft",
    ]
    for d in card_data:
        ot = d["oracle_text"]
        for mech in mechanic_keywords:
            if mech in ot or mech in d["keywords"]:
                mechanics[mech] += 1
                if len(mechanic_examples[mech]) < 3:
                    mechanic_examples[mech].append(d["linked_name"])

    w("| Mechanic | Card Count | Examples |")
    w("|----------|------------|----------|")
    for mech in sorted(mechanics, key=lambda m: -mechanics[m]):
        examples = ", ".join(mechanic_examples[mech])
        w(f"| {mech.title()} | {mechanics[mech]} | {examples} |")
    w("")

    # ── SECTION 8: Draft Signposts (Uncommon Gold) ───────────────────
    w("---")
    w("## 8. Draft Signposts (Uncommon Multicolor)")
    w("")
    w("These uncommon gold cards hint at supported archetypes.")
    w("")
    signposts = [
        d for d in card_data if d["color"] == "Multicolor" and d["rarity"] == "uncommon"
    ]
    w("| Card | P/T | Colors | Type | CMC | Effect |")
    w("|------|-----|--------|------|-----|--------|")
    for d in sorted(signposts, key=lambda x: x["name"]):
        colors = ",".join(d["card"].get("colors", []))
        tl = d["type_line"].split("//")[0].strip()
        short_ot = d["oracle_text"].replace("\n", " ")[:100].replace("|", "/")
        w(
            f"| {d['linked_name']} | {d['pt_display']} | {colors} | {tl} | {d['cmc']:.0f} | {short_ot} |"
        )
    w("")

    # ── SECTION 9: Top Limited Picks ─────────────────────────────────
    w("---")
    w("## 9. Notable Cards for Limited (by Rarity)")
    w("")
    w("### Common Removal")
    w("")
    common_removal = [d for d in removal_cards if d["rarity"] == "common"]
    w("| Card | P/T | Color | CMC | Categories |")
    w("|------|-----|-------|-----|------------|")
    for d in sorted(common_removal, key=lambda x: x["cmc"]):
        cshort = COLOR_SHORT.get(d["color"], d["color"])
        cats = ", ".join(d["removal_cats"])
        w(
            f"| {d['linked_name']} | {d['pt_display']} | {cshort} | {d['cmc']:.0f} | {cats} |"
        )
    w("")

    w("### Common Combat Tricks")
    w("")
    common_tricks = [d for d in trick_cards if d["rarity"] == "common"]
    w("| Card | P/T | Color | CMC | Categories |")
    w("|------|-----|-------|-----|------------|")
    for d in sorted(common_tricks, key=lambda x: x["cmc"]):
        cshort = COLOR_SHORT.get(d["color"], d["color"])
        cats = ", ".join(d["trick_cats"])
        w(
            f"| {d['linked_name']} | {d['pt_display']} | {cshort} | {d['cmc']:.0f} | {cats} |"
        )
    w("")

    w("### Uncommon Removal")
    w("")
    unc_removal = [d for d in removal_cards if d["rarity"] == "uncommon"]
    w("| Card | P/T | Color | CMC | Categories |")
    w("|------|-----|-------|-----|------------|")
    for d in sorted(unc_removal, key=lambda x: x["cmc"]):
        cshort = COLOR_SHORT.get(d["color"], d["color"])
        cats = ", ".join(d["removal_cats"])
        w(
            f"| {d['linked_name']} | {d['pt_display']} | {cshort} | {d['cmc']:.0f} | {cats} |"
        )
    w("")

    # ── SECTION 10: Lands ────────────────────────────────────────────
    w("---")
    w("## 10. Lands")
    w("")

    land_cards = [d for d in card_data if d["is_land"]]
    if land_cards:
        w("| Card | Color | Rarity | Type |")
        w("|------|-------|--------|------|")
        for d in sorted(
            land_cards,
            key=lambda x: (
                COLOR_ORDER.index(x["color"]) if x["color"] in COLOR_ORDER else 99,
                x["name"],
            ),
        ):
            cshort = COLOR_SHORT.get(d["color"], d["color"])
            rarity_char = d["rarity"][0].upper()
            tl = d["type_line"].replace("|", "/")
            w(f"| {d['linked_name']} | {cshort} | {rarity_char} | {tl} |")
        w("")

    # ── SECTION 11: Other Cards ──────────────────────────────────────
    w("---")
    w("## 11. Other Cards")
    w("")
    w("*Cards not classified as creatures, removal, burn, combat tricks, or lands.*")
    w("")

    classified_names = set()
    for d in card_data:
        if (
            d["is_creature"]
            or d["removal_cats"]
            or d["burn_cats"]
            or d["trick_cats"]
            or d["is_land"]
        ):
            classified_names.add(d["name"])
    other_cards = [d for d in card_data if d["name"] not in classified_names]

    if other_cards:
        for color in COLOR_ORDER:
            subset = [d for d in other_cards if d["color"] == color]
            if not subset:
                continue
            cname = COLOR_NAMES.get(color, color) if color in COLOR_NAMES else color
            w(f"#### {cname}")
            w("")
            w("| Card | Rarity | CMC | Type |")
            w("|------|--------|-----|------|")
            for d in sorted(subset, key=lambda x: (x["cmc"], x["name"])):
                rarity_char = d["rarity"][0].upper()
                w(
                    f"| {d['linked_name']} | {rarity_char} | {d['cmc']:.0f} | {short_type(d)} |"
                )
            w("")
    w("")

    report_content = "\n".join(lines) + "\n"

    # Write report.md (raw, no front matter)
    with open(REPORT_PATH, "w") as f:
        f.write(report_content)

    # Write index.md with Jekyll front matter for GitHub Pages
    with open(INDEX_PATH, "w") as f:
        f.write("---\nlayout: page\n---\n\n")
        f.write(report_content)

    print(f"Report written to {REPORT_PATH}")
    print(f"Index written to {INDEX_PATH}")
    print(f"  Total cards analyzed: {len(card_data)}")
    print(f"  Removal spells found: {len(removal_cards)}")
    print(f"  Burn cards found: {len(burn_cards)}")
    print(f"  Combat tricks found: {len(trick_cards)}")


def main():
    cards = load_cards()
    build_report(cards)


if __name__ == "__main__":
    main()
