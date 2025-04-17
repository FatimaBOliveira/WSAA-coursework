# Draw cards
# This program uses an API that simulates a draw of a deck of cards.
# First, it shuffles, then it picks 5 cards, indicating the value and suit of each card.
# It also indicates if there's any combination: pair, triple, straight or flush.
# For a detailed walkthrough, please check this section in the README file: https://github.com/FatimaBOliveira/WSAA-coursework/tree/main/assignments#the-card-draw-assignment2-carddrawpy
# Author: Fatima Oliveira

# Import library
import requests

# URL to generate the deck of cards.
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

# Shuffle the deck of cards.
response = requests.get(url)

# Get the response in JSON.
deck=response.json()

# ID of the deck of cards.
id = deck["deck_id"]

# Url that uses the deck id above and draws 5 cards.
url_2 = f"https://deckofcardsapi.com/api/deck/{id}/draw/?count=5"

# Draw the cards.
response_2 = requests.get(url_2)

# Get the results with json.
hand=response_2.json()

# Cards picked.
cards=hand["cards"]

# Get the value and suit for each card.
print(f"The cards drawn are:")
for card in cards:
    print(f"- {card["value"]} of {card["suit"]}")

# Function that checks if the user has drawn a pair, triple, straight, or all of the same suit.
def check_hand(cards):
    # Values of the cards.
    values = [card["value"] for card in cards]

    # Suit of the cards
    suits = [card["suit"] for card in cards]

    # Attribute number value for all values.
    value_card = {"ACE": 14, "KING": 13, "QUEEN": 12, "JACK": 11,
              "10": 10, "9": 9, "8": 8, "7": 7, "6": 6,
              "5": 5, "4": 4, "3": 3, "2": 2}
    
    # Sequence of values.
    for count, value in enumerate(values):
        if value in value_card:
            values[count] = value_card[value]
        else:
            values[count] = int(value)
    
    # Check for pairs and triples.
    value_counts = {}
    for value in values:
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1

    # Show the pair or triple.
    pair = []
    triple = []
    for key in value_counts:
        if value_counts[key] == 2:
            pair.append(key)
            print("Great, you have a pair.")
        elif value_counts[key] == 3:
            triple.append(key)
            print("Very good, you have a triple.")
    
    # Check for straight.
    values = sorted(values)
    count = 0
    while count < len(values) - 1:
        if values[count] + 1 != values[count + 1]:
            straight = False
            break
        count += 1
    else:
        straight = True
        print("Superb, you have a straight.")

    # Check for flush, all same suit.
    suit_counts = {}
    for suit in suits:
        if suit in suit_counts:
            suit_counts[suit] += 1
        else:
            suit_counts[suit] = 1
    
    # Confirm flush.
    flush = len(suit_counts) == 1
    if flush:
        print("Congratulations, you have a flush!")
    
    # Print final result.
    return {
        "Pair": pair,
        "Triple": triple,
        "Straight": straight,
        "Flush": flush
        }

# Check the result of the cards taken.
result = check_hand(cards)

# Print the results.
print("Results:", result)