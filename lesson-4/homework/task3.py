txt = input()
vowels = 'aeiou'
i = 2 
result = ''
while i < len(txt):
    result += txt[:i + 1]
    if i + 1 < len(txt):
        next_char = txt[i + 1]
        if next_char in vowels or next_char == '_': # Add the next character too and then underscore
            result += next_char + '_'
            txt = txt[i + 2:]  # Remove processed part
            i = 2  # Reset index for new substring
            continue
        else:
            result += '_'
    txt = txt[i + 1:]  # Remove processed part
    i = 2  # Reset index for new substring

result += txt  # Add the rest of the string
print(txt)