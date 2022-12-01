with open('/Users/nathanielmott/Desktop/aoc1-input.txt', 'r') as aoc_data:
    elves = aoc_data.read().split("\n\n")
    chunked_calories = list()
    
    for i in elves:
        held_calories = i.split("\n")
        held_calories_integer = list(map(int, held_calories))
        total_calories = sum(held_calories_integer)
        chunked_calories.append(total_calories)
    
    chunked_calories.sort(reverse = True)
    
    top_elves = [chunked_calories[0], chunked_calories[1], chunked_calories[2]]

    top_elves_total = sum(top_elves)

    print(top_elves_total)
