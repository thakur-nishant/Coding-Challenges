import functools


class Card(object):
    def __init__(self, cardstring):
        self._cardstring = cardstring
        self._rank = cardstring[0]
        self._suit = cardstring[1]

    @property
    def rank(self):
        return self._rank

    def suit(self):
        return self._suit

    def _str_(self):
        return str(self._cardstring)

    def get_rank_value(self):
        rank_value_map = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14
        };

        return rank_value_map[self._rank]


class PokerHand(object):
    def __init__(self, card_string_array):
        def to_card(c):
            return Card(c)

        self._cards = map(to_card, card_string_array)
        self.sort_by_rank();

    def sort_by_rank(self):
        def compare_cards(c1, c2):
            return c1.get_rank_value() - c2.get_rank_value()

        self._cards = sorted(self._cards, key=functools.cmp_to_key(compare_cards))


# Complete the function below.
rank_value_map = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14
        };

def is_straight_flush(hand):
    prev_card_rank = rank_value_map[hand[0][0]]
    card_suit = hand[0][1]
    for i in range(1,len(hand)):
        if hand[i][1]==card_suit and rank_value_map[hand[i][0]] - prev_card_rank == 1:
            prev_card_rank = rank_value_map[hand[i][0]]
        else:
            return False
    return True


def is_four_of_a_kind(hand):
    cards = {}
    for card in hand:
        if card[0] in cards:
            cards[card[0]] += 1
        else:
            cards[card[0]] = 1

        if cards[card[0]] == 4:
            return True, card[0]

    return False

def is_full_house(hand):
    cards = {}
    for card in hand:
        if card[0] in cards:
            cards[card[0]] += 1
        else:
            cards[card[0]] = 1

    flag_3 = False
    flag_2 = False
    for key in cards:
        if cards[key] == 3:
            flag_3 = True
            result = key
        elif cards[key] == 2:
            flag_2 = True

    return flag_2 and flag_3, result

def is_flush(hand):
    card_suit = hand[0][1]
    for card in hand:
        if card[1] != card_suit:
            return False
    return True

def is_straight(hand):
    prev_card_rank = rank_value_map[hand[0][0]]
    for i in range(1,len(hand)):
        if rank_value_map[hand[i][0]] - prev_card_rank == 1:
            prev_card_rank = rank_value_map[hand[i][0]]
        else:
            return False
    return True

def three_of_a_kind(hand):
    cards = {}
    for card in hand:
        if card[0] in cards:
            cards[card[0]] += 1
        else:
            cards[card[0]] = 1
    for key in cards:
        if cards[key] == 3:
            return True, key

    return False

def is_two_pair(hand):
    cards = {}
    count = {}
    for card in hand:
        if card[0] in cards:
            cards[card[0]] += 1
        else:
            cards[card[0]] = 1

    for key in cards:
        if cards[key] in count:
            count[cards[key]] += 1
        else:
            count[cards[key]] = 1
    if 2 in count and count[2] == 2:
        return True
    else:
        return False

def is_one_pair(hand):
    cards = {}
    count = {}
    for card in hand:
        if card[0] in cards:
            cards[card[0]] += 1
        else:
            cards[card[0]] = 1

    for key in cards:
        if cards[key] in count:
            count[cards[key]] += 1
        else:
            count[cards[key]] = 1
    if 2 in count and count[2] == 1:
        return True
    else:
        return False

def rank_poker_hands(poker_hands):
    power = {}
    for hand in poker_hands:
        current_hand = PokerHand(hand)
        hand = current_hand._cards
        sorted_hand = list()
        for card in hand:
            sorted_hand.append(str(card._cardstring))

        if is_straight_flush(sorted_hand):
            power[str(sorted_hand)] = ([1, rank_value_map[sorted_hand[-1][0]]])

        elif is_four_of_a_kind(sorted_hand):
            power[str(sorted_hand)] = ([2, rank_value_map[sorted_hand[-1][0]]])

        elif is_full_house(sorted_hand):
            power[str(sorted_hand)] = ([3, rank_value_map[sorted_hand[-1][0]]])

        elif is_flush(sorted_hand):
            power[str(sorted_hand)] = ([4, rank_value_map[sorted_hand[-1][0]]])

        elif is_straight(sorted_hand):
            power[str(sorted_hand)] = ([5, rank_value_map[sorted_hand[-1][0]]])

        elif three_of_a_kind(sorted_hand):
            power[str(sorted_hand)] = ([6, rank_value_map[sorted_hand[-1][0]]])

        elif is_two_pair(sorted_hand):
            power[str(sorted_hand)] = ([7, rank_value_map[sorted_hand[-1][0]]])

        elif is_one_pair(sorted_hand):
            power[str(sorted_hand)] = ([8, rank_value_map[sorted_hand[-1][0]]])

        else:
            power[str(sorted_hand)] = ([9, rank_value_map[sorted_hand[-1][0]]])

    print(power)




hands = [['7D','7S','9D','KC'],['8D','TC','TD','KS']]
rank_poker_hands(hands)
