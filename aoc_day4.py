import re

f = open("aoc_day4.txt", "r")
file_text = f.read()

def dict_from_str(string):
    Dict = dict((x,y)
            for x, y in (element.split(":")
            for element in string.split(" ")))
    return Dict

def process_text_to_dict(text):
    text_list = text.split("\n\n")
    text_list = [p.replace("\n", " ") for p in text_list]
    return [dict_from_str(p) for p in text_list]

def check_all_passports_part_1():
    all_passports = process_text_to_dict(file_text)
    valid_passports = 0
    for passport in all_passports:
        if {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} <= passport.keys():
            valid_passports += 1
        else:
            pass
    print("Number of valid passports (part 1): " + str(valid_passports))

check_all_passports_part_1()

def get_height(string):
    get_num_array = [int(x) for x in re.findall(r'\d+', string)]
    return get_num_array[0]

def check_hcl(string):
    return re.search(r'#([a-f0-9]){6}', string)

def check_pid(string):
    return re.search(r'[0-9]{9}', string)

def check_all_passports_part_2():
    all_passports = process_text_to_dict(file_text)
    valid_passports = 0
    for passport in all_passports:
        if {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} <= passport.keys():   # check to see if all mandatory fields are present
            all_checks = 0
            if int(passport["byr"]) >= 1920 and int(passport["byr"]) <= 2002 and int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020 and int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030:
                all_checks += 1
            height = get_height(passport["hgt"])
            if "cm" in passport["hgt"] and height >= 150 and height <= 193:
                all_checks += 1
            elif "in" in passport["hgt"] and height >= 59 and height <= 76:
                all_checks += 1
            else:
                pass
            if check_hcl(passport["hcl"]) is not None:
                all_checks += 1
            if passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                all_checks += 1
            if check_pid(passport["pid"]) is not None:
                all_checks += 1
            if all_checks == 5:
                valid_passports += 1

    print("Number of valid passports (part 2): " + str(valid_passports)) # this is out by one, more details here https://www.reddit.com/r/adventofcode/comments/k6e8sw/2020_day_04_solutions/gfaqxdk/?utm_source=reddit&utm_medium=web2x&context=3

check_all_passports_part_2()