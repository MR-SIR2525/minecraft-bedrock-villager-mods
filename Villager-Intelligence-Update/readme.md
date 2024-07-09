## Villager Intelligence Update (Helpful Villagers)
- Renaming with nametags enabled
- Inventory size increased to 10
- Using a chest, click on a villager to enable/disable inventory access.
- Make a villager follow you while holding a hale bale. Toggle on/off by clicking villager with hay bale.
- Reduced likelihood of pathfinding issues related to grass path blocks.


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

(no longer used for farmer)
- Lodestone crafting recipe (normal except use diamond instead of netherite):
   - S&nbsp;S&nbsp;S
  - S&nbsp;D&nbsp;S
  - S&nbsp;S&nbsp;S
      - where S = chiseled stonebrick and D = diamond


## Known Issues
- Enabling inventory access with the chest causes the villager to forget their trade table, but not experience. Removing inventory access restores a new, random trade table at their same level.

**Created by MRxSIR**