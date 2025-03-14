# Modifying Global Scope

enemies = 1


def increase_enemies(enemy_in):
    # global enemies # Bad usage
    print(f"enemies inside function: {enemies}")
    return enemy_in + 1


enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")


