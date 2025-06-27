import random

# Cartes et valeurs
suits = ['♠', '♥', '♦', '♣']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def deal_card():
    return (random.choice(cards), random.choice(suits))

def calculate_score(hand):
    score = 0
    aces = 0
    for card, _ in hand:
        score += values[card]
        if card == 'A':
            aces += 1
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

def display_cards(hand):
    top = ""
    mid = ""
    bot = ""
    for rank, suit in hand:
        space = " " if len(rank) == 1 else ""
        top += f" _____  "
        mid += f"|{rank}{space}   | "
        bot += f"|  {suit}  | "
    base = "¯¯¯¯¯  " * len(hand)
    print(top)
    print(mid)
    print(bot)
    print(base)

def display_cards_hidden(hand):
    top = " _____  "
    mid = "|░░░░░| "
    bot = "|░░░░░| "
    base = "¯¯¯¯¯  "

    rank, suit = hand[1]
    space = " " if len(rank) == 1 else ""
    top += f" _____  "
    mid += f"|{rank}{space}   | "
    bot += f"|  {suit}  | "
    base += "¯¯¯¯¯  "

    print(top)
    print(mid)
    print(bot)
    print(base)

def show_hand(name, hand, hide_first=False):
    print(f"{name}:")
    if hide_first:
        display_cards_hidden(hand)
    else:
        display_cards(hand)
    if not hide_first:
        print(f"Total: {calculate_score(hand)}\n")

def play_blackjack(balance):
    print("\n--- Nouvelle partie de Blackjack ---")
    print(f"Solde actuel : {balance}€")

    # Mise
    while True:
        try:
            bet = int(input("Combien voulez-vous miser ? "))
            if bet <= 0 or bet > balance:
                print("Mise invalide.")
            else:
                break
        except ValueError:
            print("ntrez un nombre entier.")

    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    show_hand("Joueur", player_hand)
    show_hand("Croupier", dealer_hand, hide_first=True)

    # Tour du joueur
    while calculate_score(player_hand) < 21:
        choice = input("Tirer une carte ? (o/n) : ").lower()
        if choice == 'o':
            player_hand.append(deal_card())
            show_hand("Joueur", player_hand)
        else:
            break

    player_score = calculate_score(player_hand)
    if player_score > 21:
        print("Vous avez dépassé 21 ! Perdu.")
        return balance - bet

    # Tour du croupier
    print("\nTour du croupier...")
    show_hand("Croupier", dealer_hand)
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deal_card())
        show_hand("Croupier", dealer_hand)

    dealer_score = calculate_score(dealer_hand)

    print("\nRésultat final :")
    show_hand("Joueur", player_hand)
    show_hand("Croupier", dealer_hand)

    if dealer_score > 21 or player_score > dealer_score:
        print("Vous gagnez !")
        return balance + bet
    elif player_score < dealer_score:
        print("Le croupier gagne.")
        return balance - bet
    else:
        print("Égalité.")
        return balance  # mise remboursée

def main():
    balance = 1000
    while True:
        if balance <= 0:
            print("Vous n’avez plus d’argent...")
            break

        balance = play_blackjack(balance)
        print(f"Nouveau solde : {balance}€")

        if balance <= 0:
            print("Vous n’avez plus d’argent...")
            break

        again = input("Rejouer ? (o/n) : ").lower()
        if again != 'o':
            break

    print("Fin du jeu. Merci d’avoir joué !")

if __name__ == "__main__":
    main()
