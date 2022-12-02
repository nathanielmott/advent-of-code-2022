# Part 1:

def outcome_score(played: str) -> int:
    if played == "A X":
        return 3
    elif played == "B Y":
        return 3
    elif played == "C Z":
        return 3
    elif played == "A Y":
        return 6
    elif played == "B Z":
        return 6
    elif played == "C X":
        return 6
    else:
        return 0

# This is an unholy "if_elif" chain, but when I tried using "or" to combine every win, lose, or draw condition, it didn't evaluate correctly.

def shape_score(played: str) -> int:
    if "X" in played:
        return 1
    elif "Y" in played: 
        return 2
    elif "Z" in played:
        return 3

with open('/Users/nathanielmott/Desktop/aoc2-input.txt', 'r') as strat_guide:
    rounds = strat_guide.read().splitlines()
    total_score = 0
    for line in rounds:
        played = line
        round_score = outcome_score(played) + shape_score(played)
        total_score += round_score
print(total_score)

