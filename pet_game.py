# 🐾 Digital Pet Care Game 🐾
# A fun interactive game to take care of your digital pet!

print("🌟 Welcome to the Digital Pet Care Game! 🌟")
print("=" * 50)

# Set up our pet
pet_name = input("What would you like to name your pet? ")
print(f"Great choice! Meet {pet_name}! 🐕")

# Starting stats
pet_happiness = 50
pet_hunger = 40
pet_energy = 60


def show_pet_status() -> None:
    """
    Displays the current status of the pet.
    
    Shows happiness, hunger, energy levels and pet's current mood
    based on happiness level.
    """
    print(f"\n📊 {pet_name}'s Status:")
    print(f"   Happiness: {pet_happiness}/100 😊")
    print(f"   Hunger: {pet_hunger}/100 🍽️")
    print(f"   Energy: {pet_energy}/100 ⚡")
    
    # Show pet's mood
    if pet_happiness >= 80:
        print(f"   {pet_name} is super happy! 🎉")
    elif pet_happiness >= 40:
        print(f"   {pet_name} is doing okay. 😐")
    else:
        print(f"   {pet_name} needs some love... 😢")


def feed_pet() -> None:
    """
    Feeds the pet, reducing hunger and increasing happiness.
    
    Checks if pet is already full before feeding. Decreases
    hunger by 25 and increases happiness by 10.
    """
    global pet_hunger, pet_happiness, pet_energy
    if pet_hunger <= 10:
        print(f"{pet_name} is already full! 🤗")
        return
    
    print(f"🍖 You feed {pet_name} some delicious food!")
    pet_hunger = max(0, pet_hunger - 25)
    pet_happiness = min(100, pet_happiness + 10)
    print(f"{pet_name}: 'Yum! Thank you!' 😋")


def play_with_pet() -> None:
    """
    Plays with the pet, increasing happiness but using energy.
    
    Checks if pet has enough energy to play. Increases happiness
    by 20, decreases energy by 15, and increases hunger by 10.
    """
    global pet_happiness, pet_hunger, pet_energy
    if pet_energy <= 15:
        print(f"{pet_name} is too tired to play right now! 😴")
        return
    
    print(f"🎾 You play fetch with {pet_name}!")
    pet_happiness = min(100, pet_happiness + 20)
    pet_energy = max(0, pet_energy - 15)
    pet_hunger = min(100, pet_hunger + 10)
    print(f"{pet_name}: 'That was fun!' 🎉")


def let_pet_sleep() -> None:
    """
    Lets the pet rest and restore energy.
    
    Increases pet's energy by 30 points up to maximum of 100.
    """
    global pet_energy
    print(f"💤 {pet_name} takes a nice nap...")
    pet_energy = min(100, pet_energy + 30)
    print(f"{pet_name}: 'Ahh, I feel refreshed!' 😌")


def show_menu() -> None:
    """
    Displays the game menu with available actions.
    
    Shows 5 options: feed, play, sleep, status, and quit.
    """
    print("\n🎮 What would you like to do?")
    print("1. Feed your pet 🍖")
    print("2. Play with your pet 🎾")
    print("3. Let your pet sleep 💤")
    print("4. Check pet status 📊")
    print("5. Quit game 👋")


# Main game loop - this is where the magic happens!
print(f"\n🎯 Your goal: Keep {pet_name} happy, fed, and rested!")
print("Let's start taking care of your pet!")

game_running = True
while game_running:
    show_menu()
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == "1":
        feed_pet()
    elif choice == "2":
        play_with_pet()
    elif choice == "3":
        let_pet_sleep()
    elif choice == "4":
        show_pet_status()
    elif choice == "5":
        print(f"\n👋 Thanks for taking care of {pet_name}!")
        print("Come back soon! 🐾")
        game_running = False
    else:
        print("🤔 That's not a valid choice. Please try again!")
    
    # Show status after each action (except quit and status check)
    if choice in ["1", "2", "3"]:
        show_pet_status()
