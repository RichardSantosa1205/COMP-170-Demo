print("\nHello COMP 170!\n")

print("Hello Kofi, Welcome to COMP 170")
print("Hello Richard, Welcome to COMP 170")
print("Hello Lilly, Welcome to COMP 170")
print("Hello Ben, WelcomE to COMPP 1760")

#Pattern:
# "Hello" fist_name", weelcome to " course_code" 

def personalized_greeting(name, course_code):
    print(f"Hello {name}, welcome to {course_code} !!!") 

personalized_greeting("Richard", "COMP 170")
personalized_greeting("Leo", "COMP 170")

print()


students = ["Omar", "Lula", "Enrique", "Arhub", "Ben", "Richard", "Heather"]
your_course = "COMP 170"

for name in students:
    personalized_greeting(name, your_course)