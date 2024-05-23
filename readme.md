# MR SIR's Villager Mods

## Lumberjack Villager
  - New lumberjack villager trade, complete with workstation and trade table.
  - in progress
## Villager Intelligence Update (Helpful Villagers) 
- Renaming with nametags enabled
- Inventory size increased to 10

### Farmer
- Make a farmer follow you while holding a chest. Toggle on/off by clicking farmer with chest.
- Farmer can drop crops to hopper:
  1. During work time, farmer has the chance to look for a lodestone...
  2. If a lodestone is found, farmer will go to it then share to a nearby "hopper marker" entity that should be places on top of a hopper and within sight of the lodestone.
  3. Farmer will share **excess crops** from his inventory to it and go back to normal activities.




# Notes for development
### 1. Namespace
- Use `mrsir` namespace
  - e.g. `mrsir:lumberjack` or `mrsir:thing`

### 2. Naming Conventions
- lowercase and underscores
  - e.g. `lumberjack` or `do_the_thing`

### 3. Methodology for alterations
- use custom files where possible and override some things, such as `villager_v2.behavior.json`, with as few alterations as possible to maintain compatibility and stability. 
- keep it kosher/vanilla for the most part.

### 4. Version History
- Notable versions/changes will have an accompanying version in the "Releases" section.