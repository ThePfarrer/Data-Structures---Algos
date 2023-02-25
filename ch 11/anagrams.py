def anagrams_of(string):
    if len(string) == 1:
        return [string[0]]

    output = []

    substring_anagrams = anagrams_of(string[1:])

    for substring in substring_anagrams:
        for index in range(len(substring)+1):
            print(string[0], substring, index)
            copy = list(substring)
            copy.insert(index, string[0])
            print(copy)

            output.append("".join(copy))

    return output


print(anagrams_of("abba"))
print(anagrams_of("abc"))
