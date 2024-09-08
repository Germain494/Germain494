```python
def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark room. There are two doors: one on your left and one on your right.")
    choice = input("Do you want to go left or right? (left/right): ").strip().lower()

    if choice == "left":
        left_room()
    elif choice == "right":
        right_room()
    else:
        print("Invalid choice. Please choose left or right.")
        start_game()

def left_room():
    print("You enter a room filled with treasure! But there is a dragon guarding it.")
    choice = input("Do you want to fight the dragon or sneak past it? (fight/sneak): ").strip().lower()

    if choice == "fight":
        print("You bravely fight the dragon and win! You take the treasure and escape.")
    elif choice == "sneak":
        print("You successfully sneak past the dragon and collect some treasure. You escape safely.")
    else:
        print("Invalid choice. Please choose fight or sneak.")
        left_room()

def right_room():
    print("You enter a room filled with strange potions.")
    choice = input("Do you want to drink a potion or leave the room? (drink/leave): ").strip().lower()

    if choice == "drink":
        print("You drink a potion and transform into a powerful wizard! You can now defeat any foe.")
    elif choice == "leave":
        print("You leave the room safely. Sometimes it's better to play it safe.")
    else:
        print("Invalid choice. Please choose drink or leave.")
        right_room()

# Start the game
start_game()```