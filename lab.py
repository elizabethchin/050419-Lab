def find_range(nums):
    """Given list of numbers, return smallest & largest number as a tuple."""
    if nums == []:
        return (None, None)
    nums = sorted(nums)
    return (nums[0], nums[-1])


print(find_range([3, 4, 2, 5, 10]))
#(2, 10)

print(find_range([43, 3, 44, 20, 2, 1, 100]))
#(1, 100)

print(find_range([]))
#(None, None)
print(find_range([7]))
#(7, 7)

def fizzbuzz():
    """Count from 1 to 20 in fizzbuzz fashion."""

    for i in range(1,21):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
fizzbuzz()

def find_longest_word(words):
    """Return longest word in list of words."""

    length = 0

    for word in words:
        if len(word) > length:
            length = len(word)
    return length

print(find_longest_word(["hi", "hello"]))
#5

print(find_longest_word(["Balloonicorn", "Hackbright"]))
#12

def decode(string):
    """Decode a string."""
    num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    code = ""
    for i, char in enumerate(string):
        if char in num_list:
            code += string[i + int(char) + 1]
    return code
      

print(decode("0h"))
#'h'
print(decode("2abh"))
#'h'
print(decode("0h1ae2bcy"))
#'hey'

def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""
    seen = {}
    
    for letter in word:
        count = seen.get(letter, 0)
        seen[letter] = count + 1
    
    seen_an_odd = False

    for count in seen.values():
        if count % 2 != 0:
            if seen_an_odd:
                return False
            seen_an_odd = True
    return True
    
print(is_anagram_of_palindrome("a"))
#True

print(is_anagram_of_palindrome("ab"))
#False

print(is_anagram_of_palindrome("aab"))
#True

print(is_anagram_of_palindrome("arceace"))
#True

print(is_anagram_of_palindrome("arceaceb"))
#False
import string
def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""
    char_list = []
    for char in sentence:
        if char.isalpha():
            char_list.append(char.lower())
    char_list = set(char_list)

    return len(char_list) == 26
    


print(is_pangram("The quick brown fox jumps over the lazy dog!"))
# #True

print(is_pangram("I like cats, but not mice"))
# #False

