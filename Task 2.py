from collections import deque

def is_palindrome(string):
    string = string.lower().replace(" ", "")
    char_queue = deque(string)
    
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            print("Рядок не є паліндромом.")
            return False
    print("Рядок є паліндромом.")
    return True
    

input_string = "Кіт утік"
is_palindrome(input_string)