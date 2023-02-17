def get_input(prompt: str) -> str:
    """Prompt the user for input and return the input as a string.

    Args:
        prompt: A string representing the input prompt.

    Returns:
        A string representing the user's input.
    """
    return input(prompt + ": ")


# Prompt the user for input and assign variables using the get_input function
adjectives = [get_input("Adjective") for _ in range(6)]
nouns = [get_input("Noun") for _ in range(4)]
verbs = [get_input("Verb") for _ in range(4)]

# Construct madlib string using f-strings
madlib = f"I walk through the color jungle. I take out my {adjectives[0]} canteen. \
There's a {adjectives[1]} parrot with a {adjectives[2]} {nouns[0]} in his mouth right \
there in front of me {adjectives[3]} {nouns[1]}. A sudden sound awakes me from my \
daydream! A panther's {verbs[0]} in front of my head! I {verbs[1]} his {adjectives[4]} \
breath. I remember I have a packet of {nouns[2]} that makes me go into a deep \
slumber! I {verbs[2]} it away from me in front of the {nouns[3]}. Yes he's eating it! \
I {verbs[3]} away through the {adjectives[5]} jungle. I meet my parents at the tent. \
Phew! It’s been an exciting day in the jungle."

# Output madlib statement
print("\n" + madlib)
