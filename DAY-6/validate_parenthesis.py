def valid_paraentheses(s):
    bal = 0
    for char in range(len(s)):
        if s[char] == '(':
            bal = bal + 1
        elif s[char] == ')':
            bal = bal - 1
        
        if bal < 0:
            return False
    
    return bal == 0


input_str = input()
print(valid_paraentheses(input_str))