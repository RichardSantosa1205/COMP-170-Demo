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

# May 28 Code
result = ( 3 > 4)
if (not result):
    print("Math is terribe")
else:
    print("Math is good")

# June 2 Code
# Functions, booleans, lists, and dictionaries

def form_letter(recipient, promise):
    """Prints a form letter for an aspiring local politician, thanking their voters
    and promising things.

    Inputs
    ------
    recipient : string
      The name of the voter the letter is sent to
    promise : string
      The promise to the voter
    """
    print("Dear " + recipient + ",")
    print("Thank you for voting for me.")
    print("I promise to ")
    print(promise)
    print()

# Simplistic dictionary to demonstrate the concept. Using first names as keys in 
# a dictionary is not a good idea. Keys must be unique and names are not. There 
# are two voters with the same name below, but only one of them will receive a
# form letter -- the most recent one with the same name.

my_voters = {
    # KEY     : VALUE (or values)
    "Richard" : "build a park in your backyard",
    "Lula"    : "fix your sidewalk",
    "Ana"     : "call a friend in DC for a pardon",
    "Cesar"   : "add a bus stop in your living room",
    "Ana"     : "fix the potholes" 
}

# for every voter:
#   call the function form letter passing to it the
#   voter's and my most insincere promise to them.

for name, promise in my_voters.items():
    form_letter(name, promise)

# A better dictionary using objects -- this is advanced stuff and shown here
# as a reference and a goal for the course.

# Create an object for voters. Each voter is defined by personal information (name,
# address, and the promise made to them).
class Voter:
    def __init__(self, first_name, last_name, street_address, promise):
        self.first_name = first_name
        self.last_name = last_name
        self.street_address = street_address
        self.promise = promise

# Create a database of voter objects
my_better_voters = {
    "frodo@shire" : Voter("Frodo", "Baggins", "123 Underhill Lane", "destroy the ring"),
    "sam@shire" : Voter("Sam", "Gamgee", "5 Gardeners Rd", "cater your wedding"),
    "gandalf@istari" : Voter("Gandalf", "the Grey", "81 Wizard's Manor", "help you defeat Sauron"),
    "sam@ecthelion" : Voter("Sam", "Fidor", "201 Tower Av", "rebuild the city")
}

# Write a function to produce a form letter using a voter object as an input
def better_form_letter(voter):
    print()
    print(f"{voter.first_name} {voter.last_name}")
    print(f"{voter.street_address}")
    print(f"Gondor, Middle Earth")
    print("")
    print(f"Dear {voter.first_name}")
    print(f"Thank you for voting for me. I promise to\n{voter.promise}")
    print()
    print("Sincerely,")
    print("Lord Voldemort")

# Produce the letters by evaluating the voters dictionary, pulling one 
# voter object at a time and passing it to the form letter function.

for voter in my_better_voters.values():
    better_form_letter(voter)

# June 3 Code

def f(x: int) -> int:
    """Squares a given number.
    
    Input
    -----
    x : int
      number to square 
    
    Returns
    -------
    int
      the number squared
    """
    return x * x

# Simple print
print(f(5))

# Fancy print
x = 6
print(f"\nThe square of {x} is {f(x)}\n")

# June 4 Code

def f(x):
    return x*x

def h(x):
    return x*x-3

def is_even(n: int) -> bool:
    if n % 2 == 0:
        return True 
    else:
        return False

def is_even_compact(n: int) -> bool:
    return (n % 2) == 0

def is_odd_compact(n: int) -> bool:
    return not is_even_compact(n)
    # return (n % 2) == 1
    


import datetime

def show_date():
    print(f"today is {datetime.date.today()}")


def tell_me_if_even(n: int):
    if n%2 == 0:
        print(f"{n} is an even number")
    else:
        print(f"{n} is an odd number")

def tell_parity(n: int):
    # We get special dispensation to allow printing this time.
    ODD = "odd"
    EVEN = "even"
    if n%2 == 0:
        parity = EVEN
    else: 
        parity = ODD
    print(f"Number {n} is {parity}")

