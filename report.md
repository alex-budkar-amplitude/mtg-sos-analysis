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


# Secrets of Strixhaven (SOS) -- Set Analysis

**Total unique cards:** 266
**Release date:** April 24, 2026
**Source:** Scryfall API (`e:sos`)

*Hover over card names to preview the card image. Click to open on Scryfall.*

---
## 1. Set Overview

### Card Count by Color

| Type | W | U | B | R | G | MC | NC |
|------|---|---|---|---|---|---|---|
| Total | 32 | 34 | 34 | 32 | 32 | 87 | 15 |
| Creatures | 18 | 17 | 19 | 17 | 18 | 42 | 7 |
| Instants | 7 | 16 | 6 | 6 | 5 | 13 | 0 |
| Sorceries | 11 | 9 | 15 | 13 | 11 | 23 | 1 |
| Enchantments | 2 | 0 | 0 | 1 | 2 | 0 | 0 |
| Artifacts | 0 | 0 | 0 | 1 | 0 | 4 | 6 |
| Planeswalkers | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
| Lands | 0 | 0 | 0 | 0 | 0 | 10 | 4 |

### Card Count by Rarity

| Type | C | U | R | M |
|------|---|---|---|---|
| Total | 86 | 100 | 60 | 20 |
| Creatures | 45 | 53 | 29 | 11 |
| Instants | 19 | 21 | 10 | 3 |
| Sorceries | 24 | 32 | 18 | 9 |
| Enchantments | 0 | 4 | 1 | 0 |
| Artifacts | 4 | 4 | 3 | 0 |
| Planeswalkers | 0 | 0 | 0 | 2 |
| Lands | 6 | 1 | 7 | 0 |

### Color x Rarity Matrix

| Color | C | U | R | M | Total |
|-------|---|---|---|---|-------|
| W | 12 | 12 | 6 | 2 | 32 |
| U | 12 | 12 | 7 | 3 | 34 |
| B | 12 | 12 | 6 | 4 | 34 |
| R | 12 | 12 | 6 | 2 | 32 |
| G | 12 | 12 | 6 | 2 | 32 |
| MC | 20 | 35 | 26 | 6 | 87 |
| NC | 6 | 5 | 3 | 1 | 15 |

---
## 2. Mana Curve

### By Color

| CMC | W | U | B | R | G | MC | NC |
|-----|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 6 | 7 | 4 | 4 | 5 | 0 | 0 |
| 2 | 9 | 8 | 8 | 8 | 9 | 24 | 3 |
| 3 | 9 | 9 | 11 | 9 | 8 | 18 | 2 |
| 4 | 4 | 4 | 5 | 3 | 6 | 19 | 1 |
| 5 | 3 | 3 | 5 | 5 | 3 | 7 | 1 |
| 6 | 0 | 2 | 1 | 2 | 1 | 4 | 2 |
| 7 | 1 | 1 | 0 | 1 | 0 | 4 | 1 |
| 8+ | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| **Avg** | 2.8 | 2.9 | 3.1 | 3.2 | 2.9 | 3.5 | 4.5 |

### By Rarity

| CMC | C | U | R | M |
|-----|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 1 | 11 | 9 | 6 | 0 |
| 2 | 25 | 30 | 12 | 2 |
| 3 | 20 | 24 | 18 | 4 |
| 4 | 12 | 17 | 10 | 3 |
| 5 | 9 | 12 | 2 | 4 |
| 6 | 2 | 6 | 2 | 2 |
| 7 | 1 | 1 | 3 | 3 |
| 8+ | 0 | 0 | 0 | 2 |
| **Avg** | 2.9 | 3.2 | 3.2 | 5.0 |

---
## 3. Creature Analysis

### Creature Stats by Color

| Color | Count | Avg P | Avg T | Avg CMC | Evasion | ETB | Keywords |
|-------|-------|-------|-------|---------|---------|-----|----------|
| W | 18 | 2.4 | 2.6 | 2.9 | 4 | 5 | 16 |
| U | 17 | 1.7 | 2.5 | 2.9 | 5 | 5 | 14 |
| B | 19 | 2.9 | 2.7 | 3.2 | 5 | 3 | 17 |
| R | 17 | 2.7 | 3.0 | 3.5 | 5 | 2 | 15 |
| G | 18 | 2.6 | 2.9 | 2.8 | 3 | 2 | 14 |
| MC | 42 | 2.9 | 3.4 | 3.6 | 17 | 12 | 30 |
| NC | 7 | 3.3 | 3.6 | 5.1 | 1 | 3 | 6 |

### Creature Stats by Rarity

| Rarity | Count | Avg P | Avg T | Avg CMC | Evasion | ETB |
|--------|-------|-------|-------|---------|---------|-----|
| C | 45 | 2.4 | 2.6 | 3.1 | 12 | 14 |
| U | 53 | 2.6 | 3.0 | 3.4 | 13 | 14 |
| R | 29 | 2.3 | 2.8 | 2.8 | 9 | 3 |
| M | 11 | 4.7 | 4.7 | 5.2 | 6 | 1 |

### Creature Mana Curve by Color

| CMC | W | U | B | R | G | MC | NC |
|-----|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 2 | 2 | 0 | 3 | 0 | 0 |
| 2 | 6 | 4 | 4 | 5 | 4 | 12 | 2 |
| 3 | 6 | 7 | 6 | 5 | 6 | 12 | 0 |
| 4 | 4 | 2 | 4 | 3 | 4 | 9 | 1 |
| 5 | 1 | 2 | 2 | 2 | 1 | 3 | 1 |
| 6 | 0 | 0 | 1 | 2 | 0 | 3 | 1 |
| 7+ | 0 | 0 | 0 | 0 | 0 | 3 | 2 |

### Keyword Frequency (Creatures)

| Keyword | Total | W | U | B | R | G | MC | NC |
|---------|-------|---|---|---|---|---|---|---|
| Flying | 30 | 8 | 5 | 4 | 1 | 0 | 12 | 0 |
| Trample | 15 | 0 | 0 | 1 | 2 | 5 | 6 | 1 |
| Vigilance | 12 | 4 | 1 | 0 | 0 | 2 | 4 | 1 |
| Lifelink | 6 | 3 | 0 | 1 | 0 | 0 | 2 | 0 |
| Deathtouch | 6 | 0 | 0 | 3 | 0 | 2 | 1 | 0 |
| First Strike | 4 | 2 | 0 | 0 | 1 | 0 | 1 | 0 |
| Double Strike | 2 | 1 | 0 | 0 | 1 | 0 | 0 | 0 |
| Menace | 5 | 0 | 0 | 1 | 2 | 0 | 2 | 0 |
| Reach | 10 | 0 | 0 | 0 | 3 | 3 | 2 | 2 |
| Haste | 6 | 0 | 0 | 0 | 3 | 0 | 3 | 0 |
| Ward | 11 | 1 | 2 | 2 | 2 | 1 | 3 | 0 |
| Flash | 2 | 0 | 1 | 0 | 0 | 0 | 1 | 0 |

### Full Creature List by Color

#### White

| Card | P/T | CMC | Rarity | Keywords |
|------|-----|-----|--------|----------|
| <a href="https://scryfall.com/card/sos/12/elite-interceptor-rejoinder" class="card-link" target="_blank">Elite Interceptor // Rejoinder<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/9/2970683e-e69c-42cb-a067-34abd56fb42b.jpg?1775936992" alt="Elite Interceptor // Rejoinder"></span></a> | 1/2 | 1 | C | - |
| <a href="https://scryfall.com/card/sos/14/ennis-debate-moderator" class="card-link" target="_blank">Ennis, Debate Moderator<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/2/d2ef31b4-24fa-4443-9f05-c8e99c3522e5.jpg?1775937005" alt="Ennis, Debate Moderator"></span></a> | 1/1 | 2 | U | - |
| <a href="https://scryfall.com/card/sos/20/informed-inkwright" class="card-link" target="_blank">Informed Inkwright<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/d/5defb2d1-d0fb-4e7f-a5c7-3df99fe675d6.jpg?1775937046" alt="Informed Inkwright"></span></a> | 2/2 | 2 | R | Vigilance |
| <a href="https://scryfall.com/card/sos/23/joined-researchers-secret-rendezvous" class="card-link" target="_blank">Joined Researchers // Secret Rendezvous<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/e/1ebaafe0-3a9a-424c-8698-d26e7be45343.jpg?1775937069" alt="Joined Researchers // Secret Rendezvous"></span></a> | 2/2 | 2 | R | First Strike |
| <a href="https://scryfall.com/card/sos/27/quill-blade-laureate-twofold-intent" class="card-link" target="_blank">Quill-Blade Laureate // Twofold Intent<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/2/62a47835-5719-48c4-a740-a0c5f00dce11.jpg?1775937102" alt="Quill-Blade Laureate // Twofold Intent"></span></a> | 1/1 | 2 | U | Double Strike |
| <a href="https://scryfall.com/card/sos/31/shattered-acolyte" class="card-link" target="_blank">Shattered Acolyte<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/c/dc0517ca-b271-49a1-a286-c20f4e5b9309.jpg?1775937130" alt="Shattered Acolyte"></span></a> | 2/2 | 2 | C | Lifelink |
| <a href="https://scryfall.com/card/sos/36/stone-docent" class="card-link" target="_blank">Stone Docent<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/2/c2abfffb-bf36-44af-9a27-6e109e4d77dd.jpg?1775937164" alt="Stone Docent"></span></a> | 3/1 | 2 | C | - |
| <a href="https://scryfall.com/card/sos/13/emeritus-of-truce-swords-to-plowshares" class="card-link" target="_blank">Emeritus of Truce // Swords to Plowshares<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/8/9869a753-5e41-4098-ab41-e75b4396ec50.jpg?1775936999" alt="Emeritus of Truce // Swords to Plowshares"></span></a> | 3/3 | 3 | M | - |
| <a href="https://scryfall.com/card/sos/24/owlin-historian" class="card-link" target="_blank">Owlin Historian<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/f/5fe99be0-e1ec-485e-82f8-02eba7b82441.jpg?1775937078" alt="Owlin Historian"></span></a> | 2/3 | 3 | C | Flying |
| <a href="https://scryfall.com/card/sos/29/rehearsed-debater" class="card-link" target="_blank">Rehearsed Debater<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/c/fc6a1425-6733-42a2-94d9-605966398092.jpg?1775937116" alt="Rehearsed Debater"></span></a> | 3/3 | 3 | C | Vigilance |
| <a href="https://scryfall.com/card/sos/32/soaring-stoneglider" class="card-link" target="_blank">Soaring Stoneglider<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/f/2fbe446b-60fd-43da-8358-985392293af8.jpg?1775937136" alt="Soaring Stoneglider"></span></a> | 4/3 | 3 | U | Flying, Vigilance |
| <a href="https://scryfall.com/card/sos/33/spiritcall-enthusiast-scrollboost" class="card-link" target="_blank">Spiritcall Enthusiast // Scrollboost<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/0/c0b85569-2cb3-4b64-b0fe-418195c4dab0.jpg?1775937144" alt="Spiritcall Enthusiast // Scrollboost"></span></a> | 3/3 | 3 | U | - |
| <a href="https://scryfall.com/card/sos/35/stirring-hopesinger" class="card-link" target="_blank">Stirring Hopesinger<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/1/21375667-b318-47f8-a482-9c8c2b5b14c0.jpg?1775937157" alt="Stirring Hopesinger"></span></a> | 1/3 | 3 | R | Flying, Lifelink |
| <a href="https://scryfall.com/card/sos/11/eager-glyphmage" class="card-link" target="_blank">Eager Glyphmage<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/f/bf736de9-9bc4-49df-ae60-672ed4f83f32.jpg?1775936986" alt="Eager Glyphmage"></span></a> | 3/3 | 4 | C | - |
| <a href="https://scryfall.com/card/sos/19/honorbound-page-forums-favor" class="card-link" target="_blank">Honorbound Page // Forum's Favor<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/9/79a70863-860f-4a7b-9cb2-d3546b689d44.jpg?1775937039" alt="Honorbound Page // Forum's Favor"></span></a> | 3/3 | 4 | C | First Strike |
| <a href="https://scryfall.com/card/sos/21/inkshape-demonstrator" class="card-link" target="_blank">Inkshape Demonstrator<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/c/bcfac992-9984-4529-b9ff-a42d58832b34.jpg?1775937053" alt="Inkshape Demonstrator"></span></a> | 3/4 | 4 | U | Ward |
| <a href="https://scryfall.com/card/sos/37/summoned-dromedary" class="card-link" target="_blank">Summoned Dromedary<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/4/44d0277c-ca82-4334-a15a-cd67a9db0d02.jpg?1775937170" alt="Summoned Dromedary"></span></a> | 4/3 | 4 | U | Vigilance |
| <a href="https://scryfall.com/card/sos/8/ascendant-dustspeaker" class="card-link" target="_blank">Ascendant Dustspeaker<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/e/de3de40b-a7ac-455e-add2-4e451b602d17.jpg?1776000359" alt="Ascendant Dustspeaker"></span></a> | 3/4 | 5 | C | Flying |

#### Blue

| Card | P/T | CMC | Rarity | Keywords |
|------|-----|-----|--------|----------|
| <a href="https://scryfall.com/card/sos/48/exhibition-tidecaller" class="card-link" target="_blank">Exhibition Tidecaller<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/5/a58c364e-d0c5-41b9-8c8b-2e5a99468cc7.jpg?1775937242" alt="Exhibition Tidecaller"></span></a> | 0/2 | 1 | R | - |
| <a href="https://scryfall.com/card/sos/52/harmonized-trio-brainstorm" class="card-link" target="_blank">Harmonized Trio // Brainstorm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/1/617208ff-dd9b-44fd-a740-d3188081e5cc.jpg?1775937273" alt="Harmonized Trio // Brainstorm"></span></a> | 1/1 | 1 | R | - |
| <a href="https://scryfall.com/card/sos/54/hydro-channeler" class="card-link" target="_blank">Hydro-Channeler<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/9/099f8400-d70a-48ef-8ff6-645eae97e072.jpg?1775937286" alt="Hydro-Channeler"></span></a> | 1/3 | 2 | C | - |
| <a href="https://scryfall.com/card/sos/56/landscape-painter-vibrant-idea" class="card-link" target="_blank">Landscape Painter // Vibrant Idea<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/0/c0bd30c4-3cdf-4eda-8be5-0fb5e5ddddbf.jpg?1775937300" alt="Landscape Painter // Vibrant Idea"></span></a> | 2/1 | 2 | C | - |
| <a href="https://scryfall.com/card/sos/60/muse-seeker" class="card-link" target="_blank">Muse Seeker<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/1/71cb4a6b-b500-4b28-bcdb-ec4188242f39.jpg?1775937328" alt="Muse Seeker"></span></a> | 1/2 | 2 | U | - |
| <a href="https://scryfall.com/card/sos/69/tester-of-the-tangential" class="card-link" target="_blank">Tester of the Tangential<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/b/bbd708ec-eef4-4f45-99dd-60e1cec4b991.jpg?1775937389" alt="Tester of the Tangential"></span></a> | 1/1 | 2 | U | - |
| <a href="https://scryfall.com/card/sos/42/deluge-virtuoso" class="card-link" target="_blank">Deluge Virtuoso<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/e/2e3b16ed-8727-48fd-8b1f-c0cbd329385e.jpg?1775937202" alt="Deluge Virtuoso"></span></a> | 2/2 | 3 | C | - |
| <a href="https://scryfall.com/card/sos/46/encouraging-aviator-jump" class="card-link" target="_blank">Encouraging Aviator // Jump<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/2/72654b84-9902-41db-92ab-a3499c31221c.jpg?1775937230" alt="Encouraging Aviator // Jump"></span></a> | 2/3 | 3 | U | Flying |
| <a href="https://scryfall.com/card/sos/55/jadzi-steward-of-fate-oracles-gift" class="card-link" target="_blank">Jadzi, Steward of Fate // Oracle's Gift<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/9/a95b6baf-01e6-49c3-9a26-394b127d53c3.jpg?1775937293" alt="Jadzi, Steward of Fate // Oracle's Gift"></span></a> | 2/4 | 3 | R | - |
| <a href="https://scryfall.com/card/sos/59/matterbending-mage" class="card-link" target="_blank">Matterbending Mage<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/6/460c6afd-cddf-4fea-925f-b27517ff250a.jpg?1775937321" alt="Matterbending Mage"></span></a> | 2/2 | 3 | U | - |
| <a href="https://scryfall.com/card/sos/63/pensive-professor" class="card-link" target="_blank">Pensive Professor<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/6/66d47940-84f9-4479-8562-45e5148435d4.jpg?1775937349" alt="Pensive Professor"></span></a> | 0/2 | 3 | R | - |
| <a href="https://scryfall.com/card/sos/67/skycoach-conductor-all-aboard" class="card-link" target="_blank">Skycoach Conductor // All Aboard<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/e/4ecbca71-9a1d-44c5-b709-d6f565941d5e.jpg?1775937376" alt="Skycoach Conductor // All Aboard"></span></a> | 2/3 | 3 | R | Flying, Vigilance, Flash |
| <a href="https://scryfall.com/card/sos/70/textbook-tabulator" class="card-link" target="_blank">Textbook Tabulator<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/6/56f54fee-b48d-4582-8982-ca4c7b8ef553.jpg?1776000387" alt="Textbook Tabulator"></span></a> | 0/3 | 3 | C | - |
| <a href="https://scryfall.com/card/sos/40/campus-composer-aqueous-aria" class="card-link" target="_blank">Campus Composer // Aqueous Aria<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/a/fac8ac39-ecb4-4142-bf37-131c65660a9b.jpg?1775937189" alt="Campus Composer // Aqueous Aria"></span></a> | 3/4 | 4 | U | Ward |
| <a href="https://scryfall.com/card/sos/68/spellbook-seeker-careful-study" class="card-link" target="_blank">Spellbook Seeker // Careful Study<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/c/cc44eaa4-59a4-419e-b1d1-d92f354ff588.jpg?1775937383" alt="Spellbook Seeker // Careful Study"></span></a> | 3/3 | 4 | C | Flying |
| <a href="https://scryfall.com/card/sos/45/emeritus-of-ideation-ancestral-recall" class="card-link" target="_blank">Emeritus of Ideation // Ancestral Recall<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/5/75961d36-acf6-425f-9698-0bf52af74f31.jpg?1775937223" alt="Emeritus of Ideation // Ancestral Recall"></span></a> | 5/5 | 5 | M | Flying, Ward |
| <a href="https://scryfall.com/card/sos/62/orysa-tide-choreographer" class="card-link" target="_blank">Orysa, Tide Choreographer<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/1/010ed379-63f5-452c-9cd4-00d51647c0e3.jpg?1775937343" alt="Orysa, Tide Choreographer"></span></a> | 2/2 | 5 | U | - |

#### Black

