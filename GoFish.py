import random

deck = {"A" : 4, "2" : 4, "3" : 4, "4" : 4, "5" : 4, "6" : 4, "7" : 4, "8" : 4, "9" : 4, "10" : 4, "J" : 4, "Q" : 4,"K" : 4}

PlayActualGame = True

def add_line(cards):
  line_str = ""
  for card in cards:
    line_str += card + " "
  line_str += "\n"
  return line_str

def deck_size():
  d_size = 0
  for num in deck.values():
    d_size += num
  return str(d_size)

def hidden(cards):
  line_str = ""
  for card in cards:
    line_str += "X "
  line_str += "\n"
  return line_str

def display(computer_hand, computer_table, player_hand, player_table):
  #displays the current board
  display_str = "Computer hand: \n"
  if PlayActualGame == True:
    display_str += hidden(computer_hand)
    display_str += add_line(computer_table)
  else:
    display_str += add_line(computer_hand)
    display_str += add_line(computer_table)
  display_str += "[" + deck_size() + "]"
  display_str += "\n\n"
  display_str += "Your hand: "
  display_str += add_line(player_table)
  display_str += add_line(player_hand)
  print(display_str)

def draw_card():
  ##currently_available represents the cards from the deck
  ##that are not in player 1 or player 2's possession
  currently_available = []
  #loop through every key in the dictionary
  for card in deck:
    #loop as many times as a card is present in the dictionary
    for y in range(deck[card]):
      #append the card to the available cards
      currently_available.append(card)
      #have the card chosen be a random choice from the currently available list
  card = random.choice(currently_available)
  #subtract 1 from the value of the key of the card chosen
  deck[card] -= 1
  #return the random card
  return card

def deal():

  # make an empty list for player 1
  player1 = []
  #loop 5 times and use the draw card function to get 5 random cards and then append them to player 1
  for i in range(5):
    x = draw_card()
    player1.append(x)

   #loop 5 times and use the draw card function to get 5 random cards and then append them to player 2
  player2 = []
  for i in range(5):
    x = draw_card()
    player2.append(x)
  #return the player 1 and player 2 lists
  return [player1 , player2]

def reset_deck():
  ##resets the deck back to its original order
    # Iterate through each key in the deck dictionary
  for x in deck:
        # Set the value of the current key to 4
        deck[x] = 4

def check_for_match(player_hand, player_table):
  # make an empty dictionary to store the number of times each card is in the hand
  counter = {}
  # loop through player hand
  for i in player_hand:
    #if the card is in player hand, increase the value of that card in the dictionary by 1
    if i not in counter:
      counter[i] = 1
    else:
      counter[i] += 1

  # loop through each card in the counter
  for x in counter:
    #check if the card is in the counter 4 times
    if counter[x] == 4:
      #if it is, append it to the player table and remove it from the player hand 4 times
      player_table.append(x)
      player_hand.remove(x)
      player_hand.remove(x)
      player_hand.remove(x)
      player_hand.remove(x)

def check_for_win(player_table, autoplayer_table):
  #check if the combined total of player and autoplayer table is 13(All of the different cards)
  if (len(player_table) + len(autoplayer_table) >= 13):

    #if player table has more than 6 cards, they won so return true
    if len(player_table) > 6:
      return True

    #if autoplayer table has more than 6 cards, they won so return true
    if len(autoplayer_table) > 6:
      return True
    #return false if neither condition is met
    return False

  else:
    #return false if combined total is not 13
    return False

def autoplay(computer_hand):
  """The computer's algorithm for selecting the card to ask for during their turn"""
  if not computer_hand:
        # if hand is empty, draw card and pick that number
        new_card = draw_card()
        computer_hand.append(new_card)
        print("Computer hand is empty, picked up: " , new_card)
        return new_card

  else:
        # if there is a choice, pick based on strategy
        card = pick_from_choices(computer_hand)
        return card


def count_occurrences(hand):
    # counting occurrences in the hand using dictionary
    counts = {} # empty dictionary
    for card in hand: #go through the cards of the hand 1 by 1
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1
    return counts

def pick_from_choices(hand):

    # count occurrences of each number in the hand
    counts = count_occurrences(hand) #uses the count occurences function to make variable with frequencies of each number in the hand
    mostCopies = [] #empty dictionary
    list_keys = counts.keys() #making a list of all the keys in the dictionary

    #If the list of cards in the hand is one, then return that card
    if len(list_keys) == 1:
      for card in counts:
        firstCard = card
        break #want to end the loop as we only want the first card
      return firstCard

    #find the key(s) with the most copies in the hand
    #getting the first card and saving it in a variable
    for card in counts:
      max = card
      break

    #find the card with the max number of instances
    for card in counts:
      if counts[card] > counts[max]:
        max = card

    #appends all the cards with the same number of copies as the card with the most copies to the mostCopies list
    for card in counts:
      if counts[card] == counts[max]:
        mostCopies.append(card)

    #random choice of cards with max instances in hand
    return random.choice(mostCopies)