def tell_parity_compact(n: int):    
    ODD = "odd"
    EVEN = "even"
    # Ternary operator -- simple if statement in a single line
    parity = "even" if n%2==0 else "odd"
    print(f"The number {n} is {parity}")


def print_first_numbers_upto(n: int):
    for i in range(n):
        print(i, end = " ")

print_first_numbers_upto(10)

# June 9 Code
# Ask user about desired height
N = input("How tall should the tower be? ")
# Python's input returns the answer as a string; convert it to an integer number
N = int(N)
# Acknoledge the entry
print(f"Thank you. I'll parameterize the tower for {N} lines height.")

# The aspect ratio of the Sears Tower 1:6.45 based on Chicago Architectural 
# Foundation. In other words, the tower is 6.45 times taller than wide
ASPECT_RATIO = 6.45 

# The tower has actually four tiers but for simplicity we assume there are
# three tiers, each occupying the following proportons of the total height
BOTTOM_TIER_PROPORTION = 0.50 # based on actual
MIDDLE_TIER_PROPORTION = 0.35 # measurements and
TOP_TIER_PROPORTION = 0.15    # omitting one setback

# These are the setback transitions for the three tiers of our tower
BOTTOM_TO_MIDDLE_SETBACK = 0.75
MIDDLE_TO_TOP_SETBACK = 0.66

# Time to compute the dimensions for each block in the tower

# Bottom block

WIDTH_BOTTOM_TIER = N / ASPECT_RATIO # height/aspect ratio
HEIGHT_BOTTOM_TIER = N * BOTTOM_TIER_PROPORTION
print(f"\nThe bottom tier is {WIDTH_BOTTOM_TIER} characters wide and {HEIGHT_BOTTOM_TIER} lines tall")

# Middle block

WIDTH_MIDDLE_TIER = BOTTOM_TO_MIDDLE_SETBACK * WIDTH_BOTTOM_TIER 
HEIGHT_MIDDLE_TIER = N*MIDDLE_TIER_PROPORTION
print(f"\nThe middle tier is {WIDTH_MIDDLE_TIER} characters wide and {HEIGHT_MIDDLE_TIER} lines tall")

# Top block

WIDTH_TOP_TIER = MIDDLE_TO_TOP_SETBACK * WIDTH_MIDDLE_TIER
HEIGHT_TOP_TIER = N*TOP_TIER_PROPORTION
print(f"\nThe top tier is {WIDTH_TOP_TIER} characters wide and {HEIGHT_TOP_TIER} lines tall")

# June 10 code
# obtain height
N = int(input("\nHow many lines tall do you want the tower? "))
print()

# The aspect ratio of the Sears Tower 1:6.45 based on Chicago Architectural 
# Foundation. In other words, the tower is 6.45 times taller than wide
ASPECT_RATIO = 6.45 

# The tower has actually four tiers but for simplicity we assume there are
# three tiers, each occupying the following proportons of the total height
BOTTOM_TIER_PROPORTION = 0.50 # based on actual
MIDDLE_TIER_PROPORTION = 0.35 # measurements and
TOP_TIER_PROPORTION = 0.15    # omitting one setback

# These are the setback transitions for the three tiers of our tower
BOTTOM_TO_MIDDLE_SETBACK = 0.66
MIDDLE_TO_TOP_SETBACK = 0.75

# Compute the dimensions for bottom block
bottom_width = N / ASPECT_RATIO # height/aspect ratio
bottom_height = N * BOTTOM_TIER_PROPORTION

# Compute the dimensions for middle block
middle_width = BOTTOM_TO_MIDDLE_SETBACK * bottom_width
middle_height = N*MIDDLE_TIER_PROPORTION

# Compute the dimensions for top block
top_width = MIDDLE_TO_TOP_SETBACK * middle_width
top_height = N*TOP_TIER_PROPORTION

# June 11 Code
def counting_numbers(n):
    for i in range(n):
        print(i)
    print(f"these were the numbers from 0 to {n-1}")

counting_numbers(15)

