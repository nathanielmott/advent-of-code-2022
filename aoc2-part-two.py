def new_score(strat: str) -> int:
    if strat == "A X":
        return 3
    elif strat == "A Y":
        return 4
    elif strat == "A Z":
        return 8
    elif strat == "B X":
        return 1
    elif strat == "B Y":
        return 5
    elif strat == "B Z":
        return 9
    elif strat == "C X":
        return 2
    elif strat == "C Y":
        return 6
    elif strat == "C Z":
        return 7

with open('/Users/nathanielmott/Desktop/aoc2-input.txt', 'r') as strat_guide:
    rounds = strat_guide.read().splitlines()
    total_score = 0
    for line in rounds:
        strat = line
        round_score = new_score(strat)
        total_score += round_score
    print(total_score)