def main():
    """
    The main part of the game: resetting deck, dealing and execution
    """

    # Make deck
    reset_deck()

    # Deal 5 cards to all
    player_hand, computer_hand = deal()

    #create the player and auto player tables
    player_table = []
    computer_table = []
    # Choose a player to start the game off
    current_player = random.choice(["Human player","autoplayer"])
    #print who the current player is
    print(current_player , " is going first")

    #make variables for the winner and the looper
    winner = ""
    looper = 1
    #start the while loop
    while looper == 1:
      #if current player is the autoplayer, have the computer guess call the autoplayer function to get a card to call
      if current_player == "autoplayer":
        computer_guess = autoplay(computer_hand)
        #if the guess is in the player's hand
        if computer_guess in player_hand:
          #count how many times the player has that card
          count = 0
          for card in player_hand:
            if card == computer_guess:
              count +=1
          #append the card to the computer hand and remove it from the player hand as many times as the card appears in the player's hand
          for i in range(count):
            computer_hand.append(computer_guess)
            player_hand.remove(computer_guess)
          #run the check for match and check for win functions to see if any new matches are created and if the game is over
          check_for_match(computer_hand,computer_table)
          winCheck = check_for_win(player_table,computer_table)
          #if check for win is true, end the loop
          if winCheck == True:
            looper = 0

        #if the guess is not in the player hand
        elif computer_guess not in player_hand:
          #have the computer draw a card and append it to their hand
          new_card = draw_card()
          computer_hand.append(new_card)
          #check if the new card is what the player guessed
          if new_card == computer_guess:
            #run the check for match and check for win functions to see if any new matches are created and if the game is over
            check_for_match(computer_hand,computer_table)
            winCheck = check_for_win(player_table,computer_table)
            #if check for win is true, end the loop
            if winCheck == True:
              looper = 0

          else:
            #run the check for match and check for win functions to see if any new matches are created and if the game is over
            check_for_match(computer_hand,computer_table)
            winCheck = check_for_win(player_table,computer_table)
            #if check for win is true, end the loop
            if winCheck == True:
              looper = 0
            #set the current player to the human player since the card was not a match for the computer guess
            current_player = "Human player"



    #gameplay if player is the current player
      #check if the current player is the human
      if current_player == "Human player":
        #call the display function so the human can see everything on the table and their hand
        display(computer_hand,computer_table,player_hand,player_table)
        #ask the player what card they want to ask for and store it in player_guess
        player_guess = input("What number do you want to ask for? ")
        #check if the player hand is empty
        if len(player_hand) == 0:
          #if it is empty, let the player know it is empty
          print("Your hand is empty, so you had to draw a card")
          #have the player_guess be a new drawn card
          player_guess = draw_card()
          #append the card to the player hand
          player_hand.append(player_guess)

        #if the player guess is in the computer's hand
        if player_guess in computer_hand:
          print("Computer has that card!")
          #count how many times the computer has that card
          count = 0
          for card in computer_hand:
            if card == player_guess:
              count +=1
          #append the card to the player hand and remove it from the computer hand as many times as the card appears in the computer's hand
          for i in range(count):
              player_hand.append(player_guess)
              computer_hand.remove(player_guess)
         #run the check for match and check for win functions to see if any new matches are created and if the game is over
          check_for_match(player_hand,player_table)
          display(computer_hand, computer_table, player_hand, player_table)
          winCheck = check_for_win(player_table,computer_table)
          #if check for win is true, end the loop
          if winCheck == True:
            looper = 0

        #if the guess is not in the computer hand
        elif player_guess not in computer_hand:
          print("computer does not have that card, you must draw a card from the deck")
          #have the player draw a card and append it to their hand
          new_card = draw_card()
          print("you drew " , new_card)
          player_hand.append(new_card)
          #check if the new drawn card is equal to the player's guess
          if new_card == player_guess:
            #run the check for match and check for win functions to see if any new matches are created and if the game is over
            check_for_match(player_hand,player_table)
            display(computer_hand, computer_table, player_hand, player_table)
            winCheck = check_for_win(player_table,computer_table)
            #if check for win is true, end the loop
            if winCheck == True:
              looper = 0

          else:
            #run the check for match and check for win functions to see if any new matches are created and if the game is over
            check_for_match(player_hand,player_table)
            winCheck = check_for_win(player_table,computer_table)
            #if check for win is true, end the loop
            if winCheck == True:
              looper = 0
            #change the current player to autoplayer because the drawn card did not match the guess
            current_player = "autoplayer"

    if len(player_table) > 6:
      winner = "Player won, computer table: " , computer_table , "player table: " , player_table
    elif len(computer_table) > 6:

      winner = "Computer won, computer table: " , computer_table , "player table: " , player_table
    print(winner)

main()