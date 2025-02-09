# Draw cards
# This program will use an API that simulates a draw of a deck of cards.
# First, it shuffles, then it picks 5 cards indicating the value and suit of each card.
# Author: Fatima Oliveira

# Import libraries.
import requests
import json

# URL to generate the deck of cards.
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

# Shuffle the deck of cards.
response = requests.get(url)

# Get the result with json.
#print(response.json())
deck=response.json()

# ID of the deck of cards.
id = deck["deck_id"]
#print(id)

# Url that uses the deck id above and draws 5 cards.
url_2 = f"https://deckofcardsapi.com/api/deck/{id}/draw/?count=5"

# Draw the cards.
response_2 = requests.get(url_2)

# Get the results with json.
deck_id=response_2.json()
#print(deck_id)

# Cards picked.
cards=deck_id["cards"]

# Get the value and suit for each card.
print(f"The cards drawn are:")
for card in cards:
    print(f"- {card["value"]} of {card["suit"]}")