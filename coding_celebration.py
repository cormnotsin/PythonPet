# 🎊 Congratulations! You're now a CODER! 🎊

from typing import List
import time


def display_banner() -> None:
    """
    Displays the celebration banner.
    
    Shows a congratulations message with decorative stars.
    """
    print("🌟" * 20)
    print("   CONGRATULATIONS!")
    print("   YOU DID IT!")
    print("🌟" * 20)


def show_skills(skills: List[str]) -> None:
    """
    Displays learned skills with animation.
    
    Parameters:
    skills (List[str]): List of skills the student learned
    """
    for skill in skills:
        print(skill)
        time.sleep(0.5)


def show_next_projects(projects: List[str]) -> None:
    """
    Displays suggested next projects.
    
    Parameters:
    projects (List[str]): List of project ideas for students
    """
    for project in projects:
        print(f"   {project}")


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

print(f"\n🏆 {name}, you are now officially a PROGRAMMER!")
print("🚀 You can build amazing things with code!")
print("🌈 Keep practicing - the coding world is yours!")

print("\n🎯 Fun projects you could try next:")
next_projects = [
    "🎲 A dice rolling game",
    "🧮 A simple calculator", 
    "📝 A story generator",
    "🎨 ASCII art creator",
    "🏃 A running tracker"
]

show_next_projects(next_projects)

print(f"\n💝 Thank you for learning to code, {name}!")
print("Remember: Every expert was once a beginner! 🌱➡️🌳")
