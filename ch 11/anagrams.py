def anagrams_of(string, level=0):
    print(level)
    if len(string) == 1:
        return [string[0]]

    output = []

    substring_anagrams = anagrams_of(string[1:], level + 1)

    for substring in substring_anagrams:
        for index in range(len(substring)+1):
            copy = list(substring)
            copy.insert(index, string[0])

            output.append("".join(copy))

    return output


# print(anagrams_of("abba"))
print(anagrams_of("abc"))
