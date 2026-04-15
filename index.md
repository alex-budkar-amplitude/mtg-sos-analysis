# Secrets of Strixhaven (SOS) -- Set Analysis

**Total unique cards:** 271
**Release date:** April 24, 2026
**Source:** Scryfall API (`e:sos`)

---
## 1. Set Overview

### Card Count by Color

| Color | Total | Creatures | Instants | Sorceries | Enchantments | Artifacts | Planeswalkers | Lands |
|-------|-------|-----------|----------|-----------|--------------|-----------|---------------|-------|
| White | 33 | 18 | 7 | 11 | 2 | 0 | 0 | 1 |
| Blue | 35 | 17 | 16 | 9 | 0 | 0 | 0 | 1 |
| Black | 35 | 19 | 6 | 15 | 0 | 0 | 1 | 1 |
| Red | 33 | 17 | 6 | 13 | 1 | 1 | 0 | 1 |
| Green | 33 | 18 | 5 | 11 | 2 | 0 | 0 | 1 |
| Multicolor | 87 | 42 | 13 | 23 | 0 | 4 | 1 | 10 |
| Colorless | 15 | 7 | 0 | 1 | 0 | 6 | 0 | 4 |

### Card Count by Rarity

| Rarity | Total | Creatures | Instants | Sorceries | Enchantments | Artifacts |
|--------|-------|-----------|----------|-----------|--------------|-----------|
| Common | 91 | 45 | 19 | 24 | 0 | 4 |
| Uncommon | 100 | 53 | 21 | 32 | 4 | 4 |
| Rare | 60 | 29 | 10 | 18 | 1 | 3 |
| Mythic | 20 | 11 | 3 | 9 | 0 | 0 |

### Color x Rarity Matrix

| Color | Common | Uncommon | Rare | Mythic | Total |
|-------|------|------|------|------|-------|
| White | 13 | 12 | 6 | 2 | 33 |
| Blue | 13 | 12 | 7 | 3 | 35 |
| Black | 13 | 12 | 6 | 4 | 35 |
| Red | 13 | 12 | 6 | 2 | 33 |
| Green | 13 | 12 | 6 | 2 | 33 |
| Multicolor | 20 | 35 | 26 | 6 | 87 |
| Colorless | 6 | 5 | 3 | 1 | 15 |

---
## 2. Mana Curve by Color

| Color | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8+ | Avg CMC |
|-------|---|---|---|---|---|---|---|---|---|---------|
| White | 0 | 6 | 9 | 9 | 4 | 3 | 0 | 1 | 0 | 2.78 |
| Blue | 0 | 7 | 8 | 9 | 4 | 3 | 2 | 1 | 0 | 2.94 |
| Black | 0 | 4 | 8 | 11 | 5 | 5 | 1 | 0 | 0 | 3.06 |
| Red | 0 | 4 | 8 | 9 | 3 | 5 | 2 | 1 | 0 | 3.22 |
| Green | 0 | 5 | 9 | 8 | 6 | 3 | 1 | 0 | 0 | 2.88 |
| Multicolor | 0 | 0 | 24 | 18 | 19 | 7 | 4 | 4 | 1 | 3.55 |
| Colorless | 0 | 0 | 3 | 2 | 1 | 1 | 2 | 1 | 1 | 4.55 |

### Mana Curve by Rarity

| Rarity | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8+ | Avg CMC |
|-------|---|---|---|---|---|---|---|---|---|---------|
| Common | 0 | 11 | 25 | 20 | 12 | 9 | 2 | 1 | 0 | 2.91 |
| Uncommon | 0 | 9 | 30 | 24 | 17 | 12 | 6 | 1 | 0 | 3.15 |
| Rare | 0 | 6 | 12 | 18 | 10 | 2 | 2 | 3 | 0 | 3.15 |
| Mythic | 0 | 0 | 2 | 4 | 3 | 4 | 2 | 3 | 2 | 4.95 |

---
## 3. Creature Analysis

### Creature Stats by Color

| Color | Count | Avg P | Avg T | Avg CMC | With Keywords |
|-------|-------|-------|-------|---------|---------------|
| White | 18 | 2.4 | 2.6 | 2.9 | 16 |
| Blue | 17 | 1.7 | 2.5 | 2.9 | 14 |
| Black | 19 | 2.9 | 2.7 | 3.2 | 17 |
| Red | 17 | 2.7 | 3.0 | 3.5 | 15 |
| Green | 18 | 2.6 | 2.9 | 2.8 | 14 |
| Multicolor | 42 | 2.9 | 3.4 | 3.6 | 30 |
| Colorless | 7 | 3.3 | 3.6 | 5.1 | 6 |