| Card | P/T | CMC | Rarity | Keywords |
|------|-----|-----|--------|----------|
| <a href="https://scryfall.com/card/sos/75/burrog-banemaker" class="card-link" target="_blank">Burrog Banemaker<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/e/3e4f9d23-1a17-4188-ac91-f8ddea46a1c4.jpg?1775937433" alt="Burrog Banemaker"></span></a> | 1/1 | 1 | C | Deathtouch |
| <a href="https://scryfall.com/card/sos/87/lecturing-scornmage" class="card-link" target="_blank">Lecturing Scornmage<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/d/ad07091e-8c24-43af-8ce8-031847bcaf30.jpg?1775937516" alt="Lecturing Scornmage"></span></a> | 1/1 | 1 | U | - |
| <a href="https://scryfall.com/card/sos/88/leech-collector-bloodletting" class="card-link" target="_blank">Leech Collector // Bloodletting<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/7/c715fe4c-c0e7-4342-811f-b74687851097.jpg?1775937525" alt="Leech Collector // Bloodletting"></span></a> | 2/2 | 2 | U | - |
| <a href="https://scryfall.com/card/sos/90/melancholic-poet" class="card-link" target="_blank">Melancholic Poet<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/8/d8309815-7035-47a5-acf2-2b2ac1e65037.jpg?1775937538" alt="Melancholic Poet"></span></a> | 2/2 | 2 | C | - |
| <a href="https://scryfall.com/card/sos/93/postmortem-professor" class="card-link" target="_blank">Postmortem Professor<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/7/174f5d7e-5d36-4d13-96bf-9b12cd644716.jpg?1775937558" alt="Postmortem Professor"></span></a> | 2/2 | 2 | R | - |
| <a href="https://scryfall.com/card/sos/99/scheming-silvertongue-sign-in-blood" class="card-link" target="_blank">Scheming Silvertongue // Sign in Blood<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/e/fe85a124-0d8b-4a29-8df1-65888a39147f.jpg?1775937600" alt="Scheming Silvertongue // Sign in Blood"></span></a> | 1/3 | 2 | R | Flying, Lifelink |
| <a href="https://scryfall.com/card/sos/72/adventurous-eater-have-a-bite" class="card-link" target="_blank">Adventurous Eater // Have a Bite<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/4/d40cc7da-c731-418e-8547-7033d1939450.jpg?1775937412" alt="Adventurous Eater // Have a Bite"></span></a> | 3/2 | 3 | C | - |
| <a href="https://scryfall.com/card/sos/74/arnyn-deathbloom-botanist" class="card-link" target="_blank">Arnyn, Deathbloom Botanist<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/1/6168b472-0930-4db5-9920-407340b99050.jpg?1775937426" alt="Arnyn, Deathbloom Botanist"></span></a> | 2/2 | 3 | U | Deathtouch |
| <a href="https://scryfall.com/card/sos/85/grave-researcher-reanimate" class="card-link" target="_blank">Grave Researcher // Reanimate<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/b/8b1e10e8-ea14-4761-910b-4072e2a18456.jpg?1775937504" alt="Grave Researcher // Reanimate"></span></a> | 3/3 | 3 | R | - |
| <a href="https://scryfall.com/card/sos/91/moseo-veins-new-dean" class="card-link" target="_blank">Moseo, Vein's New Dean<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/8/6877180c-22a1-4c4d-9178-316f4c34661b.jpg?1775937545" alt="Moseo, Vein's New Dean"></span></a> | 2/1 | 3 | R | Flying |
| <a href="https://scryfall.com/card/sos/92/poisoners-apprentice" class="card-link" target="_blank">Poisoner's Apprentice<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/7/3755a2e9-af55-4625-a006-2a86c7893a96.jpg?1775937552" alt="Poisoner's Apprentice"></span></a> | 2/2 | 3 | U | - |
| <a href="https://scryfall.com/card/sos/103/ulna-alley-shopkeep" class="card-link" target="_blank">Ulna Alley Shopkeep<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/2/c25e1ae5-f17c-4eee-98f1-5681981af31c.jpg?1775937633" alt="Ulna Alley Shopkeep"></span></a> | 2/3 | 3 | C | Menace |
| <a href="https://scryfall.com/card/sos/76/cheerful-osteomancer-raise-dead" class="card-link" target="_blank">Cheerful Osteomancer // Raise Dead<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/c/3c34660c-25e3-4ff5-9b2b-5554ded2bcc3.jpg?1775937441" alt="Cheerful Osteomancer // Raise Dead"></span></a> | 4/2 | 4 | C | - |
| <a href="https://scryfall.com/card/sos/80/emeritus-of-woe-demonic-tutor" class="card-link" target="_blank">Emeritus of Woe // Demonic Tutor<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/e/7eb9e83d-515d-4911-a06b-9982200277b2.jpg?1775937469" alt="Emeritus of Woe // Demonic Tutor"></span></a> | 5/4 | 4 | M | - |
| <a href="https://scryfall.com/card/sos/82/eternal-student" class="card-link" target="_blank">Eternal Student<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/9/f97fac69-3e77-4150-9702-cc726daa6d21.jpg?1775937483" alt="Eternal Student"></span></a> | 4/2 | 4 | U | - |
| <a href="https://scryfall.com/card/sos/102/tragedy-feaster" class="card-link" target="_blank">Tragedy Feaster<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/9/b93cbaad-8ed8-4a1d-b95a-20a616dfedc9.jpg?1775937623" alt="Tragedy Feaster"></span></a> | 7/6 | 4 | R | Trample, Ward |
| <a href="https://scryfall.com/card/sos/98/scathing-shadelock-venomous-words" class="card-link" target="_blank">Scathing Shadelock // Venomous Words<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/3/03e664cd-c3a6-4263-b2d8-dd99058fb8ec.jpg?1775937593" alt="Scathing Shadelock // Venomous Words"></span></a> | 4/6 | 5 | U | - |
| <a href="https://scryfall.com/card/sos/101/sneering-shadewriter" class="card-link" target="_blank">Sneering Shadewriter<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/b/4b4c120e-abe9-4f11-a7e4-bc3f723da4b2.jpg?1775937615" alt="Sneering Shadewriter"></span></a> | 3/3 | 5 | C | Flying |
| <a href="https://scryfall.com/card/sos/84/forum-necroscribe" class="card-link" target="_blank">Forum Necroscribe<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/7/67504a12-7414-4209-bf1c-624b4db19d52.jpg?1775937497" alt="Forum Necroscribe"></span></a> | 5/4 | 6 | U | Ward |

#### Red

| Card | P/T | CMC | Rarity | Keywords |
|------|-----|-----|--------|----------|
| <a href="https://scryfall.com/card/sos/113/emeritus-of-conflict-lightning-bolt" class="card-link" target="_blank">Emeritus of Conflict // Lightning Bolt<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/5/f58dba4f-1abb-47a3-a684-29c32bab95c0.jpg?1775937726" alt="Emeritus of Conflict // Lightning Bolt"></span></a> | 2/2 | 2 | M | First Strike |
| <a href="https://scryfall.com/card/sos/114/expressive-firedancer" class="card-link" target="_blank">Expressive Firedancer<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/5/259b8c45-6241-4206-a34e-34c7f401f47b.jpg?1775937734" alt="Expressive Firedancer"></span></a> | 2/2 | 2 | C | - |
| <a href="https://scryfall.com/card/sos/117/goblin-glasswright-craft-with-pride" class="card-link" target="_blank">Goblin Glasswright // Craft with Pride<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/8/c85c5f06-dd31-4e2c-97be-2f64d65069ea.jpg?1775937759" alt="Goblin Glasswright // Craft with Pride"></span></a> | 2/2 | 2 | C | - |
| <a href="https://scryfall.com/card/sos/125/molten-core-maestro" class="card-link" target="_blank">Molten-Core Maestro<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/2/326dfe32-3674-4a11-acd8-5ba62371235a.jpg?1775937832" alt="Molten-Core Maestro"></span></a> | 2/2 | 2 | R | Menace |
| <a href="https://scryfall.com/card/sos/134/thunderdrum-soloist" class="card-link" target="_blank">Thunderdrum Soloist<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/9/590d1d95-ed13-4121-899f-f5a2d8a6617a.jpg?1775937905" alt="Thunderdrum Soloist"></span></a> | 1/3 | 2 | U | Reach |
| <a href="https://scryfall.com/card/sos/109/blazing-firesinger-seething-song" class="card-link" target="_blank">Blazing Firesinger // Seething Song<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/b/3ba971e7-0b7a-4750-896f-7cf063e66b2a.jpg?1775937691" alt="Blazing Firesinger // Seething Song"></span></a> | 2/3 | 3 | U | - |
| <a href="https://scryfall.com/card/sos/110/charging-strifeknight" class="card-link" target="_blank">Charging Strifeknight<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/9/9940d992-1ba1-40ec-9b93-17d773452c4b.jpg?1775937699" alt="Charging Strifeknight"></span></a> | 3/3 | 3 | U | Haste |
| <a href="https://scryfall.com/card/sos/122/maelstrom-artisan-rocket-volley" class="card-link" target="_blank">Maelstrom Artisan // Rocket Volley<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/c/5c88391d-271f-4021-a5d9-158ebc1e6357.jpg?1775937805" alt="Maelstrom Artisan // Rocket Volley"></span></a> | 3/2 | 3 | R | Haste |
| <a href="https://scryfall.com/card/sos/128/rubble-rouser" class="card-link" target="_blank">Rubble Rouser<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/f/afe61957-a9bb-42b0-98e8-b5fa418cbaff.jpg?1775937860" alt="Rubble Rouser"></span></a> | 1/4 | 3 | C | - |
| <a href="https://scryfall.com/card/sos/131/strife-scholar-awaken-the-ages" class="card-link" target="_blank">Strife Scholar // Awaken the Ages<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/d/8de79312-2046-425e-9919-49afe19be81b.jpg?1775937883" alt="Strife Scholar // Awaken the Ages"></span></a> | 3/2 | 3 | C | Ward |
| <a href="https://scryfall.com/card/sos/116/garrison-excavator" class="card-link" target="_blank">Garrison Excavator<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/1/f11d2846-f181-4751-82ac-1e1ced6f46c7.jpg?1775937750" alt="Garrison Excavator"></span></a> | 3/4 | 4 | U | Menace |
| <a href="https://scryfall.com/card/sos/124/mica-reader-of-ruins" class="card-link" target="_blank">Mica, Reader of Ruins<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/4/949ad3ff-9e80-493c-a3ae-146b919bfcd7.jpg?1775937824" alt="Mica, Reader of Ruins"></span></a> | 4/4 | 4 | U | Ward |
| <a href="https://scryfall.com/card/sos/133/tackle-artist" class="card-link" target="_blank">Tackle Artist<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/8/b87e2474-98c1-4c1a-91ed-340b72d31653.jpg?1775937898" alt="Tackle Artist"></span></a> | 4/3 | 4 | C | Trample |
| <a href="https://scryfall.com/card/sos/126/pigment-wrangler-striking-palette" class="card-link" target="_blank">Pigment Wrangler // Striking Palette<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/2/c2faf4cf-c4b6-4721-ac06-0e045dd9704a.jpg?1775937841" alt="Pigment Wrangler // Striking Palette"></span></a> | 4/4 | 5 | U | Flying |
| <a href="https://scryfall.com/card/sos/127/rearing-embermare" class="card-link" target="_blank">Rearing Embermare<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/6/06dd56bd-de92-4202-af31-7e881c34d799.jpg?1775937851" alt="Rearing Embermare"></span></a> | 4/5 | 5 | C | Reach, Haste |
| <a href="https://scryfall.com/card/sos/123/magmablood-archaic" class="card-link" target="_blank">Magmablood Archaic<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/d/4d611278-9948-4345-b4dd-aa6eaf21b233.jpg?1775937816" alt="Magmablood Archaic"></span></a> | 2/2 | 6 | R | Trample, Reach |
| <a href="https://scryfall.com/card/sos/137/zealous-lorecaster" class="card-link" target="_blank">Zealous Lorecaster<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/6/36ab2130-9f21-4d30-873a-aa72d3d15fa8.jpg?1775937928" alt="Zealous Lorecaster"></span></a> | 4/4 | 6 | C | - |

#### Green

| Card | P/T | CMC | Rarity | Keywords |
|------|-----|-----|--------|----------|
| <a href="https://scryfall.com/card/sos/140/ambitious-augmenter" class="card-link" target="_blank">Ambitious Augmenter<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/5/85629088-2007-4db5-9397-bac12a3d7498.jpg?1775937950" alt="Ambitious Augmenter"></span></a> | 1/1 | 1 | R | - |
| <a href="https://scryfall.com/card/sos/160/slumbering-trudge" class="card-link" target="_blank">Slumbering Trudge<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/a/3a925370-58ac-4181-9acc-db7b0e0abf17.jpg?1775938094" alt="Slumbering Trudge"></span></a> | 6/6 | 1 | R | - |
| <a href="https://scryfall.com/card/sos/162/studious-first-year-rampant-growth" class="card-link" target="_blank">Studious First-Year // Rampant Growth<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/4/24f888dd-785c-4089-a89c-03f9080130ed.jpg?1775938109" alt="Studious First-Year // Rampant Growth"></span></a> | 1/1 | 1 | C | - |
| <a href="https://scryfall.com/card/sos/147/environmental-scientist" class="card-link" target="_blank">Environmental Scientist<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/2/f2bf6b36-43e4-49d9-98b2-cbb4304c248b.jpg?1775938001" alt="Environmental Scientist"></span></a> | 2/2 | 2 | U | - |
| <a href="https://scryfall.com/card/sos/152/infirmary-healer-stream-of-life" class="card-link" target="_blank">Infirmary Healer // Stream of Life<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/1/911442e3-3003-4683-a766-e791e9553667.jpg?1775938036" alt="Infirmary Healer // Stream of Life"></span></a> | 2/3 | 2 | U | - |
| <a href="https://scryfall.com/card/sos/154/mindful-biomancer" class="card-link" target="_blank">Mindful Biomancer<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/c/2c3a6eb8-ce0c-4dc8-9ed6-d2a9223eef53.jpg?1775938052" alt="Mindful Biomancer"></span></a> | 2/2 | 2 | C | - |
| <a href="https://scryfall.com/card/sos/155/noxious-newt" class="card-link" target="_blank">Noxious Newt<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/a/3a028306-c5d7-4f8f-b6f4-0d103fd47000.jpg?1775938060" alt="Noxious Newt"></span></a> | 1/2 | 2 | C | Deathtouch |
| <a href="https://scryfall.com/card/sos/145/emeritus-of-abundance-regrowth" class="card-link" target="_blank">Emeritus of Abundance // Regrowth<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/c/ac095763-6f4e-4d4e-9c99-414646368f8d.jpg?1775937986" alt="Emeritus of Abundance // Regrowth"></span></a> | 3/4 | 3 | M | Vigilance |
| <a href="https://scryfall.com/card/sos/146/emil-vastlands-roamer" class="card-link" target="_blank">Emil, Vastlands Roamer<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/6/3654416d-8558-4af2-9e10-18dbc8f2b376.jpg?1775937993" alt="Emil, Vastlands Roamer"></span></a> | 3/3 | 3 | U | - |
| <a href="https://scryfall.com/card/sos/159/shopkeepers-bane" class="card-link" target="_blank">Shopkeeper's Bane<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/7/97f7fbb9-228c-4a74-975b-38d3b6cecb32.jpg?1775938087" alt="Shopkeeper's Bane"></span></a> | 4/2 | 3 | C | Trample |
| <a href="https://scryfall.com/card/sos/164/thornfist-striker" class="card-link" target="_blank">Thornfist Striker<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/6/f6cb838e-a06a-46ae-a30f-e5192178c1cc.jpg?1775938123" alt="Thornfist Striker"></span></a> | 3/3 | 3 | U | Ward |
| <a href="https://scryfall.com/card/sos/165/topiary-lecturer" class="card-link" target="_blank">Topiary Lecturer<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/f/4f16a1c2-0a80-45e4-b025-3aa0c0b03812.jpg?1776000370" alt="Topiary Lecturer"></span></a> | 1/2 | 3 | U | - |
| <a href="https://scryfall.com/card/sos/166/vastlands-scavenger-bind-to-life" class="card-link" target="_blank">Vastlands Scavenger // Bind to Life<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/7/476b6a4d-cc05-4e98-8a45-a5c6582ec514.jpg?1775938136" alt="Vastlands Scavenger // Bind to Life"></span></a> | 4/4 | 3 | R | Deathtouch |
| <a href="https://scryfall.com/card/sos/138/aberrant-manawurm" class="card-link" target="_blank">Aberrant Manawurm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/9/797131cf-d80d-4050-bebd-2ce1d7fae5d0.jpg?1775937935" alt="Aberrant Manawurm"></span></a> | 2/5 | 4 | U | Trample |
| <a href="https://scryfall.com/card/sos/151/hungry-graffalon" class="card-link" target="_blank">Hungry Graffalon<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/3/030b1272-5990-4bc9-8fc1-82cc05602060.jpg?1775938030" alt="Hungry Graffalon"></span></a> | 3/4 | 4 | C | Reach |
| <a href="https://scryfall.com/card/sos/157/pestbrood-sloth" class="card-link" target="_blank">Pestbrood Sloth<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/1/c1251ae6-2f19-4f84-ab02-6a6cc7ce6056.jpg?1775938073" alt="Pestbrood Sloth"></span></a> | 4/4 | 4 | U | Reach |
| <a href="https://scryfall.com/card/sos/168/wildgrowth-archaic" class="card-link" target="_blank">Wildgrowth Archaic<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/e/0e6e2188-7203-4d10-a838-27233f283cd5.jpg?1775938149" alt="Wildgrowth Archaic"></span></a> | 0/0 | 4 | R | Trample, Reach |
| <a href="https://scryfall.com/card/sos/163/tenured-concocter" class="card-link" target="_blank">Tenured Concocter<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/7/376c8b7d-1c90-47e1-bd01-e4c67f3fc4fc.jpg?1775938116" alt="Tenured Concocter"></span></a> | 4/5 | 5 | C | Vigilance |

#### Multicolor

