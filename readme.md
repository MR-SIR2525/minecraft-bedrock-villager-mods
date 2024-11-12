
## Helpful Villagers addon

- Renaming with nametags enabled
- Inventory size increased to 10
- Using a chest, click on a villager to enable/disable inventory access.
- Make a villager follow you while holding a hale bale. Toggle on/off by clicking villager with hay bale.
- Reduced likelihood of pathfinding issues related to dirt path blocks.

### Farmer
- Delay between consecutive harvests/replants reduced from vanilla 1 second to 0.5 seconds.
- Farmer will now fertilize crops without fail if the farmer has bonemeal.
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


## Known Issues
- Enabling inventory access with the chest causes the villager to forget their trade table, but not experience. Removing inventory access restores a new, random trade table at their same level.

## Dev notes
- the error "molang error found multiple operations without a combining operation between them: ? )" means one of the operations is failing.

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