### Creature Stats by Rarity

| Rarity | Count | Avg P | Avg T | Avg CMC |
|--------|-------|-------|-------|---------|
| Common | 45 | 2.4 | 2.6 | 3.1 |
| Uncommon | 53 | 2.6 | 3.0 | 3.4 |
| Rare | 29 | 2.3 | 2.8 | 2.8 |
| Mythic | 11 | 4.7 | 4.7 | 5.2 |

### Keyword Frequency (Creatures)

| Keyword | Total | W | U | B | R | G | Multi | C'less |
|---------|-------|---|---|---|---|---|-------|--------|
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

| Color | Total | -X/-X | Bite | Board Wipe | Bounce | Bounce (Library) | Conditional Destroy | Counter | Damage | Destroy | Edict | Exile | Fight | Tap/Stun |
|-------|-------|---|---|---|---|---|---|---|---|---|---|---|---|---|
| White | 7 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 2 | 0 | 1 |
| Blue | 8 | 0 | 0 | 0 | 1 | 1 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 3 |
| Black | 6 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Red | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 |
| Green | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 1 | 0 |
| Multicolor | 15 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 6 | 2 | 1 | 2 | 0 | 1 |
| Colorless | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |

### Removal Count by Rarity

| Rarity | Total | -X/-X | Bite | Board Wipe | Bounce | Bounce (Library) | Conditional Destroy | Counter | Damage | Destroy | Edict | Exile | Fight | Tap/Stun |
|--------|-------|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Common | 17 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 7 | 1 | 0 | 1 | 0 | 4 |
| Uncommon | 21 | 1 | 0 | 0 | 1 | 0 | 2 | 2 | 7 | 2 | 2 | 3 | 1 | 1 |
| Rare | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 5 | 2 | 0 | 1 | 0 | 0 |
| Mythic | 4 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 |

### Full Removal List by Color

#### White

| Card | Rarity | CMC | Type | Categories |
|------|--------|-----|------|------------|
| Daydream | U | 1 | Sorc | Exile |
| Erode | R | 1 | Inst | Destroy |
| Harsh Annotation | U | 2 | Inst | Destroy |
| Rapier Wit | C | 2 | Inst | Tap/Stun |
| Emeritus of Truce // Swords to Plowshares | M | 3 | Inst/Crea | Exile |
| Stand Up for Yourself | U | 3 | Inst | Conditional Destroy |
| Ajani's Response | C | 5 | Inst | Destroy |

#### Blue

| Card | Rarity | CMC | Type | Categories |
|------|--------|-----|------|------------|
| Procrastinate | C | 1 | Sorc | Tap/Stun |
| Banishing Betrayal | C | 2 | Inst | Bounce |
| Essence Scatter | C | 2 | Inst | Counter |
| Deluge Virtuoso | C | 3 | Crea | Tap/Stun |
| Mana Sculpt | R | 3 | Inst | Counter |
| Brush Off | U | 4 | Inst | Counter |
| Run Behind | C | 4 | Inst | Bounce (Library) |
| Homesickness | U | 6 | Inst | Tap/Stun |

#### Black

| Card | Rarity | CMC | Type | Categories |
|------|--------|-----|------|------------|
| Dissection Practice | U | 1 | Inst | -X/-X |
| End of the Hunt | U | 2 | Sorc | Edict |
| Last Gasp | C | 2 | Inst | -X/-X |
| Foolish Fate | U | 3 | Inst | Destroy |
| Withering Curse | M | 3 | Sorc | Board Wipe |
| Wander Off | C | 4 | Inst | Exile |

#### Red

| Card | Rarity | CMC | Type | Categories |
|------|--------|-----|------|------------|
| Duel Tactics | U | 1 | Sorc | Damage |
| Emeritus of Conflict // Lightning Bolt | M | 2 | Inst/Crea | Damage |
| Thunderdrum Soloist | U | 2 | Crea | Damage |
| Tome Blast | C | 2 | Sorc | Damage |
| Rubble Rouser | C | 3 | Crea | Damage |
| Steal the Show | R | 3 | Sorc | Damage |
| Unsubtle Mockery | C | 3 | Inst | Damage |
| Archaic's Agony | U | 5 | Sorc | Damage |
| Artistic Process | U | 5 | Sorc | Damage |
| Heated Argument | C | 5 | Inst | Damage |

#### Green

| Card | Rarity | CMC | Type | Categories |
|------|--------|-----|------|------------|
| Burrog Barrage | C | 2 | Inst | Bite, Damage |
| Glorious Decay | C | 2 | Inst | Damage |
| Chelonian Tackle | U | 3 | Sorc | Fight, Damage |