| Card | P/T | CMC | Rarity | Keywords |
|------|-----|-----|--------|----------|
| <a href="https://scryfall.com/card/sos/174/aziza-mage-tower-captain" class="card-link" target="_blank">Aziza, Mage Tower Captain<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/2/6261e89a-dbf1-481a-823e-6bb00be57195.jpg?1775938194" alt="Aziza, Mage Tower Captain"></span></a> | 2/2 | 2 | R | - |
| <a href="https://scryfall.com/card/sos/177/bogwater-lumaret" class="card-link" target="_blank">Bogwater Lumaret<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/a/7a42f51a-3377-47bb-b6fb-c0515bf1dcfb.jpg?1775938216" alt="Bogwater Lumaret"></span></a> | 2/2 | 2 | C | - |
| <a href="https://scryfall.com/card/sos/183/cuboid-colony" class="card-link" target="_blank">Cuboid Colony<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/3/6384d135-7780-4d75-9e95-71bce506948e.jpg?1775938265" alt="Cuboid Colony"></span></a> | 1/1 | 2 | U | Flying, Trample, Flash |
| <a href="https://scryfall.com/card/sos/191/geometers-arthropod" class="card-link" target="_blank">Geometer's Arthropod<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/c/ec0f3613-1edc-40e8-8f26-2e5ef13be55e.jpg?1775938325" alt="Geometer's Arthropod"></span></a> | 1/4 | 2 | R | - |
| <a href="https://scryfall.com/card/sos/194/hardened-academic" class="card-link" target="_blank">Hardened Academic<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/6/06c9e8a7-2840-4cff-90af-c6636e598f78.jpg?1775938346" alt="Hardened Academic"></span></a> | 2/1 | 2 | R | Flying, Haste |
| <a href="https://scryfall.com/card/sos/196/inkling-mascot" class="card-link" target="_blank">Inkling Mascot<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/d/6d4a2f39-0e1e-4076-815a-2676a09a1aab.jpg?1775938360" alt="Inkling Mascot"></span></a> | 2/2 | 2 | C | - |
| <a href="https://scryfall.com/card/sos/198/kirol-history-buff-pack-a-punch" class="card-link" target="_blank">Kirol, History Buff // Pack a Punch<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/7/676ba521-66e4-42cf-a315-70d03cb7334e.jpg?1775938375" alt="Kirol, History Buff // Pack a Punch"></span></a> | 2/3 | 2 | U | - |
| <a href="https://scryfall.com/card/sos/215/pterafractyl" class="card-link" target="_blank">Pterafractyl<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/c/ecd33152-e290-4505-addd-a8d08cefdddd.jpg?1775938495" alt="Pterafractyl"></span></a> | 1/0 | 2 | C | Flying |
| <a href="https://scryfall.com/card/sos/223/sanar-unfinished-genius-wild-idea" class="card-link" target="_blank">Sanar, Unfinished Genius // Wild Idea<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/7/173157aa-712d-44f2-89ba-dd2511a07f26.jpg?1775938553" alt="Sanar, Unfinished Genius // Wild Idea"></span></a> | 0/4 | 2 | U | - |
| <a href="https://scryfall.com/card/sos/224/scolding-administrator" class="card-link" target="_blank">Scolding Administrator<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/9/69757177-aefa-44a6-81db-5ae9b5d2f117.jpg?1775938562" alt="Scolding Administrator"></span></a> | 2/2 | 2 | U | Menace |
| <a href="https://scryfall.com/card/sos/230/spirit-mascot" class="card-link" target="_blank">Spirit Mascot<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/2/123f1fde-d8de-4640-baa1-bb3781713168.jpg?1775938605" alt="Spirit Mascot"></span></a> | 2/2 | 2 | C | - |
| <a href="https://scryfall.com/card/sos/238/teachers-pest" class="card-link" target="_blank">Teacher's Pest<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/a/eaa358ac-761d-4507-aa15-3d4684027207.jpg?1775938661" alt="Teacher's Pest"></span></a> | 1/1 | 2 | U | Menace |
| <a href="https://scryfall.com/card/sos/170/abigale-poet-laureate-heroic-stanza" class="card-link" target="_blank">Abigale, Poet Laureate // Heroic Stanza<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/7/77285d12-e658-4eb3-ba13-ff202afab9c8.jpg?1775938164" alt="Abigale, Poet Laureate // Heroic Stanza"></span></a> | 2/3 | 3 | U | Flying |
| <a href="https://scryfall.com/card/sos/171/abstract-paintmage" class="card-link" target="_blank">Abstract Paintmage<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/a/ea008094-d995-4740-9b39-c61049356c55.jpg?1775938173" alt="Abstract Paintmage"></span></a> | 2/2 | 3 | U | - |
| <a href="https://scryfall.com/card/sos/176/blech-loafing-pest" class="card-link" target="_blank">Blech, Loafing Pest<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/5/f588fa50-7cc5-41ba-90df-2d252eb5c785.jpg?1775938208" alt="Blech, Loafing Pest"></span></a> | 3/4 | 3 | R | - |
| <a href="https://scryfall.com/card/sos/180/colorstorm-stallion" class="card-link" target="_blank">Colorstorm Stallion<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/5/f5b54d46-2caf-4d1b-8be1-dbd9e9dce058.jpg?1775938240" alt="Colorstorm Stallion"></span></a> | 3/3 | 3 | R | Haste, Ward |
| <a href="https://scryfall.com/card/sos/185/elemental-mascot" class="card-link" target="_blank">Elemental Mascot<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/5/c507eb1c-48e9-4d28-bb2d-71f2a9df9ab0.jpg?1775938280" alt="Elemental Mascot"></span></a> | 1/4 | 3 | C | Flying, Vigilance |
| <a href="https://scryfall.com/card/sos/187/essenceknit-scholar" class="card-link" target="_blank">Essenceknit Scholar<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/a/2a3cba55-3fae-4d45-ae03-4d662ec13718.jpg?1775938295" alt="Essenceknit Scholar"></span></a> | 3/1 | 3 | U | - |
| <a href="https://scryfall.com/card/sos/195/imperious-inkmage" class="card-link" target="_blank">Imperious Inkmage<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/5/d5df1c3f-2536-4476-b8cd-34b026c38366.jpg?1775938353" alt="Imperious Inkmage"></span></a> | 3/3 | 3 | C | Vigilance |
| <a href="https://scryfall.com/card/sos/206/nita-forum-conciliator" class="card-link" target="_blank">Nita, Forum Conciliator<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/d/fd80a87d-35d3-4ad1-8172-c85e93032d1d.jpg?1775938431" alt="Nita, Forum Conciliator"></span></a> | 2/3 | 3 | R | - |
| <a href="https://scryfall.com/card/sos/208/paradox-surveyor" class="card-link" target="_blank">Paradox Surveyor<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/7/d7cb1af2-0302-46ff-8303-ae9d07541a01.jpg?1775938445" alt="Paradox Surveyor"></span></a> | 3/3 | 3 | U | Reach |
| <a href="https://scryfall.com/card/sos/209/pest-mascot" class="card-link" target="_blank">Pest Mascot<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/8/d882beb9-6766-4818-afbb-f6fd7a2d5b70.jpg?1775938452" alt="Pest Mascot"></span></a> | 2/3 | 3 | C | Trample |
| <a href="https://scryfall.com/card/sos/210/practiced-scrollsmith" class="card-link" target="_blank">Practiced Scrollsmith<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/0/40075e3f-58b3-47fd-8fbe-4b301e9ce7a1.jpg?1775938459" alt="Practiced Scrollsmith"></span></a> | 3/2 | 3 | U | First Strike |
| <a href="https://scryfall.com/card/sos/227/snooping-page" class="card-link" target="_blank">Snooping Page<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/3/73d06987-8686-461b-b260-9a4fee6a3b32.jpg?1775938584" alt="Snooping Page"></span></a> | 2/3 | 3 | U | - |
| <a href="https://scryfall.com/card/sos/175/berta-wise-extrapolator" class="card-link" target="_blank">Berta, Wise Extrapolator<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/5/75f89c36-c81d-4580-9a5c-218fed0c5c9a.jpg?1775938201" alt="Berta, Wise Extrapolator"></span></a> | 1/4 | 4 | R | - |
| <a href="https://scryfall.com/card/sos/182/conciliators-duelist" class="card-link" target="_blank">Conciliator's Duelist<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/2/e225929b-6197-4550-969e-3c4a97206a68.jpg?1775938257" alt="Conciliator's Duelist"></span></a> | 4/3 | 4 | R | - |
| <a href="https://scryfall.com/card/sos/199/lluwen-exchange-student-pest-friend" class="card-link" target="_blank">Lluwen, Exchange Student // Pest Friend<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/0/a0bcb638-c3c8-4973-9537-5c471f43f34f.jpg?1775938382" alt="Lluwen, Exchange Student // Pest Friend"></span></a> | 3/4 | 4 | U | - |
| <a href="https://scryfall.com/card/sos/207/old-growth-educator" class="card-link" target="_blank">Old-Growth Educator<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/b/eb7e858a-9b85-49b2-a379-ee656b64935a.jpg?1775938438" alt="Old-Growth Educator"></span></a> | 4/4 | 4 | U | Vigilance, Reach |
| <a href="https://scryfall.com/card/sos/226/silverquill-the-disputant" class="card-link" target="_blank">Silverquill, the Disputant<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/7/1742c9cd-5ba0-4335-9999-acc7f9d4f73c.jpg?1775938577" alt="Silverquill, the Disputant"></span></a> | 4/4 | 4 | M | Flying, Vigilance |
| <a href="https://scryfall.com/card/sos/229/spectacular-skywhale" class="card-link" target="_blank">Spectacular Skywhale<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/9/c90366d5-b4ba-4772-a3c5-f138bbe7f305.jpg?1775938597" alt="Spectacular Skywhale"></span></a> | 1/4 | 4 | U | Flying |
| <a href="https://scryfall.com/card/sos/232/stadium-tidalmage" class="card-link" target="_blank">Stadium Tidalmage<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/6/a689289e-7141-4950-8a87-82e9bd6846fe.jpg?1775938619" alt="Stadium Tidalmage"></span></a> | 4/4 | 4 | C | - |
| <a href="https://scryfall.com/card/sos/233/startled-relic-sloth" class="card-link" target="_blank">Startled Relic Sloth<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/1/f143fd41-58c3-45a0-bef8-e9e4b4a502a5.jpg?1775938628" alt="Startled Relic Sloth"></span></a> | 4/4 | 4 | U | Trample, Lifelink |
| <a href="https://scryfall.com/card/sos/237/tam-observant-sequencer-deep-sight" class="card-link" target="_blank">Tam, Observant Sequencer // Deep Sight<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/1/7120e71b-2976-451b-89a7-a1665dc6fb6b.jpg?1775938655" alt="Tam, Observant Sequencer // Deep Sight"></span></a> | 4/3 | 4 | U | - |
| <a href="https://scryfall.com/card/sos/190/fractal-tender" class="card-link" target="_blank">Fractal Tender<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/a/ea7f5262-4ddb-410a-be72-4bac6af9b4ec.jpg?1775938318" alt="Fractal Tender"></span></a> | 3/3 | 5 | U | Ward |
| <a href="https://scryfall.com/card/sos/201/lorehold-the-historian" class="card-link" target="_blank">Lorehold, the Historian<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/1/71a6701f-40f1-43ef-bff5-a5907fd67cd6.jpg?1775938396" alt="Lorehold, the Historian"></span></a> | 5/5 | 5 | M | Flying, Haste |
| <a href="https://scryfall.com/card/sos/234/stirring-honormancer" class="card-link" target="_blank">Stirring Honormancer<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/e/ee84b04d-78fc-416f-9166-72e5417c3e17.jpg?1775938634" alt="Stirring Honormancer"></span></a> | 4/5 | 5 | U | - |
| <a href="https://scryfall.com/card/sos/181/colossus-of-the-blood-age" class="card-link" target="_blank">Colossus of the Blood Age<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/f/bfa7f0a4-6b65-4e53-ba00-848df260d8e3.jpg?1775938248" alt="Colossus of the Blood Age"></span></a> | 6/6 | 6 | U | - |
| <a href="https://scryfall.com/card/sos/189/fractal-mascot" class="card-link" target="_blank">Fractal Mascot<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/f/cf5b19e3-eed1-4b36-9756-660ffb3baa08.jpg?1775938311" alt="Fractal Mascot"></span></a> | 6/6 | 6 | C | Trample |
| <a href="https://scryfall.com/card/sos/218/quandrix-the-proof" class="card-link" target="_blank">Quandrix, the Proof<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/1/015afe31-af3c-4c9b-9997-d7c33b915a33.jpg?1775938517" alt="Quandrix, the Proof"></span></a> | 6/6 | 6 | M | Flying, Trample |
| <a href="https://scryfall.com/card/sos/212/prismari-the-inspiration" class="card-link" target="_blank">Prismari, the Inspiration<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/6/767ff9fa-4e7f-421a-b911-45186b520ae1.jpg?1775938472" alt="Prismari, the Inspiration"></span></a> | 7/7 | 7 | M | Flying, Ward |
| <a href="https://scryfall.com/card/sos/246/zaffai-and-the-tempests" class="card-link" target="_blank">Zaffai and the Tempests<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/b/5bdbf507-6fd7-49f6-b437-8f2ce2d0eb0f.jpg?1775938717" alt="Zaffai and the Tempests"></span></a> | 5/7 | 7 | R | - |
| <a href="https://scryfall.com/card/sos/245/witherbloom-the-balancer" class="card-link" target="_blank">Witherbloom, the Balancer<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/d/ed7b2361-97c6-49e2-bf0b-4770f4ffe2f0.jpg?1775938710" alt="Witherbloom, the Balancer"></span></a> | 5/5 | 8 | M | Flying, Deathtouch |

#### Colorless

| Card | P/T | CMC | Rarity | Keywords |
|------|-----|-----|--------|----------|
| <a href="https://scryfall.com/card/sos/249/mage-tower-referee" class="card-link" target="_blank">Mage Tower Referee<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/c/1ceb704a-97a8-49f9-b799-30f001404144.jpg?1775938737" alt="Mage Tower Referee"></span></a> | 2/1 | 2 | C | - |
| <a href="https://scryfall.com/card/sos/250/page-loose-leaf" class="card-link" target="_blank">Page, Loose Leaf<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/c/8c6fecfd-8241-4cf0-b1eb-19472b99e0ed.jpg?1775938744" alt="Page, Loose Leaf"></span></a> | 0/2 | 2 | C | - |
| <a href="https://scryfall.com/card/sos/247/biblioplex-tomekeeper" class="card-link" target="_blank">Biblioplex Tomekeeper<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/f/bf2efdd9-d2b4-4bea-a5b9-dbb2eee4dfba.jpg?1775938724" alt="Biblioplex Tomekeeper"></span></a> | 3/4 | 4 | C | - |
| <a href="https://scryfall.com/card/sos/2/rancorous-archaic" class="card-link" target="_blank">Rancorous Archaic<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/5/2565e16a-ed31-4867-adb8-f1633d580397.jpg?1775936927" alt="Rancorous Archaic"></span></a> | 2/2 | 5 | C | Trample, Reach |
| <a href="https://scryfall.com/card/sos/3/sundering-archaic" class="card-link" target="_blank">Sundering Archaic<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/3/c35b57e4-2358-46c0-8f09-cd27c10eaf2d.jpg?1775936933" alt="Sundering Archaic"></span></a> | 3/3 | 6 | U | - |
| <a href="https://scryfall.com/card/sos/5/transcendent-archaic" class="card-link" target="_blank">Transcendent Archaic<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/6/1624c680-502b-474a-b9b2-888fe3ca008c.jpg?1775936948" alt="Transcendent Archaic"></span></a> | 6/6 | 7 | U | Vigilance |
| <a href="https://scryfall.com/card/sos/1/the-dawning-archaic" class="card-link" target="_blank">The Dawning Archaic<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/a/7a451985-37e1-44d8-839b-dc1e88df5c96.jpg?1775936921" alt="The Dawning Archaic"></span></a> | 7/7 | 10 | M | Reach |

### Evasion Creatures

*Creatures with flying, menace, trample, or that can't be blocked.*

#### White

| Card | P/T | CMC | Rarity | Evasion |
|------|-----|-----|--------|---------|
| <a href="https://scryfall.com/card/sos/24/owlin-historian" class="card-link" target="_blank">Owlin Historian<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/f/5fe99be0-e1ec-485e-82f8-02eba7b82441.jpg?1775937078" alt="Owlin Historian"></span></a> | 2/3 | 3 | C | Flying |
| <a href="https://scryfall.com/card/sos/32/soaring-stoneglider" class="card-link" target="_blank">Soaring Stoneglider<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/f/2fbe446b-60fd-43da-8358-985392293af8.jpg?1775937136" alt="Soaring Stoneglider"></span></a> | 4/3 | 3 | U | Flying |
| <a href="https://scryfall.com/card/sos/35/stirring-hopesinger" class="card-link" target="_blank">Stirring Hopesinger<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/1/21375667-b318-47f8-a482-9c8c2b5b14c0.jpg?1775937157" alt="Stirring Hopesinger"></span></a> | 1/3 | 3 | R | Flying |
| <a href="https://scryfall.com/card/sos/8/ascendant-dustspeaker" class="card-link" target="_blank">Ascendant Dustspeaker<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/e/de3de40b-a7ac-455e-add2-4e451b602d17.jpg?1776000359" alt="Ascendant Dustspeaker"></span></a> | 3/4 | 5 | C | Flying |

#### Blue

| Card | P/T | CMC | Rarity | Evasion |
|------|-----|-----|--------|---------|
| <a href="https://scryfall.com/card/sos/46/encouraging-aviator-jump" class="card-link" target="_blank">Encouraging Aviator // Jump<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/2/72654b84-9902-41db-92ab-a3499c31221c.jpg?1775937230" alt="Encouraging Aviator // Jump"></span></a> | 2/3 | 3 | U | Flying |
| <a href="https://scryfall.com/card/sos/59/matterbending-mage" class="card-link" target="_blank">Matterbending Mage<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/6/460c6afd-cddf-4fea-925f-b27517ff250a.jpg?1775937321" alt="Matterbending Mage"></span></a> | 2/2 | 3 | U | Unblockable |
| <a href="https://scryfall.com/card/sos/67/skycoach-conductor-all-aboard" class="card-link" target="_blank">Skycoach Conductor // All Aboard<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/e/4ecbca71-9a1d-44c5-b709-d6f565941d5e.jpg?1775937376" alt="Skycoach Conductor // All Aboard"></span></a> | 2/3 | 3 | R | Flying |
| <a href="https://scryfall.com/card/sos/68/spellbook-seeker-careful-study" class="card-link" target="_blank">Spellbook Seeker // Careful Study<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/c/cc44eaa4-59a4-419e-b1d1-d92f354ff588.jpg?1775937383" alt="Spellbook Seeker // Careful Study"></span></a> | 3/3 | 4 | C | Flying |
| <a href="https://scryfall.com/card/sos/45/emeritus-of-ideation-ancestral-recall" class="card-link" target="_blank">Emeritus of Ideation // Ancestral Recall<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/5/75961d36-acf6-425f-9698-0bf52af74f31.jpg?1775937223" alt="Emeritus of Ideation // Ancestral Recall"></span></a> | 5/5 | 5 | M | Flying |

#### Black

| Card | P/T | CMC | Rarity | Evasion |
|------|-----|-----|--------|---------|
| <a href="https://scryfall.com/card/sos/99/scheming-silvertongue-sign-in-blood" class="card-link" target="_blank">Scheming Silvertongue // Sign in Blood<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/e/fe85a124-0d8b-4a29-8df1-65888a39147f.jpg?1775937600" alt="Scheming Silvertongue // Sign in Blood"></span></a> | 1/3 | 2 | R | Flying |
| <a href="https://scryfall.com/card/sos/91/moseo-veins-new-dean" class="card-link" target="_blank">Moseo, Vein's New Dean<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/8/6877180c-22a1-4c4d-9178-316f4c34661b.jpg?1775937545" alt="Moseo, Vein's New Dean"></span></a> | 2/1 | 3 | R | Flying |
| <a href="https://scryfall.com/card/sos/103/ulna-alley-shopkeep" class="card-link" target="_blank">Ulna Alley Shopkeep<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/2/c25e1ae5-f17c-4eee-98f1-5681981af31c.jpg?1775937633" alt="Ulna Alley Shopkeep"></span></a> | 2/3 | 3 | C | Menace, Unblockable |
| <a href="https://scryfall.com/card/sos/102/tragedy-feaster" class="card-link" target="_blank">Tragedy Feaster<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/9/b93cbaad-8ed8-4a1d-b95a-20a616dfedc9.jpg?1775937623" alt="Tragedy Feaster"></span></a> | 7/6 | 4 | R | Trample |
| <a href="https://scryfall.com/card/sos/101/sneering-shadewriter" class="card-link" target="_blank">Sneering Shadewriter<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/b/4b4c120e-abe9-4f11-a7e4-bc3f723da4b2.jpg?1775937615" alt="Sneering Shadewriter"></span></a> | 3/3 | 5 | C | Flying |

#### Red

| Card | P/T | CMC | Rarity | Evasion |
|------|-----|-----|--------|---------|
| <a href="https://scryfall.com/card/sos/125/molten-core-maestro" class="card-link" target="_blank">Molten-Core Maestro<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/2/326dfe32-3674-4a11-acd8-5ba62371235a.jpg?1775937832" alt="Molten-Core Maestro"></span></a> | 2/2 | 2 | R | Menace |
| <a href="https://scryfall.com/card/sos/116/garrison-excavator" class="card-link" target="_blank">Garrison Excavator<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/1/f11d2846-f181-4751-82ac-1e1ced6f46c7.jpg?1775937750" alt="Garrison Excavator"></span></a> | 3/4 | 4 | U | Menace, Unblockable |
| <a href="https://scryfall.com/card/sos/133/tackle-artist" class="card-link" target="_blank">Tackle Artist<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/8/b87e2474-98c1-4c1a-91ed-340b72d31653.jpg?1775937898" alt="Tackle Artist"></span></a> | 4/3 | 4 | C | Trample |
| <a href="https://scryfall.com/card/sos/126/pigment-wrangler-striking-palette" class="card-link" target="_blank">Pigment Wrangler // Striking Palette<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/2/c2faf4cf-c4b6-4721-ac06-0e045dd9704a.jpg?1775937841" alt="Pigment Wrangler // Striking Palette"></span></a> | 4/4 | 5 | U | Flying |
| <a href="https://scryfall.com/card/sos/123/magmablood-archaic" class="card-link" target="_blank">Magmablood Archaic<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/d/4d611278-9948-4345-b4dd-aa6eaf21b233.jpg?1775937816" alt="Magmablood Archaic"></span></a> | 2/2 | 6 | R | Trample |

#### Green

| Card | P/T | CMC | Rarity | Evasion |
|------|-----|-----|--------|---------|
| <a href="https://scryfall.com/card/sos/159/shopkeepers-bane" class="card-link" target="_blank">Shopkeeper's Bane<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/7/97f7fbb9-228c-4a74-975b-38d3b6cecb32.jpg?1775938087" alt="Shopkeeper's Bane"></span></a> | 4/2 | 3 | C | Trample |
| <a href="https://scryfall.com/card/sos/138/aberrant-manawurm" class="card-link" target="_blank">Aberrant Manawurm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/9/797131cf-d80d-4050-bebd-2ce1d7fae5d0.jpg?1775937935" alt="Aberrant Manawurm"></span></a> | 2/5 | 4 | U | Trample |
| <a href="https://scryfall.com/card/sos/168/wildgrowth-archaic" class="card-link" target="_blank">Wildgrowth Archaic<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/e/0e6e2188-7203-4d10-a838-27233f283cd5.jpg?1775938149" alt="Wildgrowth Archaic"></span></a> | 0/0 | 4 | R | Trample |

#### Multicolor

