# To be used by farmer villager to save coordinates of hopper to scoreboard
function save_hopper_to_scoreboard
    # execute as self a test for hopper, then save coordinates to scoreboard
    execute as self run scoreboard players set @s hopperX {x}
    execute as self run scoreboard players set @s hopperY {y}
    execute as self run scoreboard players set @s hopperZ {z}
end