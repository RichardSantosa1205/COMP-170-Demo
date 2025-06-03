# May 19&20 Code

print("\nHello COMP 170!\n")

print("Hello Kofi, Welcome to COMP 170")
print("Hello Richard, Welcome to COMP 170")
print("Hello Lilly, Welcome to COMP 170")
print("Hello Ben, WelcomE to COMPP 1760")

#Pattern:
# "Hello" fist_name", welcome to " course_code" 

def personalized_greeting(name, course_code):
    print(f"Hello {name}, welcome to {course_code} !!!") 

personalized_greeting("Richard", "COMP 170")
personalized_greeting("Leo", "COMP 170")

print()


students = ["Omar", "Lula", "Enrique", "Arhub", "Ben", "Richard", "Heather"]
your_course = "COMP 170"

for name in students:
    personalized_greeting(name, your_course)

# June 2 Code
#Functions, booleans, lists, and dictionaries

def form_letter(recipient, promise):
    print("dear " + recipient + ",")
    print("Thank you for voting for me.")
    print("I promise to ")
    print(promise)

my_voters = {
    "Richard": "build a park in your backyard",
    "Lula": "fix your side walk",
    "Ana": "call a friend in DC for a pardon"
    "Richard": "add a bus sto in your living room"
}
# for every voter: 
# call the function form letter passing to it the 
# voter's and my most insincere promise to them

form_letter ("Omar", "erase your parking tickets")