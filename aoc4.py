with open('/Users/nathanielmott/Desktop/aoc4-input.txt', 'r') as aoc_input:
    list_assignments = aoc_input.readlines()
    count = 0 #tallies the fully contained ranges
    overlap = 0 #tallies the number of overlaps

    
    for x in list_assignments:
        split_pairs = x.split(",")
        pair_one = split_pairs[0]
        pair_two = split_pairs[1]
        split_pair_one = pair_one.split("-")
        split_pair_two = pair_two.split("-")
        start_range_one = int(split_pair_one[0])
        end_range_one = int(split_pair_one[1])
        start_range_two = int(split_pair_two[0])
        end_range_two = int(split_pair_two[1])
        first_range = set(range(start_range_one, end_range_one+1))
        second_range = set(range(start_range_two, end_range_two+1))
        
        # It took me an hour to realize that Python ranges are inclusive at the start but exclusive at the end, which is solved with the +1s.

        if first_range.issubset(second_range) or second_range.issubset(first_range):
            count += 1
        
        if not first_range.isdisjoint(second_range):
            overlap += 1

        

    print(count)    
    print(overlap)
