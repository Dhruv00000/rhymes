# Importing the necessary function from the module.
from requests import get

# Getting the user input.
word = input("Enter the word or phrase you want to find the rhyming words of: ").lower()

try:

    maximum = int(input("Enter the maximum number of rhyming words you want: "))

# If the user enters a string instead of an integer, this message is printed out instead of the program crashing with an error.
except ValueError:

    print("Please enter a valid value.")

if maximum > 0:

    # Getting the json response from the api.
    response = get(f"https://api.datamuse.com/words?rel_rhy={word}&max={maximum}")

    if len(response.json()) > 0:

        # Output.
        print("The rhyming words are-:\n")

        for output in response.json():

            print(f"\t{output['word']}")

    # If no rhyming words are found for the word/phrase that the user entered, this message is printed out instead of the program terminating.
    else:

        print("No rhyming words found.")

# If the user doesnt enter a natural number, this message is printed out instead of the program terminating.
else:

    print("Please enter a valid value.")