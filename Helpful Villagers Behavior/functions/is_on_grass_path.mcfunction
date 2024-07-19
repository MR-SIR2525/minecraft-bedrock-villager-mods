## Returns 'is_on_grass_path' if the entity is standing on a grass_path block
execute as @s at @s if block ~ ~-0.50 ~ grass_path run tag @s add is_on_grass_path