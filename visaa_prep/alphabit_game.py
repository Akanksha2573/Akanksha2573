s = input().strip()
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for char in s:
    if char.isalpha(): 
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print(f"{vowel_count},{consonant_count}")
