# ======================================
# SECTION 1: CREATE AN ITEMS DICTIONARY - PEDRO CODE
# ======================================
def create_item_database():
    """
    Create a dictionary describing all items in the game.
    Each item has: description, value (points), and category.
    """
    items = {
        "rusty key": {
            "description": "An old brass key covered in rust. It looks like it could open an ancient lock.",
            "value": 50,
            "category": "key"
        },
        "mysterious book": {
            "description": "A heavy leather-bound book with strange symbols carved into the cover.",
            "value": 30,
            "category": "book"
        },
        "ancient book": {
            "description": "A fragile book with yellow pages. The ink looks faded, but important.",
            "value": 45,
            "category": "book"
        },
        "ghost token": {
            "description": "A cold, transparent coin-like token. It hums softly in your hand.",
            "value": 60,
            "category": "token"
        },
        "golden amulet": {
            "description": "A shining amulet with a sun emblem. It feels warm, like it has power.",
            "value": 100,
            "category": "treasure"
        },
        "silver coin": {
            "description": "A worn silver coin with a knight engraved on it. It looks valuable.",
            "value": 55,
            "category": "coin"
        },
        # Optional extra item (your game already had this)
        "silver shard": {
            "description": "A small silver shard pulled from the fountain. It might be part of something larger.",
            "value": 25,
            "category": "shard"
        }
    }
    return items


# ======================================
# SECTION 2: LIST COMPREHENSION #1 - PEDRO CODE
# ======================================
def get_valuable_items(inventory, items_db):
    """
    Return list of items in inventory worth more than 40 points.
    Uses list comprehension.
    """
    # Only include items that exist in items_db AND have value > 40
    valuable = [item for item in inventory if item in items_db and items_db[item]["value"] > 40]
    return valuable


# ======================================
# SECTION 3: LIST Comprehension - PEDRO CODE
# ======================================
def get_untalked_npcs(npcs):
    """
    Return list of NPC names the player hasn't talked to yet.
    Uses list comprehension.
    """
    untalked = [name for name, data in npcs.items() if data["talked"] == False]
    return untalked


# =========================
# ROOMS + NPCs (Original) - PEDRO CODE
# =========================
def create_rooms():
    rooms = {
        "library": {
            "description": "A dusty library with ancient books.",
            "exits": {"north": "hallway"},
            "details": {
                "desk": "An old oak desk. You find a **rusty key** in the drawer!",
                "bookshelf": "Shelves of books. One looks like a secret lever."
            },
            "items": ["rusty key"],
            "visited": False
        },
        "hallway": {
            "description": "A narrow hallway.",
            "exits": {"south": "library", "west": "garden"},
            "details": {
                "painting": "You see a painting. The eyes seem to follow you..."
            },
            "visited": False
        },
        "garden": {
            "description": "An overgrown garden with a crumbling fountain.",
            "exits": {"east": "hallway"},
            "details": {
                "fountain": "You spot a silver shard in the shimmering water.",
                "statue": "It looks to be a knight pointing north."
            },
            "items": ["silver shard"],
            "visited": False
        }
    }
    return rooms


