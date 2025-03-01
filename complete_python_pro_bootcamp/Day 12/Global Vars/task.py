# Modifying Global Scope

# enemies = 1
enemies = "Skeleton"


def increase_enemies():
    # global enemies
    # enemies += 1
    enemies = "Zombie"
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


