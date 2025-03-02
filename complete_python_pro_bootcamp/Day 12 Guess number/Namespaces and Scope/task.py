enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside 📲 function: {enemies}")


increase_enemies()
print(f"enemies outside 📤 function: {enemies}")

# Local Scope
def drink_potion():
    potion_strength = 2
    print(f"💪 potion strength: {potion_strength}")

# drink_potion()
# print(potion_strength)

# Global Scope
player_health = 10

def drink_potion_2():
    print(f"🤾‍♀️ potion strength: {player_health}")