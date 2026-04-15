---
layout: default
---

<style>
.card-link {
  position: relative;
  text-decoration: none;
  border-bottom: 1px dotted #666;
  color: inherit;
  white-space: nowrap;
}
.card-link:hover {
  color: #1a6baa;
}
.card-preview {
  display: none;
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1000;
  padding: 4px;
  pointer-events: none;
}
.card-link:hover .card-preview {
  display: block;
}
.card-preview img {
  width: 244px;
  height: auto;
  border-radius: 10px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.4);
}
/* Keep preview in viewport */
td:first-child .card-preview,
td:nth-child(1) .card-preview {
  left: 0;
  transform: translateX(0);
}
</style>


# Secrets of Strixhaven (SOS) -- Set Analysis

**Total unique cards:** 271
**Release date:** April 24, 2026
**Source:** Scryfall API (`e:sos`)

*Hover over card names to preview the card image. Click to open on Scryfall.*

---
## 1. Set Overview

### Card Count by Color

| Type | W | U | B | R | G | MC | NC |
|------|---|---|---|---|---|---|---|
| Total | 33 | 35 | 35 | 33 | 33 | 87 | 15 |
| Creatures | 18 | 17 | 19 | 17 | 18 | 42 | 7 |
| Instants | 7 | 16 | 6 | 6 | 5 | 13 | 0 |
| Sorceries | 11 | 9 | 15 | 13 | 11 | 23 | 1 |
| Enchantments | 2 | 0 | 0 | 1 | 2 | 0 | 0 |
| Artifacts | 0 | 0 | 0 | 1 | 0 | 4 | 6 |
| Planeswalkers | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
| Lands | 1 | 1 | 1 | 1 | 1 | 10 | 4 |

### Card Count by Rarity

| Type | C | U | R | M |
|------|---|---|---|---|
| Total | 91 | 100 | 60 | 20 |
| Creatures | 45 | 53 | 29 | 11 |
| Instants | 19 | 21 | 10 | 3 |
| Sorceries | 24 | 32 | 18 | 9 |
| Enchantments | 0 | 4 | 1 | 0 |
| Artifacts | 4 | 4 | 3 | 0 |
| Planeswalkers | 0 | 0 | 0 | 2 |
| Lands | 11 | 1 | 7 | 0 |

### Color x Rarity Matrix

| Color | C | U | R | M | Total |
|-------|---|---|---|---|-------|
| W | 13 | 12 | 6 | 2 | 33 |
| U | 13 | 12 | 7 | 3 | 35 |
| B | 13 | 12 | 6 | 4 | 35 |
| R | 13 | 12 | 6 | 2 | 33 |
| G | 13 | 12 | 6 | 2 | 33 |
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

| Color | Count | Avg P | Avg T | Avg CMC | Keywords |
|-------|-------|-------|-------|---------|----------|
| W | 18 | 2.4 | 2.6 | 2.9 | 16 |
| U | 17 | 1.7 | 2.5 | 2.9 | 14 |
| B | 19 | 2.9 | 2.7 | 3.2 | 17 |
| R | 17 | 2.7 | 3.0 | 3.5 | 15 |
| G | 18 | 2.6 | 2.9 | 2.8 | 14 |
| MC | 42 | 2.9 | 3.4 | 3.6 | 30 |
| NC | 7 | 3.3 | 3.6 | 5.1 | 6 |

### Creature Stats by Rarity

| Rarity | Count | Avg P | Avg T | Avg CMC |
|--------|-------|-------|-------|---------|
| C | 45 | 2.4 | 2.6 | 3.1 |
| U | 53 | 2.6 | 3.0 | 3.4 |
| R | 29 | 2.3 | 2.8 | 2.8 |
| M | 11 | 4.7 | 4.7 | 5.2 |

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

---
## 4. Removal Spells

### Removal Count by Color

| Category | W | U | B | R | G | MC | NC |
|----------|---|---|---|---|---|---|---|
| **Total** | 7 | 8 | 6 | 10 | 3 | 15 | 2 |
| -X/-X | 0 | 0 | 2 | 0 | 0 | 0 | 0 |
| Bite | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Board Wipe | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| Bounce | 0 | 1 | 0 | 0 | 0 | 1 | 0 |
| Bounce (Library) | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| Conditional Destroy | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| Counter | 0 | 3 | 0 | 0 | 0 | 1 | 0 |
| Damage | 0 | 0 | 0 | 10 | 3 | 6 | 1 |
| Destroy | 3 | 0 | 1 | 0 | 0 | 2 | 0 |
| Edict | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
| Exile | 2 | 0 | 1 | 0 | 0 | 2 | 1 |
| Fight | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Tap/Stun | 1 | 3 | 0 | 0 | 0 | 1 | 0 |

### Removal Count by Rarity

| Category | C | U | R | M |
|----------|---|---|---|---|
| **Total** | 17 | 21 | 9 | 4 |
| -X/-X | 1 | 1 | 0 | 0 |
| Bite | 1 | 0 | 0 | 0 |
| Board Wipe | 0 | 0 | 0 | 1 |
| Bounce | 1 | 1 | 0 | 0 |
| Bounce (Library) | 1 | 0 | 0 | 0 |
| Conditional Destroy | 0 | 2 | 0 | 0 |
| Counter | 1 | 2 | 1 | 0 |
| Damage | 7 | 7 | 5 | 1 |
| Destroy | 1 | 2 | 2 | 1 |
| Edict | 0 | 2 | 0 | 0 |
| Exile | 1 | 3 | 1 | 1 |
| Fight | 0 | 1 | 0 | 0 |
| Tap/Stun | 4 | 1 | 0 | 0 |

