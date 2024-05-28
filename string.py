1.def create_new_string(input_string):
    length = len(input_string)
    if length < 3:
        return "Input string should have at least 3 characters."
    else:
        first_char = input_string[0]
        middle_char = input_string[length // 2]
        last_char = input_string[-1]
        new_string = first_char + middle_char + last_char
        return new_string


2.input_string = input("Enter a string: ")
new_string = create_new_string(input_string)
print("New string:", new_string)

def create_new_string(input_string):
    if len(input_string) >= 3:
        middle_index = len(input_string) // 2
        new_string = input_string[middle_index - 1: middle_index + 2]
        print("New string:", new_string)
    else:
        print("Input string should have at least three characters.")

if __name__ == "__main__":
    input_string = input("Enter the input string: ")
    create_new_string(input_string)
3.def append_middle(str1, str2):
    length_str1 = len(str1)
    middle_index = length_str1 // 2
    new_string = str1[:middle_index] + str2 + str1[middle_index:]
    return new_string

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
new_string = append_middle(str1, str2)
print("New string:", new_string)

4.def count_characters(str1):
    letters = 0
    digits = 0
    special_symbols = 0
    
    for char in str1:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        else:
            special_symbols += 1
    
    return letters, digits, special_symbols
str1 = "p@#yn26at^&i5ve"
letters, digits, special_symbols = count_characters(str1)
print("Letters:", letters)
print("Digits:", digits)
print("Special symbols:", special_symbols)

5.def create_string(s1, s2):
    s3 = ''
    len_s1 = len(s1)
    len_s2 = len(s2)
    i = 0
    j = len_s2 - 1

    while i < len_s1 and j >= 0:
        s3 += s1[i]
        s3 += s2[j]
        i += 1
        j -= 1
    while i < len_s1:
        s3 += s1[i]
        i += 1
    while j >= 0:
        s3 += s2[j]
        j -= 1

    return s3
s1 = "super"
s2 = "world"
print(create_string(s1, s2)) 
