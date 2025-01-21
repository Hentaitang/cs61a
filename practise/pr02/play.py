def play(strategy0, strategy1, gold=21):
    """ a function take two strategies and one gold number, strategy will return a number (1 to 3)
    two players use two strategies to play the game, the game will end when score reach the gold number or more
    return player number(player0 -> 0 or player1 -> 1)
    """
    total, who = 0, 0
    while total < gold:
        if who == 0:
            total += strategy0(total)
            who = 1
        else:
            total += strategy1(total)
            who = 0
    return who

def always_two(n):
    return 2

def interactive_start(n):
    print(f"Current Score is {n}")
    number = int(input("Enter a number(1 - 3): "))
    while number > 3 or number < 1:
        number = int(input("Enter a number(1 - 3): "))
    return number

def strategy_wrapper(who, strategy):
    def prev(score):
        print(f"Player{who} is playing now!!!")
        return strategy(score)
    return prev