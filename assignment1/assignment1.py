# Write your code here.

# Task 1: Hello
def hello():
    return "Hello!"

print(hello())

# Task 2: Greet with a Formatted String
def greet(name):
    return f"Hello, {name}!"

print(greet("James"))

# Task 3: Calculator
#  - only integers and floats can be calculated, so chheck if num1 and num2 are either integers or floats
#  - division by 0 is undefined, so check if num2, divisor in this case, is 0 and the operation to be performed is either division, integer divission, or modulus 
def calc(num1, num2, str="multiply"):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        if (num2 == 0) and (str == "divide" or str == "int_divide" or str == "modulo"):
            return "You can't divide by 0!"
        else:
            if str == "add":
                return num1 + num2
            elif str == "subtract":
                return num1 - num2
            elif str == "multiply":
                return num1 * num2
            elif str == "power":
                return num1 ** num2
            elif str == "divide":
                return num1 / num2
            elif str == "int_divide":
                return num1 // num2
            elif str == "modulo":
                return num1 % num2
            else:
                return num1 * num2
    else:
        return f"You can't {str} those values!"

print(f"4 * 5 = {calc(4,5)}")
print(f'4 + 5 = {calc(4,5,"add")}')
print(f'4 - 5 = {calc(4,5,"subtract")}')
print(f'4 * 5 = {calc(4,5,"multiply")}')
print(f'4 ** 5 = {calc(4,5,"power")}')
print(f'4 / 5 = {calc(4,5,"divide")}')
print(f'4 // 5 = {calc(4,5,"int_divide")}')
print(f'9 % 5 = {calc(4,5,"modulo")}')

print(f"4.6 * 5 = {calc(4.6,5)}")
print(f'4.6 + 5 = {calc(4.6,5,"add")}')
print(f'4.6 - 5 = {calc(4.6,5,"subtract")}')
print(f'4.6 * 5 = {calc(4.6,5,"multiply")}')
print(f'4.6 ** 5 = {calc(4.6,5,"power")}')
print(f'4.6 / 5 = {calc(4.6,5,"divide")}')
print(f'4.6 // 5 = {calc(4.6,5,"int_divide")}')
print(f'4.6 % 5 = {calc(4.6,5,"modulo")}')

print(f"4 * 5.3 = {calc(4,5.3)}")
print(f'4 + 5.3 = {calc(4,5.3,"add")}')
print(f'4 - 5.3 = {calc(4,5.3,"subtract")}')
print(f'4 * 5.3 = {calc(4,5.3,"multiply")}')
print(f'4 ** 5.3 = {calc(4,5.3,"power")}')
print(f'4 / 5.3 = {calc(4,5.3,"divide")}')
print(f'4 // 5.3 = {calc(4,5.3,"int_divide")}')
print(f'4 % 5.3 = {calc(4,5.3,"modulo")}')

print(f'4 / 0 = {calc(4,0,"divide")}')
print(f'4 // 0 = {calc(4,0,"int_divide")}')
print(f'4 % 0 = {calc(4,0,"modulo")}')

print(f'0 / 5 = {calc(0,5,"divide")}')

print(f'"first" % "second" = {calc("first","second","modulo")}')

# Task 4: Data Type Conversion
#  - if string starts with the non digits, throw an error
def data_type_conversion(value, type):
    if type == "str":
        return str(value)
    elif isinstance(value, (int, float)) or value[0].isdigit():
        if type == "int":
            return int(value)
        elif type == "float":
            return float(value)
    else:
        return f"You can't convert {value} into a {type}."

print(data_type_conversion(84, "str"))
print(data_type_conversion("84", "int"))
print(data_type_conversion("84", "float"))

print(data_type_conversion("banana", "int"))

# Task 5: Grading System, Using *args
#  - check if each arg in args is integer of float
#  - sum args, count args, calculate args average
def grade(*args):
    if all(isinstance(arg, (int, float)) for arg in args):
        result = sum(args)/len(args)
    else:
        return "Invalid data was provided."
    
    if result > 90:
        return "A"
    elif result > 80:
        return "B"
    elif result > 70:
        return "C"
    elif result > 60:
        return "D"
    else:
        return "F"
    
print(grade(95,95,95))
print(grade(75,85,95))
print(grade(75,65,95))
print(grade(75,55,65))
print(grade(45,55,65))

print(grade("three", "blind", "mice"))

# # Task 6: Use a For Loop with a Range
def repeat(string, count):
    new_string = ""
    for _ in range(count):
        new_string += string
    return new_string
    
print(repeat("up,", 4))

# Task 7: Student Scores, Using **kwargs
#  - if "mean", pick values, calculate average,
#  - if "best", iterate through the values, find the greatest, return the key for that value
def student_scores(score, **kwargs):
    if score == "mean":
        return sum(kwargs.values())/len(kwargs)
    elif score == "best":
        best_key = None
        best_value = 0
        for key, value in kwargs.items():
            if best_value < value:
                best_value = value
                best_key = key
            else:
                best_value
                best_key
        return best_key
                                 
print(student_scores("mean", Tom=75, Dick=89, Angela=91))
print(student_scores("best", Tom=75, Dick=89, Angela=91))

# Task 8: Titleize, with String and List Operations
# - since string can contain >1 word, split string into words
# - 

def titleize(string):
    words = string.split()
    exceptions = {"a", "on", "an", "the", "of", "and", "is", "in"}
    for i, word in enumerate(words):
        if i == 0 or i == (len(words) - 1) or (word not in exceptions):
            words[i] = word.capitalize()
    return " ".join(words)

print(titleize("war and peace"))
print(titleize("a separate peace"))
print(titleize("after on"))

# Task 9: Hangman, with more String Operations
# - iterate through secret,
# - return letter if matching, _ if not
# - concat results in a string
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result
    
print(hangman("difficulty","ic"))

# Task 10: Pig Latin, Another String Manipulation Exercise
# - since string can contain >1 word, split string into words
# - check if it starts with vowel, consonant, or "qu"
# -- if consonant, then
# --- if "q", then move 2 letters to the end of the word
# --- else move 1 letter to the end of the word
# -- all (vowel original and modified) add "ay" to the end of the word
# - join words into one string

def pig_latin(string):
    vowels = "aeiou"
    result = []  
    
    words = string.split()

    # iteratinng through each word
    for word in words:
        temp = ""  # Holds consonants before the first vowel
        i = 0  # Reset index for each word

        # Move consonants (including "qu") to `temp`
        while i < len(word) and word[i] not in vowels:
            # Handle special case: "qu" together as a unit
            if word[i] == "q" and i + 1 < len(word) and word[i + 1] == "u":
                temp += "qu"
                i += 2
            else:
                temp += word[i]
                i += 1

        # Construct Pig Latin word
        pig_latin_word = word[i:] + temp + "ay"
        result.append(pig_latin_word)

    # Join Pig Latin words into a single string
    return " ".join(result)

print(pig_latin("apple"))
print(pig_latin("banana"))
print(pig_latin("cherry"))
print(pig_latin("quiet"))
print(pig_latin("square"))
print(pig_latin("the quick brown fox"))