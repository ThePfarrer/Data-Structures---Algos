def missing_letter(sentence):
    sentence = "".join(sentence.split(" "))

    letters = "abcdefghijklmnopqrstuvwxyz"

    hash_map = {}

    for ch in sentence:
        hash_map[ch] = True

    for ch in letters:
        if ch not in hash_map:
            return ch

sentence1 = "the quick brown box jumps over a lazy dog"
print(missing_letter(sentence1))