import random
# Function to deal a card
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Function to calculate score
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Function to compare scores
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Computer wins with a Blackjack 😱"
    elif user_score == 0:
        return "You win with a Blackjack 🎉"
    elif user_score > 21:
        return "You went over. Computer wins 😭"
    elif computer_score > 21:
        return "Computer went over. You win 🎉"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lost 😢"

# Function to play a game
def play_game():
    print(logo)
    
    user_cards = []
    computer_cards = []
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            another_card = input("Type 'y' to get another card, 'n' to pass: ")
            if another_card == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    # Computer's turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Main game loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()