| Card | P/T | CMC | Rarity | Evasion |
|------|-----|-----|--------|---------|
| <a href="https://scryfall.com/card/sos/183/cuboid-colony" class="card-link" target="_blank">Cuboid Colony<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/3/6384d135-7780-4d75-9e95-71bce506948e.jpg?1775938265" alt="Cuboid Colony"></span></a> | 1/1 | 2 | U | Flying, Trample |
| <a href="https://scryfall.com/card/sos/194/hardened-academic" class="card-link" target="_blank">Hardened Academic<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/6/06c9e8a7-2840-4cff-90af-c6636e598f78.jpg?1775938346" alt="Hardened Academic"></span></a> | 2/1 | 2 | R | Flying |
| <a href="https://scryfall.com/card/sos/215/pterafractyl" class="card-link" target="_blank">Pterafractyl<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/c/ecd33152-e290-4505-addd-a8d08cefdddd.jpg?1775938495" alt="Pterafractyl"></span></a> | 1/0 | 2 | C | Flying |
| <a href="https://scryfall.com/card/sos/224/scolding-administrator" class="card-link" target="_blank">Scolding Administrator<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/9/69757177-aefa-44a6-81db-5ae9b5d2f117.jpg?1775938562" alt="Scolding Administrator"></span></a> | 2/2 | 2 | U | Menace, Unblockable |
| <a href="https://scryfall.com/card/sos/238/teachers-pest" class="card-link" target="_blank">Teacher's Pest<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/a/eaa358ac-761d-4507-aa15-3d4684027207.jpg?1775938661" alt="Teacher's Pest"></span></a> | 1/1 | 2 | U | Menace, Unblockable |
| <a href="https://scryfall.com/card/sos/170/abigale-poet-laureate-heroic-stanza" class="card-link" target="_blank">Abigale, Poet Laureate // Heroic Stanza<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/7/77285d12-e658-4eb3-ba13-ff202afab9c8.jpg?1775938164" alt="Abigale, Poet Laureate // Heroic Stanza"></span></a> | 2/3 | 3 | U | Flying |
| <a href="https://scryfall.com/card/sos/185/elemental-mascot" class="card-link" target="_blank">Elemental Mascot<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/5/c507eb1c-48e9-4d28-bb2d-71f2a9df9ab0.jpg?1775938280" alt="Elemental Mascot"></span></a> | 1/4 | 3 | C | Flying |
| <a href="https://scryfall.com/card/sos/209/pest-mascot" class="card-link" target="_blank">Pest Mascot<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/8/d882beb9-6766-4818-afbb-f6fd7a2d5b70.jpg?1775938452" alt="Pest Mascot"></span></a> | 2/3 | 3 | C | Trample |
| <a href="https://scryfall.com/card/sos/227/snooping-page" class="card-link" target="_blank">Snooping Page<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/3/73d06987-8686-461b-b260-9a4fee6a3b32.jpg?1775938584" alt="Snooping Page"></span></a> | 2/3 | 3 | U | Unblockable |
| <a href="https://scryfall.com/card/sos/226/silverquill-the-disputant" class="card-link" target="_blank">Silverquill, the Disputant<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/7/1742c9cd-5ba0-4335-9999-acc7f9d4f73c.jpg?1775938577" alt="Silverquill, the Disputant"></span></a> | 4/4 | 4 | M | Flying |
| <a href="https://scryfall.com/card/sos/229/spectacular-skywhale" class="card-link" target="_blank">Spectacular Skywhale<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/9/c90366d5-b4ba-4772-a3c5-f138bbe7f305.jpg?1775938597" alt="Spectacular Skywhale"></span></a> | 1/4 | 4 | U | Flying |
| <a href="https://scryfall.com/card/sos/233/startled-relic-sloth" class="card-link" target="_blank">Startled Relic Sloth<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/1/f143fd41-58c3-45a0-bef8-e9e4b4a502a5.jpg?1775938628" alt="Startled Relic Sloth"></span></a> | 4/4 | 4 | U | Trample |
| <a href="https://scryfall.com/card/sos/201/lorehold-the-historian" class="card-link" target="_blank">Lorehold, the Historian<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/1/71a6701f-40f1-43ef-bff5-a5907fd67cd6.jpg?1775938396" alt="Lorehold, the Historian"></span></a> | 5/5 | 5 | M | Flying |
| <a href="https://scryfall.com/card/sos/189/fractal-mascot" class="card-link" target="_blank">Fractal Mascot<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/f/cf5b19e3-eed1-4b36-9756-660ffb3baa08.jpg?1775938311" alt="Fractal Mascot"></span></a> | 6/6 | 6 | C | Trample |
| <a href="https://scryfall.com/card/sos/218/quandrix-the-proof" class="card-link" target="_blank">Quandrix, the Proof<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/1/015afe31-af3c-4c9b-9997-d7c33b915a33.jpg?1775938517" alt="Quandrix, the Proof"></span></a> | 6/6 | 6 | M | Flying, Trample |
| <a href="https://scryfall.com/card/sos/212/prismari-the-inspiration" class="card-link" target="_blank">Prismari, the Inspiration<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/6/767ff9fa-4e7f-421a-b911-45186b520ae1.jpg?1775938472" alt="Prismari, the Inspiration"></span></a> | 7/7 | 7 | M | Flying |
| <a href="https://scryfall.com/card/sos/245/witherbloom-the-balancer" class="card-link" target="_blank">Witherbloom, the Balancer<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/d/ed7b2361-97c6-49e2-bf0b-4770f4ffe2f0.jpg?1775938710" alt="Witherbloom, the Balancer"></span></a> | 5/5 | 8 | M | Flying |

#### Colorless

| Card | P/T | CMC | Rarity | Evasion |
|------|-----|-----|--------|---------|
| <a href="https://scryfall.com/card/sos/2/rancorous-archaic" class="card-link" target="_blank">Rancorous Archaic<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/5/2565e16a-ed31-4867-adb8-f1633d580397.jpg?1775936927" alt="Rancorous Archaic"></span></a> | 2/2 | 5 | C | Trample |

### ETB Creatures (Enters-the-Battlefield)

*Creatures with enters-the-battlefield triggers -- key for limited value.*

#### White

| Card | P/T | CMC | Rarity | ETB Effect |
|------|-----|-----|--------|------------|
| <a href="https://scryfall.com/card/sos/14/ennis-debate-moderator" class="card-link" target="_blank">Ennis, Debate Moderator<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/2/d2ef31b4-24fa-4443-9f05-c8e99c3522e5.jpg?1775937005" alt="Ennis, Debate Moderator"></span></a> | 1/1 | 2 | U | exile up to one other target creature you control. Return that card to the battlefield und |
| <a href="https://scryfall.com/card/sos/13/emeritus-of-truce-swords-to-plowshares" class="card-link" target="_blank">Emeritus of Truce // Swords to Plowshares<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/8/9869a753-5e41-4098-ab41-e75b4396ec50.jpg?1775936999" alt="Emeritus of Truce // Swords to Plowshares"></span></a> | 3/3 | 3 | M | target player creates a 1/1 white and black Inkling creature token with flying. Then if an |
| <a href="https://scryfall.com/card/sos/24/owlin-historian" class="card-link" target="_blank">Owlin Historian<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/f/5fe99be0-e1ec-485e-82f8-02eba7b82441.jpg?1775937078" alt="Owlin Historian"></span></a> | 2/3 | 3 | C | surveil 1. (Look at the top card of your library. You may put it into your graveyard.) |
| <a href="https://scryfall.com/card/sos/11/eager-glyphmage" class="card-link" target="_blank">Eager Glyphmage<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/f/bf736de9-9bc4-49df-ae60-672ed4f83f32.jpg?1775936986" alt="Eager Glyphmage"></span></a> | 3/3 | 4 | C | create a 1/1 white and black Inkling creature token with flying. |
| <a href="https://scryfall.com/card/sos/8/ascendant-dustspeaker" class="card-link" target="_blank">Ascendant Dustspeaker<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/e/de3de40b-a7ac-455e-add2-4e451b602d17.jpg?1776000359" alt="Ascendant Dustspeaker"></span></a> | 3/4 | 5 | C | put a +1/+1 counter on another target creature you control. |

#### Blue

| Card | P/T | CMC | Rarity | ETB Effect |
|------|-----|-----|--------|------------|
| <a href="https://scryfall.com/card/sos/42/deluge-virtuoso" class="card-link" target="_blank">Deluge Virtuoso<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/e/2e3b16ed-8727-48fd-8b1f-c0cbd329385e.jpg?1775937202" alt="Deluge Virtuoso"></span></a> | 2/2 | 3 | C | tap target creature an opponent controls and put a stun counter on it. (If a permanent wit |
| <a href="https://scryfall.com/card/sos/55/jadzi-steward-of-fate-oracles-gift" class="card-link" target="_blank">Jadzi, Steward of Fate // Oracle's Gift<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/9/a95b6baf-01e6-49c3-9a26-394b127d53c3.jpg?1775937293" alt="Jadzi, Steward of Fate // Oracle's Gift"></span></a> | 2/4 | 3 | R | prepared. (While it's prepared, you may cast a copy of its spell. Doing so unprepares it.) |
| <a href="https://scryfall.com/card/sos/59/matterbending-mage" class="card-link" target="_blank">Matterbending Mage<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/6/460c6afd-cddf-4fea-925f-b27517ff250a.jpg?1775937321" alt="Matterbending Mage"></span></a> | 2/2 | 3 | U | return up to one other target creature to its owner's hand. |
| <a href="https://scryfall.com/card/sos/70/textbook-tabulator" class="card-link" target="_blank">Textbook Tabulator<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/6/56f54fee-b48d-4582-8982-ca4c7b8ef553.jpg?1776000387" alt="Textbook Tabulator"></span></a> | 0/3 | 3 | C | surveil 2. (Look at the top two cards of your library, then put any number of them into yo |
| <a href="https://scryfall.com/card/sos/62/orysa-tide-choreographer" class="card-link" target="_blank">Orysa, Tide Choreographer<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/1/010ed379-63f5-452c-9cd4-00d51647c0e3.jpg?1775937343" alt="Orysa, Tide Choreographer"></span></a> | 2/2 | 5 | U | draw two cards. |

#### Black

| Card | P/T | CMC | Rarity | ETB Effect |
|------|-----|-----|--------|------------|
| <a href="https://scryfall.com/card/sos/91/moseo-veins-new-dean" class="card-link" target="_blank">Moseo, Vein's New Dean<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/8/6877180c-22a1-4c4d-9178-316f4c34661b.jpg?1775937545" alt="Moseo, Vein's New Dean"></span></a> | 2/1 | 3 | R | create a 1/1 black and green Pest creature token with "Whenever this token attacks, you ga |
| <a href="https://scryfall.com/card/sos/92/poisoners-apprentice" class="card-link" target="_blank">Poisoner's Apprentice<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/7/3755a2e9-af55-4625-a006-2a86c7893a96.jpg?1775937552" alt="Poisoner's Apprentice"></span></a> | 2/2 | 3 | U | target creature an opponent controls gets -4/-4 until end of turn if you gained life this  |
| <a href="https://scryfall.com/card/sos/101/sneering-shadewriter" class="card-link" target="_blank">Sneering Shadewriter<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/b/4b4c120e-abe9-4f11-a7e4-bc3f723da4b2.jpg?1775937615" alt="Sneering Shadewriter"></span></a> | 3/3 | 5 | C | each opponent loses 2 life and you gain 2 life. |

#### Red

| Card | P/T | CMC | Rarity | ETB Effect |
|------|-----|-----|--------|------------|
| <a href="https://scryfall.com/card/sos/128/rubble-rouser" class="card-link" target="_blank">Rubble Rouser<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/f/afe61957-a9bb-42b0-98e8-b5fa418cbaff.jpg?1775937860" alt="Rubble Rouser"></span></a> | 1/4 | 3 | C | you may discard a card. If you do, draw a card. |
| <a href="https://scryfall.com/card/sos/137/zealous-lorecaster" class="card-link" target="_blank">Zealous Lorecaster<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/6/36ab2130-9f21-4d30-873a-aa72d3d15fa8.jpg?1775937928" alt="Zealous Lorecaster"></span></a> | 4/4 | 6 | C | return target instant or sorcery card from your graveyard to your hand. |

#### Green

| Card | P/T | CMC | Rarity | ETB Effect |
|------|-----|-----|--------|------------|
| <a href="https://scryfall.com/card/sos/147/environmental-scientist" class="card-link" target="_blank">Environmental Scientist<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/2/f2bf6b36-43e4-49d9-98b2-cbb4304c248b.jpg?1775938001" alt="Environmental Scientist"></span></a> | 2/2 | 2 | U | you may search your library for a basic land card, reveal it, put it into your hand, then  |
| <a href="https://scryfall.com/card/sos/154/mindful-biomancer" class="card-link" target="_blank">Mindful Biomancer<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/c/2c3a6eb8-ce0c-4dc8-9ed6-d2a9223eef53.jpg?1775938052" alt="Mindful Biomancer"></span></a> | 2/2 | 2 | C | you gain 1 life. |

#### Multicolor

| Card | P/T | CMC | Rarity | ETB Effect |
|------|-----|-----|--------|------------|
| <a href="https://scryfall.com/card/sos/177/bogwater-lumaret" class="card-link" target="_blank">Bogwater Lumaret<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/a/7a42f51a-3377-47bb-b6fb-c0515bf1dcfb.jpg?1775938216" alt="Bogwater Lumaret"></span></a> | 2/2 | 2 | C | you gain 1 life. |
| <a href="https://scryfall.com/card/sos/215/pterafractyl" class="card-link" target="_blank">Pterafractyl<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/c/ecd33152-e290-4505-addd-a8d08cefdddd.jpg?1775938495" alt="Pterafractyl"></span></a> | 1/0 | 2 | C | with X +1/+1 counters on it. |
| <a href="https://scryfall.com/card/sos/187/essenceknit-scholar" class="card-link" target="_blank">Essenceknit Scholar<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/a/2a3cba55-3fae-4d45-ae03-4d662ec13718.jpg?1775938295" alt="Essenceknit Scholar"></span></a> | 3/1 | 3 | U | create a 1/1 black and green Pest creature token with "Whenever this token attacks, you ga |
| <a href="https://scryfall.com/card/sos/195/imperious-inkmage" class="card-link" target="_blank">Imperious Inkmage<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/5/d5df1c3f-2536-4476-b8cd-34b026c38366.jpg?1775938353" alt="Imperious Inkmage"></span></a> | 3/3 | 3 | C | surveil 2. (Look at the top two cards of your library, then put any number of them into yo |
| <a href="https://scryfall.com/card/sos/208/paradox-surveyor" class="card-link" target="_blank">Paradox Surveyor<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/7/d7cb1af2-0302-46ff-8303-ae9d07541a01.jpg?1775938445" alt="Paradox Surveyor"></span></a> | 3/3 | 3 | U | look at the top five cards of your library. You may reveal a land card or a card with {X}  |
| <a href="https://scryfall.com/card/sos/210/practiced-scrollsmith" class="card-link" target="_blank">Practiced Scrollsmith<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/0/40075e3f-58b3-47fd-8fbe-4b301e9ce7a1.jpg?1775938459" alt="Practiced Scrollsmith"></span></a> | 3/2 | 3 | U | exile target noncreature, nonland card from your graveyard. Until the end of your next tur |
| <a href="https://scryfall.com/card/sos/182/conciliators-duelist" class="card-link" target="_blank">Conciliator's Duelist<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/2/e225929b-6197-4550-969e-3c4a97206a68.jpg?1775938257" alt="Conciliator's Duelist"></span></a> | 4/3 | 4 | R | draw a card. Each player loses 1 life. |
| <a href="https://scryfall.com/card/sos/207/old-growth-educator" class="card-link" target="_blank">Old-Growth Educator<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/b/eb7e858a-9b85-49b2-a379-ee656b64935a.jpg?1775938438" alt="Old-Growth Educator"></span></a> | 4/4 | 4 | U | put two +1/+1 counters on it if you gained life this turn. |
| <a href="https://scryfall.com/card/sos/237/tam-observant-sequencer-deep-sight" class="card-link" target="_blank">Tam, Observant Sequencer // Deep Sight<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/1/7120e71b-2976-451b-89a7-a1665dc6fb6b.jpg?1775938655" alt="Tam, Observant Sequencer // Deep Sight"></span></a> | 4/3 | 4 | U | Tam becomes prepared. (While it's prepared, you may cast a copy of its spell. Doing so unp |
| <a href="https://scryfall.com/card/sos/234/stirring-honormancer" class="card-link" target="_blank">Stirring Honormancer<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/e/ee84b04d-78fc-416f-9166-72e5417c3e17.jpg?1775938634" alt="Stirring Honormancer"></span></a> | 4/5 | 5 | U | look at the top X cards of your library, where X is the number of creatures you control. P |
| <a href="https://scryfall.com/card/sos/181/colossus-of-the-blood-age" class="card-link" target="_blank">Colossus of the Blood Age<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/f/bfa7f0a4-6b65-4e53-ba00-848df260d8e3.jpg?1775938248" alt="Colossus of the Blood Age"></span></a> | 6/6 | 6 | U | it deals 3 damage to each opponent and you gain 3 life. |
| <a href="https://scryfall.com/card/sos/189/fractal-mascot" class="card-link" target="_blank">Fractal Mascot<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/f/cf5b19e3-eed1-4b36-9756-660ffb3baa08.jpg?1775938311" alt="Fractal Mascot"></span></a> | 6/6 | 6 | C | tap target creature an opponent controls. Put a stun counter on it. (If a permanent with a |

#### Colorless

| Card | P/T | CMC | Rarity | ETB Effect |
|------|-----|-----|--------|------------|
| <a href="https://scryfall.com/card/sos/247/biblioplex-tomekeeper" class="card-link" target="_blank">Biblioplex Tomekeeper<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/f/bf2efdd9-d2b4-4bea-a5b9-dbb2eee4dfba.jpg?1775938724" alt="Biblioplex Tomekeeper"></span></a> | 3/4 | 4 | C | choose up to one — |
| <a href="https://scryfall.com/card/sos/3/sundering-archaic" class="card-link" target="_blank">Sundering Archaic<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/3/c35b57e4-2358-46c0-8f09-cd27c10eaf2d.jpg?1775936933" alt="Sundering Archaic"></span></a> | 3/3 | 6 | U | exile target nonland permanent an opponent controls with mana value less than or equal to  |
| <a href="https://scryfall.com/card/sos/5/transcendent-archaic" class="card-link" target="_blank">Transcendent Archaic<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/6/1624c680-502b-474a-b9b2-888fe3ca008c.jpg?1775936948" alt="Transcendent Archaic"></span></a> | 6/6 | 7 | U | you may draw X cards, where X is the number of colors of mana spent to cast this spell. If |

### Mana Creatures

*Creatures that produce mana -- enable splashing and ramp.*

| Card | P/T | Color | CMC | Rarity |
|------|-----|-------|-----|--------|
| <a href="https://scryfall.com/card/sos/54/hydro-channeler" class="card-link" target="_blank">Hydro-Channeler<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/9/099f8400-d70a-48ef-8ff6-645eae97e072.jpg?1775937286" alt="Hydro-Channeler"></span></a> | 1/3 | U | 2 | C |
| <a href="https://scryfall.com/card/sos/117/goblin-glasswright-craft-with-pride" class="card-link" target="_blank">Goblin Glasswright // Craft with Pride<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/8/c85c5f06-dd31-4e2c-97be-2f64d65069ea.jpg?1775937759" alt="Goblin Glasswright // Craft with Pride"></span></a> | 2/2 | R | 2 | C |
| <a href="https://scryfall.com/card/sos/155/noxious-newt" class="card-link" target="_blank">Noxious Newt<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/a/3a028306-c5d7-4f8f-b6f4-0d103fd47000.jpg?1775938060" alt="Noxious Newt"></span></a> | 1/2 | G | 2 | C |
| <a href="https://scryfall.com/card/sos/250/page-loose-leaf" class="card-link" target="_blank">Page, Loose Leaf<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/c/8c6fecfd-8241-4cf0-b1eb-19472b99e0ed.jpg?1775938744" alt="Page, Loose Leaf"></span></a> | 0/2 | NC | 2 | C |
| <a href="https://scryfall.com/card/sos/109/blazing-firesinger-seething-song" class="card-link" target="_blank">Blazing Firesinger // Seething Song<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/b/3ba971e7-0b7a-4750-896f-7cf063e66b2a.jpg?1775937691" alt="Blazing Firesinger // Seething Song"></span></a> | 2/3 | R | 3 | U |
| <a href="https://scryfall.com/card/sos/128/rubble-rouser" class="card-link" target="_blank">Rubble Rouser<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/f/afe61957-a9bb-42b0-98e8-b5fa418cbaff.jpg?1775937860" alt="Rubble Rouser"></span></a> | 1/4 | R | 3 | C |
| <a href="https://scryfall.com/card/sos/171/abstract-paintmage" class="card-link" target="_blank">Abstract Paintmage<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/a/ea008094-d995-4740-9b39-c61049356c55.jpg?1775938173" alt="Abstract Paintmage"></span></a> | 2/2 | MC | 3 | U |
| <a href="https://scryfall.com/card/sos/175/berta-wise-extrapolator" class="card-link" target="_blank">Berta, Wise Extrapolator<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/5/75f89c36-c81d-4580-9a5c-218fed0c5c9a.jpg?1775938201" alt="Berta, Wise Extrapolator"></span></a> | 1/4 | MC | 4 | R |

---
## 4. Removal Spells

### Removal Count by Color

| Category | W | U | B | R | G | MC | NC |
|----------|---|---|---|---|---|---|---|
| **Total** | 6 | 8 | 7 | 9 | 3 | 14 | 2 |
| -X/-X | 0 | 0 | 3 | 0 | 0 | 0 | 0 |
| Bite | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Board Wipe | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| Bounce | 0 | 1 | 0 | 0 | 0 | 1 | 0 |
| Bounce (Library) | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| Conditional Destroy | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| Counter | 0 | 3 | 0 | 0 | 0 | 1 | 0 |
| Damage | 0 | 0 | 0 | 9 | 3 | 5 | 1 |
| Destroy | 3 | 0 | 1 | 0 | 0 | 2 | 0 |
| Edict | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
| Exile | 1 | 0 | 1 | 0 | 0 | 2 | 1 |
| Fight | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Tap/Stun | 1 | 3 | 0 | 0 | 0 | 1 | 0 |