### Full Removal List by Color

#### White

| Card | P/T | Rarity | CMC | Type | Categories |
|------|-----|--------|-----|------|------------|
| <a href="https://scryfall.com/card/sos/9/daydream" class="card-link" target="_blank">Daydream<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/2/e2b16cb2-b8b2-45df-9695-3c16e9d89e28.jpg?1775936973" alt="Daydream"></span></a> | - | U | 1 | Sorc | Exile |
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
| <a href="https://scryfall.com/card/sos/79/dissection-practice" class="card-link" target="_blank">Dissection Practice<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/d/ddbf1242-6832-475e-9a77-65dd9b4bb32a.jpg?1775937462" alt="Dissection Practice"></span></a> | - | U | 1 | Inst | -X/-X |
| <a href="https://scryfall.com/card/sos/81/end-of-the-hunt" class="card-link" target="_blank">End of the Hunt<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/8/0809b51a-6a05-4f18-9bf4-1b8382da648f.jpg?1775937476" alt="End of the Hunt"></span></a> | - | U | 2 | Sorc | Edict |
| <a href="https://scryfall.com/card/sos/86/last-gasp" class="card-link" target="_blank">Last Gasp<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/a/da5f3729-6ec7-4482-90cb-83b973edeae4.jpg?1775937510" alt="Last Gasp"></span></a> | - | C | 2 | Inst | -X/-X |
| <a href="https://scryfall.com/card/sos/83/foolish-fate" class="card-link" target="_blank">Foolish Fate<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/2/d278f4c9-d20b-4a76-8c5c-4d3e985948b9.jpg?1775937489" alt="Foolish Fate"></span></a> | - | U | 3 | Inst | Destroy |
| <a href="https://scryfall.com/card/sos/105/withering-curse" class="card-link" target="_blank">Withering Curse<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/0/50aaf618-dddb-4cbe-8231-d634b4498563.jpg?1775937655" alt="Withering Curse"></span></a> | - | M | 3 | Sorc | Board Wipe |
| <a href="https://scryfall.com/card/sos/104/wander-off" class="card-link" target="_blank">Wander Off<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/d/3d409512-50b9-4a38-91b0-19ba25227992.jpg?1775937643" alt="Wander Off"></span></a> | - | C | 4 | Inst | Exile |

#### Red

| Card | P/T | Rarity | CMC | Type | Categories |
|------|-----|--------|-----|------|------------|
| <a href="https://scryfall.com/card/sos/112/duel-tactics" class="card-link" target="_blank">Duel Tactics<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/f/8f3a1675-0cc7-4dfd-a12e-4740a2cf81e8.jpg?1775937718" alt="Duel Tactics"></span></a> | - | U | 1 | Sorc | Damage |
| <a href="https://scryfall.com/card/sos/113/emeritus-of-conflict-lightning-bolt" class="card-link" target="_blank">Emeritus of Conflict // Lightning Bolt<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/5/f58dba4f-1abb-47a3-a684-29c32bab95c0.jpg?1775937726" alt="Emeritus of Conflict // Lightning Bolt"></span></a> | 2/2 | M | 2 | Inst/Crea | Damage |
| <a href="https://scryfall.com/card/sos/134/thunderdrum-soloist" class="card-link" target="_blank">Thunderdrum Soloist<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/9/590d1d95-ed13-4121-899f-f5a2d8a6617a.jpg?1775937905" alt="Thunderdrum Soloist"></span></a> | 1/3 | U | 2 | Crea | Damage |
| <a href="https://scryfall.com/card/sos/135/tome-blast" class="card-link" target="_blank">Tome Blast<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/2/72a3b17d-1e00-48e9-8402-c81bacd595a7.jpg?1775937914" alt="Tome Blast"></span></a> | - | C | 2 | Sorc | Damage |
| <a href="https://scryfall.com/card/sos/128/rubble-rouser" class="card-link" target="_blank">Rubble Rouser<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/f/afe61957-a9bb-42b0-98e8-b5fa418cbaff.jpg?1775937860" alt="Rubble Rouser"></span></a> | 1/4 | C | 3 | Crea | Damage |
| <a href="https://scryfall.com/card/sos/130/steal-the-show" class="card-link" target="_blank">Steal the Show<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/a/7ac6649f-980e-4404-9c05-458c30578ecc.jpg?1775937875" alt="Steal the Show"></span></a> | - | R | 3 | Sorc | Damage |
| <a href="https://scryfall.com/card/sos/136/unsubtle-mockery" class="card-link" target="_blank">Unsubtle Mockery<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/b/2b7cb1a3-761e-470e-a164-6e29dd9448cd.jpg?1775937921" alt="Unsubtle Mockery"></span></a> | - | C | 3 | Inst | Damage |
| <a href="https://scryfall.com/card/sos/107/archaics-agony" class="card-link" target="_blank">Archaic's Agony<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/d/8d99f8b2-5c1c-4059-bf68-c6b2e9e5b275.jpg?1775937675" alt="Archaic's Agony"></span></a> | - | U | 5 | Sorc | Damage |
| <a href="https://scryfall.com/card/sos/108/artistic-process" class="card-link" target="_blank">Artistic Process<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/c/bce9d933-be58-4301-beb4-07b04d0b69f0.jpg?1775937683" alt="Artistic Process"></span></a> | - | U | 5 | Sorc | Damage |
| <a href="https://scryfall.com/card/sos/118/heated-argument" class="card-link" target="_blank">Heated Argument<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/0/0038d212-3d95-4f98-8c2e-7b2404d0ced7.jpg?1775937767" alt="Heated Argument"></span></a> | - | C | 5 | Inst | Damage |

