import random
import sqlite3

points = {"A": 1, "J": 10, "Q": 10, "K": 10}
points.update({n: n for n in range(2, 11)})


def hand_score(hand):
    total = sum([points[card] for card in hand])
    if "A" in hand and total <= 11:
        return total + 10
    return total


db = sqlite3.Connection("cards.sql")
sql = db.execute
sql("drop table if exists cards;")
sql("create table cards(card, place);")


def play(card, place):
    sql("insert into cards values (?, ?);", (card, place))
    db.commit()


def score(who):
    cards = sql("select * from cards where place=?;", [who])
    return hand_score([card for card, place in cards.fetchall()])


def bust(who):
    return score(who) > 21


player, dealer = "Player", "Dealer"


def play_hand(deck):
    play(deck.pop(), player)
    play(deck.pop(), dealer)
    play(deck.pop(), player)
    hidden = deck.pop()

    while "y" in input("Hit? ").lower():
        play(deck.pop(), player)
        if bust(player):
            print(player, "went bust!")
            return

    play(hidden, dealer)

    while score(dealer) < 17:
        play(deck.pop(), dealer)
        if bust(dealer):
            print(dealer, "went bust!")
            return

    print(player, score(player), "and", dealer, score(dealer))


deck = list(points.keys()) * 4
random.shuffle(deck)
while len(deck) > 10:
    print("\nDealing...")
    play_hand(deck)
    sql("update cards set place='Discard';")