### Removal Count by Rarity

| Category | C | U | R | M |
|----------|---|---|---|---|
| **Total** | 16 | 21 | 8 | 4 |
| -X/-X | 1 | 2 | 0 | 0 |
| Bite | 1 | 0 | 0 | 0 |
| Board Wipe | 0 | 0 | 0 | 1 |
| Bounce | 1 | 1 | 0 | 0 |
| Bounce (Library) | 1 | 0 | 0 | 0 |
| Conditional Destroy | 0 | 2 | 0 | 0 |
| Counter | 1 | 2 | 1 | 0 |
| Damage | 6 | 7 | 4 | 1 |
| Destroy | 1 | 2 | 2 | 1 |
| Edict | 0 | 2 | 0 | 0 |
| Exile | 1 | 2 | 1 | 1 |
| Fight | 0 | 1 | 0 | 0 |
| Tap/Stun | 4 | 1 | 0 | 0 |

### Full Removal List by Color

#### White

| Card | P/T | Rarity | CMC | Type | Categories |
|------|-----|--------|-----|------|------------|
| <a href="https://scryfall.com/card/sos/15/erode" class="card-link" target="_blank">Erode<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/2/32e670da-7563-4f6a-a7db-4c126a440eb8.jpg?1775937013" alt="Erode"></span></a> | - | R | 1 | Inst | Destroy |
| <a href="https://scryfall.com/card/sos/18/harsh-annotation" class="card-link" target="_blank">Harsh Annotation<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/0/e07a8fc7-c11c-4469-a31d-0abf40e57bbf.jpg?1775937033" alt="Harsh Annotation"></span></a> | - | U | 2 | Inst | Destroy |
| <a href="https://scryfall.com/card/sos/28/rapier-wit" class="card-link" target="_blank">Rapier Wit<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/7/97b50521-5a0f-4dbd-8e15-f0f0d059c258.jpg?1775937109" alt="Rapier Wit"></span></a> | - | C | 2 | Inst | Tap/Stun |
| <a href="https://scryfall.com/card/sos/13/emeritus-of-truce-swords-to-plowshares" class="card-link" target="_blank">Emeritus of Truce // Swords to Plowshares<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/8/9869a753-5e41-4098-ab41-e75b4396ec50.jpg?1775936999" alt="Emeritus of Truce // Swords to Plowshares"></span></a> | 3/3 | M | 3 | Inst/Crea | Exile |
| <a href="https://scryfall.com/card/sos/34/stand-up-for-yourself" class="card-link" target="_blank">Stand Up for Yourself<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/7/b756ca13-b904-4510-9bbb-5bc2864abfbd.jpg?1775937151" alt="Stand Up for Yourself"></span></a> | - | U | 3 | Inst | Conditional Destroy |
| <a href="https://scryfall.com/card/sos/6/ajanis-response" class="card-link" target="_blank">Ajani's Response<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/c/9cd1417a-badc-4abd-a8ca-5b31f85c1072.jpg?1776047920" alt="Ajani's Response"></span></a> | - | C | 5 | Inst | Destroy |

#### Blue

| Card | P/T | Rarity | CMC | Type | Categories |
|------|-----|--------|-----|------|------------|
| <a href="https://scryfall.com/card/sos/64/procrastinate" class="card-link" target="_blank">Procrastinate<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/e/1edb449d-620f-4e21-9d76-2c840635eb9d.jpg?1775937356" alt="Procrastinate"></span></a> | - | C | 1 | Sorc | Tap/Stun |
| <a href="https://scryfall.com/card/sos/38/banishing-betrayal" class="card-link" target="_blank">Banishing Betrayal<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/a/1ae9d2f3-7a9f-433a-aa1f-14337ae6f9d4.jpg?1775937176" alt="Banishing Betrayal"></span></a> | - | C | 2 | Inst | Bounce |
| <a href="https://scryfall.com/card/sos/47/essence-scatter" class="card-link" target="_blank">Essence Scatter<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/2/32840097-0531-4c43-b6a8-e76c17420b04.jpg?1775937236" alt="Essence Scatter"></span></a> | - | C | 2 | Inst | Counter |
| <a href="https://scryfall.com/card/sos/42/deluge-virtuoso" class="card-link" target="_blank">Deluge Virtuoso<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/e/2e3b16ed-8727-48fd-8b1f-c0cbd329385e.jpg?1775937202" alt="Deluge Virtuoso"></span></a> | 2/2 | C | 3 | Crea | Tap/Stun |
| <a href="https://scryfall.com/card/sos/57/mana-sculpt" class="card-link" target="_blank">Mana Sculpt<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/0/200c8e3d-c53b-40c7-a29a-fccc1281bfc6.jpg?1775937307" alt="Mana Sculpt"></span></a> | - | R | 3 | Inst | Counter |
| <a href="https://scryfall.com/card/sos/39/brush-off" class="card-link" target="_blank">Brush Off<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/5/151eab82-d20f-433b-b3bb-1d44e2871d5c.jpg?1775937183" alt="Brush Off"></span></a> | - | U | 4 | Inst | Counter |
| <a href="https://scryfall.com/card/sos/66/run-behind" class="card-link" target="_blank">Run Behind<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/0/40ecc34b-4cd0-4998-bbf4-7faa6fd3d7e0.jpg?1775937369" alt="Run Behind"></span></a> | - | C | 4 | Inst | Bounce (Library) |
| <a href="https://scryfall.com/card/sos/53/homesickness" class="card-link" target="_blank">Homesickness<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/e/6e4a1f82-b0b1-4608-91f8-130bee731435.jpg?1775937280" alt="Homesickness"></span></a> | - | U | 6 | Inst | Tap/Stun |

#### Black

| Card | P/T | Rarity | CMC | Type | Categories |
|------|-----|--------|-----|------|------------|
| <a href="https://scryfall.com/card/sos/79/dissection-practice" class="card-link" target="_blank">Dissection Practice<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/d/ddbf1242-6832-475e-9a77-65dd9b4bb32a.jpg?1775937462" alt="Dissection Practice"></span></a> | - | U | 1 | Inst | -1/-1 |
| <a href="https://scryfall.com/card/sos/81/end-of-the-hunt" class="card-link" target="_blank">End of the Hunt<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/8/0809b51a-6a05-4f18-9bf4-1b8382da648f.jpg?1775937476" alt="End of the Hunt"></span></a> | - | U | 2 | Sorc | Edict |
| <a href="https://scryfall.com/card/sos/86/last-gasp" class="card-link" target="_blank">Last Gasp<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/a/da5f3729-6ec7-4482-90cb-83b973edeae4.jpg?1775937510" alt="Last Gasp"></span></a> | - | C | 2 | Inst | -3/-3 |
| <a href="https://scryfall.com/card/sos/83/foolish-fate" class="card-link" target="_blank">Foolish Fate<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/2/d278f4c9-d20b-4a76-8c5c-4d3e985948b9.jpg?1775937489" alt="Foolish Fate"></span></a> | - | U | 3 | Inst | Destroy |
| <a href="https://scryfall.com/card/sos/92/poisoners-apprentice" class="card-link" target="_blank">Poisoner's Apprentice<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/7/3755a2e9-af55-4625-a006-2a86c7893a96.jpg?1775937552" alt="Poisoner's Apprentice"></span></a> | 2/2 | U | 3 | Crea | -4/-4 |
| <a href="https://scryfall.com/card/sos/105/withering-curse" class="card-link" target="_blank">Withering Curse<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/0/50aaf618-dddb-4cbe-8231-d634b4498563.jpg?1775937655" alt="Withering Curse"></span></a> | - | M | 3 | Sorc | Board Wipe / -2/-2 |
| <a href="https://scryfall.com/card/sos/104/wander-off" class="card-link" target="_blank">Wander Off<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/d/3d409512-50b9-4a38-91b0-19ba25227992.jpg?1775937643" alt="Wander Off"></span></a> | - | C | 4 | Inst | Exile |

#### Red

| Card | P/T | Rarity | CMC | Type | Categories |
|------|-----|--------|-----|------|------------|
| <a href="https://scryfall.com/card/sos/112/duel-tactics" class="card-link" target="_blank">Duel Tactics<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/f/8f3a1675-0cc7-4dfd-a12e-4740a2cf81e8.jpg?1775937718" alt="Duel Tactics"></span></a> | - | U | 1 | Sorc | Damage: 1 |
| <a href="https://scryfall.com/card/sos/119/impractical-joke" class="card-link" target="_blank">Impractical Joke<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/9/39a816b4-39b8-421c-b828-68db901d34b7.jpg?1775937777" alt="Impractical Joke"></span></a> | - | U | 1 | Sorc | Damage: 3 |
| <a href="https://scryfall.com/card/sos/113/emeritus-of-conflict-lightning-bolt" class="card-link" target="_blank">Emeritus of Conflict // Lightning Bolt<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/5/f58dba4f-1abb-47a3-a684-29c32bab95c0.jpg?1775937726" alt="Emeritus of Conflict // Lightning Bolt"></span></a> | 2/2 | M | 2 | Inst/Crea | Damage: 3 |
| <a href="https://scryfall.com/card/sos/135/tome-blast" class="card-link" target="_blank">Tome Blast<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/2/72a3b17d-1e00-48e9-8402-c81bacd595a7.jpg?1775937914" alt="Tome Blast"></span></a> | - | C | 2 | Sorc | Damage: 2 |
| <a href="https://scryfall.com/card/sos/130/steal-the-show" class="card-link" target="_blank">Steal the Show<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/a/7ac6649f-980e-4404-9c05-458c30578ecc.jpg?1775937875" alt="Steal the Show"></span></a> | - | R | 3 | Sorc | Damage: X |
| <a href="https://scryfall.com/card/sos/136/unsubtle-mockery" class="card-link" target="_blank">Unsubtle Mockery<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/b/2b7cb1a3-761e-470e-a164-6e29dd9448cd.jpg?1775937921" alt="Unsubtle Mockery"></span></a> | - | C | 3 | Inst | Damage: 4 |
| <a href="https://scryfall.com/card/sos/107/archaics-agony" class="card-link" target="_blank">Archaic's Agony<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/d/8d99f8b2-5c1c-4059-bf68-c6b2e9e5b275.jpg?1775937675" alt="Archaic's Agony"></span></a> | - | U | 5 | Sorc | Damage: X |
| <a href="https://scryfall.com/card/sos/108/artistic-process" class="card-link" target="_blank">Artistic Process<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/c/bce9d933-be58-4301-beb4-07b04d0b69f0.jpg?1775937683" alt="Artistic Process"></span></a> | - | U | 5 | Sorc | Damage: 6 |
| <a href="https://scryfall.com/card/sos/118/heated-argument" class="card-link" target="_blank">Heated Argument<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/0/0038d212-3d95-4f98-8c2e-7b2404d0ced7.jpg?1775937767" alt="Heated Argument"></span></a> | - | C | 5 | Inst | Damage: 6 |

#### Green

| Card | P/T | Rarity | CMC | Type | Categories |
|------|-----|--------|-----|------|------------|
| <a href="https://scryfall.com/card/sos/141/burrog-barrage" class="card-link" target="_blank">Burrog Barrage<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/5/95d5b0a8-2b66-418e-9e5e-ecf7b304c31e.jpg?1775937957" alt="Burrog Barrage"></span></a> | - | C | 2 | Inst | Bite, Damage: P |
| <a href="https://scryfall.com/card/sos/150/glorious-decay" class="card-link" target="_blank">Glorious Decay<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/3/a335f396-1004-4fee-842a-a35ff6ba17f2.jpg?1775938023" alt="Glorious Decay"></span></a> | - | C | 2 | Inst | Damage: 4 |
| <a href="https://scryfall.com/card/sos/142/chelonian-tackle" class="card-link" target="_blank">Chelonian Tackle<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/8/a82a4d8c-4105-4923-85a2-ef58241f725c.jpg?1775937964" alt="Chelonian Tackle"></span></a> | - | U | 3 | Sorc | Fight, Damage: P |

#### Multicolor

| Card | P/T | Rarity | CMC | Type | Categories |
|------|-----|--------|-----|------|------------|
| <a href="https://scryfall.com/card/sos/200/lorehold-charm" class="card-link" target="_blank">Lorehold Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/f/5fe70295-e550-4577-a341-dab6c25aabfd.jpg?1775938389" alt="Lorehold Charm"></span></a> | - | U | 2 | Inst | Edict |
| <a href="https://scryfall.com/card/sos/211/prismari-charm" class="card-link" target="_blank">Prismari Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/f/8f6c2a5e-fe13-407c-aadd-c9caf2884ff1.jpg?1775938465" alt="Prismari Charm"></span></a> | - | U | 2 | Inst | Bounce |
| <a href="https://scryfall.com/card/sos/217/quandrix-charm" class="card-link" target="_blank">Quandrix Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/1/318486e0-f255-40f5-8150-dc272eec9d7d.jpg?1775938509" alt="Quandrix Charm"></span></a> | - | U | 2 | Inst | Counter |
| <a href="https://scryfall.com/card/sos/225/silverquill-charm" class="card-link" target="_blank">Silverquill Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/e/3eb73579-f1c6-4762-81d2-9568ab501fac.jpg?1775938570" alt="Silverquill Charm"></span></a> | - | U | 2 | Inst | Exile |
| <a href="https://scryfall.com/card/sos/239/traumatic-critique" class="card-link" target="_blank">Traumatic Critique<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/a/2a812fa7-4599-4e25-97db-20ffc6bc0b26.jpg?1775938668" alt="Traumatic Critique"></span></a> | - | R | 2 | Inst | Damage: X |
| <a href="https://scryfall.com/card/sos/240/vibrant-outburst" class="card-link" target="_blank">Vibrant Outburst<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/9/f9ba68ef-6efc-4249-8b74-e33f47173902.jpg?1775938674" alt="Vibrant Outburst"></span></a> | - | U | 2 | Inst | Damage: 3 |
| <a href="https://scryfall.com/card/sos/244/witherbloom-charm" class="card-link" target="_blank">Witherbloom Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/5/254437f7-7a8a-4b11-9cea-e8e7ea23c59e.jpg?1775938703" alt="Witherbloom Charm"></span></a> | - | U | 2 | Inst | Conditional Destroy |
| <a href="https://scryfall.com/card/sos/236/suspend-aggression" class="card-link" target="_blank">Suspend Aggression<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/3/135c0696-d86d-4e48-988c-5c218de451fc.jpg?1775938648" alt="Suspend Aggression"></span></a> | - | R | 3 | Inst | Exile |
| <a href="https://scryfall.com/card/sos/214/professor-dellian-fel" class="card-link" target="_blank">Professor Dellian Fel<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/f/6ff3b4d8-1271-4c5d-8834-7662244f173d.jpg?1775938486" alt="Professor Dellian Fel"></span></a> | - | M | 4 | Plan | Destroy |
| <a href="https://scryfall.com/card/sos/243/wilt-in-the-heat" class="card-link" target="_blank">Wilt in the Heat<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/6/f63f7209-fc0f-400c-8076-125f3131cb32.jpg?1775938697" alt="Wilt in the Heat"></span></a> | - | C | 4 | Inst | Damage: 5 |
| <a href="https://scryfall.com/card/sos/231/splatter-technique" class="card-link" target="_blank">Splatter Technique<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/6/969b6657-c3b9-47e1-a42e-95bbcccf452d.jpg?1775938612" alt="Splatter Technique"></span></a> | - | R | 5 | Sorc | Damage: 4 |
| <a href="https://scryfall.com/card/sos/235/stress-dream" class="card-link" target="_blank">Stress Dream<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/e/1ec40a1b-51e7-4a35-966c-ab2a10f21a80.jpg?1775938641" alt="Stress Dream"></span></a> | - | U | 5 | Inst | Damage: 5 |
| <a href="https://scryfall.com/card/sos/189/fractal-mascot" class="card-link" target="_blank">Fractal Mascot<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/f/cf5b19e3-eed1-4b36-9756-660ffb3baa08.jpg?1775938311" alt="Fractal Mascot"></span></a> | 6/6 | C | 6 | Crea | Tap/Stun |
| <a href="https://scryfall.com/card/sos/205/moment-of-reckoning" class="card-link" target="_blank">Moment of Reckoning<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/7/577d9dc8-7720-4dc9-b650-64b4729b309b.jpg?1775938423" alt="Moment of Reckoning"></span></a> | - | R | 7 | Sorc | Destroy |

#### Colorless

| Card | P/T | Rarity | CMC | Type | Categories |
|------|-----|--------|-----|------|------------|
| <a href="https://scryfall.com/card/sos/3/sundering-archaic" class="card-link" target="_blank">Sundering Archaic<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/3/c35b57e4-2358-46c0-8f09-cd27c10eaf2d.jpg?1775936933" alt="Sundering Archaic"></span></a> | 3/3 | U | 6 | Crea | Exile |
| <a href="https://scryfall.com/card/sos/4/together-as-one" class="card-link" target="_blank">Together as One<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/c/ac2a8a66-e38c-42ab-83e1-d2d99ee48861.jpg?1775936940" alt="Together as One"></span></a> | - | R | 6 | Sorc | Damage: X |

---
## 5. Burn (Player-Only Damage)

*Cards that deal damage to opponents only -- cannot remove creatures.*

| Card | P/T | Color | Rarity | CMC | Type | Categories |
|------|-----|-------|--------|-----|------|------------|
| <a href="https://scryfall.com/card/sos/134/thunderdrum-soloist" class="card-link" target="_blank">Thunderdrum Soloist<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/9/590d1d95-ed13-4121-899f-f5a2d8a6617a.jpg?1775937905" alt="Thunderdrum Soloist"></span></a> | 1/3 | R | U | 2 | Crea | Burn: 3 |
| <a href="https://scryfall.com/card/sos/128/rubble-rouser" class="card-link" target="_blank">Rubble Rouser<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/f/afe61957-a9bb-42b0-98e8-b5fa418cbaff.jpg?1775937860" alt="Rubble Rouser"></span></a> | 1/4 | R | C | 3 | Crea | Burn: 1 |
| <a href="https://scryfall.com/card/sos/173/ark-of-hunger" class="card-link" target="_blank">Ark of Hunger<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/9/79d01c19-162b-4a12-9e27-18366d95eaa0.jpg?1775938187" alt="Ark of Hunger"></span></a> | - | MC | R | 4 | Arti | Burn: 1 |
| <a href="https://scryfall.com/card/sos/181/colossus-of-the-blood-age" class="card-link" target="_blank">Colossus of the Blood Age<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/f/bfa7f0a4-6b65-4e53-ba00-848df260d8e3.jpg?1775938248" alt="Colossus of the Blood Age"></span></a> | 6/6 | MC | U | 6 | Crea/Arti | Burn: 3 |

---
## 6. Combat Tricks

### Combat Trick Count by Color

| Category | W | U | B | R | G | MC |
|----------|---|---|---|---|---|---|
| **Total** | 3 | 4 | 3 | 1 | 3 | 3 |
| Blink | 2 | 1 | 0 | 0 | 0 | 1 |
| Counters | 0 | 1 | 0 | 0 | 1 | 1 |
| Falter | 0 | 0 | 0 | 1 | 0 | 0 |
| Grants First Strike | 1 | 0 | 0 | 0 | 0 | 0 |
| Grants Flying | 0 | 1 | 0 | 0 | 0 | 0 |
| Grants Hexproof | 0 | 1 | 0 | 0 | 0 | 0 |
| Grants Indestructible | 0 | 0 | 1 | 0 | 0 | 0 |
| Grants Trample | 0 | 0 | 0 | 0 | 1 | 1 |
| P/T Buff | 1 | 1 | 3 | 0 | 2 | 0 |
| P/T Buff (Team) | 0 | 0 | 0 | 0 | 0 | 1 |
| Protection | 0 | 1 | 1 | 0 | 0 | 0 |

### Combat Trick Count by Rarity

| Category | C | U | R |
|----------|---|---|---|
| **Total** | 5 | 10 | 2 |
| Blink | 0 | 2 | 2 |
| Counters | 1 | 2 | 0 |
| Falter | 0 | 1 | 0 |
| Grants First Strike | 1 | 0 | 0 |
| Grants Flying | 0 | 1 | 0 |
| Grants Hexproof | 1 | 0 | 0 |
| Grants Indestructible | 1 | 0 | 0 |
| Grants Trample | 1 | 1 | 0 |
| P/T Buff | 4 | 3 | 0 |
| P/T Buff (Team) | 0 | 1 | 0 |
| Protection | 2 | 0 | 0 |

### Full Combat Tricks List by Color

#### White

