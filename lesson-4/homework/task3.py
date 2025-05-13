txt = input()
vowels = "aeiou"
i = 2
used_letters = ""
while i < len(txt):
    if txt[i] not in vowels and txt[i] not in used_letters and i != len(txt) - 1:
        txt = txt[: i + 1] + "_" + txt[i + 1 :]
        used_letters += txt[i]
        i += 4
    else:
        i += 1
print(txt)