#### Multicolor

| Card | Rarity | CMC | Type | Categories |
|------|--------|-----|------|------------|
| Lorehold Charm | U | 2 | Inst | Edict |
| Prismari Charm | U | 2 | Inst | Bounce |
| Quandrix Charm | U | 2 | Inst | Counter |
| Silverquill Charm | U | 2 | Inst | Exile |
| Traumatic Critique | R | 2 | Inst | Damage |
| Vibrant Outburst | U | 2 | Inst | Damage |
| Witherbloom Charm | U | 2 | Inst | Conditional Destroy |
| Suspend Aggression | R | 3 | Inst | Exile |
| Ark of Hunger | R | 4 | Arti | Damage |
| Professor Dellian Fel | M | 4 | Plan | Destroy |
| Wilt in the Heat | C | 4 | Inst | Damage |
| Splatter Technique | R | 5 | Sorc | Damage |
| Colossus of the Blood Age | U | 6 | Crea/Arti | Damage |
| Fractal Mascot | C | 6 | Crea | Tap/Stun |
| Moment of Reckoning | R | 7 | Sorc | Destroy |

#### Colorless

| Card | Rarity | CMC | Type | Categories |
|------|--------|-----|------|------------|
| Sundering Archaic | U | 6 | Crea | Exile |
| Together as One | R | 6 | Sorc | Damage |

---
## 5. Combat Tricks

### Combat Trick Count by Color

| Color | Total | Counters | Falter | Grants First Strike | Grants Flying | Grants Hexproof | Grants Indestructible | Grants Trample | P/T Buff | P/T Buff (Team) | Protection |
|-------|-------|---|---|---|---|---|---|---|---|---|---|
| White | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Blue | 3 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 1 |
| Black | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 3 | 0 | 1 |
| Red | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Green | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 0 |
| Multicolor | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |

### Combat Trick Count by Rarity

| Rarity | Total | Counters | Falter | Grants First Strike | Grants Flying | Grants Hexproof | Grants Indestructible | Grants Trample | P/T Buff | P/T Buff (Team) | Protection |
|--------|-------|---|---|---|---|---|---|---|---|---|---|
| Common | 5 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 4 | 0 | 2 |
| Uncommon | 8 | 2 | 1 | 0 | 1 | 0 | 0 | 1 | 3 | 1 | 0 |

### Full Combat Tricks List

