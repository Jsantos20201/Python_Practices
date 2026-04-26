def isValid(s):
    i = "()"

    for string in s:
        if string in i:
            return True
        else:
            return False
        
print(isValid("()[]{}"))