#### Green

| Card | P/T | Rarity | CMC | Type | Categories |
|------|-----|--------|-----|------|------------|
| <a href="https://scryfall.com/card/sos/141/burrog-barrage" class="card-link" target="_blank">Burrog Barrage<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/5/95d5b0a8-2b66-418e-9e5e-ecf7b304c31e.jpg?1775937957" alt="Burrog Barrage"></span></a> | - | C | 2 | Inst | Damage, Bite |
| <a href="https://scryfall.com/card/sos/150/glorious-decay" class="card-link" target="_blank">Glorious Decay<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/3/a335f396-1004-4fee-842a-a35ff6ba17f2.jpg?1775938023" alt="Glorious Decay"></span></a> | - | C | 2 | Inst | Damage |
| <a href="https://scryfall.com/card/sos/142/chelonian-tackle" class="card-link" target="_blank">Chelonian Tackle<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/8/a82a4d8c-4105-4923-85a2-ef58241f725c.jpg?1775937964" alt="Chelonian Tackle"></span></a> | - | U | 3 | Sorc | Damage, Fight |

#### Multicolor

| Card | P/T | Rarity | CMC | Type | Categories |
|------|-----|--------|-----|------|------------|
| <a href="https://scryfall.com/card/sos/200/lorehold-charm" class="card-link" target="_blank">Lorehold Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/f/5fe70295-e550-4577-a341-dab6c25aabfd.jpg?1775938389" alt="Lorehold Charm"></span></a> | - | U | 2 | Inst | Edict |
| <a href="https://scryfall.com/card/sos/211/prismari-charm" class="card-link" target="_blank">Prismari Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/f/8f6c2a5e-fe13-407c-aadd-c9caf2884ff1.jpg?1775938465" alt="Prismari Charm"></span></a> | - | U | 2 | Inst | Bounce |
| <a href="https://scryfall.com/card/sos/217/quandrix-charm" class="card-link" target="_blank">Quandrix Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/1/318486e0-f255-40f5-8150-dc272eec9d7d.jpg?1775938509" alt="Quandrix Charm"></span></a> | - | U | 2 | Inst | Counter |
| <a href="https://scryfall.com/card/sos/225/silverquill-charm" class="card-link" target="_blank">Silverquill Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/e/3eb73579-f1c6-4762-81d2-9568ab501fac.jpg?1775938570" alt="Silverquill Charm"></span></a> | - | U | 2 | Inst | Exile |
| <a href="https://scryfall.com/card/sos/239/traumatic-critique" class="card-link" target="_blank">Traumatic Critique<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/a/2a812fa7-4599-4e25-97db-20ffc6bc0b26.jpg?1775938668" alt="Traumatic Critique"></span></a> | - | R | 2 | Inst | Damage |
| <a href="https://scryfall.com/card/sos/240/vibrant-outburst" class="card-link" target="_blank">Vibrant Outburst<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/9/f9ba68ef-6efc-4249-8b74-e33f47173902.jpg?1775938674" alt="Vibrant Outburst"></span></a> | - | U | 2 | Inst | Damage |
| <a href="https://scryfall.com/card/sos/244/witherbloom-charm" class="card-link" target="_blank">Witherbloom Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/5/254437f7-7a8a-4b11-9cea-e8e7ea23c59e.jpg?1775938703" alt="Witherbloom Charm"></span></a> | - | U | 2 | Inst | Conditional Destroy |
| <a href="https://scryfall.com/card/sos/236/suspend-aggression" class="card-link" target="_blank">Suspend Aggression<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/3/135c0696-d86d-4e48-988c-5c218de451fc.jpg?1775938648" alt="Suspend Aggression"></span></a> | - | R | 3 | Inst | Exile |
| <a href="https://scryfall.com/card/sos/173/ark-of-hunger" class="card-link" target="_blank">Ark of Hunger<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/9/79d01c19-162b-4a12-9e27-18366d95eaa0.jpg?1775938187" alt="Ark of Hunger"></span></a> | - | R | 4 | Arti | Damage |
| <a href="https://scryfall.com/card/sos/214/professor-dellian-fel" class="card-link" target="_blank">Professor Dellian Fel<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/f/6ff3b4d8-1271-4c5d-8834-7662244f173d.jpg?1775938486" alt="Professor Dellian Fel"></span></a> | - | M | 4 | Plan | Destroy |
| <a href="https://scryfall.com/card/sos/243/wilt-in-the-heat" class="card-link" target="_blank">Wilt in the Heat<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/6/f63f7209-fc0f-400c-8076-125f3131cb32.jpg?1775938697" alt="Wilt in the Heat"></span></a> | - | C | 4 | Inst | Damage |
| <a href="https://scryfall.com/card/sos/231/splatter-technique" class="card-link" target="_blank">Splatter Technique<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/6/969b6657-c3b9-47e1-a42e-95bbcccf452d.jpg?1775938612" alt="Splatter Technique"></span></a> | - | R | 5 | Sorc | Damage |
| <a href="https://scryfall.com/card/sos/181/colossus-of-the-blood-age" class="card-link" target="_blank">Colossus of the Blood Age<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/f/bfa7f0a4-6b65-4e53-ba00-848df260d8e3.jpg?1775938248" alt="Colossus of the Blood Age"></span></a> | 6/6 | U | 6 | Crea/Arti | Damage |
| <a href="https://scryfall.com/card/sos/189/fractal-mascot" class="card-link" target="_blank">Fractal Mascot<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/f/cf5b19e3-eed1-4b36-9756-660ffb3baa08.jpg?1775938311" alt="Fractal Mascot"></span></a> | 6/6 | C | 6 | Crea | Tap/Stun |
| <a href="https://scryfall.com/card/sos/205/moment-of-reckoning" class="card-link" target="_blank">Moment of Reckoning<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/7/577d9dc8-7720-4dc9-b650-64b4729b309b.jpg?1775938423" alt="Moment of Reckoning"></span></a> | - | R | 7 | Sorc | Destroy |