# June 16 Code
# Same data as in JUN16-bad-code.py file, only neatly organized as a list
daily_highs = [75, 77, 68, 65, 71, 78, 73, 56, 66, 68, 65, 83, 84, 78]

def average(values: list[int]) -> int:
    """Basic function that averages the values in a given list
    
    Input
    -----
    values : list
      values to average - must be numeric data. Dear user, please please please
      make sure that the list is not empty.
    
    Returns
    -------
    The average of the values entered.
    """

    # initialize average to None
    avg = None
    
    if len(values) > 0:
        
      # Initialize the sum accumulator
      sum = 0
      
      # Iterate the list (traverse it one element at a time from beginning to end)
      # and add its values together.      ALTERNATIVELY, with ENHANCED-FOR loop:
      for i in range(len(values)):        # for val in values:
          sum = sum + values[i]           #     sum = sum + val

      # Loop completed, compute average by dividing sum computed in the loop with
      # the number of values -- that's the length of the array. This operation
      # can be risky. Why? 
      avg = sum / len(values)

    # Done. Return the average value
    return avg

# Simple demo
# average_daily_high = average(daily_highs)
# Plain printing
# print(average_daily_high)
# Fancy printing
# print(f"{average_daily_high:.1f}")


def find_min(values: list[int]) -> int:
    """Basic technique to find the smallest item in an list.
    
    Input
    -----
    values : list
      values to search - must be numeric data
    
    Returns
    -------
    The smallest of the values entered. 
    """
    # Assume that the first item in the list is the smallest
    smallest = values[0]

    # Check every remaining item in the list if they are smaller than the
    # smallest value. When a smaller item is found, update the smallest
    # value to match. Loop stars from second element [i=1]. Why?
    #
    for i in range(1, len(values)):  # also:  for val in values:
        if values[i] < smallest:     #          if val < smallest:
            smallest = values[i]     #            smallest = val
    
    # Done
    return smallest

def find_max(values: list[int]) -> int:
    """Basic technique to find the largest item in an list. 
    This method uses a WHILE loop to demonstreate its equivalence
    to an exhaustive FOR loop
    
    Input
    -----
    values : list
      values to search - must be numeric data
    
    Returns
    -------
    The largest of the values entered. 
    """
    # Assume that the first item in the list is the largest
    
    i = 0
    largest = values[i]

    # Check every remaining item in the list if they are smaller than the
    # largest value. When a smaller item is found, update the largest
    # value to match. Loop stars from second element [i=1]. Why?
    while i < len(values):
        if values[i] > largest:
            largest = values[i]
        i = i+1
    
    # Done
    return largest

def exists(value: int, values: list[int]) -> bool:
    """
    for i in range(len(values)):
        if values[i] == value:
            return True
    return False
    """
    # Assume that the item is not present in the array
    found = False
    for val in values:
        if val == value:
            found = True
            break
    return found

demo = [1,2,3]
print(find_max(demo))

# June 18 Code
# a simple string array

zoom_call = ["Kofi", "Leo", "Lula", "Lillie", "Elizabeth", "Emmanuel", "Ben", "Delaney", "Heather", "Omar"]

middle_of_array = len(zoom_call) // 2

print(middle_of_array)

print("Middle element of array: " + zoom_call[middle_of_array])

left_half = zoom_call[0:middle_of_array]
right_half = zoom_call[middle_of_array:len(zoom_call)]

print(f"{left_half=}")
print(f"{right_half=}")

simplified_left_half = zoom_call[:middle_of_array]
simplified_right_half = zoom_call[middle_of_array:]

print(f"{simplified_left_half=}\n{simplified_right_half=}")

# June 23 Code
def our_upper_case(word:str) -> str:
    result = None
    if len(word) > 0:
        result = ""
        for i in range(len(word)):
            current_character = word[i]
            # find the ascii value of the current character
            current_ascii = ord(current_character)
            # Subtract to bring to upper case
            new_ascii = current_ascii - 32
            # create a new symbol with this ascii code
            new_character = chr(new_ascii)
            # concatenate new char to the output string
            result = result + new_character
    # done
    return result

# quick demo
print(our_upper_case("Leo9"))

