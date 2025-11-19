# 🐾 Digital Pet Simulator - 3-Day Coding Adventure!

## Welcome, Young Coders! 👋

Get ready for an exciting 3-day journey where you'll learn to code
by creating your very own digital pet! By the end, you'll have a pet
you can feed, play with, and take care of using code YOU wrote!

## What You'll Learn 🎓
- How to give instructions to a computer (programming)
- How to store information (variables)
- How to make decisions (if/else statements)
- How to repeat actions (loops)
- How to organize code (functions)

## What You Need 🛠️
- A computer with Python installed
- VS Code (our coding editor)
- Your creativity and curiosity!

## 📚 Helpful Resources

### For Students:
- **STUDENT_DEFINITIONS.md** - Complete dictionary of all coding words
- **QUICK_REFERENCE.md** - One-page cheat sheet to print and keep

### For Teachers:
- **TEACHER_GUIDE.md** - Complete guide for teachers
- **MATERIALS_GUIDE.md** - How to use student materials
- **PLAN_B_LOCKED_COMPUTERS.md** - Backup plan for locked computers

---

# 📅 Day 1: Meeting Your Digital Pet (45 minutes)

## Today's Goal: Create your first pet and learn basic coding!

### What We'll Do:
1. Learn what programming is
2. Create our first Python file
3. Store information in variables
4. Make our pet respond with if/else
5. Create functions to interact with our pet

### Step 1: Create Your Pet File 📝
1. Open VS Code
2. Create a new file called `my_pet.py`
3. The `.py` ending tells the computer this is a Python file!

### Step 2: Your First Code! 💻
Type or copy this code into your `my_pet.py` file:

```python
# This is a comment - it's a note for humans!
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
```

### Step 3: Run Your Code! ▶️
1. Save your file (Ctrl+S or Cmd+S)
2. Open the terminal in VS Code
3. Type: `python my_pet.py`
4. Watch your pet come to life!

### Step 4: Add Decision-Making 🧠
Add this code to make your pet respond based on how it feels:

```python
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
    print(f"{pet_name} is very hungry! 🍖")
elif pet_hunger >= 30:
    print(f"{pet_name} could use a snack. 🥨")
else:
    print(f"{pet_name} is well-fed! 😋")
```

### Step 5: Create Functions 🔧
Functions are like recipes - instructions with a name! Add this:

```python
def feed_pet() -> None:
    """
    Feeds the pet, reducing hunger and increasing happiness.
    
    This function decreases hunger by 20 and increases
    happiness by 10, keeping values between 0 and 100.
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
    
    This function increases happiness by 15 and hunger by 10.
    """
    global pet_hunger, pet_happiness
    print(f"\n🎾 Playing with {pet_name}...")
    pet_happiness = pet_happiness + 15
    pet_hunger = pet_hunger + 10
    
    # Make sure numbers stay between 0 and 100
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
```

### Run Your Complete Pet! ▶️
Save and run your code again: `python my_pet.py`

### Today's Challenge 🌟
1. Change `pet_name` and `pet_type` to your favorites!
2. Try different starting values for happiness and hunger
3. See how the pet's responses change

### What You Learned Today ✅
- Variables store information
- `print()` shows text on screen
- `if/elif/else` makes decisions
- Functions organize code into reusable pieces

---

# 📅 Day 2: Creating an Interactive Pet Game (45 minutes)

## Today's Goal: Build a game with loops and player choices!

### What We'll Do:
1. Learn about loops (repeating actions)
2. Get input from the player
3. Create a menu of choices
4. Make a complete interactive game

### Step 1: Create Your Game File 🎮
Create a new file called `pet_game.py`

### Step 2: Set Up Your Interactive Pet 🐕
Type this code into `pet_game.py`:

```python
# 🐾 Digital Pet Care Game 🐾
# A fun interactive game!

print("🌟 Welcome to the Digital Pet Care Game! 🌟")
print("=" * 50)

# Set up our pet
pet_name = input("What would you like to name your pet? ")
print(f"Great choice! Meet {pet_name}! 🐕")

# Starting stats
pet_happiness = 50
pet_hunger = 40
pet_energy = 60
```

### Step 3: Create Helper Functions 🔧
Add these functions to show status and interact:

