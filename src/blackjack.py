import pygame
import random
import copy
import time

pygame.init()
# Load Images
bg_image = pygame.image.load("resources/casino_table_background.jpg")
score_bg_img = pygame.image.load("resources/casino_table_mini.jpg")


screen = pygame.display.set_mode((640, 480))

# icon = pygame.image.load('resources/icon.png')

cBack = pygame.image.load('resources/cards/cardback.png')
diamondA = pygame.image.load('resources/cards/ad.png')
clubA = pygame.image.load('resources/cards/ac.png')
heartA = pygame.image.load('resources/cards/ah.png')
spadeA = pygame.image.load('resources/cards/as.png')
diamond2 = pygame.image.load('resources/cards/2d.png')
club2 = pygame.image.load('resources/cards/2c.png')
heart2 = pygame.image.load('resources/cards/2h.png')
spade2 = pygame.image.load('resources/cards/2s.png')
diamond3 = pygame.image.load('resources/cards/3d.png')
club3 = pygame.image.load('resources/cards/3c.png')
heart3 = pygame.image.load('resources/cards/3h.png')
spade3 = pygame.image.load('resources/cards/3s.png')
diamond4 = pygame.image.load('resources/cards/4d.png')
club4 = pygame.image.load('resources/cards/4c.png')
heart4 = pygame.image.load('resources/cards/4h.png')
spade4 = pygame.image.load('resources/cards/4s.png')
diamond5 = pygame.image.load('resources/cards/5d.png')
club5 = pygame.image.load('resources/cards/5c.png')
heart5 = pygame.image.load('resources/cards/5h.png')
spade5 = pygame.image.load('resources/cards/5s.png')
diamond6 = pygame.image.load('resources/cards/6d.png')
club6 = pygame.image.load('resources/cards/6c.png')
heart6 = pygame.image.load('resources/cards/6h.png')
spade6 = pygame.image.load('resources/cards/6s.png')
diamond7 = pygame.image.load('resources/cards/7d.png')
club7 = pygame.image.load('resources/cards/7c.png')
heart7 = pygame.image.load('resources/cards/7h.png')
spade7 = pygame.image.load('resources/cards/7s.png')
diamond8 = pygame.image.load('resources/cards/8d.png')
club8 = pygame.image.load('resources/cards/8c.png')
heart8 = pygame.image.load('resources/cards/8h.png')
spade8 = pygame.image.load('resources/cards/8s.png')
diamond9 = pygame.image.load('resources/cards/9d.png')
club9 = pygame.image.load('resources/cards/9c.png')
heart9 = pygame.image.load('resources/cards/9h.png')
spade9 = pygame.image.load('resources/cards/9s.png')
diamond10 = pygame.image.load('resources/cards/10d.png')
club10 = pygame.image.load('resources/cards/10c.png')
heart10 = pygame.image.load('resources/cards/10h.png')
spade10 = pygame.image.load('resources/cards/10s.png')
diamondJ = pygame.image.load('resources/cards/jd.png')
clubJ = pygame.image.load('resources/cards/jc.png')
heartJ = pygame.image.load('resources/cards/jh.png')
spadeJ = pygame.image.load('resources/cards/js.png')
diamondQ = pygame.image.load('resources/cards/qd.png')
clubQ = pygame.image.load('resources/cards/qc.png')
heartQ = pygame.image.load('resources/cards/qh.png')
spadeQ = pygame.image.load('resources/cards/qs.png')
diamondK = pygame.image.load('resources/cards/kd.png')
clubK = pygame.image.load('resources/cards/kc.png')
heartK = pygame.image.load('resources/cards/kh.png')
spadeK = pygame.image.load('resources/cards/ks.png')

font = pygame.font.SysFont("arial", 60)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
DARK_GREEN = (25, 126, 30)

WIDTH = 640
HEIGHT = 480

# All the cards
card_deck = [diamondA, clubA, heartA, spadeA,
             diamond2, club2, heart2, spade2,
             diamond3, club3, heart3, spade3,
             diamond4, club4, heart4, spade4,
             diamond5, club5, heart5, spade5,
             diamond6, club6, heart6, spade6,
             diamond7, club7, heart7, spade7,
             diamond8, club8, heart8, spade8,
             diamond9, club9, heart9, spade9,
             diamond10, club10, heart10, spade10,
             diamondJ, clubJ, heartJ, spadeJ,
             diamondQ, clubQ, heartQ, spadeQ,
             diamondK, clubK, heartK, spadeK]