def our_upper_case(word:str) -> str:
    result = None
    if len(word) > 0:
        result = ""
        for i in range(len(word)):
            current_character = word[i]
            # find the ascii value of the current character
            current_ascii = ord(current_character)
            # Is this ascci value a letter? Is it between a-thru-z

            if current_ascii >= ord('a') and current_ascii <= ord('z'):
                # Subtract to bring to upper case
                new_ascii = current_ascii - 32
                # create a new symbol with this ascii code
                new_character = chr(new_ascii)
            else:
                new_character = current_character
                
            # concatenate new char to the output string
            result = result + new_character
    # done
    return result

# quick demo
print(our_upper_case("leo 1967"))

#June 30 Code
# example with full path to file

with open("/workspaces/comp-170-su25-live-coding/demo_data/text_file.txt", "r") as leo_masterpiece:
    opening_from = leo_masterpiece.read()
    print(opening_from) # OK, maybe William Shakespeare helped a bit too.

# Same but better organized ... this time it counts lines instead of just printing them

path_to_file = "/workspaces/comp-170-su25-live-coding/demo_data/"
file_name =  "text_file.txt"
line_count = 0
with open(path_to_file + file_name) as richard3:
    for line in richard3:
        line_count += 1 
print(f"\n\nThere are {line_count} line(s) in file {file_name}.\n")

# Try a file in the same folder as our program
path_to_file = "./" # File system speak for "same folder"
file_name =  "README.md"
with open(path_to_file + file_name) as local_file:
    contents_of_local_file = local_file.read()
    print(f"\n\nContents of {file_name}:\n\n{contents_of_local_file}\n")

# July 1 Code
import requests

book_url = "https://www.gutenberg.org/cache/epub/98/pg98.txt"

# Establish connection to website

connection = requests.get(book_url, stream=True)

line_counter = 0
word_count = 0
for line in connection.iter_lines():
    if line:
        line_counter += 1
        word_count += len(line.split())

print(f"There are {line_counter:,d} lines in the book")
print(f"THere are {word_count:,d} words.")



some_words = ["it", "was", "a", "dark", "and", "stormy", "night"]
char_count = 0
for word in some_words:
    char_count += len(word)
print(char_count)

# Where to find the file
path_to_file = "/workspaces/comp-170-su25-live-coding/data/"
file_name = "temperatures.txt" \

# initialize accumulator
temperature_average = 0
count = 0
# connect to the file
with open(path_to_file+file_name, "r") as our_data_file:
    for line in our_data_file:
        temperature = int(line)
        temperature_average += temperature
        count += 1

# Compute average and return
temperature_average /= count
print(f"\nThe temperature over a period of {count} days is {temperature_average:.2f}\n")

outliar_margin = 0.33
with open(path_to_file+file_name) as our_data_file:
    for line in our_data_file:
        value = float(line)
        if value < temperature_average*(1-outliar_margin) or value > temperature_average*(1+outliar_margin):
            print(f"\nOutliar: {value}")

# July 2 Code
import requests

book_url = "https://www.gutenberg.org/cache/epub/98/pg98.txt"

# Establish connection to PG webserver
connection = requests.get(book_url)
# Initialize a dictionary to count word frequencies
frequency_of = dict()

for text_line in connection.iter_lines():
    # make sure line is not empty
    if text_line:
        text_line = text_line.decode('utf-8')
        words = text_line.split()
        for word in words:
            # Ask if this word is in the dictionary
            if word in frequency_of:
                frequency_of[word] = frequency_of[word] + 1
            else:
                frequency_of[word] = 1

print(f"\n\nThere are {len(frequency_of):,d} words in the book\n")

highest_frequency = 0
most_frequent_word = ""
# iterate over the dictionary, obtaining its key-value pairs, one at a time
for word, count in frequency_of.items():
    if count > highest_frequency:
        highest_frequency = count
        most_frequent_word = word
    if count == 1:
        print(f"\nunique word: {word}")

print(f"\n{most_frequent_word=} with {highest_frequency=}\n")

# Object Oriented Programing

