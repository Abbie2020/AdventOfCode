### https://adventofcode.com/2020/day/2

import csv

## PART 1

num_valid_part_1 = 0

with open('aoc_passwords.csv') as csvfile:
    pwreader = csv.reader(csvfile)
    for row in pwreader:
        pw_policy = row[0]
        pw_pieces = pw_policy.split()
        rng = pw_pieces[0]
        rng_low = int(rng.split("-")[0])
        rng_high = int(rng.split("-")[1])
        char = pw_pieces[1].split(":")[0]
        password = pw_pieces[2]
        char_in_str = password.count(char)

        if char_in_str in range(rng_low,rng_high + 1):
            num_valid_part_1 += 1

print('Number of valid passwords (Part 1): ' + str(num_valid_part_1))


## PART 2

num_valid_part_2 = 0

with open('aoc_passwords.csv') as csvfile:
    pwreader = csv.reader(csvfile)
    for row in pwreader:
        pw_policy = row[0]
        pw_pieces = pw_policy.split()
        rng = pw_pieces[0]
        rng_low = int(rng.split("-")[0])
        rng_high = int(rng.split("-")[1])
        char = pw_pieces[1].split(":")[0]
        password = pw_pieces[2]

        if char == password[rng_low-1] and char != password[rng_high-1]:
            num_valid_part_2 += 1
        elif char != password[rng_low-1] and char == password[rng_high-1]:
            num_valid_part_2 += 1
        else:
            pass

print('Number of valid passwords (Part 2): ' + str(num_valid_part_2))