# Create array for each card value

card_ace = [diamondA, clubA, heartA, spadeA]
card_2 = [diamond2, club2, heart2, spade2]
card_3 = [diamond3, club3, heart3, spade3]
card_4 = [diamond4, club4, heart4, spade4]
card_5 = [diamond5, club5, heart5, spade5]
card_6 = [diamond6, club6, heart6, spade6]
card_7 = [diamond7, club7, heart7, spade7]
card_8 = [diamond8, club8, heart8, spade8]
card_9 = [diamond9, club9, heart9, spade9]

# Face cards are all worth 10
card_10 = [diamond10, club10, heart10, spade10,
           diamondJ, clubJ, heartJ, spadeJ,
           diamondQ, clubQ, heartQ, spadeQ,
           diamondK, clubK, heartK, spadeK]


def get_card_value(card):
    if card in card_ace:
        return 11
    elif card in card_2:
        return 2
    elif card in card_3:
        return 3
    elif card in card_4:
        return 4
    elif card in card_5:
        return 5
    elif card in card_6:
        return 6
    elif card in card_7:
        return 7
    elif card in card_8:
        return 8
    elif card in card_9:
        return 9
    elif card in card_10:
        return 10
    else:
        print("get card value broke")


def deal(card_deck, used_cards):
    # Initialize both hands
    user_hand, dealer_hand = [], []

    user_first_card = get_card(card_deck, used_cards)
    user_hand.append(user_first_card)
    used_cards.append(user_first_card)

    dealer_first_card = get_card(card_deck, used_cards)
    dealer_hand.append(dealer_first_card)
    used_cards.append(dealer_first_card)

    user_second_card = get_card(card_deck, used_cards)
    user_hand.append(user_second_card)
    used_cards.append(user_second_card)

    dealer_second_card = get_card(card_deck, used_cards)
    dealer_hand.append(dealer_second_card)
    used_cards.append(dealer_second_card)

    return user_hand, dealer_hand, used_cards


def get_hand_value(hand):
    hand_max = 0
    hand_min = 0

    for i in hand:
        hand_max += get_card_value(i)
        hand_min += get_card_value(i)
        if i in card_ace:
            hand_min -= 10
    return hand_max, hand_min


def get_card(card_deck, used_cards):
    # Generates a random card from cardDeck, removes it from card_deck, and appends it to used_cards.
    card = random.choice(card_deck)
    card_deck.remove(card)
    used_cards.append(card)

    return card


def hit(card_deck, used_cards, player):
    player.append(get_card(card_deck, used_cards))


def display_dealer_hand(dealer_hand, screen):
    # Display dealer's cards
    for card in dealer_hand:
        x_pos = 10 + dealer_hand.index(card) * 110
        screen.blit(card, (x_pos, 10))

        # Cover the dealer's second card
        screen.blit(cBack, (120, 10))


def display_user_hand(screen, user_hand):
    # displays player's cards
    for card in user_hand:
        x = 10 + user_hand.index(card) * 110
        screen.blit(card, (x, 330))


def display_user_score( user_total_max, user_total_min):
    # label = font.render(str(user_total_max), 1, WHITE)
    # screen.blit(label, (WIDTH - 100, HEIGHT - 110))

    score_img = font.render(str(user_total_max), True, BLACK)
    score_rect = score_img.get_rect(center=(WIDTH - 100, HEIGHT - 110))

    screen.blit(score_img, score_rect)


def is_game_over(dealer_hand, dealer_total_max, user_hand, user_total_max, user_total_min):
    if (user_total_min >= 21) or len(user_hand) == 5:
        return True
    if len(user_hand) == 2 and user_total_max == 21:
        return True
    elif len(dealer_hand) == 2 and dealer_total_max == 21:
        return True

    else:
        return False


