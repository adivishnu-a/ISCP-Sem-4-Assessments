def are_anagrams(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        string1 = f1.read().strip()
        string2 = f2.read().strip()

    if sorted(string1) == sorted(string2):
        return "Anagram"
    else:
        return "Not Anagram"


# Input files
file1 = 'input.txt'
file2 = 'input1.txt'

result = are_anagrams(file1, file2)
print(result)
