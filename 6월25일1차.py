# -*- coding: utf-8 -*-
def is_palindrome(word):
    length = len(word)-1
    answer = False
    for i in range(0, length):
        if (word[i] == word[length - i]):
            answer = True
        else:
            answer = False
    return answer
        

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("≈‰∏∂≈‰"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))