| Card | Color | Rarity | CMC | Categories | Effect Summary |
|------|-------|--------|-----|------------|----------------|
| Interjection | White | C | 1 | P/T Buff, Grants First Strike | target creature gets +2/+2 and gains first strike until end of turn. |
| Chase Inspiration | Blue | C | 1 | Protection, P/T Buff, Grants Hexproof | target creature you control gets +0/+3 and gains hexproof until end of turn. (it |
| Fractal Anomaly | Blue | U | 1 | Counters | create a 0/0 green and blue fractal creature token and put x +1/+1 counters on i |
| Encouraging Aviator // Jump | Blue | U | 3 | Grants Flying | target creature gains flying until end of turn. |
| Dissection Practice | Black | U | 1 | P/T Buff | up to one target creature gets +1/+1 until end of turn. |
| Masterful Flourish | Black | C | 1 | Protection, P/T Buff, Grants Indestructible | target creature you control gets +1/+0 and gains indestructible until end of tur |
| Rabid Attack | Black | U | 2 | P/T Buff | until end of turn, any number of target creatures you control each get +1/+0 and |
| Duel Tactics | Red | U | 1 | Falter | duel tactics deals 1 damage to target creature. it can't block this turn. |
| Burrog Barrage | Green | C | 2 | P/T Buff | target creature you control gets +1/+0 until end of turn if you've cast another  |
| Lumaret's Favor | Green | U | 2 | P/T Buff | target creature gets +2/+4 until end of turn. |
| Efflorescence | Green | C | 3 | Counters, Grants Trample | put two +1/+1 counters on target creature. |
| Lorehold Charm | Multicolor | U | 2 | P/T Buff (Team), Grants Trample | choose one —
• each opponent sacrifices a nontoken artifact of their choice.
• r |
| Silverquill Charm | Multicolor | U | 2 | Counters | • put two +1/+1 counters on target creature. |

---
## 6. Set Mechanics

| Mechanic | Card Count | Examples |
|----------|------------|----------|
| Surveil | 17 | Owlin Historian, Stone Docent, Banishing Betrayal |
| Infusion | 12 | Foolish Fate, Moseo, Vein's New Dean, Poisoner's Apprentice |
| Ward | 11 | Inkshape Demonstrator, Campus Composer // Aqueous Aria, Emeritus of Ideation // Ancestral Recall |
| Flashback | 10 | Antiquities on the Loose, Daydream, Dig Site Inventory |
| Converge | 9 | Rancorous Archaic, Sundering Archaic, Together as One |
| Paradigm | 5 | Restoration Seminar, Echocasting Symposium, Decorum Dissertation |

---
## 7. Draft Signposts (Uncommon Multicolor)

These uncommon gold cards hint at supported archetypes.

| Card | Colors | Type | CMC | Effect |
|------|--------|------|-----|--------|
| Abigale, Poet Laureate // Heroic Stanza | B,W | Legendary Creature — Bird Bard | 3 | flying whenever you cast a creature spell, abigale becomes prepared. (while it's prepared, you may c |
| Abstract Paintmage | R,U | Creature — Djinn Sorcerer | 3 | at the beginning of your first main phase, add {u}{r}. spend this mana only to cast instant and sorc |
| Borrowed Knowledge | R,W | Sorcery | 4 | choose one — • discard your hand, then draw cards equal to the number of cards in target opponent's  |
| Colossus of the Blood Age | R,W | Artifact Creature — Construct | 6 | when this creature enters, it deals 3 damage to each opponent and you gain 3 life. when this creatur |
| Cuboid Colony | G,U | Creature — Insect | 2 | flash flying, trample increment (whenever you cast a spell, if the amount of mana you spent is great |
| Essenceknit Scholar | B,G | Creature — Dryad Warlock | 3 | when this creature enters, create a 1/1 black and green pest creature token with "whenever this toke |
| Fractal Tender | G,U | Creature — Elf Wizard | 5 | ward {2} increment (whenever you cast a spell, if the amount of mana you spent is greater than this  |
| Growth Curve | G,U | Sorcery | 2 | put a +1/+1 counter on target creature you control, then double the number of +1/+1 counters on that |
| Killian's Confidence | B,W | Sorcery | 2 | target creature gets +1/+1 until end of turn. draw a card. whenever one or more creatures you contro |
| Kirol, History Buff // Pack a Punch | R,W | Legendary Creature — Vampire Cleric | 2 | whenever one or more cards leave your graveyard, kirol becomes prepared. (while it's prepared, you m |
| Lluwen, Exchange Student // Pest Friend | B,G | Legendary Creature — Elf Druid | 4 | lluwen enters prepared. (while it's prepared, you may cast a copy of its spell. doing so unprepares  |
| Lorehold Charm | R,W | Instant | 2 | choose one — • each opponent sacrifices a nontoken artifact of their choice. • return target artifac |
| Mind Roots | B,G | Sorcery | 3 | target player discards two cards. put up to one land card discarded this way onto the battlefield ta |
| Molten Note | R,W | Sorcery | 2 | molten note deals damage to target creature equal to the amount of mana spent to cast this spell. un |
| Old-Growth Educator | B,G | Creature — Treefolk Druid | 4 | vigilance, reach infusion — when this creature enters, put two +1/+1 counters on it if you gained li |
| Paradox Surveyor | G,U | Creature — Elf Druid | 3 | reach when this creature enters, look at the top five cards of your library. you may reveal a land c |
| Practiced Scrollsmith | R,W | Creature — Dwarf Cleric | 3 | first strike when this creature enters, exile target noncreature, nonland card from your graveyard.  |
| Prismari Charm | R,U | Instant | 2 | choose one — • surveil 2, then draw a card. • prismari charm deals 1 damage to each of one or two ta |
| Proctor's Gaze | G,U | Instant | 4 | return up to one target nonland permanent to its owner's hand. search your library for a basic land  |
| Quandrix Charm | G,U | Instant | 2 | choose one — • counter target spell unless its controller pays {2}. • destroy target enchantment. •  |
| Rapturous Moment | R,U | Sorcery | 6 | draw three cards, then discard two cards. add {u}{u}{r}{r}{r}. |
| Root Manipulation | B,G | Sorcery | 5 | until end of turn, creatures you control get +2/+2 and gain menace and "whenever this creature attac |
| Sanar, Unfinished Genius // Wild Idea | R,U | Legendary Creature — Goblin Sorcerer | 2 | sanar enters prepared. (while it's prepared, you may cast a copy of its spell. doing so unprepares i |
| Scolding Administrator | B,W | Creature — Dwarf Cleric | 2 | menace (this creature can't be blocked except by two or more creatures.) repartee — whenever you cas |
| Silverquill Charm | B,W | Instant | 2 | choose one — • put two +1/+1 counters on target creature. • exile target creature with power 2 or le |
| Snooping Page | B,W | Creature — Human Cleric | 3 | repartee — whenever you cast an instant or sorcery spell that targets a creature, this creature can' |
| Social Snub | B,W | Sorcery | 3 | when you cast this spell while you control a creature, you may copy this spell. each player sacrific |
| Spectacular Skywhale | R,U | Creature — Elemental Whale | 4 | flying opus — whenever you cast an instant or sorcery spell, this creature gets +3/+0 until end of t |
| Startled Relic Sloth | R,W | Creature — Sloth Beast | 4 | trample, lifelink at the beginning of combat on your turn, exile up to one target card from a gravey |
| Stirring Honormancer | B,W | Creature — Rhino Bard | 5 | when this creature enters, look at the top x cards of your library, where x is the number of creatur |
| Stress Dream | R,U | Instant | 5 | stress dream deals 5 damage to up to one target creature. look at the top two cards of your library. |
| Tam, Observant Sequencer // Deep Sight | G,U | Legendary Creature — Gorgon Wizard | 4 | landfall — whenever a land you control enters, tam becomes prepared. (while it's prepared, you may c |
| Teacher's Pest | B,G | Creature — Skeleton Pest | 2 | menace (this creature can't be blocked except by two or more creatures.) whenever this creature atta |
| Vibrant Outburst | R,U | Instant | 2 | vibrant outburst deals 3 damage to any target. tap up to one target creature. |
| Witherbloom Charm | B,G | Instant | 2 | choose one — • you may sacrifice a permanent. if you do, draw two cards. • you gain 5 life. • destro |

---
## 8. Notable Cards for Limited (by Rarity)

### Common Removal

| Card | Color | CMC | Categories |
|------|-------|-----|------------|
| Procrastinate | Blue | 1 | Tap/Stun |
| Rapier Wit | White | 2 | Tap/Stun |
| Banishing Betrayal | Blue | 2 | Bounce |
| Essence Scatter | Blue | 2 | Counter |
| Last Gasp | Black | 2 | -X/-X |
| Tome Blast | Red | 2 | Damage |
| Burrog Barrage | Green | 2 | Bite, Damage |
| Glorious Decay | Green | 2 | Damage |
| Deluge Virtuoso | Blue | 3 | Tap/Stun |
| Rubble Rouser | Red | 3 | Damage |
| Unsubtle Mockery | Red | 3 | Damage |
| Run Behind | Blue | 4 | Bounce (Library) |
| Wander Off | Black | 4 | Exile |
| Wilt in the Heat | Multicolor | 4 | Damage |
| Ajani's Response | White | 5 | Destroy |
| Heated Argument | Red | 5 | Damage |
| Fractal Mascot | Multicolor | 6 | Tap/Stun |

### Common Combat Tricks

| Card | Color | CMC | Categories |
|------|-------|-----|------------|
| Interjection | White | 1 | P/T Buff, Grants First Strike |
| Chase Inspiration | Blue | 1 | Protection, P/T Buff, Grants Hexproof |
| Masterful Flourish | Black | 1 | Protection, P/T Buff, Grants Indestructible |
| Burrog Barrage | Green | 2 | P/T Buff |
| Efflorescence | Green | 3 | Counters, Grants Trample |

### Uncommon Removal

| Card | Color | CMC | Categories |
|------|-------|-----|------------|
| Daydream | White | 1 | Exile |
| Dissection Practice | Black | 1 | -X/-X |
| Duel Tactics | Red | 1 | Damage |
| Harsh Annotation | White | 2 | Destroy |
| End of the Hunt | Black | 2 | Edict |
| Thunderdrum Soloist | Red | 2 | Damage |
| Lorehold Charm | Multicolor | 2 | Edict |
| Prismari Charm | Multicolor | 2 | Bounce |
| Quandrix Charm | Multicolor | 2 | Counter |
| Silverquill Charm | Multicolor | 2 | Exile |
| Vibrant Outburst | Multicolor | 2 | Damage |
| Witherbloom Charm | Multicolor | 2 | Conditional Destroy |
| Stand Up for Yourself | White | 3 | Conditional Destroy |
| Foolish Fate | Black | 3 | Destroy |
| Chelonian Tackle | Green | 3 | Fight, Damage |
| Brush Off | Blue | 4 | Counter |
| Archaic's Agony | Red | 5 | Damage |
| Artistic Process | Red | 5 | Damage |
| Sundering Archaic | Colorless | 6 | Exile |
| Homesickness | Blue | 6 | Tap/Stun |
| Colossus of the Blood Age | Multicolor | 6 | Damage |

