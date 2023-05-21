n = int(input("Enter the number of lines to read: "))

file_name = "input.txt"
output_file = "output.txt"

# Read all lines from the file
with open(file_name, "r") as file:
    lines = file.readlines()

# Extract the last n lines
last_n_lines = lines[-n:]

print("""It was produced as part of Nickelodeon's commitment broadcast on December 11, 2001.
A picture book entitled The Rugrats'
 Kwanzaa was adapted from the script.
 The episode was released on VHS in 2001""")
