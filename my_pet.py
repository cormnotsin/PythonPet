# This is a comment - it's a note for humans, not the computer!
# Let's create our digital pet!

print("🐶 Welcome to your Digital Pet Simulator! 🐶")
print("=" * 40)

# Variables are like boxes that hold information
pet_name = "Buddy"
pet_type = "Dog"
pet_happiness = 50
pet_hunger = 30

# Let's meet our pet!
print(f"Meet your new pet: {pet_name} the {pet_type}! 🎉")
print(f"Happiness: {pet_happiness}/100 😊")
print(f"Hunger: {pet_hunger}/100 🍽️")

# Let's make our pet respond based on how it feels!
print("\n" + "=" * 40)
print("How is your pet feeling?")

if pet_happiness >= 80:
    print(f"{pet_name} is super happy! 😄 *tail wagging*")
elif pet_happiness >= 50:
    print(f"{pet_name} is feeling okay. 😐")
else:
    print(f"{pet_name} looks sad... 😢")

if pet_hunger >= 70:
    print(f"{pet_name} is very hungry! 🍖 *stomach growling*")
elif pet_hunger >= 30:
    print(f"{pet_name} could use a snack. 🥨")
else:
    print(f"{pet_name} is well-fed! 😋")


def feed_pet() -> None:
    """
    Feeds the pet, reducing hunger and increasing happiness.
    
    This function decreases hunger by 20 and increases happiness
    by 10, keeping both values between 0 and 100.
    """
    global pet_hunger, pet_happiness
    print(f"\n🍖 Feeding {pet_name}...")
    pet_hunger = pet_hunger - 20
    pet_happiness = pet_happiness + 10
    
    # Make sure numbers don't go below 0 or above 100
    if pet_hunger < 0:
        pet_hunger = 0
    if pet_happiness > 100:
        pet_happiness = 100
    
    print(f"{pet_name}: 'Woof! Thank you!' 🐕")
    print(f"Hunger: {pet_hunger}/100 🍽️")
    print(f"Happiness: {pet_happiness}/100 😊")


def play_with_pet() -> None:
    """
    Plays with the pet, increasing happiness and hunger.
    
    This function increases happiness by 15 and hunger by 10,
    keeping both values between 0 and 100.
    """
    global pet_hunger, pet_happiness
    print(f"\n🎾 Playing with {pet_name}...")
    pet_happiness = pet_happiness + 15
    pet_hunger = pet_hunger + 10
    
    # Make sure numbers don't go below 0 or above 100
    if pet_hunger > 100:
        pet_hunger = 100
    if pet_happiness > 100:
        pet_happiness = 100
    
    print(f"{pet_name}: 'This is fun!' 🎉")
    print(f"Happiness: {pet_happiness}/100 😊")
    print(f"Hunger: {pet_hunger}/100 🍽️")


# Let's try our new functions!
print("\n" + "🎮 Let's interact with our pet! 🎮")
feed_pet()
play_with_pet()