def main():
    # Local Variable
    card_copy = copy.copy(card_deck)
    stand = False
    user_hand = []
    dealer_hand = []
    used_cards = []
    # winning_num = 0
    # losing_num = 0

    # Initialize Game
    pygame.init()
    pygame.display.set_caption('Blackjack')
    font = pygame.font.SysFont('arial', 15)

    score_bg = score_bg_img.get_rect(center=(400, HEIGHT - 130))
    # Set background
    screen.blit(bg_image, (0, 0))

    # Create text for buttons
    hit_text = font.render('Hit', 1, BLACK)
    stand_text = font.render('Stand', 1, BLACK)
    restart_text = font.render('Restart', 1, BLACK)
    game_over_text = font.render('GAME OVER', 1, WHITE)

    hit_button, stand_button = create_hit_and_stand_buttons(hit_text, screen, stand_text)

    user_hand, dealer_hand, used_cards = deal(card_copy, used_cards)

    user_total_max, user_total_min = get_hand_value(user_hand)
    print('User: %i' % user_total_max)
    dealer_total_max, dealer_total_min = get_hand_value(dealer_hand)

    game_over = False

    # Game Loop
    while True:
        game_over = is_game_over(dealer_hand, dealer_total_max, user_hand, user_total_max, user_total_min)
        display_user_score(user_total_max, user_total_min)

        first_hit = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()

            # player hits
            elif event.type == pygame.MOUSEBUTTONDOWN and not (game_over or stand) and hit_button.collidepoint(
                    pygame.mouse.get_pos()):
                hit(card_copy, used_cards, user_hand)
                user_total_max, user_total_min = get_hand_value(user_hand)
                if first_hit:
                    screen.blit(bg_image, score_bg)

                display_user_score(user_total_max, user_total_min)

                display_user_score(user_total_max, user_total_min)
                print('User: %i' % user_total_max)


            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over and stand_button.collidepoint(
                    pygame.mouse.get_pos()):
                # when player stands, the dealer plays
                time.sleep(0.5)
                stand = True
                screen.blit(dealer_hand[1], (120, 10))
                print('Dealer: %i' % dealer_total_max)
                while dealer_total_max <= user_total_max and dealer_total_max < 17:
                    print('Dealer: %i' % dealer_total_max)

                    hit(card_copy, used_cards, dealer_hand)
                    time.sleep(0.5)
                    display_dealer_hand(dealer_hand, screen)

                    dealer_total_max, dealer_total_min = get_hand_value(dealer_hand)

                    print('Dealer: %i' % dealer_total_max)

            elif event.type == pygame.MOUSEBUTTONDOWN and (game_over or stand) and restart_button.collidepoint(
                    pygame.mouse.get_pos()):
                # restarts the game, updating scores
                # TODO win/loss stats
                game_over = False
                stand = False
                user_hand = []
                dealer_hand = []
                card_copy = copy.copy(card_deck)
                user_hand, dealer_hand, used_cards = deal(card_copy, used_cards)

                user_total_max, user_total_min = get_hand_value(user_hand)
                print('User: %i' % user_total_max)
                dealer_total_max, dealer_total_min = get_hand_value(dealer_hand)

                screen.blit(bg_image, (0, 0))

                # Draw Buttons again
                hit_button, stand_button = create_hit_and_stand_buttons(hit_text, screen, stand_text)

        # screen.blit(winTxt, (565, 423))
        # screen.blit(loseTxt, (565, 448))

        display_dealer_hand(dealer_hand, screen)

        display_user_hand(screen, user_hand)


        # when game is over, draws restart button and text, and shows the dealer's second card
        if game_over or stand:
            screen.blit(game_over_text, (270, 200))
            restart_button = pygame.draw.rect(screen, GRAY, (270, 225, 75, 25))
            screen.blit(restart_text, (287, 228))
            screen.blit(dealer_hand[1], (120, 10))

        pygame.display.update()


def create_hit_and_stand_buttons(hit_text, screen, stand_text):
    # Draw buttons
    hit_button = pygame.draw.rect(screen, GRAY, (510, 190, 75, 25))
    stand_button = pygame.draw.rect(screen, GRAY, (510, 240, 75, 25))
    # ratio_button = pygame.draw.rect(screen, GRAY, (555, 420, 75, 50))
    # Write text on buttons
    screen.blit(hit_text, (538, 193))
    screen.blit(stand_text, (531, 243))
    return hit_button, stand_button


if __name__ == '__main__':
    main()
