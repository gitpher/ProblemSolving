import sys

vowel = ('a', 'e', 'i', 'o', 'u')
exception = ('e', 'o')

while True:
    word = sys.stdin.readline().rstrip()
    if word == "end":
        break

    has_vowel = False
    has_same_2_characters = False
    has_3_consecutive_vowels = False
    has_3_consecutive_consonants = False

    for i in range(len(word)):
        if not has_vowel and word[i] in vowel:
            has_vowel = True

        if i > 0:
            if word[i] == word[i-1] and word[i] not in exception:
                has_same_2_characters = True

        if i > 1:
            if word[i] in vowel and word[i-1] in vowel and word[i-2] in vowel:
                has_3_consecutive_vowels = True
            if word[i] not in vowel and word[i-1] not in vowel and word[i-2] not in vowel:
                has_3_consecutive_consonants = True

        if (i == len(word) - 1 and not has_vowel) or has_same_2_characters or has_3_consecutive_vowels or has_3_consecutive_consonants:
            print(f"<{word}> is not acceptable.")
            break
    else:
        print(f"<{word}> is acceptable.")
