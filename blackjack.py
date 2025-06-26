import random

# Cartes et valeurs
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def calculate_score(hand):
    score = sum(values[card] for card in hand)
    # Ajustement pour les As
    aces = hand.count('A')
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

def deal_card():
    return random.choice(cards)

def show_hand(name, hand, hide_first=False):
    if hide_first:
        print(f"{name}: ['??'] + {hand[1:]}")
    else:
        print(f"{name}: {hand} (Total: {calculate_score(hand)})")

def play_blackjack():
    print("Bienvenue au Blackjack !\n")

    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    # Afficher les mains
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
        return

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
    elif player_score < dealer_score:
        print("Le croupier gagne.")
    else:
        print("Égalité.")

if __name__ == "__main__":
    play_blackjack()