#### Colorless

| Card | P/T | Rarity | CMC | Type | Categories |
|------|-----|--------|-----|------|------------|
| <a href="https://scryfall.com/card/sos/3/sundering-archaic" class="card-link" target="_blank">Sundering Archaic<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/3/c35b57e4-2358-46c0-8f09-cd27c10eaf2d.jpg?1775936933" alt="Sundering Archaic"></span></a> | 3/3 | U | 6 | Crea | Exile |
| <a href="https://scryfall.com/card/sos/4/together-as-one" class="card-link" target="_blank">Together as One<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/c/ac2a8a66-e38c-42ab-83e1-d2d99ee48861.jpg?1775936940" alt="Together as One"></span></a> | - | R | 6 | Sorc | Damage |

---
## 5. Combat Tricks

### Combat Trick Count by Color

| Category | W | U | B | R | G | MC |
|----------|---|---|---|---|---|---|
| **Total** | 1 | 3 | 3 | 1 | 3 | 2 |
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

| Category | C | U |
|----------|---|---|
| **Total** | 5 | 8 |
| Counters | 1 | 2 |
| Falter | 0 | 1 |
| Grants First Strike | 1 | 0 |
| Grants Flying | 0 | 1 |
| Grants Hexproof | 1 | 0 |
| Grants Indestructible | 1 | 0 |
| Grants Trample | 1 | 1 |
| P/T Buff | 4 | 3 |
| P/T Buff (Team) | 0 | 1 |
| Protection | 2 | 0 |

### Full Combat Tricks List

| Card | P/T | Color | Rarity | CMC | Categories | Effect Summary |
|------|-----|-------|--------|-----|------------|----------------|
| <a href="https://scryfall.com/card/sos/22/interjection" class="card-link" target="_blank">Interjection<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/5/0534cff6-299c-4155-b318-eb7581989e8a.jpg?1775937061" alt="Interjection"></span></a> | - | W | C | 1 | P/T Buff, Grants First Strike | target creature gets +2/+2 and gains first strike until end of turn. |
| <a href="https://scryfall.com/card/sos/41/chase-inspiration" class="card-link" target="_blank">Chase Inspiration<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/6/06f9f257-c7ef-44b7-8b2b-f038fba900af.jpg?1775937195" alt="Chase Inspiration"></span></a> | - | U | C | 1 | P/T Buff, Protection, Grants Hexproof | target creature you control gets +0/+3 and gains hexproof until end of turn. (it |
| <a href="https://scryfall.com/card/sos/50/fractal-anomaly" class="card-link" target="_blank">Fractal Anomaly<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/1/e1975a61-aef0-49a6-a6d6-c3a37e2e2b22.jpg?1775937257" alt="Fractal Anomaly"></span></a> | - | U | U | 1 | Counters | create a 0/0 green and blue fractal creature token and put x +1/+1 counters on i |
| <a href="https://scryfall.com/card/sos/46/encouraging-aviator-jump" class="card-link" target="_blank">Encouraging Aviator // Jump<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/2/72654b84-9902-41db-92ab-a3499c31221c.jpg?1775937230" alt="Encouraging Aviator // Jump"></span></a> | 2/3 | U | U | 3 | Grants Flying | target creature gains flying until end of turn. |
| <a href="https://scryfall.com/card/sos/79/dissection-practice" class="card-link" target="_blank">Dissection Practice<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/d/ddbf1242-6832-475e-9a77-65dd9b4bb32a.jpg?1775937462" alt="Dissection Practice"></span></a> | - | B | U | 1 | P/T Buff | up to one target creature gets +1/+1 until end of turn. |
| <a href="https://scryfall.com/card/sos/89/masterful-flourish" class="card-link" target="_blank">Masterful Flourish<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/d/8d93d14d-7760-4af2-a237-2df326dd28d3.jpg?1775937531" alt="Masterful Flourish"></span></a> | - | B | C | 1 | P/T Buff, Grants Indestructible, Protection | target creature you control gets +1/+0 and gains indestructible until end of tur |
| <a href="https://scryfall.com/card/sos/96/rabid-attack" class="card-link" target="_blank">Rabid Attack<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/5/f5e67560-3135-4b27-a344-5859edf8bcd9.jpg?1775937579" alt="Rabid Attack"></span></a> | - | B | U | 2 | P/T Buff | until end of turn, any number of target creatures you control each get +1/+0 and |
| <a href="https://scryfall.com/card/sos/112/duel-tactics" class="card-link" target="_blank">Duel Tactics<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/f/8f3a1675-0cc7-4dfd-a12e-4740a2cf81e8.jpg?1775937718" alt="Duel Tactics"></span></a> | - | R | U | 1 | Falter | duel tactics deals 1 damage to target creature. it can't block this turn. |
| <a href="https://scryfall.com/card/sos/141/burrog-barrage" class="card-link" target="_blank">Burrog Barrage<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/5/95d5b0a8-2b66-418e-9e5e-ecf7b304c31e.jpg?1775937957" alt="Burrog Barrage"></span></a> | - | G | C | 2 | P/T Buff | target creature you control gets +1/+0 until end of turn if you've cast another  |
| <a href="https://scryfall.com/card/sos/153/lumarets-favor" class="card-link" target="_blank">Lumaret's Favor<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/5/c5e7c856-8b71-44e6-8998-0b0b3ff0ef99.jpg?1775938045" alt="Lumaret's Favor"></span></a> | - | G | U | 2 | P/T Buff | target creature gets +2/+4 until end of turn. |
| <a href="https://scryfall.com/card/sos/144/efflorescence" class="card-link" target="_blank">Efflorescence<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/9/79b9ace7-eceb-4f97-9ee7-d5ee3e0b3515.jpg?1775937979" alt="Efflorescence"></span></a> | - | G | C | 3 | Counters, Grants Trample | put two +1/+1 counters on target creature. |
| <a href="https://scryfall.com/card/sos/200/lorehold-charm" class="card-link" target="_blank">Lorehold Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/f/5fe70295-e550-4577-a341-dab6c25aabfd.jpg?1775938389" alt="Lorehold Charm"></span></a> | - | MC | U | 2 | P/T Buff (Team), Grants Trample | choose one —
• each opponent sacrifices a nontoken artifact of their choice.
• r |
| <a href="https://scryfall.com/card/sos/225/silverquill-charm" class="card-link" target="_blank">Silverquill Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/e/3eb73579-f1c6-4762-81d2-9568ab501fac.jpg?1775938570" alt="Silverquill Charm"></span></a> | - | MC | U | 2 | Counters | • put two +1/+1 counters on target creature. |