| Card | P/T | Rarity | CMC | Categories | Effect Summary |
|------|-----|--------|-----|------------|----------------|
| <a href="https://scryfall.com/card/sos/9/daydream" class="card-link" target="_blank">Daydream<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/2/e2b16cb2-b8b2-45df-9695-3c16e9d89e28.jpg?1775936973" alt="Daydream"></span></a> | - | U | 1 | Blink | exile target creature you control, then return that card to the battlefield unde |
| <a href="https://scryfall.com/card/sos/22/interjection" class="card-link" target="_blank">Interjection<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/5/0534cff6-299c-4155-b318-eb7581989e8a.jpg?1775937061" alt="Interjection"></span></a> | - | C | 1 | P/T Buff, Grants First Strike | target creature gets +2/+2 and gains first strike until end of turn. |
| <a href="https://scryfall.com/card/sos/14/ennis-debate-moderator" class="card-link" target="_blank">Ennis, Debate Moderator<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/2/d2ef31b4-24fa-4443-9f05-c8e99c3522e5.jpg?1775937005" alt="Ennis, Debate Moderator"></span></a> | 1/1 | U | 2 | Blink | at the beginning of your end step, if one or more cards were put into exile this |

#### Blue

| Card | P/T | Rarity | CMC | Categories | Effect Summary |
|------|-----|--------|-----|------------|----------------|
| <a href="https://scryfall.com/card/sos/41/chase-inspiration" class="card-link" target="_blank">Chase Inspiration<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/6/06f9f257-c7ef-44b7-8b2b-f038fba900af.jpg?1775937195" alt="Chase Inspiration"></span></a> | - | C | 1 | P/T Buff, Protection, Grants Hexproof | target creature you control gets +0/+3 and gains hexproof until end of turn. (it |
| <a href="https://scryfall.com/card/sos/50/fractal-anomaly" class="card-link" target="_blank">Fractal Anomaly<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/1/e1975a61-aef0-49a6-a6d6-c3a37e2e2b22.jpg?1775937257" alt="Fractal Anomaly"></span></a> | - | U | 1 | Counters | create a 0/0 green and blue fractal creature token and put x +1/+1 counters on i |
| <a href="https://scryfall.com/card/sos/46/encouraging-aviator-jump" class="card-link" target="_blank">Encouraging Aviator // Jump<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/2/72654b84-9902-41db-92ab-a3499c31221c.jpg?1775937230" alt="Encouraging Aviator // Jump"></span></a> | 2/3 | U | 3 | Grants Flying | target creature gains flying until end of turn. |
| <a href="https://scryfall.com/card/sos/67/skycoach-conductor-all-aboard" class="card-link" target="_blank">Skycoach Conductor // All Aboard<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/e/4ecbca71-9a1d-44c5-b709-d6f565941d5e.jpg?1775937376" alt="Skycoach Conductor // All Aboard"></span></a> | 2/3 | R | 3 | Blink | flash flying, vigilance this creature enters prepared. (while it's prepared, you |

#### Black

| Card | P/T | Rarity | CMC | Categories | Effect Summary |
|------|-----|--------|-----|------------|----------------|
| <a href="https://scryfall.com/card/sos/79/dissection-practice" class="card-link" target="_blank">Dissection Practice<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/d/ddbf1242-6832-475e-9a77-65dd9b4bb32a.jpg?1775937462" alt="Dissection Practice"></span></a> | - | U | 1 | P/T Buff | up to one target creature gets +1/+1 until end of turn. |
| <a href="https://scryfall.com/card/sos/89/masterful-flourish" class="card-link" target="_blank">Masterful Flourish<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/d/8d93d14d-7760-4af2-a237-2df326dd28d3.jpg?1775937531" alt="Masterful Flourish"></span></a> | - | C | 1 | P/T Buff, Grants Indestructible, Protection | target creature you control gets +1/+0 and gains indestructible until end of tur |
| <a href="https://scryfall.com/card/sos/96/rabid-attack" class="card-link" target="_blank">Rabid Attack<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/5/f5e67560-3135-4b27-a344-5859edf8bcd9.jpg?1775937579" alt="Rabid Attack"></span></a> | - | U | 2 | P/T Buff | until end of turn, any number of target creatures you control each get +1/+0 and |

#### Red

| Card | P/T | Rarity | CMC | Categories | Effect Summary |
|------|-----|--------|-----|------------|----------------|
| <a href="https://scryfall.com/card/sos/112/duel-tactics" class="card-link" target="_blank">Duel Tactics<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/f/8f3a1675-0cc7-4dfd-a12e-4740a2cf81e8.jpg?1775937718" alt="Duel Tactics"></span></a> | - | U | 1 | Falter | duel tactics deals 1 damage to target creature. it can't block this turn. |

#### Green

| Card | P/T | Rarity | CMC | Categories | Effect Summary |
|------|-----|--------|-----|------------|----------------|
| <a href="https://scryfall.com/card/sos/141/burrog-barrage" class="card-link" target="_blank">Burrog Barrage<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/5/95d5b0a8-2b66-418e-9e5e-ecf7b304c31e.jpg?1775937957" alt="Burrog Barrage"></span></a> | - | C | 2 | P/T Buff | target creature you control gets +1/+0 until end of turn if you've cast another  |
| <a href="https://scryfall.com/card/sos/153/lumarets-favor" class="card-link" target="_blank">Lumaret's Favor<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/5/c5e7c856-8b71-44e6-8998-0b0b3ff0ef99.jpg?1775938045" alt="Lumaret's Favor"></span></a> | - | U | 2 | P/T Buff | target creature gets +2/+4 until end of turn. |
| <a href="https://scryfall.com/card/sos/144/efflorescence" class="card-link" target="_blank">Efflorescence<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/9/79b9ace7-eceb-4f97-9ee7-d5ee3e0b3515.jpg?1775937979" alt="Efflorescence"></span></a> | - | C | 3 | Grants Trample, Counters | put two +1/+1 counters on target creature. |

#### Multicolor

| Card | P/T | Rarity | CMC | Categories | Effect Summary |
|------|-----|--------|-----|------------|----------------|
| <a href="https://scryfall.com/card/sos/200/lorehold-charm" class="card-link" target="_blank">Lorehold Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/f/5fe70295-e550-4577-a341-dab6c25aabfd.jpg?1775938389" alt="Lorehold Charm"></span></a> | - | U | 2 | P/T Buff (Team), Grants Trample | creatures you control get +1/+1 and gain trample until end of turn. |
| <a href="https://scryfall.com/card/sos/225/silverquill-charm" class="card-link" target="_blank">Silverquill Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/e/3eb73579-f1c6-4762-81d2-9568ab501fac.jpg?1775938570" alt="Silverquill Charm"></span></a> | - | U | 2 | Counters | put two +1/+1 counters on target creature. |
| <a href="https://scryfall.com/card/sos/182/conciliators-duelist" class="card-link" target="_blank">Conciliator's Duelist<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/2/e225929b-6197-4550-969e-3c4a97206a68.jpg?1775938257" alt="Conciliator's Duelist"></span></a> | 4/3 | R | 4 | Blink | when this creature enters, draw a card. each player loses 1 life. repartee — whe |

---
## 7. Set Mechanics

| Mechanic | Card Count | Examples |
|----------|------------|----------|
| Surveil | 17 | <a href="https://scryfall.com/card/sos/24/owlin-historian" class="card-link" target="_blank">Owlin Historian<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/f/5fe99be0-e1ec-485e-82f8-02eba7b82441.jpg?1775937078" alt="Owlin Historian"></span></a>, <a href="https://scryfall.com/card/sos/36/stone-docent" class="card-link" target="_blank">Stone Docent<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/2/c2abfffb-bf36-44af-9a27-6e109e4d77dd.jpg?1775937164" alt="Stone Docent"></span></a>, <a href="https://scryfall.com/card/sos/38/banishing-betrayal" class="card-link" target="_blank">Banishing Betrayal<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/a/1ae9d2f3-7a9f-433a-aa1f-14337ae6f9d4.jpg?1775937176" alt="Banishing Betrayal"></span></a> |
| Infusion | 12 | <a href="https://scryfall.com/card/sos/83/foolish-fate" class="card-link" target="_blank">Foolish Fate<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/2/d278f4c9-d20b-4a76-8c5c-4d3e985948b9.jpg?1775937489" alt="Foolish Fate"></span></a>, <a href="https://scryfall.com/card/sos/91/moseo-veins-new-dean" class="card-link" target="_blank">Moseo, Vein's New Dean<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/8/6877180c-22a1-4c4d-9178-316f4c34661b.jpg?1775937545" alt="Moseo, Vein's New Dean"></span></a>, <a href="https://scryfall.com/card/sos/92/poisoners-apprentice" class="card-link" target="_blank">Poisoner's Apprentice<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/7/3755a2e9-af55-4625-a006-2a86c7893a96.jpg?1775937552" alt="Poisoner's Apprentice"></span></a> |
| Ward | 11 | <a href="https://scryfall.com/card/sos/21/inkshape-demonstrator" class="card-link" target="_blank">Inkshape Demonstrator<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/c/bcfac992-9984-4529-b9ff-a42d58832b34.jpg?1775937053" alt="Inkshape Demonstrator"></span></a>, <a href="https://scryfall.com/card/sos/40/campus-composer-aqueous-aria" class="card-link" target="_blank">Campus Composer // Aqueous Aria<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/a/fac8ac39-ecb4-4142-bf37-131c65660a9b.jpg?1775937189" alt="Campus Composer // Aqueous Aria"></span></a>, <a href="https://scryfall.com/card/sos/45/emeritus-of-ideation-ancestral-recall" class="card-link" target="_blank">Emeritus of Ideation // Ancestral Recall<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/5/75961d36-acf6-425f-9698-0bf52af74f31.jpg?1775937223" alt="Emeritus of Ideation // Ancestral Recall"></span></a> |
| Flashback | 10 | <a href="https://scryfall.com/card/sos/7/antiquities-on-the-loose" class="card-link" target="_blank">Antiquities on the Loose<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/8/68ee92cd-51af-4de5-bcc8-34d0bb2fd398.jpg?1775936960" alt="Antiquities on the Loose"></span></a>, <a href="https://scryfall.com/card/sos/9/daydream" class="card-link" target="_blank">Daydream<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/2/e2b16cb2-b8b2-45df-9695-3c16e9d89e28.jpg?1775936973" alt="Daydream"></span></a>, <a href="https://scryfall.com/card/sos/10/dig-site-inventory" class="card-link" target="_blank">Dig Site Inventory<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/5/e52464ee-df8b-41ec-af93-4b0eb004383e.jpg?1775936980" alt="Dig Site Inventory"></span></a> |
| Converge | 9 | <a href="https://scryfall.com/card/sos/2/rancorous-archaic" class="card-link" target="_blank">Rancorous Archaic<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/5/2565e16a-ed31-4867-adb8-f1633d580397.jpg?1775936927" alt="Rancorous Archaic"></span></a>, <a href="https://scryfall.com/card/sos/3/sundering-archaic" class="card-link" target="_blank">Sundering Archaic<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/3/c35b57e4-2358-46c0-8f09-cd27c10eaf2d.jpg?1775936933" alt="Sundering Archaic"></span></a>, <a href="https://scryfall.com/card/sos/4/together-as-one" class="card-link" target="_blank">Together as One<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/c/ac2a8a66-e38c-42ab-83e1-d2d99ee48861.jpg?1775936940" alt="Together as One"></span></a> |
| Paradigm | 5 | <a href="https://scryfall.com/card/sos/30/restoration-seminar" class="card-link" target="_blank">Restoration Seminar<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/e/9ebc4ecf-2fa2-4ab8-afde-3b91cf5eadb6.jpg?1775937123" alt="Restoration Seminar"></span></a>, <a href="https://scryfall.com/card/sos/44/echocasting-symposium" class="card-link" target="_blank">Echocasting Symposium<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/d/5d7086a7-dc42-468a-a2cf-a6f89030f947.jpg?1775937216" alt="Echocasting Symposium"></span></a>, <a href="https://scryfall.com/card/sos/78/decorum-dissertation" class="card-link" target="_blank">Decorum Dissertation<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/4/f4ab2d9b-c73d-478d-aac7-4d3bb24296d2.jpg?1775937454" alt="Decorum Dissertation"></span></a> |

---
## 8. Draft Signposts (Uncommon Multicolor)

These uncommon gold cards hint at supported archetypes.

| Card | P/T | Colors | Type | CMC | Effect |
|------|-----|--------|------|-----|--------|
| <a href="https://scryfall.com/card/sos/170/abigale-poet-laureate-heroic-stanza" class="card-link" target="_blank">Abigale, Poet Laureate // Heroic Stanza<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/7/77285d12-e658-4eb3-ba13-ff202afab9c8.jpg?1775938164" alt="Abigale, Poet Laureate // Heroic Stanza"></span></a> | 2/3 | B,W | Legendary Creature — Bird Bard | 3 | flying whenever you cast a creature spell, abigale becomes prepared. (while it's prepared, you may c |
| <a href="https://scryfall.com/card/sos/171/abstract-paintmage" class="card-link" target="_blank">Abstract Paintmage<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/a/ea008094-d995-4740-9b39-c61049356c55.jpg?1775938173" alt="Abstract Paintmage"></span></a> | 2/2 | R,U | Creature — Djinn Sorcerer | 3 | at the beginning of your first main phase, add {u}{r}. spend this mana only to cast instant and sorc |
| <a href="https://scryfall.com/card/sos/178/borrowed-knowledge" class="card-link" target="_blank">Borrowed Knowledge<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/3/a3226e14-554d-47c9-b8b6-dfeb53cc41ba.jpg?1775938224" alt="Borrowed Knowledge"></span></a> | - | R,W | Sorcery | 4 | choose one — • discard your hand, then draw cards equal to the number of cards in target opponent's  |
| <a href="https://scryfall.com/card/sos/181/colossus-of-the-blood-age" class="card-link" target="_blank">Colossus of the Blood Age<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/f/bfa7f0a4-6b65-4e53-ba00-848df260d8e3.jpg?1775938248" alt="Colossus of the Blood Age"></span></a> | 6/6 | R,W | Artifact Creature — Construct | 6 | when this creature enters, it deals 3 damage to each opponent and you gain 3 life. when this creatur |
| <a href="https://scryfall.com/card/sos/183/cuboid-colony" class="card-link" target="_blank">Cuboid Colony<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/3/6384d135-7780-4d75-9e95-71bce506948e.jpg?1775938265" alt="Cuboid Colony"></span></a> | 1/1 | G,U | Creature — Insect | 2 | flash flying, trample increment (whenever you cast a spell, if the amount of mana you spent is great |
| <a href="https://scryfall.com/card/sos/187/essenceknit-scholar" class="card-link" target="_blank">Essenceknit Scholar<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/a/2a3cba55-3fae-4d45-ae03-4d662ec13718.jpg?1775938295" alt="Essenceknit Scholar"></span></a> | 3/1 | B,G | Creature — Dryad Warlock | 3 | when this creature enters, create a 1/1 black and green pest creature token with "whenever this toke |
| <a href="https://scryfall.com/card/sos/190/fractal-tender" class="card-link" target="_blank">Fractal Tender<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/a/ea7f5262-4ddb-410a-be72-4bac6af9b4ec.jpg?1775938318" alt="Fractal Tender"></span></a> | 3/3 | G,U | Creature — Elf Wizard | 5 | ward {2} increment (whenever you cast a spell, if the amount of mana you spent is greater than this  |
| <a href="https://scryfall.com/card/sos/193/growth-curve" class="card-link" target="_blank">Growth Curve<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/6/1675a445-86ae-413b-b95a-a1c254a7f252.jpg?1775938339" alt="Growth Curve"></span></a> | - | G,U | Sorcery | 2 | put a +1/+1 counter on target creature you control, then double the number of +1/+1 counters on that |
| <a href="https://scryfall.com/card/sos/197/killians-confidence" class="card-link" target="_blank">Killian's Confidence<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/5/55ff776a-fc3b-4338-8864-d57a85b3f123.jpg?1775938369" alt="Killian's Confidence"></span></a> | - | B,W | Sorcery | 2 | target creature gets +1/+1 until end of turn. draw a card. whenever one or more creatures you contro |
| <a href="https://scryfall.com/card/sos/198/kirol-history-buff-pack-a-punch" class="card-link" target="_blank">Kirol, History Buff // Pack a Punch<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/7/676ba521-66e4-42cf-a315-70d03cb7334e.jpg?1775938375" alt="Kirol, History Buff // Pack a Punch"></span></a> | 2/3 | R,W | Legendary Creature — Vampire Cleric | 2 | whenever one or more cards leave your graveyard, kirol becomes prepared. (while it's prepared, you m |
| <a href="https://scryfall.com/card/sos/199/lluwen-exchange-student-pest-friend" class="card-link" target="_blank">Lluwen, Exchange Student // Pest Friend<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/0/a0bcb638-c3c8-4973-9537-5c471f43f34f.jpg?1775938382" alt="Lluwen, Exchange Student // Pest Friend"></span></a> | 3/4 | B,G | Legendary Creature — Elf Druid | 4 | lluwen enters prepared. (while it's prepared, you may cast a copy of its spell. doing so unprepares  |
| <a href="https://scryfall.com/card/sos/200/lorehold-charm" class="card-link" target="_blank">Lorehold Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/f/5fe70295-e550-4577-a341-dab6c25aabfd.jpg?1775938389" alt="Lorehold Charm"></span></a> | - | R,W | Instant | 2 | choose one — • each opponent sacrifices a nontoken artifact of their choice. • return target artifac |
| <a href="https://scryfall.com/card/sos/203/mind-roots" class="card-link" target="_blank">Mind Roots<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/d/9d5fdbda-ebbe-45d6-a668-5ddee057a063.jpg?1775938410" alt="Mind Roots"></span></a> | - | B,G | Sorcery | 3 | target player discards two cards. put up to one land card discarded this way onto the battlefield ta |
| <a href="https://scryfall.com/card/sos/204/molten-note" class="card-link" target="_blank">Molten Note<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/0/506f69aa-7dc4-4dd7-990a-7371fc1762c0.jpg?1775938416" alt="Molten Note"></span></a> | - | R,W | Sorcery | 2 | molten note deals damage to target creature equal to the amount of mana spent to cast this spell. un |
| <a href="https://scryfall.com/card/sos/207/old-growth-educator" class="card-link" target="_blank">Old-Growth Educator<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/b/eb7e858a-9b85-49b2-a379-ee656b64935a.jpg?1775938438" alt="Old-Growth Educator"></span></a> | 4/4 | B,G | Creature — Treefolk Druid | 4 | vigilance, reach infusion — when this creature enters, put two +1/+1 counters on it if you gained li |
| <a href="https://scryfall.com/card/sos/208/paradox-surveyor" class="card-link" target="_blank">Paradox Surveyor<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/7/d7cb1af2-0302-46ff-8303-ae9d07541a01.jpg?1775938445" alt="Paradox Surveyor"></span></a> | 3/3 | G,U | Creature — Elf Druid | 3 | reach when this creature enters, look at the top five cards of your library. you may reveal a land c |
| <a href="https://scryfall.com/card/sos/210/practiced-scrollsmith" class="card-link" target="_blank">Practiced Scrollsmith<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/0/40075e3f-58b3-47fd-8fbe-4b301e9ce7a1.jpg?1775938459" alt="Practiced Scrollsmith"></span></a> | 3/2 | R,W | Creature — Dwarf Cleric | 3 | first strike when this creature enters, exile target noncreature, nonland card from your graveyard.  |
| <a href="https://scryfall.com/card/sos/211/prismari-charm" class="card-link" target="_blank">Prismari Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/f/8f6c2a5e-fe13-407c-aadd-c9caf2884ff1.jpg?1775938465" alt="Prismari Charm"></span></a> | - | R,U | Instant | 2 | choose one — • surveil 2, then draw a card. • prismari charm deals 1 damage to each of one or two ta |
| <a href="https://scryfall.com/card/sos/213/proctors-gaze" class="card-link" target="_blank">Proctor's Gaze<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/1/b127d543-0a90-4af6-9410-94d5cd30389e.jpg?1775938479" alt="Proctor's Gaze"></span></a> | - | G,U | Instant | 4 | return up to one target nonland permanent to its owner's hand. search your library for a basic land  |
| <a href="https://scryfall.com/card/sos/217/quandrix-charm" class="card-link" target="_blank">Quandrix Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/1/318486e0-f255-40f5-8150-dc272eec9d7d.jpg?1775938509" alt="Quandrix Charm"></span></a> | - | G,U | Instant | 2 | choose one — • counter target spell unless its controller pays {2}. • destroy target enchantment. •  |
| <a href="https://scryfall.com/card/sos/219/rapturous-moment" class="card-link" target="_blank">Rapturous Moment<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/1/21afe19d-881a-48cb-863e-22942bea5ebe.jpg?1775938524" alt="Rapturous Moment"></span></a> | - | R,U | Sorcery | 6 | draw three cards, then discard two cards. add {u}{u}{r}{r}{r}. |
| <a href="https://scryfall.com/card/sos/222/root-manipulation" class="card-link" target="_blank">Root Manipulation<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/3/5390a79c-bc4b-4edb-a845-0d3514986401.jpg?1775938546" alt="Root Manipulation"></span></a> | - | B,G | Sorcery | 5 | until end of turn, creatures you control get +2/+2 and gain menace and "whenever this creature attac |
| <a href="https://scryfall.com/card/sos/223/sanar-unfinished-genius-wild-idea" class="card-link" target="_blank">Sanar, Unfinished Genius // Wild Idea<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/7/173157aa-712d-44f2-89ba-dd2511a07f26.jpg?1775938553" alt="Sanar, Unfinished Genius // Wild Idea"></span></a> | 0/4 | R,U | Legendary Creature — Goblin Sorcerer | 2 | sanar enters prepared. (while it's prepared, you may cast a copy of its spell. doing so unprepares i |
| <a href="https://scryfall.com/card/sos/224/scolding-administrator" class="card-link" target="_blank">Scolding Administrator<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/9/69757177-aefa-44a6-81db-5ae9b5d2f117.jpg?1775938562" alt="Scolding Administrator"></span></a> | 2/2 | B,W | Creature — Dwarf Cleric | 2 | menace (this creature can't be blocked except by two or more creatures.) repartee — whenever you cas |
| <a href="https://scryfall.com/card/sos/225/silverquill-charm" class="card-link" target="_blank">Silverquill Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/e/3eb73579-f1c6-4762-81d2-9568ab501fac.jpg?1775938570" alt="Silverquill Charm"></span></a> | - | B,W | Instant | 2 | choose one — • put two +1/+1 counters on target creature. • exile target creature with power 2 or le |
| <a href="https://scryfall.com/card/sos/227/snooping-page" class="card-link" target="_blank">Snooping Page<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/3/73d06987-8686-461b-b260-9a4fee6a3b32.jpg?1775938584" alt="Snooping Page"></span></a> | 2/3 | B,W | Creature — Human Cleric | 3 | repartee — whenever you cast an instant or sorcery spell that targets a creature, this creature can' |
| <a href="https://scryfall.com/card/sos/228/social-snub" class="card-link" target="_blank">Social Snub<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/0/a04b6900-0436-4920-a0d4-c0186d605ae3.jpg?1775938590" alt="Social Snub"></span></a> | - | B,W | Sorcery | 3 | when you cast this spell while you control a creature, you may copy this spell. each player sacrific |
| <a href="https://scryfall.com/card/sos/229/spectacular-skywhale" class="card-link" target="_blank">Spectacular Skywhale<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/9/c90366d5-b4ba-4772-a3c5-f138bbe7f305.jpg?1775938597" alt="Spectacular Skywhale"></span></a> | 1/4 | R,U | Creature — Elemental Whale | 4 | flying opus — whenever you cast an instant or sorcery spell, this creature gets +3/+0 until end of t |
| <a href="https://scryfall.com/card/sos/233/startled-relic-sloth" class="card-link" target="_blank">Startled Relic Sloth<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/1/f143fd41-58c3-45a0-bef8-e9e4b4a502a5.jpg?1775938628" alt="Startled Relic Sloth"></span></a> | 4/4 | R,W | Creature — Sloth Beast | 4 | trample, lifelink at the beginning of combat on your turn, exile up to one target card from a gravey |
| <a href="https://scryfall.com/card/sos/234/stirring-honormancer" class="card-link" target="_blank">Stirring Honormancer<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/e/ee84b04d-78fc-416f-9166-72e5417c3e17.jpg?1775938634" alt="Stirring Honormancer"></span></a> | 4/5 | B,W | Creature — Rhino Bard | 5 | when this creature enters, look at the top x cards of your library, where x is the number of creatur |
| <a href="https://scryfall.com/card/sos/235/stress-dream" class="card-link" target="_blank">Stress Dream<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/e/1ec40a1b-51e7-4a35-966c-ab2a10f21a80.jpg?1775938641" alt="Stress Dream"></span></a> | - | R,U | Instant | 5 | stress dream deals 5 damage to up to one target creature. look at the top two cards of your library. |
| <a href="https://scryfall.com/card/sos/237/tam-observant-sequencer-deep-sight" class="card-link" target="_blank">Tam, Observant Sequencer // Deep Sight<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/1/7120e71b-2976-451b-89a7-a1665dc6fb6b.jpg?1775938655" alt="Tam, Observant Sequencer // Deep Sight"></span></a> | 4/3 | G,U | Legendary Creature — Gorgon Wizard | 4 | landfall — whenever a land you control enters, tam becomes prepared. (while it's prepared, you may c |
| <a href="https://scryfall.com/card/sos/238/teachers-pest" class="card-link" target="_blank">Teacher's Pest<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/a/eaa358ac-761d-4507-aa15-3d4684027207.jpg?1775938661" alt="Teacher's Pest"></span></a> | 1/1 | B,G | Creature — Skeleton Pest | 2 | menace (this creature can't be blocked except by two or more creatures.) whenever this creature atta |
| <a href="https://scryfall.com/card/sos/240/vibrant-outburst" class="card-link" target="_blank">Vibrant Outburst<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/9/f9ba68ef-6efc-4249-8b74-e33f47173902.jpg?1775938674" alt="Vibrant Outburst"></span></a> | - | R,U | Instant | 2 | vibrant outburst deals 3 damage to any target. tap up to one target creature. |
| <a href="https://scryfall.com/card/sos/244/witherbloom-charm" class="card-link" target="_blank">Witherbloom Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/5/254437f7-7a8a-4b11-9cea-e8e7ea23c59e.jpg?1775938703" alt="Witherbloom Charm"></span></a> | - | B,G | Instant | 2 | choose one — • you may sacrifice a permanent. if you do, draw two cards. • you gain 5 life. • destro |

