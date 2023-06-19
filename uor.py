import time

def introduction():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself in a dense forest, surrounded by tall trees.")
    time.sleep(1)
    print("Your goal is to find the legendary treasure hidden deep within these woods.")
    time.sleep(1)
    print("But be careful, for many dangers lie ahead!")
    time.sleep(1)

def choose_path():
    print("\nWhich path will you choose?")
    time.sleep(1)
    print("1. Follow the winding river.")
    time.sleep(1)
    print("2. Venture through the dark cave.")
    time.sleep(1)
    return input("Enter your choice (1 or 2): ")

def explore_river():
    print("\nYou decide to follow the winding river.")
    time.sleep(1)
    print("As you walk along the riverbank, you hear the sound of rushing water.")
    time.sleep(1)
    print("Suddenly, a group of hungry wolves appears!")
    time.sleep(1)
    choice = input("What will you do? (1. Fight, 2. Run): ")
    if choice == "1":
        print("\nYou bravely fight off the wolves with your sword and manage to escape.")
    else:
        print("\nYou run as fast as you can, narrowly escaping the wolves' pursuit.")

def explore_cave():
    print("\nYou decide to venture through the dark cave.")
    time.sleep(1)
    print("As you enter the cave, you feel a chilling breeze and hear mysterious whispers.")
    time.sleep(1)
    print("The cave splits into two paths, one leading up and the other going deeper into darkness.")
    time.sleep(1)
    choice = input("Which path will you take? (1. Up, 2. Deeper): ")
    if choice == "1":
        print("\nYou climb up the rocky path and discover a hidden treasure chest!")
        time.sleep(1)
        print("Congratulations! You found the legendary treasure!")
    else:
        print("\nYou descend into the depths of the cave, but the darkness consumes you.")
        time.sleep(1)
        print("Unfortunately, you are lost forever.")

def play_game():
    introduction()
    path_choice = choose_path()

    if path_choice == "1":
        explore_river()
    elif path_choice == "2":
        explore_cave()
    else:
        print("Invalid choice. Please try again.")

play_game()
# The end of the game