---
## 6. Set Mechanics

| Mechanic | Card Count | Examples |
|----------|------------|----------|
| Surveil | 17 | <a href="https://scryfall.com/card/sos/24/owlin-historian" class="card-link" target="_blank">Owlin Historian<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/f/5fe99be0-e1ec-485e-82f8-02eba7b82441.jpg?1775937078" alt="Owlin Historian"></span></a>, <a href="https://scryfall.com/card/sos/36/stone-docent" class="card-link" target="_blank">Stone Docent<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/2/c2abfffb-bf36-44af-9a27-6e109e4d77dd.jpg?1775937164" alt="Stone Docent"></span></a>, <a href="https://scryfall.com/card/sos/38/banishing-betrayal" class="card-link" target="_blank">Banishing Betrayal<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/a/1ae9d2f3-7a9f-433a-aa1f-14337ae6f9d4.jpg?1775937176" alt="Banishing Betrayal"></span></a> |
| Infusion | 12 | <a href="https://scryfall.com/card/sos/83/foolish-fate" class="card-link" target="_blank">Foolish Fate<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/2/d278f4c9-d20b-4a76-8c5c-4d3e985948b9.jpg?1775937489" alt="Foolish Fate"></span></a>, <a href="https://scryfall.com/card/sos/91/moseo-veins-new-dean" class="card-link" target="_blank">Moseo, Vein's New Dean<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/8/6877180c-22a1-4c4d-9178-316f4c34661b.jpg?1775937545" alt="Moseo, Vein's New Dean"></span></a>, <a href="https://scryfall.com/card/sos/92/poisoners-apprentice" class="card-link" target="_blank">Poisoner's Apprentice<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/7/3755a2e9-af55-4625-a006-2a86c7893a96.jpg?1775937552" alt="Poisoner's Apprentice"></span></a> |
| Ward | 11 | <a href="https://scryfall.com/card/sos/21/inkshape-demonstrator" class="card-link" target="_blank">Inkshape Demonstrator<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/c/bcfac992-9984-4529-b9ff-a42d58832b34.jpg?1775937053" alt="Inkshape Demonstrator"></span></a>, <a href="https://scryfall.com/card/sos/40/campus-composer-aqueous-aria" class="card-link" target="_blank">Campus Composer // Aqueous Aria<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/a/fac8ac39-ecb4-4142-bf37-131c65660a9b.jpg?1775937189" alt="Campus Composer // Aqueous Aria"></span></a>, <a href="https://scryfall.com/card/sos/45/emeritus-of-ideation-ancestral-recall" class="card-link" target="_blank">Emeritus of Ideation // Ancestral Recall<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/5/75961d36-acf6-425f-9698-0bf52af74f31.jpg?1775937223" alt="Emeritus of Ideation // Ancestral Recall"></span></a> |
| Flashback | 10 | <a href="https://scryfall.com/card/sos/7/antiquities-on-the-loose" class="card-link" target="_blank">Antiquities on the Loose<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/8/68ee92cd-51af-4de5-bcc8-34d0bb2fd398.jpg?1775936960" alt="Antiquities on the Loose"></span></a>, <a href="https://scryfall.com/card/sos/9/daydream" class="card-link" target="_blank">Daydream<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/2/e2b16cb2-b8b2-45df-9695-3c16e9d89e28.jpg?1775936973" alt="Daydream"></span></a>, <a href="https://scryfall.com/card/sos/10/dig-site-inventory" class="card-link" target="_blank">Dig Site Inventory<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/5/e52464ee-df8b-41ec-af93-4b0eb004383e.jpg?1775936980" alt="Dig Site Inventory"></span></a> |
| Converge | 9 | <a href="https://scryfall.com/card/sos/2/rancorous-archaic" class="card-link" target="_blank">Rancorous Archaic<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/5/2565e16a-ed31-4867-adb8-f1633d580397.jpg?1775936927" alt="Rancorous Archaic"></span></a>, <a href="https://scryfall.com/card/sos/3/sundering-archaic" class="card-link" target="_blank">Sundering Archaic<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/3/c35b57e4-2358-46c0-8f09-cd27c10eaf2d.jpg?1775936933" alt="Sundering Archaic"></span></a>, <a href="https://scryfall.com/card/sos/4/together-as-one" class="card-link" target="_blank">Together as One<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/c/ac2a8a66-e38c-42ab-83e1-d2d99ee48861.jpg?1775936940" alt="Together as One"></span></a> |
| Paradigm | 5 | <a href="https://scryfall.com/card/sos/30/restoration-seminar" class="card-link" target="_blank">Restoration Seminar<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/e/9ebc4ecf-2fa2-4ab8-afde-3b91cf5eadb6.jpg?1775937123" alt="Restoration Seminar"></span></a>, <a href="https://scryfall.com/card/sos/44/echocasting-symposium" class="card-link" target="_blank">Echocasting Symposium<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/d/5d7086a7-dc42-468a-a2cf-a6f89030f947.jpg?1775937216" alt="Echocasting Symposium"></span></a>, <a href="https://scryfall.com/card/sos/78/decorum-dissertation" class="card-link" target="_blank">Decorum Dissertation<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/4/f4ab2d9b-c73d-478d-aac7-4d3bb24296d2.jpg?1775937454" alt="Decorum Dissertation"></span></a> |