---
## 9. Notable Cards for Limited (by Rarity)

### Common Removal

| Card | P/T | Color | CMC | Categories |
|------|-----|-------|-----|------------|
| <a href="https://scryfall.com/card/sos/64/procrastinate" class="card-link" target="_blank">Procrastinate<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/e/1edb449d-620f-4e21-9d76-2c840635eb9d.jpg?1775937356" alt="Procrastinate"></span></a> | - | U | 1 | Tap/Stun |
| <a href="https://scryfall.com/card/sos/28/rapier-wit" class="card-link" target="_blank">Rapier Wit<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/7/97b50521-5a0f-4dbd-8e15-f0f0d059c258.jpg?1775937109" alt="Rapier Wit"></span></a> | - | W | 2 | Tap/Stun |
| <a href="https://scryfall.com/card/sos/38/banishing-betrayal" class="card-link" target="_blank">Banishing Betrayal<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/a/1ae9d2f3-7a9f-433a-aa1f-14337ae6f9d4.jpg?1775937176" alt="Banishing Betrayal"></span></a> | - | U | 2 | Bounce |
| <a href="https://scryfall.com/card/sos/47/essence-scatter" class="card-link" target="_blank">Essence Scatter<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/2/32840097-0531-4c43-b6a8-e76c17420b04.jpg?1775937236" alt="Essence Scatter"></span></a> | - | U | 2 | Counter |
| <a href="https://scryfall.com/card/sos/86/last-gasp" class="card-link" target="_blank">Last Gasp<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/a/da5f3729-6ec7-4482-90cb-83b973edeae4.jpg?1775937510" alt="Last Gasp"></span></a> | - | B | 2 | -3/-3 |
| <a href="https://scryfall.com/card/sos/135/tome-blast" class="card-link" target="_blank">Tome Blast<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/2/72a3b17d-1e00-48e9-8402-c81bacd595a7.jpg?1775937914" alt="Tome Blast"></span></a> | - | R | 2 | Damage: 2 |
| <a href="https://scryfall.com/card/sos/141/burrog-barrage" class="card-link" target="_blank">Burrog Barrage<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/5/95d5b0a8-2b66-418e-9e5e-ecf7b304c31e.jpg?1775937957" alt="Burrog Barrage"></span></a> | - | G | 2 | Bite, Damage: P |
| <a href="https://scryfall.com/card/sos/150/glorious-decay" class="card-link" target="_blank">Glorious Decay<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/3/a335f396-1004-4fee-842a-a35ff6ba17f2.jpg?1775938023" alt="Glorious Decay"></span></a> | - | G | 2 | Damage: 4 |
| <a href="https://scryfall.com/card/sos/42/deluge-virtuoso" class="card-link" target="_blank">Deluge Virtuoso<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/e/2e3b16ed-8727-48fd-8b1f-c0cbd329385e.jpg?1775937202" alt="Deluge Virtuoso"></span></a> | 2/2 | U | 3 | Tap/Stun |
| <a href="https://scryfall.com/card/sos/136/unsubtle-mockery" class="card-link" target="_blank">Unsubtle Mockery<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/b/2b7cb1a3-761e-470e-a164-6e29dd9448cd.jpg?1775937921" alt="Unsubtle Mockery"></span></a> | - | R | 3 | Damage: 4 |
| <a href="https://scryfall.com/card/sos/66/run-behind" class="card-link" target="_blank">Run Behind<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/0/40ecc34b-4cd0-4998-bbf4-7faa6fd3d7e0.jpg?1775937369" alt="Run Behind"></span></a> | - | U | 4 | Bounce (Library) |
| <a href="https://scryfall.com/card/sos/104/wander-off" class="card-link" target="_blank">Wander Off<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/d/3d409512-50b9-4a38-91b0-19ba25227992.jpg?1775937643" alt="Wander Off"></span></a> | - | B | 4 | Exile |
| <a href="https://scryfall.com/card/sos/243/wilt-in-the-heat" class="card-link" target="_blank">Wilt in the Heat<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/6/f63f7209-fc0f-400c-8076-125f3131cb32.jpg?1775938697" alt="Wilt in the Heat"></span></a> | - | MC | 4 | Damage: 5 |
| <a href="https://scryfall.com/card/sos/6/ajanis-response" class="card-link" target="_blank">Ajani's Response<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/c/9cd1417a-badc-4abd-a8ca-5b31f85c1072.jpg?1776047920" alt="Ajani's Response"></span></a> | - | W | 5 | Destroy |
| <a href="https://scryfall.com/card/sos/118/heated-argument" class="card-link" target="_blank">Heated Argument<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/0/0038d212-3d95-4f98-8c2e-7b2404d0ced7.jpg?1775937767" alt="Heated Argument"></span></a> | - | R | 5 | Damage: 6 |
| <a href="https://scryfall.com/card/sos/189/fractal-mascot" class="card-link" target="_blank">Fractal Mascot<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/f/cf5b19e3-eed1-4b36-9756-660ffb3baa08.jpg?1775938311" alt="Fractal Mascot"></span></a> | 6/6 | MC | 6 | Tap/Stun |

### Common Combat Tricks

| Card | P/T | Color | CMC | Categories |
|------|-----|-------|-----|------------|
| <a href="https://scryfall.com/card/sos/22/interjection" class="card-link" target="_blank">Interjection<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/5/0534cff6-299c-4155-b318-eb7581989e8a.jpg?1775937061" alt="Interjection"></span></a> | - | W | 1 | P/T Buff, Grants First Strike |
| <a href="https://scryfall.com/card/sos/41/chase-inspiration" class="card-link" target="_blank">Chase Inspiration<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/6/06f9f257-c7ef-44b7-8b2b-f038fba900af.jpg?1775937195" alt="Chase Inspiration"></span></a> | - | U | 1 | P/T Buff, Protection, Grants Hexproof |
| <a href="https://scryfall.com/card/sos/89/masterful-flourish" class="card-link" target="_blank">Masterful Flourish<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/d/8d93d14d-7760-4af2-a237-2df326dd28d3.jpg?1775937531" alt="Masterful Flourish"></span></a> | - | B | 1 | P/T Buff, Grants Indestructible, Protection |
| <a href="https://scryfall.com/card/sos/141/burrog-barrage" class="card-link" target="_blank">Burrog Barrage<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/5/95d5b0a8-2b66-418e-9e5e-ecf7b304c31e.jpg?1775937957" alt="Burrog Barrage"></span></a> | - | G | 2 | P/T Buff |
| <a href="https://scryfall.com/card/sos/144/efflorescence" class="card-link" target="_blank">Efflorescence<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/9/79b9ace7-eceb-4f97-9ee7-d5ee3e0b3515.jpg?1775937979" alt="Efflorescence"></span></a> | - | G | 3 | Grants Trample, Counters |

### Uncommon Removal

| Card | P/T | Color | CMC | Categories |
|------|-----|-------|-----|------------|
| <a href="https://scryfall.com/card/sos/79/dissection-practice" class="card-link" target="_blank">Dissection Practice<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/d/ddbf1242-6832-475e-9a77-65dd9b4bb32a.jpg?1775937462" alt="Dissection Practice"></span></a> | - | B | 1 | -1/-1 |
| <a href="https://scryfall.com/card/sos/112/duel-tactics" class="card-link" target="_blank">Duel Tactics<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/f/8f3a1675-0cc7-4dfd-a12e-4740a2cf81e8.jpg?1775937718" alt="Duel Tactics"></span></a> | - | R | 1 | Damage: 1 |
| <a href="https://scryfall.com/card/sos/119/impractical-joke" class="card-link" target="_blank">Impractical Joke<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/9/39a816b4-39b8-421c-b828-68db901d34b7.jpg?1775937777" alt="Impractical Joke"></span></a> | - | R | 1 | Damage: 3 |
| <a href="https://scryfall.com/card/sos/18/harsh-annotation" class="card-link" target="_blank">Harsh Annotation<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/0/e07a8fc7-c11c-4469-a31d-0abf40e57bbf.jpg?1775937033" alt="Harsh Annotation"></span></a> | - | W | 2 | Destroy |
| <a href="https://scryfall.com/card/sos/81/end-of-the-hunt" class="card-link" target="_blank">End of the Hunt<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/8/0809b51a-6a05-4f18-9bf4-1b8382da648f.jpg?1775937476" alt="End of the Hunt"></span></a> | - | B | 2 | Edict |
| <a href="https://scryfall.com/card/sos/200/lorehold-charm" class="card-link" target="_blank">Lorehold Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/f/5fe70295-e550-4577-a341-dab6c25aabfd.jpg?1775938389" alt="Lorehold Charm"></span></a> | - | MC | 2 | Edict |
| <a href="https://scryfall.com/card/sos/211/prismari-charm" class="card-link" target="_blank">Prismari Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/f/8f6c2a5e-fe13-407c-aadd-c9caf2884ff1.jpg?1775938465" alt="Prismari Charm"></span></a> | - | MC | 2 | Bounce |
| <a href="https://scryfall.com/card/sos/217/quandrix-charm" class="card-link" target="_blank">Quandrix Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/1/318486e0-f255-40f5-8150-dc272eec9d7d.jpg?1775938509" alt="Quandrix Charm"></span></a> | - | MC | 2 | Counter |
| <a href="https://scryfall.com/card/sos/225/silverquill-charm" class="card-link" target="_blank">Silverquill Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/e/3eb73579-f1c6-4762-81d2-9568ab501fac.jpg?1775938570" alt="Silverquill Charm"></span></a> | - | MC | 2 | Exile |
| <a href="https://scryfall.com/card/sos/240/vibrant-outburst" class="card-link" target="_blank">Vibrant Outburst<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/9/f9ba68ef-6efc-4249-8b74-e33f47173902.jpg?1775938674" alt="Vibrant Outburst"></span></a> | - | MC | 2 | Damage: 3 |
| <a href="https://scryfall.com/card/sos/244/witherbloom-charm" class="card-link" target="_blank">Witherbloom Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/5/254437f7-7a8a-4b11-9cea-e8e7ea23c59e.jpg?1775938703" alt="Witherbloom Charm"></span></a> | - | MC | 2 | Conditional Destroy |
| <a href="https://scryfall.com/card/sos/34/stand-up-for-yourself" class="card-link" target="_blank">Stand Up for Yourself<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/7/b756ca13-b904-4510-9bbb-5bc2864abfbd.jpg?1775937151" alt="Stand Up for Yourself"></span></a> | - | W | 3 | Conditional Destroy |
| <a href="https://scryfall.com/card/sos/83/foolish-fate" class="card-link" target="_blank">Foolish Fate<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/2/d278f4c9-d20b-4a76-8c5c-4d3e985948b9.jpg?1775937489" alt="Foolish Fate"></span></a> | - | B | 3 | Destroy |
| <a href="https://scryfall.com/card/sos/92/poisoners-apprentice" class="card-link" target="_blank">Poisoner's Apprentice<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/7/3755a2e9-af55-4625-a006-2a86c7893a96.jpg?1775937552" alt="Poisoner's Apprentice"></span></a> | 2/2 | B | 3 | -4/-4 |
| <a href="https://scryfall.com/card/sos/142/chelonian-tackle" class="card-link" target="_blank">Chelonian Tackle<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/8/a82a4d8c-4105-4923-85a2-ef58241f725c.jpg?1775937964" alt="Chelonian Tackle"></span></a> | - | G | 3 | Fight, Damage: P |
| <a href="https://scryfall.com/card/sos/39/brush-off" class="card-link" target="_blank">Brush Off<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/5/151eab82-d20f-433b-b3bb-1d44e2871d5c.jpg?1775937183" alt="Brush Off"></span></a> | - | U | 4 | Counter |
| <a href="https://scryfall.com/card/sos/107/archaics-agony" class="card-link" target="_blank">Archaic's Agony<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/d/8d99f8b2-5c1c-4059-bf68-c6b2e9e5b275.jpg?1775937675" alt="Archaic's Agony"></span></a> | - | R | 5 | Damage: X |
| <a href="https://scryfall.com/card/sos/108/artistic-process" class="card-link" target="_blank">Artistic Process<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/c/bce9d933-be58-4301-beb4-07b04d0b69f0.jpg?1775937683" alt="Artistic Process"></span></a> | - | R | 5 | Damage: 6 |
| <a href="https://scryfall.com/card/sos/235/stress-dream" class="card-link" target="_blank">Stress Dream<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/e/1ec40a1b-51e7-4a35-966c-ab2a10f21a80.jpg?1775938641" alt="Stress Dream"></span></a> | - | MC | 5 | Damage: 5 |
| <a href="https://scryfall.com/card/sos/3/sundering-archaic" class="card-link" target="_blank">Sundering Archaic<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/3/c35b57e4-2358-46c0-8f09-cd27c10eaf2d.jpg?1775936933" alt="Sundering Archaic"></span></a> | 3/3 | NC | 6 | Exile |
| <a href="https://scryfall.com/card/sos/53/homesickness" class="card-link" target="_blank">Homesickness<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/e/6e4a1f82-b0b1-4608-91f8-130bee731435.jpg?1775937280" alt="Homesickness"></span></a> | - | U | 6 | Tap/Stun |

---
## 10. Lands