def create_npcs():
    """
    NPCs have:
    - location
    - dialogue
    - item they can give (optional)
    - talked: have we spoken to them before?
    """
    npcs = {
        "librarian": {
            "location": "library",
            "dialogue": "The safe code is hidden in the oldest book on the third shelf.",
            "item": "ancient book",
            "talked": False
        },
        "ghost": {
            "location": "hallway",
            "dialogue": "I once guarded this mansion. The master key is in three pieces...",
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
    Have a simple conversation with an NPC.
    One exchange with each NPC.
    """
    npc_name = npc_name.lower()

    if npc_name not in npcs:
        available = ", ".join([name.title() for name in npcs.keys()])
        print(f"\nNo NPC named '{npc_name}'. Try: {available}")
        return False

    npc = npcs[npc_name]

    if npc["location"] != current_room:
        print(f"\n{npc_name.title()} is not in this room.")
        return False

    # Show dialogue
    print(f"\n{npc_name.title()}: \"{npc['dialogue']}\"")

    # Give an item (only once)
    if npc["item"] and not npc["talked"]:
        print(f"\n{npc_name.title()} gives you: {npc['item']}")
        inventory.append(npc["item"])
        npc["talked"] = True
    elif npc["talked"]:
        print(f"\n{npc_name.title()}: I've already spoken with you and told you what I know.")

    return True


def list_npcs_in_room(current_room, npcs):
    """Show which NPCs are in the room."""
    npcs_here = [name for name, data in npcs.items() if data["location"] == current_room]

    if npcs_here:
        print("\nPeople are here:")
        for npc in npcs_here:
            print(f" - {npc.title()}")
        return True

    return False


def display_inventory(inventory):
    """Display the user's current inventory."""
    if not inventory:
        print("\nYour inventory is empty.")
    else:
        print("\nYour inventory:")
        for i, item in enumerate(inventory, 1):
            print(f"  {i}. {item}")


def examine_object(obj_name, current_room_data, inventory):
    """
    Examine an object in the current room.
    If the room still has items left, the player may collect one.
    """
    obj_name = obj_name.lower()

    if obj_name in current_room_data["details"]:
        print(f"\n{current_room_data['details'][obj_name]}")

        # If there are items available in the room, collect one
        if "items" in current_room_data and len(current_room_data["items"]) > 0:
            item = current_room_data["items"].pop(0)
            inventory.append(item)
            print(f"\nAdded '{item}' to inventory.")
        return True
    else:
        print(f"\nYou don't see any '{obj_name}' here.")
        return False


def describe_room(room_name, rooms, npcs):
    """Describe the current room to the player."""
    room = rooms[room_name]

    print("\n" + "=" * 50)
    print(f"LOCATION: {room_name.upper()}")
    print("=" * 50)
    print(room["description"])

    if room["details"]:
        print("\nYou see:")
        for obj in room["details"]:
            print(f"  - {obj}")

    list_npcs_in_room(room_name, npcs)

    if not room["visited"]:
        print("\n(First time here)")
        room["visited"] = True


# ======================================
# SECTION 4: ADD NEW FUNCTIONALITY - PEDRO CODE
# ======================================
def examine_inventory_item(inventory, items_db):
    """
    Let player examine an item in their inventory for details.
    Prints description, value, category.
    Mentions if it is valuable using get_valuable_items().
    """
    item_name = input("\nWhich item do you want to examine? ").lower()

    # Check if item is in inventory
    if item_name not in inventory:
        print(f"\nYou don't have '{item_name}' in your inventory.")
        return False

    # Check if item exists in database
    if item_name not in items_db:
        print(f"\nNo information available about '{item_name}'.")
        return False

    # Get item data
    item_data = items_db[item_name]

    # Print item details
    print("\n" + "-" * 40)
    print(f"Item: {item_name.title()}")
    print(f"Description: {item_data['description']}")
    print(f"Value: {item_data['value']} points")
    print(f"Category: {item_data['category']}")
    print("-" * 40)

    # Bonus: mention if valuable
    valuable_items = get_valuable_items(inventory, items_db)
    if item_name in valuable_items:
        print("This is a valuable item!")

    return True


# ======================================
# BONUS (Optional): HINT SYSTEM - PEDRO CODE
# ======================================
def get_hints(inventory, items_db, npcs):
    """
    Provide hints based on current game state.
    Returns a list of hint strings.
    """
    hints = []

    # Hint 1: NPCs you haven't talked to
    untalked = [name for name, data in npcs.items() if not data["talked"]]
    if untalked:
        hints.append(f"Try talking to: {', '.join([name.title() for name in untalked])}")

    # Hint 2: Valuable items NOT in inventory (list comprehension)
    valuable_not_collected = [
        item for item, data in items_db.items()
        if data["value"] > 40 and item not in inventory
    ]
    if valuable_not_collected:
        hints.append("Valuable items you still might find: " + ", ".join([i.title() for i in valuable_not_collected]))

    # Hint 3: Key item needed to escape
    if "rusty key" not in inventory:
        hints.append("You need a key to escape. Search the library carefully (try examining objects).")
    else:
        hints.append("You have the key! Try escaping when you're ready.")

    return hints


# =========================
# MAIN GAME LOOP - PEDRO CODE
# =========================
def main():
    """
    Welcome to our Escape Room.
    The challenge is for users to explore rooms, collect items, talk to NPCs, and escape.
    """
    npcs = create_npcs()
    rooms = create_rooms()

    # SECTION 1 INTEGRATION: create the items database (required)
    items_db = create_item_database()

    current_room = "library"
    player_name = input("What's your name, challenger? ")
    print(f"\nWelcome, {player_name}.\nLet's get started on your adventure...")

    game_over = False
    moves = 0
    inventory = []

    # OPTIONAL TESTING (uncomment if your teacher wants proof in terminal)
    # test_inv = ["rusty key", "mysterious book", "golden amulet"]
    # print(get_valuable_items(test_inv, items_db))
    # print("NPCs you haven't talked to:", get_untalked_npcs(npcs))

    while not game_over:
        print("\n" + "=" * 50)
        print("What do you want to do?")
        print("1. Look around the room")
        print("2. Move to another room")
        print("3. Check your inventory")
        print("4. Examine an object")
        print("5. Talk to someone")
        print("6. Examine item in inventory")
        print("7. Get hints")
        print("8. Try to escape")
        print("9. Quit game")

        choice = input("Enter your choice (1-9): ")
        moves += 1

        if choice == "1":
            describe_room(current_room, rooms, npcs)

        elif choice == "2":
            direction = input("\nWhich direction? (north/south/east/west): ").lower()
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
            examine_object(obj, rooms[current_room], inventory)

        elif choice == "5":
            who = input("\nTalk to whom? ")
            talk_to_npc(who, npcs, current_room, inventory)

        elif choice == "6":
            examine_inventory_item(inventory, items_db)

        elif choice == "7":
            hints = get_hints(inventory, items_db, npcs)
            print("\nHints:")
            for h in hints:
                print(f" - {h}")

        elif choice == "8":
            print("\nYou try the door...")
            if "rusty key" in inventory:
                print("The rusty key works! The door creaks open...")
                print(f"\nCongratulations, {player_name}! You escaped in {moves} moves!")
                game_over = True
            else:
                print("The door is locked. You need to find a key!")

        elif choice == "9":
            print(f"\nThanks for playing, {player_name}! You made {moves} moves.")
            game_over = True

        else:
            print("\nInvalid choice. Try again.")
            moves -= 1

    print("\nGame Over!")


# Run the game
main()  