---
## 7. Draft Signposts (Uncommon Multicolor)

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
## 8. Notable Cards for Limited (by Rarity)

### Common Removal

| Card | P/T | Color | CMC | Categories |
|------|-----|-------|-----|------------|
| <a href="https://scryfall.com/card/sos/64/procrastinate" class="card-link" target="_blank">Procrastinate<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/e/1edb449d-620f-4e21-9d76-2c840635eb9d.jpg?1775937356" alt="Procrastinate"></span></a> | - | U | 1 | Tap/Stun |
| <a href="https://scryfall.com/card/sos/28/rapier-wit" class="card-link" target="_blank">Rapier Wit<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/7/97b50521-5a0f-4dbd-8e15-f0f0d059c258.jpg?1775937109" alt="Rapier Wit"></span></a> | - | W | 2 | Tap/Stun |
| <a href="https://scryfall.com/card/sos/38/banishing-betrayal" class="card-link" target="_blank">Banishing Betrayal<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/a/1ae9d2f3-7a9f-433a-aa1f-14337ae6f9d4.jpg?1775937176" alt="Banishing Betrayal"></span></a> | - | U | 2 | Bounce |
| <a href="https://scryfall.com/card/sos/47/essence-scatter" class="card-link" target="_blank">Essence Scatter<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/2/32840097-0531-4c43-b6a8-e76c17420b04.jpg?1775937236" alt="Essence Scatter"></span></a> | - | U | 2 | Counter |
| <a href="https://scryfall.com/card/sos/86/last-gasp" class="card-link" target="_blank">Last Gasp<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/a/da5f3729-6ec7-4482-90cb-83b973edeae4.jpg?1775937510" alt="Last Gasp"></span></a> | - | B | 2 | -X/-X |
| <a href="https://scryfall.com/card/sos/135/tome-blast" class="card-link" target="_blank">Tome Blast<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/2/72a3b17d-1e00-48e9-8402-c81bacd595a7.jpg?1775937914" alt="Tome Blast"></span></a> | - | R | 2 | Damage |
| <a href="https://scryfall.com/card/sos/141/burrog-barrage" class="card-link" target="_blank">Burrog Barrage<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/5/95d5b0a8-2b66-418e-9e5e-ecf7b304c31e.jpg?1775937957" alt="Burrog Barrage"></span></a> | - | G | 2 | Damage, Bite |
| <a href="https://scryfall.com/card/sos/150/glorious-decay" class="card-link" target="_blank">Glorious Decay<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/3/a335f396-1004-4fee-842a-a35ff6ba17f2.jpg?1775938023" alt="Glorious Decay"></span></a> | - | G | 2 | Damage |
| <a href="https://scryfall.com/card/sos/42/deluge-virtuoso" class="card-link" target="_blank">Deluge Virtuoso<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/e/2e3b16ed-8727-48fd-8b1f-c0cbd329385e.jpg?1775937202" alt="Deluge Virtuoso"></span></a> | 2/2 | U | 3 | Tap/Stun |
| <a href="https://scryfall.com/card/sos/128/rubble-rouser" class="card-link" target="_blank">Rubble Rouser<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/f/afe61957-a9bb-42b0-98e8-b5fa418cbaff.jpg?1775937860" alt="Rubble Rouser"></span></a> | 1/4 | R | 3 | Damage |
| <a href="https://scryfall.com/card/sos/136/unsubtle-mockery" class="card-link" target="_blank">Unsubtle Mockery<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/b/2b7cb1a3-761e-470e-a164-6e29dd9448cd.jpg?1775937921" alt="Unsubtle Mockery"></span></a> | - | R | 3 | Damage |
| <a href="https://scryfall.com/card/sos/66/run-behind" class="card-link" target="_blank">Run Behind<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/4/0/40ecc34b-4cd0-4998-bbf4-7faa6fd3d7e0.jpg?1775937369" alt="Run Behind"></span></a> | - | U | 4 | Bounce (Library) |
| <a href="https://scryfall.com/card/sos/104/wander-off" class="card-link" target="_blank">Wander Off<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/d/3d409512-50b9-4a38-91b0-19ba25227992.jpg?1775937643" alt="Wander Off"></span></a> | - | B | 4 | Exile |
| <a href="https://scryfall.com/card/sos/243/wilt-in-the-heat" class="card-link" target="_blank">Wilt in the Heat<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/6/f63f7209-fc0f-400c-8076-125f3131cb32.jpg?1775938697" alt="Wilt in the Heat"></span></a> | - | MC | 4 | Damage |
| <a href="https://scryfall.com/card/sos/6/ajanis-response" class="card-link" target="_blank">Ajani's Response<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/c/9cd1417a-badc-4abd-a8ca-5b31f85c1072.jpg?1776047920" alt="Ajani's Response"></span></a> | - | W | 5 | Destroy |
| <a href="https://scryfall.com/card/sos/118/heated-argument" class="card-link" target="_blank">Heated Argument<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/0/0038d212-3d95-4f98-8c2e-7b2404d0ced7.jpg?1775937767" alt="Heated Argument"></span></a> | - | R | 5 | Damage |
| <a href="https://scryfall.com/card/sos/189/fractal-mascot" class="card-link" target="_blank">Fractal Mascot<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/f/cf5b19e3-eed1-4b36-9756-660ffb3baa08.jpg?1775938311" alt="Fractal Mascot"></span></a> | 6/6 | MC | 6 | Tap/Stun |