```python
def show_pet_status() -> None:
    """
    Displays the current status of the pet.
    
    Shows happiness, hunger, energy and current mood.
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
    Feeds the pet, reducing hunger.
    
    Checks if pet is full before feeding.
    """
    global pet_hunger, pet_happiness
    if pet_hunger <= 10:
        print(f"{pet_name} is already full! 🤗")
        return
    
    print(f"🍖 You feed {pet_name} delicious food!")
    pet_hunger = max(0, pet_hunger - 25)
    pet_happiness = min(100, pet_happiness + 10)
    print(f"{pet_name}: 'Yum! Thank you!' 😋")


def play_with_pet() -> None:
    """
    Plays with the pet, using energy.
    
    Checks if pet has enough energy to play.
    """
    global pet_happiness, pet_hunger, pet_energy
    if pet_energy <= 15:
        print(f"{pet_name} is too tired to play! 😴")
        return
    
    print(f"🎾 You play fetch with {pet_name}!")
    pet_happiness = min(100, pet_happiness + 20)
    pet_energy = max(0, pet_energy - 15)
    pet_hunger = min(100, pet_hunger + 10)
    print(f"{pet_name}: 'That was fun!' 🎉")


def let_pet_sleep() -> None:
    """
    Lets the pet rest and restore energy.
    """
    global pet_energy
    print(f"💤 {pet_name} takes a nice nap...")
    pet_energy = min(100, pet_energy + 30)
    print(f"{pet_name}: 'Ahh, I feel refreshed!' 😌")


def show_menu() -> None:
    """
    Displays the game menu with available actions.
    """
    print("\n🎮 What would you like to do?")
    print("1. Feed your pet 🍖")
    print("2. Play with your pet 🎾")
    print("3. Let your pet sleep 💤")
    print("4. Check pet status 📊")
    print("5. Quit game 👋")
```

### Step 4: Create the Game Loop 🔄
This is where the magic happens! Add this code:

```python
# Main game loop
print(f"\n🎯 Goal: Keep {pet_name} happy, fed, and rested!")
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
        print("🤔 That's not a valid choice. Try again!")
    
    # Show status after each action
    if choice in ["1", "2", "3"]:
        show_pet_status()
```

### Step 5: Run Your Game! ▶️
Run: `python pet_game.py`
Try all the different options and see how your pet responds!

### Today's Challenge 🌟
1. Add a message when energy gets too low
2. Try changing the stat values (how much feeding helps)
3. Make your pet say different things

### What You Learned Today ✅
- `while` loops repeat code until something changes
- `input()` lets players type responses
- Games can have menus and choices
- Functions keep code organized

---

# 📅 Day 3: Review & Celebration! (45 minutes)

## Today's Goal: Review, customize, and celebrate!

### What We'll Do:
1. Review what we learned (15 minutes)
2. Customize our pets (15 minutes)
3. Share and celebrate (15 minutes)

### Step 1: Review Time 📚
Open both your files (`my_pet.py` and `pet_game.py`)

**Quick Review Questions:**
- What does a variable do? (Stores information)
- What does `if/else` do? (Makes decisions)
- What does a function do? (Groups code we can reuse)
- What does a `while` loop do? (Repeats until we tell it to stop)

### Step 2: Customize Your Pet! 🎨
Pick one or both files and customize:

**Easy Changes:**
- Change pet name and type
- Change emojis
- Change what your pet says
- Change stat values (how hungry they get)

**Medium Changes:**
- Add new responses based on different stat levels
- Add a new stat (like "cleanliness")
- Create a new function (like "give_treat()")

**Challenge Changes:**
- Add a pet age that increases
- Make different pet types respond differently
- Add a happiness counter for the whole game

### Step 3: Create Celebration Program 🎉
Create a new file called `coding_celebration.py`:

```python
# 🎊 Congratulations! You're now a CODER! 🎊

from typing import List
import time


def display_banner() -> None:
    """Displays the celebration banner."""
    print("🌟" * 20)
    print("   CONGRATULATIONS!")
    print("   YOU DID IT!")
    print("🌟" * 20)


def show_skills(skills: List[str]) -> None:
    """Displays learned skills with animation."""
    for skill in skills:
        print(skill)
        time.sleep(0.5)


# Main celebration program
display_banner()

name = input("\nWhat's your name, amazing coder? ")

print(f"\n🎉 {name}, you completed your coding journey!")
print("\n📚 Here's everything you learned:")

skills = [
    "✅ How to give instructions to computers",
    "✅ How to store information in variables", 
    "✅ How to make decisions with if/else",
    "✅ How to repeat actions with loops",
    "✅ How to organize code with functions",
    "✅ How to get input from users",
    "✅ How to create interactive programs"
]

show_skills(skills)

print(f"\n🏆 {name}, you are now a PROGRAMMER!")
print("🚀 You can build amazing things with code!")
print("🌈 Keep practicing - the coding world is yours!")

print(f"\n💝 Thank you for learning to code, {name}!")
print("Remember: Every expert was once a beginner! 🌱➡️🌳")
```

### Run Your Celebration! ▶️
`python coding_celebration.py`

### Step 4: Share Your Work! 🎤
- Show your customized pet to a classmate
- Explain one thing you learned
- Tell what you want to build next

---

## 🎉 Congratulations, Young Programmer!

You've created your own digital pet simulator! You now know the
fundamental building blocks that ALL computer programs use.

### 🚀 What's Next?
- Keep experimenting with your pet code
- Try building other simple programs
- Ask questions and keep learning
- Most importantly: HAVE FUN CODING!

### 🌟 Fun Ideas to Try:
- 🎲 A dice rolling game
- 🧮 A simple calculator
- 📝 A story generator
- 🎨 Draw with turtle graphics

---

**Remember: The best way to learn programming is by doing it!
Keep coding and creating amazing things!** 🌟
