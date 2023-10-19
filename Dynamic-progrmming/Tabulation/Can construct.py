def can_construct(target, word_bank):  # time : O(m square n), space: O(m)
    table = [False] * (len(target) + 1)
    table[0] = True

    for i in range(len(target)):
        if table[i] is True:
            for word in word_bank:
                if target[i:i + len(word)] == word:
                    table[i + len(word)] = True

    return table[len(target)]


print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee']))