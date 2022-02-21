import pygame


class Card:
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


    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def get_card_value(card):
        if card in Card.card_ace:
            return 11
        elif card in Card.card_2:
            return 2
        elif card in Card.card_3:
            return 3
        elif card in Card.card_4:
            return 4
        elif card in Card.card_5:
            return 5
        elif card in Card.card_6:
            return 6
        elif card in Card.card_7:
            return 7
        elif card in Card.card_8:
            return 8
        elif card in Card.card_9:
            return 9
        elif card in Card.card_10:
            return 10
        else:
            print("get card value broke")