#Animal
class Animal:

    def __init__(self, species, color:str, weight:int, fur:bool=True, mammal:bool=True, vocalization:str=""):
        self.species = species 
        self.color = color
        self.weight = weight
        self.fur = fur
        self.mammal = mammal
        self.vocalization = vocalization

    def animal_says(self):
        print(f"I am a {self.species} and I say: {self.vocalization}")

#Bird
class Bird:
    
    def __init__(self, color):
        self.color = color
    
    def bird_say(self):
        print("chirp")

#Cat
class Cat:

    def __init__(self, color):
        self.color = color
    
    def cat_says(self):
        print("meow")

#Dog
from Animal import Animal

class Dog(Animal):
    pass
    

milo = Dog("dog", "chocolate", 45, True, True, "woof")

milo.animal_says()

#Goat
class Goat:
    
    def __init__(self, color):
        self.color = color
    
    def goat_says(self):
        print("bah")

#Gold Fish
class GoldFish:

    def __init__(self, color):
        self.color = color

    def goldfish_says(self):
        print()

#Person
from datetime import date

class Person:

    # define state: what are the variables of the object
    # The best way to show an object's variables (aka attributes or fields)
    # is to show how an object is instantiated.
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._ssn = -1 # private please
        self._dob = None

    # define behavior: what are the method the object offers?
    def introduce(self):
        print(f"\nHello, my name is {self.first_name} and I am {self.get_age()} years old.")

    def set_ssn(self, ssn: int) -> None:
        # simple rule: SSNs cannot have all-0s in any of their parts. For example,
        # 000-GG-SSSS, AAA-00-SSSS, and AAA-GG-0000 are illegal values. The method
        # should not allow such values. If SSN security number is to be represented
        # as an integer, then 000-GG-SSSS becomes GGS,SSS whose greatest value is
        # 999,999. So any SSN has to have an int value > 999,999, etc. We wont 
        # worry about the other restrictions for now because, really, SSN, should be
        # an object itself, not an int variable.
        if ssn < 1_000_000:
            raise ValueError("SSN cannot start with 000")
        else:
            self._ssn = ssn
    
    
    def set_dob(self, year, month, day):
        self._dob = date(year, month, day)
    
    def get_age(self):
        age = -1
        if self._dob:
            today = date.today()
            age = today.year-self._dob.year
            if (today.month, today.day) < (self._dob.month, self._dob.day):
                age -= 1
        return age
    
    def get_name(self):
        return self.first_name
    
    def __str__(self):
        return f"[ {self.first_name} {self.last_name}]"
    
    def __lt__(self, other):
        return self.get_age() < other.get_age()
    #def __gt__(self, other):
    #    return self.get_age() > other.get_age()

#Implement_Person
from Person import Person

persons = list()

a_hobit = (Person("Frodo", "Baggins"))
another_hobbit = (Person("Bilbo", "Baggins"))
bad_wizard = (Person("Saruman", "the White"))
good_wizard = (Person("Gandal", "the Gray"))

a_hobit.set_dob(1900, 1, 1)
another_hobbit.set_dob(1800, 1, 1)
bad_wizard.set_dob(1200, 1, 1)
good_wizard.set_dob(1200, 2, 2)

if good_wizard == bad_wizard:
    print(f"{good_wizard.get_name()} is same age as {bad_wizard.get_name()}")

#Sorting
def naive_sorting(our_data: list[int]):
    # Consider a progressively decreasing version of
    # our input array
    for end in range(len(our_data), 1, -1):
        # Find the largest element in this version of the array
        # Assume largest is the first element
        largest = 0
        for i in range(1, end):
            if our_data[i] > our_data[largest]:
                largest = i
        # When the loop ends, largest points to the largest
        # element in range 0...end-1. Place the largest element
        # at position end-1 and whatever was at position end-1
        # at position largest
        temp = our_data[largest]
        our_data[largest] = our_data[end - 1]
        our_data[end - 1] = temp
    return our_data

#  test
demo = [9,4,3,8,7,1,6,2]
print(naive_sorting(demo))

