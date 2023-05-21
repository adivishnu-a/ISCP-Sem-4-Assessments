file_name = "numbers.txt"
sum_of_integers = 0

with open(file_name, "r") as file:
    for line in file:
        # Convert each line to an integer and add it to the sum
        sum_of_integers += int(line.strip())

print(sum_of_integers)
