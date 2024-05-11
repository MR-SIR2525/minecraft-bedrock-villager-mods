import {
    world,
    system,
    EntityInventoryComponent,
    ItemStack
  } from "@minecraft/server";
  
  // Function to drop all items from an entity
  function dropCrops(villager) {
    const inventory = villager.getComponent("minecraft:inventory");
    const inventoryContainer = inventory.container;

    let items_to_drop = [
      "minecraft:wheat",
      "minecraft:carrot",
      "minecraft:potato",
      "minecraft:beetroot",
    ];
  
    for (let i = 0; i < inventoryContainer.size; i++) {
      const itemStack = inventoryContainer.getItem(i);
  
      if (itemStack && items_to_drop.includes(itemStack.type)) {
        // Create a copy of the ItemStack to drop
        const dropStack = new ItemStack(itemStack.type, itemStack.amount);
  
        // Spawn the item stack in front of the villager
        const position = villager.location;
        const dropPosition = {
          x: position.x + villager.getViewDirection().x,
          y: position.y + 1, // Drop the item at the head level
          z: position.z + villager.getViewDirection().z
        };
  
        world.getDimension("overworld").spawnItem(dropStack, dropPosition);
  
        // Clear the item from the inventory slot
        inventoryContainer.setItem(i, undefined);
      }
    }
  }
  

  // Subscribe to events to listen for the villager reaching the hopper
  world.events.scriptEventReceive.subscribe((event) => {
    const entity = event.sourceEntity;
    const eventName = event.id;
  
    if (entity && eventName === "minecraft:drop_crops_event") {
      dropCrops(entity);
    }
  });
  