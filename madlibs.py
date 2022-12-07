# Mad Libs - A player in the word game Mad Libs asks another player for a list of
# words to fill in the blanks in a story. When the resulting story is read aloud,
# the word substitutions have a humorous effect. Mad Libs is a play on ad lib,
# from the Latin ad libitum, which means as you wish.

# Author: Alliyson Bonner
# Github: https://github.com/alliysonbonner
# Linkedin: https://www.linkedin.com/in/alliyson-bonner-6404976b/
# Email: alliyson.bonner@gmail.com
# Date: December 07 2022

# Prompt user for input and assign varibles
adjective1 = input("Adjective: ")
adjective2 = input("Adjective: ")
adjective3 = input("Adjective: ")
noun1 = input("Noun: ")
adjective4 = input("Adjective: ")
noun2 = input("Noun: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
adjective5 = input("Adjective: ")
noun3 = input("Noun: ")
verb3 = input("Verb: ")
noun4 = input("Noun: ")
verb4 = input("Verb: ")
adjective6 = input("Adjective: ")

# Construct madlib string
madlib = f"I walk through the color jungle. I take out my {adjective1} canteen. \
There's a {adjective2} parrot with a {adjective3} {noun1} in his mouth right \
there in front of me {adjective4} {noun2}. A sudden sound awakes me from my \
daydream! A panther's {verb1} in front of my head! I {verb2} his {adjective5} \
breath. I remember I have a packet of {noun3} that makes me go into a deep \
slumber! I {verb3} it away from me in front of the {noun4}. Yes he's eating it! \
I {verb4} away through the {adjective6} jungle. I meet my parents at the tent. \
Phew! It’s been an exciting day in the jungle."

# Output madlib statement
print("\n" + madlib)




