# 📖 Python Coding Dictionary for Young Programmers

## Your Handy Guide to Coding Words!

This sheet explains all the important words and symbols you'll use
while creating your digital pet. Keep this nearby while you code!

---

## 🔤 Programming Vocabulary

### **Programming**
Giving step-by-step instructions to a computer to make it do
something. Just like following a recipe to bake cookies!

### **Code**
The instructions you write that tell the computer what to do.
Code is written in special languages that computers understand.

### **Python**
The name of the programming language we're using. It's one of
the easiest languages to learn!

### **Run**
Making the computer follow your instructions. When you "run"
your code, the computer does what you told it to do.

---

## 📦 Variables (Storing Information)

### **Variable**
A box that holds information the computer remembers. You give
it a name so you can use it later.

**Example:** `pet_name = "Buddy"`
- The box is named `pet_name`
- It holds the information `"Buddy"`

### **String**
Text that the computer remembers. Always put strings inside
quotes: `"like this"` or `'like this'`

**Examples:**
- `"Fluffy"` ← a string
- `"Hello!"` ← a string
- `"123"` ← this is also a string (not a number!)

### **Number (Integer)**
A number without a decimal point. You don't use quotes for numbers.

**Examples:**
- `50` ← a number
- `100` ← a number
- `0` ← a number

### **Assignment**
Putting information into a variable using the equals sign `=`

**Example:** `pet_happiness = 50`
- This puts the number 50 into the pet_happiness variable

---

## 🖨️ Showing Information

### **print()**
A command that shows text on the screen. Whatever you put
inside the parentheses will appear.

**Example:** `print("Hello!")`
- This shows: Hello!

### **f-string**
A special way to mix variables and text together. Put `f` before
the quotes and use `{}` around variable names.

**Example:** `print(f"My pet is {pet_name}")`
- If pet_name is "Buddy", this shows: My pet is Buddy

---

## 🤔 Making Decisions

### **if**
A word that means "only do this IF something is true"

**Example:**
```python
if pet_happiness >= 80:
    print("Pet is happy!")
```
This only prints "Pet is happy!" IF happiness is 80 or more.

### **elif**
Short for "else if" - checks another condition if the first
one wasn't true. Means "but if this other thing is true instead"

**Example:**
```python
if pet_happiness >= 80:
    print("Super happy!")
elif pet_happiness >= 50:
    print("Pretty good!")
```

### **else**
What to do if none of the other conditions were true.
Means "if nothing else was true, do this"

**Example:**
```python
if pet_happiness >= 80:
    print("Super happy!")
else:
    print("Needs attention")
```

### **Condition**
A question that is either true or false. The computer checks
if it's true to decide what to do.

**Examples:**
- `pet_happiness >= 80` ← Is happiness 80 or more?
- `pet_hunger < 20` ← Is hunger less than 20?

---

## 🔁 Repeating Actions

### **Loop**
A way to repeat code over and over without writing it again.
Like doing jumping jacks - you repeat the same action!

### **while**
Keeps repeating code as long as something is true.

**Example:**
```python
while game_running == True:
    show_menu()
```
This keeps showing the menu while the game is running.

---

## 📋 Functions (Organized Instructions)

### **Function**
A group of instructions with a name. Like a recipe you can
use over and over. Write it once, use it many times!

**Example:**
```python
def feed_pet():
    print("Feeding pet...")
    pet_hunger = pet_hunger - 20
```

### **def**
The word that starts creating a function. Short for "define"

**Example:** `def feed_pet():`
- This starts defining a function named feed_pet

### **Call (a function)**
Using a function you already created. Just write its name
with parentheses.

**Example:** `feed_pet()`
- This makes the computer run all the code inside feed_pet

### **Return**
When used in functions, it stops the function and goes back
to where you called it from. Like finishing a recipe.

---

## 💬 Getting Input from Players

### **input()**
A command that lets the player type something. The computer
waits for them to type and press Enter.

**Example:**
```python
pet_name = input("What's your pet's name? ")
```
This asks the question and saves the answer in pet_name.

---

## ➕ Math Symbols (Operators)

### **=** (equals sign)
Puts a value into a variable. NOT asking if things are equal!

**Example:** `pet_happiness = 50`

### **==** (double equals)
Checks if two things are the same. Asks "are these equal?"

