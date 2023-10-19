def all_construct(target, word_bank):  # time: O(n to the bar m) , space: O(n to the bar m)
    table = [[]] * (len(target) + 1)
    table[0] = [[]]
    for i in range(len(target)):
        for word in word_bank:
            if target[i: i + len(word)] == word:
                new_combinations = [*table[i], word]
                table[i + len(word)] += new_combinations

    return table[len(target)]


print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))

