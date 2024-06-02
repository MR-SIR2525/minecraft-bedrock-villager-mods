# MR SIR's Villager Mods

## Lumberjack Villager
  - New lumberjack villager trade, complete with workstation and trade table.
  - in progress
## Villager Intelligence Update (Helpful Villagers)
- Renaming with nametags enabled
- Inventory size increased to 10
- Reduced likelihood of pathfinding issues related to grass path blocks.


### Farmer
- Make a farmer follow you while holding a chest. Toggle on/off by clicking farmer with chest.
- Farmer can drop crops to hopper:
  1. During work time, farmer has the chance to look for a "farmer guide stone"...
  2. If a Guide Stone is found, farmer will go to it then share to a nearby "hopper marker" entity that should be placed on top of a hopper and within sight of the Farmer Guide Stone.
  3. Farmer will share **excess crops** from his inventory to it and go back to normal activities.
   
#### Hopper Marker
- Hopper Marker crafting recipe:
   - i&nbsp;i&nbsp;i
   - i&nbsp;&nbsp;&nbsp;i
   - i&nbsp;i&nbsp;i
      - where "i" is an iron nugget

#### Farmer Guide Stone
- Farmer Guide Stone crafting recipe:
   - &nbsp;&nbsp;i&nbsp;&nbsp;
   - i&nbsp;S&nbsp;i
   - &nbsp;&nbsp;i&nbsp;&nbsp;
      - where "S" is stone
      - where "i" is an iron nugget

(no longer used for farmer)
- Lodestone crafting recipe (normal except use diamond instead of netherite):
   - S&nbsp;S&nbsp;S
  - S&nbsp;D&nbsp;S
  - S&nbsp;S&nbsp;S
      - where S = chiseled stonebrick and D = diamond

**Created by MRxSIR**


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