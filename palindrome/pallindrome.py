def is_palindrome(s):
    s = str(s)  # convert element to string (works for numbers too)
    return s == s[::-1]

def contains_palindrome(lst):
    for item in lst:
        if is_palindrome(item):
            return True, item
    return False, None

# Example
my_list = ["apple", "madam", "hello", 121, "world"]
result, palindrome = contains_palindrome(my_list)

if result:
    print(f"Yes, the list contains a palindrome: {palindrome}")
else:
    print("No palindrome found in the list")