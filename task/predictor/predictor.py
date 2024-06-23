print("Print a random string containing 0 or 1:")
user_input = input()
numbers = [int(x) for x in user_input if x in ["0", "1"]]
while len(numbers) < 100:
    print(f"Current data length is {len(numbers)}, {100 - len(numbers)} symbols left")
    print("Print a random string containing 0 or 1:")
    user_input = input()
    numbers += [int(x) for x in user_input if user_input if x in ["0", "1"]]

print("Final data string:")
final_input = ''.join([str(i) for i in numbers])
print(final_input)

possible_values = ["000", "001", "010", "011", "100", "101", "110", "111"]
values_dict = {possible_value: [0,0] for possible_value in possible_values}
for _ in range(0, len(final_input) - 3):
    substring = final_input[_:_ + 3]
    if substring in values_dict:
        if final_input[_ + 3] == '0':
            values_dict[substring][0] += 1
        else:
            values_dict[substring][1] += 1

for values in values_dict.keys():
    list_values = values_dict[values]
    print(f"{values}: {list_values[0]},{list_values[1]}")