| Card | Color | Rarity | Type |
|------|-------|--------|------|
| <a href="https://scryfall.com/card/sos/253/deathcap-glade" class="card-link" target="_blank">Deathcap Glade<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/8/78897104-80e1-4d8a-9958-145b40f679e8.jpg?1775938766" alt="Deathcap Glade"></span></a> | MC | R | Land |
| <a href="https://scryfall.com/card/sos/254/dreamroot-cascade" class="card-link" target="_blank">Dreamroot Cascade<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/f/ef662b92-5a7f-48c9-bcc1-14b55e091aef.jpg?1775938773" alt="Dreamroot Cascade"></span></a> | MC | R | Land |
| <a href="https://scryfall.com/card/sos/255/fields-of-strife" class="card-link" target="_blank">Fields of Strife<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/d/3dc7a4c3-c356-4fba-bea0-e8788da3eb57.jpg?1775938780" alt="Fields of Strife"></span></a> | MC | C | Land |
| <a href="https://scryfall.com/card/sos/256/forum-of-amity" class="card-link" target="_blank">Forum of Amity<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/d/1de6c6cc-0c55-4997-8623-d7f796bd9ab8.jpg?1775938787" alt="Forum of Amity"></span></a> | MC | C | Land |
| <a href="https://scryfall.com/card/sos/258/paradox-gardens" class="card-link" target="_blank">Paradox Gardens<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/b/dbc3447e-1329-4ea1-b4ca-b321b0ffec8f.jpg?1775938801" alt="Paradox Gardens"></span></a> | MC | C | Land |
| <a href="https://scryfall.com/card/sos/260/shattered-sanctum" class="card-link" target="_blank">Shattered Sanctum<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/a/5aa0c810-3b7d-4661-979e-e84fb327742d.jpg?1775938816" alt="Shattered Sanctum"></span></a> | MC | R | Land |
| <a href="https://scryfall.com/card/sos/262/spectacle-summit" class="card-link" target="_blank">Spectacle Summit<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/0/a0a66f7b-eab4-45da-8895-c2c2c7eb05f8.jpg?1775938830" alt="Spectacle Summit"></span></a> | MC | C | Land |
| <a href="https://scryfall.com/card/sos/263/stormcarved-coast" class="card-link" target="_blank">Stormcarved Coast<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/d/bd3ae4fa-4c97-410a-8c0a-bd203342595d.jpg?1775938837" alt="Stormcarved Coast"></span></a> | MC | R | Land |
| <a href="https://scryfall.com/card/sos/264/sundown-pass" class="card-link" target="_blank">Sundown Pass<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/3/b34000e9-ff20-4fb4-9d0b-03a172a92457.jpg?1775938845" alt="Sundown Pass"></span></a> | MC | R | Land |
| <a href="https://scryfall.com/card/sos/266/titans-grave" class="card-link" target="_blank">Titan's Grave<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/9/a9ab41c8-3ee2-4676-9b8b-20c34d9f5f21.jpg?1775938861" alt="Titan's Grave"></span></a> | MC | C | Land |
| <a href="https://scryfall.com/card/sos/257/great-hall-of-the-biblioplex" class="card-link" target="_blank">Great Hall of the Biblioplex<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/2/42d92674-2664-411c-b9c5-b04da7c845f4.jpg?1775938794" alt="Great Hall of the Biblioplex"></span></a> | NC | R | Land |
| <a href="https://scryfall.com/card/sos/259/petrified-hamlet" class="card-link" target="_blank">Petrified Hamlet<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/5/355dd460-b0e9-41f2-a058-b7f7e39ac387.jpg?1775938807" alt="Petrified Hamlet"></span></a> | NC | R | Land |
| <a href="https://scryfall.com/card/sos/261/skycoach-waypoint" class="card-link" target="_blank">Skycoach Waypoint<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/7/6747657b-5ce4-4dbd-b924-ca1f7119faf7.jpg?1775938823" alt="Skycoach Waypoint"></span></a> | NC | U | Land |
| <a href="https://scryfall.com/card/sos/265/terramorphic-expanse" class="card-link" target="_blank">Terramorphic Expanse<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/a/9a4c5629-fadd-42b9-850f-9f8586a2ca50.jpg?1775938853" alt="Terramorphic Expanse"></span></a> | NC | C | Land |

---
## 11. Other Cards

*Cards not classified as creatures, removal, burn, combat tricks, or lands.*

#### White

| Card | Rarity | CMC | Type |
|------|--------|-----|------|
| <a href="https://scryfall.com/card/sos/10/dig-site-inventory" class="card-link" target="_blank">Dig Site Inventory<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/5/e52464ee-df8b-41ec-af93-4b0eb004383e.jpg?1775936980" alt="Dig Site Inventory"></span></a> | C | 1 | Sorc |
| <a href="https://scryfall.com/card/sos/16/graduation-day" class="card-link" target="_blank">Graduation Day<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/b/db1cea01-123e-4b23-8b98-f94cabce3912.jpg?1775937020" alt="Graduation Day"></span></a> | U | 1 | Ench |
| <a href="https://scryfall.com/card/sos/17/group-project" class="card-link" target="_blank">Group Project<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/8/e8abc1eb-6225-4b18-8502-b5324b818aed.jpg?1775937026" alt="Group Project"></span></a> | U | 2 | Sorc |
| <a href="https://scryfall.com/card/sos/7/antiquities-on-the-loose" class="card-link" target="_blank">Antiquities on the Loose<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/8/68ee92cd-51af-4de5-bcc8-34d0bb2fd398.jpg?1775936960" alt="Antiquities on the Loose"></span></a> | R | 3 | Sorc |
| <a href="https://scryfall.com/card/sos/25/practiced-offense" class="card-link" target="_blank">Practiced Offense<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/9/79c7cf94-c0a1-432d-90d7-7f0599c2e7a8.jpg?1775937087" alt="Practiced Offense"></span></a> | R | 3 | Sorc |
| <a href="https://scryfall.com/card/sos/26/primary-research" class="card-link" target="_blank">Primary Research<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/6/f6fdb814-45c6-4d14-afff-7f5bd1bd10a1.jpg?1775937094" alt="Primary Research"></span></a> | U | 5 | Ench |
| <a href="https://scryfall.com/card/sos/30/restoration-seminar" class="card-link" target="_blank">Restoration Seminar<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/e/9ebc4ecf-2fa2-4ab8-afde-3b91cf5eadb6.jpg?1775937123" alt="Restoration Seminar"></span></a> | M | 7 | Sorc |

#### Blue

| Card | Rarity | CMC | Type |
|------|--------|-----|------|
| <a href="https://scryfall.com/card/sos/43/divergent-equation" class="card-link" target="_blank">Divergent Equation<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/6/26295e25-f1bf-4665-ba00-dad35c49bbc2.jpg?1775937210" alt="Divergent Equation"></span></a> | U | 1 | Inst |
| <a href="https://scryfall.com/card/sos/51/fractalize" class="card-link" target="_blank">Fractalize<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/3/e3c3b19b-01b6-4f5a-b428-513b778c5d89.jpg?1775937264" alt="Fractalize"></span></a> | U | 1 | Inst |
| <a href="https://scryfall.com/card/sos/49/flow-state" class="card-link" target="_blank">Flow State<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/7/47d6093b-b1b6-4956-8bfd-02cce899f832.jpg?1775937249" alt="Flow State"></span></a> | U | 2 | Sorc |
| <a href="https://scryfall.com/card/sos/58/mathemagics" class="card-link" target="_blank">Mathemagics<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/d/cd3cc172-5609-4bc8-9d84-50680fed6df9.jpg?1775937314" alt="Mathemagics"></span></a> | M | 2 | Sorc |
| <a href="https://scryfall.com/card/sos/65/quick-study" class="card-link" target="_blank">Quick Study<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/d/2d4f0bc7-da7c-4749-a24c-b01f3eb5860c.jpg?1775937363" alt="Quick Study"></span></a> | C | 3 | Inst |
| <a href="https://scryfall.com/card/sos/61/muses-encouragement" class="card-link" target="_blank">Muse's Encouragement<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/5/c59e0004-1d6a-42a1-8ce4-31da2af2e1bf.jpg?1775937336" alt="Muse's Encouragement"></span></a> | C | 5 | Inst |
| <a href="https://scryfall.com/card/sos/44/echocasting-symposium" class="card-link" target="_blank">Echocasting Symposium<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/d/5d7086a7-dc42-468a-a2cf-a6f89030f947.jpg?1775937216" alt="Echocasting Symposium"></span></a> | M | 6 | Sorc |
| <a href="https://scryfall.com/card/sos/71/wisdom-of-ages" class="card-link" target="_blank">Wisdom of Ages<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/2/b227ef04-33e4-44e8-a357-0ea3dfe5d49b.jpg?1775937405" alt="Wisdom of Ages"></span></a> | R | 7 | Sorc |

#### Black

| Card | Rarity | CMC | Type |
|------|--------|-----|------|
| <a href="https://scryfall.com/card/sos/100/send-in-the-pest" class="card-link" target="_blank">Send in the Pest<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/8/283b508b-89f0-4c23-9686-b049e402b73c.jpg?1775937607" alt="Send in the Pest"></span></a> | C | 2 | Sorc |
| <a href="https://scryfall.com/card/sos/77/cost-of-brilliance" class="card-link" target="_blank">Cost of Brilliance<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/a/3a46816b-9f75-4c72-9ec6-cded6a4a0d01.jpg?1775937447" alt="Cost of Brilliance"></span></a> | C | 3 | Sorc |
| <a href="https://scryfall.com/card/sos/95/pull-from-the-grave" class="card-link" target="_blank">Pull from the Grave<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/7/d73612fe-8992-4650-a7e3-c7b662da6a03.jpg?1775937572" alt="Pull from the Grave"></span></a> | C | 3 | Sorc |
| <a href="https://scryfall.com/card/sos/97/ral-zarek-guest-lecturer" class="card-link" target="_blank">Ral Zarek, Guest Lecturer<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/f/8fbad757-4081-42f7-a460-68ac03e77510.jpg?1775937587" alt="Ral Zarek, Guest Lecturer"></span></a> | M | 3 | Plan |
| <a href="https://scryfall.com/card/sos/73/arcane-omens" class="card-link" target="_blank">Arcane Omens<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/3/d357d997-9d4e-4ade-81f2-37629853f13a.jpg?1775937419" alt="Arcane Omens"></span></a> | U | 5 | Sorc |
| <a href="https://scryfall.com/card/sos/78/decorum-dissertation" class="card-link" target="_blank">Decorum Dissertation<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/4/f4ab2d9b-c73d-478d-aac7-4d3bb24296d2.jpg?1775937454" alt="Decorum Dissertation"></span></a> | M | 5 | Sorc |
| <a href="https://scryfall.com/card/sos/94/pox-plague" class="card-link" target="_blank">Pox Plague<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/c/9c99c17b-ad3a-4859-97e8-469718b81cd9.jpg?1775937566" alt="Pox Plague"></span></a> | R | 5 | Sorc |

#### Red

| Card | Rarity | CMC | Type |
|------|--------|-----|------|
| <a href="https://scryfall.com/card/sos/106/ancestral-anger" class="card-link" target="_blank">Ancestral Anger<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/c/6c5a93d6-d4ab-4062-bb3c-1b5330bf15ad.jpg?1775937666" alt="Ancestral Anger"></span></a> | C | 1 | Sorc |
| <a href="https://scryfall.com/card/sos/115/flashback" class="card-link" target="_blank">Flashback<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/b/1b832fda-d7c4-4566-884c-2a8b6da15488.jpg?1775937742" alt="Flashback"></span></a> | R | 1 | Inst |
| <a href="https://scryfall.com/card/sos/111/choreographed-sparks" class="card-link" target="_blank">Choreographed Sparks<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/c/0cda4235-4dce-48fe-a8a5-2a952dedbe25.jpg?1775937707" alt="Choreographed Sparks"></span></a> | R | 2 | Inst |
| <a href="https://scryfall.com/card/sos/121/living-history" class="card-link" target="_blank">Living History<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/0/2028792c-fd60-40d4-bff7-3b82dbe1ffb5.jpg?1775937797" alt="Living History"></span></a> | U | 2 | Ench |
| <a href="https://scryfall.com/card/sos/129/seize-the-spoils" class="card-link" target="_blank">Seize the Spoils<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/d/4ddf4e34-a1f9-4636-942d-0a08e9f94320.jpg?1775937868" alt="Seize the Spoils"></span></a> | C | 3 | Sorc |
| <a href="https://scryfall.com/card/sos/132/tablet-of-discovery" class="card-link" target="_blank">Tablet of Discovery<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/3/13059664-a940-4a66-8100-0c90b884bab4.jpg?1775937891" alt="Tablet of Discovery"></span></a> | U | 3 | Arti |
| <a href="https://scryfall.com/card/sos/120/improvisation-capstone" class="card-link" target="_blank">Improvisation Capstone<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/0/d01fe6e9-49ee-4708-833e-75cd5a9f167c.jpg?1775937787" alt="Improvisation Capstone"></span></a> | M | 7 | Sorc |

#### Green

| Card | Rarity | CMC | Type |
|------|--------|-----|------|
| <a href="https://scryfall.com/card/sos/156/oracles-restoration" class="card-link" target="_blank">Oracle's Restoration<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/8/0863a19d-4511-4a78-98dd-d194afd1c39b.jpg?1775938067" alt="Oracle's Restoration"></span></a> | C | 1 | Sorc |
| <a href="https://scryfall.com/card/sos/167/wild-hypothesis" class="card-link" target="_blank">Wild Hypothesis<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/4/04fdfabc-c247-4384-a5bb-f49035f8aae0.jpg?1775938142" alt="Wild Hypothesis"></span></a> | C | 1 | Sorc |
| <a href="https://scryfall.com/card/sos/143/comforting-counsel" class="card-link" target="_blank">Comforting Counsel<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/2/5223a04f-6b47-4379-80ce-8489c4a91734.jpg?1775937970" alt="Comforting Counsel"></span></a> | R | 2 | Ench |
| <a href="https://scryfall.com/card/sos/148/follow-the-lumarets" class="card-link" target="_blank">Follow the Lumarets<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/9/f9488480-2b6c-40bc-a93e-29fb1292a2e4.jpg?1775938009" alt="Follow the Lumarets"></span></a> | C | 2 | Sorc |
| <a href="https://scryfall.com/card/sos/158/planar-engineering" class="card-link" target="_blank">Planar Engineering<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/8/c83b96a3-ddfd-4d11-8a85-5bf62087cbb9.jpg?1775938080" alt="Planar Engineering"></span></a> | R | 4 | Sorc |
| <a href="https://scryfall.com/card/sos/169/zimones-experiment" class="card-link" target="_blank">Zimone's Experiment<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/6/a6597852-4267-4ea6-a391-f927e4833be2.jpg?1775938156" alt="Zimone's Experiment"></span></a> | U | 4 | Sorc |
| <a href="https://scryfall.com/card/sos/139/additive-evolution" class="card-link" target="_blank">Additive Evolution<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/4/b44ec684-d558-45eb-bcd6-8119428634c2.jpg?1775937943" alt="Additive Evolution"></span></a> | U | 5 | Ench |
| <a href="https://scryfall.com/card/sos/149/germination-practicum" class="card-link" target="_blank">Germination Practicum<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/b/abe8332f-c76e-44e2-9427-d1228453abec.jpg?1775938016" alt="Germination Practicum"></span></a> | M | 5 | Sorc |
| <a href="https://scryfall.com/card/sos/161/snarl-song" class="card-link" target="_blank">Snarl Song<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/c/fc4c7fa2-aebb-4636-9afd-f1010c923316.jpg?1775938101" alt="Snarl Song"></span></a> | U | 6 | Sorc |

#### Multicolor

| Card | Rarity | CMC | Type |
|------|--------|-----|------|
| <a href="https://scryfall.com/card/sos/193/growth-curve" class="card-link" target="_blank">Growth Curve<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/6/1675a445-86ae-413b-b95a-a1c254a7f252.jpg?1775938339" alt="Growth Curve"></span></a> | U | 2 | Sorc |
| <a href="https://scryfall.com/card/sos/197/killians-confidence" class="card-link" target="_blank">Killian's Confidence<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/5/55ff776a-fc3b-4338-8864-d57a85b3f123.jpg?1775938369" alt="Killian's Confidence"></span></a> | U | 2 | Sorc |
| <a href="https://scryfall.com/card/sos/202/mind-into-matter" class="card-link" target="_blank">Mind into Matter<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/a/0a7f0fdf-1d4b-4458-a19c-274611e8a59a.jpg?1775938403" alt="Mind into Matter"></span></a> | R | 2 | Sorc |
| <a href="https://scryfall.com/card/sos/204/molten-note" class="card-link" target="_blank">Molten Note<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/0/506f69aa-7dc4-4dd7-990a-7371fc1762c0.jpg?1775938416" alt="Molten Note"></span></a> | U | 2 | Sorc |
| <a href="https://scryfall.com/card/sos/216/pursue-the-past" class="card-link" target="_blank">Pursue the Past<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/5/4584d5f7-b1f1-4c8e-80c5-ad35e44a968e.jpg?1775938502" alt="Pursue the Past"></span></a> | C | 2 | Sorc |
| <a href="https://scryfall.com/card/sos/179/cauldron-of-essence" class="card-link" target="_blank">Cauldron of Essence<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/7/b7091740-e70c-4cf2-8d3d-b8e1ac1fbbdd.jpg?1775938230" alt="Cauldron of Essence"></span></a> | R | 3 | Arti |
| <a href="https://scryfall.com/card/sos/184/dinas-guidance" class="card-link" target="_blank">Dina's Guidance<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/7/775c1e50-08a4-413f-ab0f-f1c2a79cfe94.jpg?1775938273" alt="Dina's Guidance"></span></a> | R | 3 | Inst |
| <a href="https://scryfall.com/card/sos/192/grapple-with-death" class="card-link" target="_blank">Grapple with Death<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/2/62842fb4-8bd3-4d80-b4f9-5bc3c5cebd3a.jpg?1775938332" alt="Grapple with Death"></span></a> | C | 3 | Sorc |
| <a href="https://scryfall.com/card/sos/203/mind-roots" class="card-link" target="_blank">Mind Roots<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/d/9d5fdbda-ebbe-45d6-a668-5ddee057a063.jpg?1775938410" alt="Mind Roots"></span></a> | U | 3 | Sorc |
| <a href="https://scryfall.com/card/sos/228/social-snub" class="card-link" target="_blank">Social Snub<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/0/a04b6900-0436-4920-a0d4-c0186d605ae3.jpg?1775938590" alt="Social Snub"></span></a> | U | 3 | Sorc |
| <a href="https://scryfall.com/card/sos/172/applied-geometry" class="card-link" target="_blank">Applied Geometry<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/1/f109f2eb-895b-44a6-b6b5-81bf3831ccd5.jpg?1775938180" alt="Applied Geometry"></span></a> | R | 4 | Sorc |
| <a href="https://scryfall.com/card/sos/178/borrowed-knowledge" class="card-link" target="_blank">Borrowed Knowledge<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/3/a3226e14-554d-47c9-b8b6-dfeb53cc41ba.jpg?1775938224" alt="Borrowed Knowledge"></span></a> | U | 4 | Sorc |
| <a href="https://scryfall.com/card/sos/188/fix-whats-broken" class="card-link" target="_blank">Fix What's Broken<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/0/c0cd1d71-8e4a-4e00-80cd-83aec231fa57.jpg?1775938304" alt="Fix What's Broken"></span></a> | R | 4 | Sorc |
| <a href="https://scryfall.com/card/sos/213/proctors-gaze" class="card-link" target="_blank">Proctor's Gaze<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/1/b127d543-0a90-4af6-9410-94d5cd30389e.jpg?1775938479" alt="Proctor's Gaze"></span></a> | U | 4 | Inst |
| <a href="https://scryfall.com/card/sos/220/render-speechless" class="card-link" target="_blank">Render Speechless<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/5/25bbb1c7-14e8-444f-ab98-e95f50927460.jpg?1775938531" alt="Render Speechless"></span></a> | C | 4 | Sorc |
| <a href="https://scryfall.com/card/sos/221/resonating-lute" class="card-link" target="_blank">Resonating Lute<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/e/6ef168d6-28f2-4c24-9bfa-82c35663b729.jpg?1775938538" alt="Resonating Lute"></span></a> | R | 4 | Arti |
| <a href="https://scryfall.com/card/sos/241/vicious-rivalry" class="card-link" target="_blank">Vicious Rivalry<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/f/6fa9cd18-3181-4373-ab65-49bf9de9487f.jpg?1775938681" alt="Vicious Rivalry"></span></a> | R | 4 | Sorc |
| <a href="https://scryfall.com/card/sos/186/embrace-the-paradox" class="card-link" target="_blank">Embrace the Paradox<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/0/c0cf5e0f-3668-46f2-850d-d91a538e8ead.jpg?1775938288" alt="Embrace the Paradox"></span></a> | C | 5 | Inst |
| <a href="https://scryfall.com/card/sos/222/root-manipulation" class="card-link" target="_blank">Root Manipulation<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/3/5390a79c-bc4b-4edb-a845-0d3514986401.jpg?1775938546" alt="Root Manipulation"></span></a> | U | 5 | Sorc |
| <a href="https://scryfall.com/card/sos/219/rapturous-moment" class="card-link" target="_blank">Rapturous Moment<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/1/21afe19d-881a-48cb-863e-22942bea5ebe.jpg?1775938524" alt="Rapturous Moment"></span></a> | U | 6 | Sorc |
| <a href="https://scryfall.com/card/sos/242/visionarys-dance" class="card-link" target="_blank">Visionary's Dance<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/4/846a0e79-a530-429e-8f7f-4b87f1b0156e.jpg?1776000377" alt="Visionary's Dance"></span></a> | C | 7 | Sorc |

#### Colorless

| Card | Rarity | CMC | Type |
|------|--------|-----|------|
| <a href="https://scryfall.com/card/sos/248/diary-of-dreams" class="card-link" target="_blank">Diary of Dreams<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/e/ee1e0a96-af80-444e-a456-5b256cf60625.jpg?1775938731" alt="Diary of Dreams"></span></a> | U | 2 | Arti |
| <a href="https://scryfall.com/card/sos/251/potioners-trove" class="card-link" target="_blank">Potioner's Trove<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/1/2123b349-4649-4a15-a8b5-b54414d2b1b7.jpg?1775938752" alt="Potioner's Trove"></span></a> | C | 3 | Arti |
| <a href="https://scryfall.com/card/sos/252/strixhaven-skycoach" class="card-link" target="_blank">Strixhaven Skycoach<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/7/87741fbb-b426-4f83-a358-587b0907f081.jpg?1775938759" alt="Strixhaven Skycoach"></span></a> | U | 3 | Arti |