### Common Combat Tricks

| Card | P/T | Color | CMC | Categories |
|------|-----|-------|-----|------------|
| <a href="https://scryfall.com/card/sos/22/interjection" class="card-link" target="_blank">Interjection<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/5/0534cff6-299c-4155-b318-eb7581989e8a.jpg?1775937061" alt="Interjection"></span></a> | - | W | 1 | P/T Buff, Grants First Strike |
| <a href="https://scryfall.com/card/sos/41/chase-inspiration" class="card-link" target="_blank">Chase Inspiration<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/6/06f9f257-c7ef-44b7-8b2b-f038fba900af.jpg?1775937195" alt="Chase Inspiration"></span></a> | - | U | 1 | P/T Buff, Protection, Grants Hexproof |
| <a href="https://scryfall.com/card/sos/89/masterful-flourish" class="card-link" target="_blank">Masterful Flourish<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/d/8d93d14d-7760-4af2-a237-2df326dd28d3.jpg?1775937531" alt="Masterful Flourish"></span></a> | - | B | 1 | P/T Buff, Grants Indestructible, Protection |
| <a href="https://scryfall.com/card/sos/141/burrog-barrage" class="card-link" target="_blank">Burrog Barrage<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/9/5/95d5b0a8-2b66-418e-9e5e-ecf7b304c31e.jpg?1775937957" alt="Burrog Barrage"></span></a> | - | G | 2 | P/T Buff |
| <a href="https://scryfall.com/card/sos/144/efflorescence" class="card-link" target="_blank">Efflorescence<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/7/9/79b9ace7-eceb-4f97-9ee7-d5ee3e0b3515.jpg?1775937979" alt="Efflorescence"></span></a> | - | G | 3 | Counters, Grants Trample |

### Uncommon Removal

