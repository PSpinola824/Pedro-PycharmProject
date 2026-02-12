def create_npcs():
    """
    non-player character (computer controlled - character)

    NPC's to have the following characteristics
    - locations
    - be able to talk (text dialogue)
    - item: they may be able to offer users an item 
    - TALKED? have we spoken to them before

    """
    npcs = {
        "librarian": {
            "location": "library",
            "dialogue": "The safe code is hidden in the oldest book on the third shelf. ",
            "item": "ancient book",
            "talked": False,
        },
        "ghost": {
            "location": "hallway",
            "dialogue": "I once guarded this mansion. The master key is in three pieces.",
            "item": "ghost token",
            "talked": False
        },
        "gardener": {
            "location": "garden",
            "dialogue": "The fountain holds secrets. Look closely at the inscription.",
            "item": None,
            "talked": False
        }
    }
    return npcs

def talk_to_npc(npc_name, npcs, current_room, inventory):
    """
    have a simple conversation with an npc 
    one exchange with each npc
    """
    npc_name = npc_name.lower()

    if npc_name not in npcs:
        available = ", ".join(npcs.keys())
        print(f"\nNo NPCS named '{npc_name}. Try {available}")
        return False
    
    npc = npcs[npc_name]
    
    if npc["location"] != current_room: 
        print(f"\n{npc_name.title()} is not in this room.")
        return False
    # npc is available and in the room.. we can have a dialogue
    # show the dialogue

    print(f"\n{npc_name.title()}: \"{npc['dialogue']}\"")

    # give an item
    if npc["item"] and not npc["talked"]:
        print(f"\n{npc_name.title()} gives you: {npc['item']}")
        inventory.append(npc['item'])
        npc["talked"] = True
    elif npc["talked"]:
        print(f"\n{npc_name.title()}: I've already spoken with you and told you what i know")
    return True    

def list_npcs_in_room(current_room, npcs):
    """show which NPCs are in the room"""
    # list comprehension - technique in python for generating a list by providing rules for the # members of the list.
    npcs_here = [name for name, data in npcs.items() if data["location"] == current_room ]

    if npcs_here:
        print("\nPeople are here")
        for npc in npcs_here:
            print(f". - {npc.title()}")
        return True
    return False


def display_inventory(inventory):
    """
    Display the user's current inventory.
    """ 
    if not inventory:
        print("\nYour inventory is empty. ")
    else:
        print("\nYour inventory:")
        for i, item in enumerate(inventory, 1):
            print(f"  {i}. {item}")
def examine_object(obj_name, inventory):
    """
    Examine an object and maybe add it to our inventory. 
    Return True if item added. otherwise it will return False
    """
    obj_name = obj_name.lower()

    if obj_name == "desk":
        print("You seach the desk drawers...")
        if "rusty key" not in inventory:
            print("You found a rusty key!")
            inventory.append("rusty key")
            return True
        else:
            print("The desk is empty now")
            return False
    elif obj_name == "bookshelf":
        print("\nYou examine the bookshelf...")
        if "mysterious book" not in inventory:
            print("One book seems different. You take it.")
            inventory.append("mysterious book")
            return True
        else:
            print("Just dusty old books.")
            return False
    
    else:
        print(f"\nYou can't examine '{obj_name}'. Try 'desk' or 'bookshelf'.")
        return False

def describe_room(room_name, rooms, npcs):
    """
    describe the curent room to the player
    show description, any objects, NPCS
    """
    room = rooms[room_name]

    print("\n" + "="*50)
    print(f"LOCATION: {room_name.upper()}")
    print("\n" + "="*50)
    print(room["description"])

    # show all obejcts in the room
    if room["obects"]:
        print("\nYou see:")
        for obj in room["objects"]:
            print (f"  - {obj}")
    list_npcs_in_room(room_name, npcs)

    # have we visited this room before BOOLEAN
    if not room["visited"]:
        print("\n (First time here)")
        room["visited"] = True

def main():
    """
    Welcome to our Escape Room. 
    The challenge is for users to use the tools to "escape" 
    """
    npcs = create_npcs()

    rooms = {
        "library": {
            "description": "A dusty library with ancient books lining the walls.",
            "objects": ["desk", "bookshelf"],
            "exits": {"north": "hallway"},
            "visited": False
        },
        "hallway": {
            "description": "A narrow hallway with portraits on the walls.",
            "objects": ["painting"],
            "exits": {"south": "library", "west": "garden"},
            "visited": False
        },
        "garden": {
            "description": "An overgrown garden with a crumbling fountain.",
            "objects": ["fountain"],
            "exits": {"east": "hallway"},
            "visited": False
        }
    }
    
    current_room = "library" # every time we start the game in the library

    # game variables

    player_name = input("what's your name, challenger? ")
    print(f"\nWelcome, {player_name}.   \nLet's get started on your adventure... ") 

    # initializing variables
    game_over = False
    # escaped = False 
    moves = 0
    inventory = [] #empty list?

    while not game_over:
        print("\n" + "="*50)
        print("What do you want to do?")
        print("1. Look around the room")
        print("2. Move to another room")
        print("3. Check your inventory")
        print("4. Examine an object")
        print("5. Talk to someone")
        print("6. Try to escape")
        print("7. Quit game")
    
        choice = input("Enter your choice (1-7): ")
        # print(f"DEBUG you chose number {choice}")
        moves += 1

        if choice == "1":
            print("\nYou see a dusty room with:")
            print("  - A wooden desk")
            print("  - A locked door")
            print("  - A bookshelf")
        elif choice == "2":
            direction = input("\nWhich direction? (north/south/east/west): ")
            direction = direction.lower()
            room = rooms[current_room]
            
            if direction in room["exits"]:
                current_room = room["exits"][direction]
                print(f"\nYou move {direction}...")
                describe_room(current_room, rooms, npcs)
            else:
                print(f"\nYou can't go {direction} from here.")
                moves -= 1 
        elif choice == "3":
            display_inventory(inventory)
        elif choice == "4":
            obj = input("\nWhat do you want to examine? ")
            examine_object(obj, inventory)
        elif choice == "5":
            who = input("\nTalk to whom? ")
            talk_to_npc(who, npcs, current_room, inventory)
        
        elif choice == "6":
            print("\nYou try the door...")
            if "rusty key" in inventory:
                print("The rusty key works! The door creaks open...")
                print(f"\nCongratulations, {player_name}! You escaped in {moves} moves!")
                # escaped = True
                game_over = True
            else:
                print("The door is locked. You need to find a key!")
        elif choice == "7":
            print(f"\nThanks for playing, {player_name}! You made {moves} moves.")
            game_over = True

        else: 
            print("\nInvalid choice. Try again ")
            moves -= 1

    print("\nGame Over!")

# if __name__ == "__main__":
main()  
