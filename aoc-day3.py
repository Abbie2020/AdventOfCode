f = open("aoc_3_sled_run.txt", "r")

pattern = []

for line in f:
    pattern.append(line.strip()) 

# print(pattern) 
new_pattern = pattern # this creates the initial pattern

## Extend pattern as we go down the hill
def extend_pattern(tp):
    total_pattern_length = len(new_pattern[0])
    print("Toboggan position: " + str(tp))
    print("Current pattern length: " + str(total_pattern_length))
    if tp > total_pattern_length:
        for index, line in enumerate(new_pattern):
            # print(line)
            new_pattern[index] = line *
            print("New pattern length: " + str(len(new_pattern[0])))

## Go down the hill
def downhill():
    num_trees = 0
    tob_pos = 0
    # print(tob_pos)

    for line in new_pattern:
        # print(line)
        # print("Toboggan position: " + str(tob_pos))
        if line[tob_pos] == '#':
            print("tree")
            num_trees += 1
            tob_pos += 3
            extend_pattern(tob_pos)
        else:
            tob_pos += 3
            extend_pattern(tob_pos)

    return num_trees

downhill()

print("Number of trees: " + str(num_trees))