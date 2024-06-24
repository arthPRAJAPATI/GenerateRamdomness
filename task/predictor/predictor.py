print("Please provide AI some data to learn...")
print("The current data length is 0, 100 symbols left")
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

print("You have $1000. Every time the system successfully predicts your next press, you lose $1.Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!")
balance = 1000
possible_values = ["000", "001", "010", "011", "100", "101", "110", "111"]
values_dict = {possible_value: [0,0] for possible_value in possible_values}
for _ in range(0, len(final_input) - 3):
    substring = final_input[_:_ + 3]
    if substring in values_dict:
        if final_input[_ + 3] == '0':
            values_dict[substring][0] += 1
        else:
            values_dict[substring][1] += 1

print("Print a random string containing 0 or 1:")
test_input = input()
while test_input != "enough":
    while len(test_input) < 4:
        print("Print a random string containing 0 or 1:")
        test_input = input()
    totalCount = 0
    trueCount = 0
    predictions = ""
    test_numbers = ''.join([str(i) for i in [int(x) for x in test_input if x in ["0", "1"]]])
    for _ in range(0, len(test_numbers) - 3):
        test_substring = test_numbers[_:_ + 3]
        if test_substring in values_dict:
            prediction = '0' if values_dict[test_substring][0] > values_dict[test_substring][1] else '1'
            predictions += prediction
            totalCount += 1
            if test_numbers[_ + 3] == prediction:
                trueCount += 1
                balance -= 1
            else:
                balance += 1

    print(f"predictions:")
    print(predictions)
    print(f"Computer guessed {trueCount} out of {totalCount} symbols right ({(trueCount/totalCount)*100:.2f} %)")
    print(f"Your balance is now ${balance}")
    print("Print a random string containing 0 or 1:")
    test_input = input()

print("Game over!")