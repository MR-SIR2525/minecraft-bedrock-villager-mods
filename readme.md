# Helpful Villagers Addon

**Vanilla-friendly enhancements for villagers - smarter behaviors and new functionalities!**  

Farmers now reliably fertilize and harvest crops, store excess crops in hoppers, and get stuck less often. Villager pathfinding on dirt paths is improved, inventories are expanded to 10 slots, and they run slightly faster to escape monsters.

**Craft new items to unlock features:**  
- **Hopper Marker**: Helps farmers drop excess crops into hoppers.  
- **Farmer Guide Stone**: Guides farmers to share crops near hoppers.  

**How to use the new farmer features:**  
1. Place a Farmer Guide Stone near a hopper.  
2. Place a Hopper Marker on top of the hopper.  
3. During work time, farmers will locate the Guide Stone and drop their excess crops into the Hopper Marker before resuming normal activities.  


## Key Features

- **Renaming with Nametags**: Easily rename villagers using nametags.  
- **Expanded Inventories**: Villagers now have 10 inventory slots for more storage.  
- **Inventory Access**: Use a chest on a villager to enable or disable access to their inventory.  
- **Follow Mode**: Make villagers follow you by holding a hay bale. Toggle this feature on or off by clicking the villager with the hay bale.  
- **Improved Pathfinding**: Reduced likelihood of pathfinding issues when navigating grass path blocks.  
- **Pre-nerf Discounts**: Villagers still use the old op discounts after being healed.

---

## Farmer Improvements

- **Faster Harvesting**: The delay between consecutive harvests/replants is reduced from 1 second to 0.5 seconds.  
- **Reliable Fertilizing**: Farmers now fertilize crops consistently if bonemeal is available.  
- **Crop Sharing to Hoppers**:  
  - During work time, farmers check for nearby Farmer Guide Stones.  
  - If a Guide Stone is present, they share excess crops with a "Hopper Marker" placed on top of a hopper and within sight of the Guide Stone.  
  - After sharing, farmers resume their regular activities.  

---

## Crafting Recipes

### Hopper Marker  
Helps farmers drop crops into hoppers.  

```
i   i   i
i       i
i   i   i
```
- **"i"** = Iron Nugget  

---

### Farmer Guide Stone  
Guides farmers to hoppers for crop sharing.  

```
    i
i   S   i
    i
```
- **"S"** = Stone  
- **"i"** = Iron Nugget  


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



[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/donate?hosted_button_id=XGM24VCE7A5LY)