| Card | P/T | Color | CMC | Categories |
|------|-----|-------|-----|------------|
| <a href="https://scryfall.com/card/sos/9/daydream" class="card-link" target="_blank">Daydream<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/2/e2b16cb2-b8b2-45df-9695-3c16e9d89e28.jpg?1775936973" alt="Daydream"></span></a> | - | W | 1 | Exile |
| <a href="https://scryfall.com/card/sos/79/dissection-practice" class="card-link" target="_blank">Dissection Practice<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/d/ddbf1242-6832-475e-9a77-65dd9b4bb32a.jpg?1775937462" alt="Dissection Practice"></span></a> | - | B | 1 | -X/-X |
| <a href="https://scryfall.com/card/sos/112/duel-tactics" class="card-link" target="_blank">Duel Tactics<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/f/8f3a1675-0cc7-4dfd-a12e-4740a2cf81e8.jpg?1775937718" alt="Duel Tactics"></span></a> | - | R | 1 | Damage |
| <a href="https://scryfall.com/card/sos/18/harsh-annotation" class="card-link" target="_blank">Harsh Annotation<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/e/0/e07a8fc7-c11c-4469-a31d-0abf40e57bbf.jpg?1775937033" alt="Harsh Annotation"></span></a> | - | W | 2 | Destroy |
| <a href="https://scryfall.com/card/sos/81/end-of-the-hunt" class="card-link" target="_blank">End of the Hunt<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/0/8/0809b51a-6a05-4f18-9bf4-1b8382da648f.jpg?1775937476" alt="End of the Hunt"></span></a> | - | B | 2 | Edict |
| <a href="https://scryfall.com/card/sos/134/thunderdrum-soloist" class="card-link" target="_blank">Thunderdrum Soloist<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/9/590d1d95-ed13-4121-899f-f5a2d8a6617a.jpg?1775937905" alt="Thunderdrum Soloist"></span></a> | 1/3 | R | 2 | Damage |
| <a href="https://scryfall.com/card/sos/200/lorehold-charm" class="card-link" target="_blank">Lorehold Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/5/f/5fe70295-e550-4577-a341-dab6c25aabfd.jpg?1775938389" alt="Lorehold Charm"></span></a> | - | MC | 2 | Edict |
| <a href="https://scryfall.com/card/sos/211/prismari-charm" class="card-link" target="_blank">Prismari Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/f/8f6c2a5e-fe13-407c-aadd-c9caf2884ff1.jpg?1775938465" alt="Prismari Charm"></span></a> | - | MC | 2 | Bounce |
| <a href="https://scryfall.com/card/sos/217/quandrix-charm" class="card-link" target="_blank">Quandrix Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/1/318486e0-f255-40f5-8150-dc272eec9d7d.jpg?1775938509" alt="Quandrix Charm"></span></a> | - | MC | 2 | Counter |
| <a href="https://scryfall.com/card/sos/225/silverquill-charm" class="card-link" target="_blank">Silverquill Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/3/e/3eb73579-f1c6-4762-81d2-9568ab501fac.jpg?1775938570" alt="Silverquill Charm"></span></a> | - | MC | 2 | Exile |
| <a href="https://scryfall.com/card/sos/240/vibrant-outburst" class="card-link" target="_blank">Vibrant Outburst<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/f/9/f9ba68ef-6efc-4249-8b74-e33f47173902.jpg?1775938674" alt="Vibrant Outburst"></span></a> | - | MC | 2 | Damage |
| <a href="https://scryfall.com/card/sos/244/witherbloom-charm" class="card-link" target="_blank">Witherbloom Charm<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/2/5/254437f7-7a8a-4b11-9cea-e8e7ea23c59e.jpg?1775938703" alt="Witherbloom Charm"></span></a> | - | MC | 2 | Conditional Destroy |
| <a href="https://scryfall.com/card/sos/34/stand-up-for-yourself" class="card-link" target="_blank">Stand Up for Yourself<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/7/b756ca13-b904-4510-9bbb-5bc2864abfbd.jpg?1775937151" alt="Stand Up for Yourself"></span></a> | - | W | 3 | Conditional Destroy |
| <a href="https://scryfall.com/card/sos/83/foolish-fate" class="card-link" target="_blank">Foolish Fate<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/d/2/d278f4c9-d20b-4a76-8c5c-4d3e985948b9.jpg?1775937489" alt="Foolish Fate"></span></a> | - | B | 3 | Destroy |
| <a href="https://scryfall.com/card/sos/142/chelonian-tackle" class="card-link" target="_blank">Chelonian Tackle<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/a/8/a82a4d8c-4105-4923-85a2-ef58241f725c.jpg?1775937964" alt="Chelonian Tackle"></span></a> | - | G | 3 | Damage, Fight |
| <a href="https://scryfall.com/card/sos/39/brush-off" class="card-link" target="_blank">Brush Off<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/1/5/151eab82-d20f-433b-b3bb-1d44e2871d5c.jpg?1775937183" alt="Brush Off"></span></a> | - | U | 4 | Counter |
| <a href="https://scryfall.com/card/sos/107/archaics-agony" class="card-link" target="_blank">Archaic's Agony<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/8/d/8d99f8b2-5c1c-4059-bf68-c6b2e9e5b275.jpg?1775937675" alt="Archaic's Agony"></span></a> | - | R | 5 | Damage |
| <a href="https://scryfall.com/card/sos/108/artistic-process" class="card-link" target="_blank">Artistic Process<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/c/bce9d933-be58-4301-beb4-07b04d0b69f0.jpg?1775937683" alt="Artistic Process"></span></a> | - | R | 5 | Damage |
| <a href="https://scryfall.com/card/sos/3/sundering-archaic" class="card-link" target="_blank">Sundering Archaic<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/c/3/c35b57e4-2358-46c0-8f09-cd27c10eaf2d.jpg?1775936933" alt="Sundering Archaic"></span></a> | 3/3 | NC | 6 | Exile |
| <a href="https://scryfall.com/card/sos/53/homesickness" class="card-link" target="_blank">Homesickness<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/6/e/6e4a1f82-b0b1-4608-91f8-130bee731435.jpg?1775937280" alt="Homesickness"></span></a> | - | U | 6 | Tap/Stun |
| <a href="https://scryfall.com/card/sos/181/colossus-of-the-blood-age" class="card-link" target="_blank">Colossus of the Blood Age<span class="card-preview"><img src="https://cards.scryfall.io/normal/front/b/f/bfa7f0a4-6b65-4e53-ba00-848df260d8e3.jpg?1775938248" alt="Colossus of the Blood Age"></span></a> | 6/6 | MC | 6 | Damage |

