def find_duplicate(rucksack: str) -> str:
    compartment_one = rucksack[:len(rucksack)//2]
    compartment_two = rucksack[len(rucksack)//2:]
    
    for char in compartment_one:
        if char in compartment_two:
            return char
        else:
            continue
        # I suspect this would loop forever if there's no duplicate character, but I know there is, so YOLO.

def assign_priority(duplicate_character: str) -> int:
    scores = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
        "A": 27,
        "B": 28,
        "C": 29,
        "D": 30,
        "E": 31,
        "F": 32,
        "G": 33,
        "H": 34,
        "I": 35,
        "J": 36,
        "K": 37,
        "L": 38,
        "M": 39,
        "N": 40,
        "O": 41,
        "P": 42,
        "Q": 43,
        "R": 44,
        "S": 45,
        "T": 46,
        "U": 47,
        "V": 48,
        "W": 49,
        "X": 50,
        "Y": 51,
        "Z": 52,
    }
    
    # Probably could have defined a rule that looped through each letter, adding one to its value, then resetting and adding 26 for capitals.

    line_priority = scores.get(duplicate_character)

    return line_priority

with open("/Users/nathanielmott/Desktop/aoc3-input.txt", 'r') as inventory:
    all_rucksacks = inventory.readlines()
    sum_priorities = 0

    for line in all_rucksacks:
        priority = 0
        duplicate_character = find_duplicate(line)
        priority = assign_priority(duplicate_character)
        sum_priorities += priority
    print(sum_priorities)