**Example:** `if pet_hunger == 0:`

### **+** (plus)
Adds numbers together or joins strings together.

**Examples:**
- `5 + 3` = 8
- `"Hi " + "there"` = "Hi there"

### **-** (minus)
Subtracts one number from another.

**Example:** `pet_hunger - 20`

### **>** (greater than)
Checks if the first number is bigger than the second.

**Example:** `if pet_happiness > 50:`

### **<** (less than)
Checks if the first number is smaller than the second.

**Example:** `if pet_energy < 20:`

### **>=** (greater than or equal to)
Checks if the first number is bigger OR the same as the second.

**Example:** `if pet_happiness >= 80:`

### **<=** (less than or equal to)
Checks if the first number is smaller OR the same as the second.

**Example:** `if pet_hunger <= 10:`

---

## 🎯 Important Python Rules

### **Indentation**
Spaces at the beginning of lines that show which code belongs
together. Python is VERY picky about indentation!

**Correct:**
```python
def feed_pet():
    print("Feeding...")
    pet_hunger = 0
```

**Wrong:**
```python
def feed_pet():
print("Feeding...")
    pet_hunger = 0
```

**Rule:** Always use 4 spaces for each level of indentation.

### **Colon :**
You need a colon at the end of lines that start with:
- `def` (functions)
- `if` / `elif` / `else` (decisions)
- `while` (loops)

**Example:** `def feed_pet():`  ← don't forget the colon!

### **Quotes**
Use matching quotes around text (strings):
- Both `"` like this: `"Hello"`
- Both `'` like this: `'Hello'`

**Wrong:** `"Hello'` ← quotes don't match!

### **Case Sensitivity**
Python cares about capital and lowercase letters!
- `pet_name` is NOT the same as `Pet_name`
- `Pet_Name` is NOT the same as `pet_name`

**Rule:** Keep your variable names the same every time!

### **Comments**
Notes for humans that the computer ignores. Start with `#`

**Example:**
```python
# This is a comment for people to read
pet_name = "Buddy"  # You can also put comments here
```

### **Parentheses ( )**
Used after function names to call the function.

**Examples:**
- `print("Hello")` ← parentheses around what to print
- `feed_pet()` ← empty parentheses to call the function

### **Global**
A special word that lets a function change a variable from
outside the function.

**Example:**
```python
def feed_pet():
    global pet_hunger
    pet_hunger = pet_hunger - 20
```

Without `global`, the function can't change pet_hunger.

---

## 🔢 Special Functions We Use

### **max()**
Picks the bigger number out of two numbers.

**Example:** `max(0, pet_hunger - 25)`
- If result is negative, use 0 instead

### **min()**
Picks the smaller number out of two numbers.

**Example:** `min(100, pet_happiness + 20)`
- If result is over 100, use 100 instead

---

## 🎨 Special Characters

### **\n**
Makes a new line (like pressing Enter).

**Example:** `print("\nNew line!")`
- The `\n` creates a blank line before "New line!"

### ***** (asterisk)
Can multiply numbers OR repeat strings.

**Examples:**
- `5 * 3` = 15
- `"=" * 10` = "=========="

---

## 🐛 Error Words You Might See

### **SyntaxError**
You wrote something Python doesn't understand. Usually means:
- Missing a colon `:`
- Wrong indentation
- Unclosed quotes

### **NameError**
You used a variable name that doesn't exist yet. Check spelling!

### **IndentationError**
Your spaces at the start of lines are wrong. Count your spaces!

### **TypeError**
You tried to mix things that don't go together (like adding
a number and text).

---

## 💡 Quick Tips

1. **Save your file** before running it! (Ctrl+S or Cmd+S)

2. **Read error messages** - they tell you what's wrong!

3. **Check your spelling** - Python is very picky!

4. **Count your spaces** - indentation must be exact!

5. **Match your quotes** - `"` with `"` or `'` with `'`

6. **Don't forget colons** - after `def`, `if`, `while`

7. **Ask for help** - everyone gets stuck sometimes!

---

## 🎉 Remember:

- Every programmer makes mistakes - even experts!
- Errors are how we learn
- Keep trying and don't give up
- Have fun creating your digital pet!

---

**You're doing great! Keep this sheet handy and refer to it
whenever you need help remembering what something means.** 🌟
