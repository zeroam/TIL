# game.py
import random

from typing import List, Tuple, Any, Sequence, TypeVar, Optional

# Types
Card = Tuple[str, str]
Deck = List[Card]
Choosable = TypeVar("Choosable", str, Card)

SUITS: List[str] = "♠ ♡ ♢ ♣".split()
RANKS: List[str] = "2 3 4 5 6 7 8 9 10 J Q K A".split()


def create_deck(shuffle: bool = False) -> List[Tuple[str, str]]:
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck


def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])


def choose(items: Sequence[Choosable]) -> Choosable:
    """Choose and return a random item"""
    return random.choice(items)


def player_order(names: List[str], start: Optional[str] = None) -> List[str]:
    """Rotate player order so that start goes first"""
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]


def play():
    """Play a 4-player card game"""
    deck = create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}
    start_player = choose(names)
    turn_order = player_order(names, start=start_player)

    # Randomly play cards from each player's hand until empty
    while hands[start_player]:
        for name in turn_order:
            card = choose(hands[name])
            hands[name].remove(card)
            print(f"{name}: {card[0] + card[1]:<3}  ", end="")
        print()


if __name__ == "__main__":
    play()
