def all_construct(target,word_bank, cache=None):
    if cache is None:
        cache = {}
    if target in cache:
        return cache[target]
    if target == '':
        return [[]]

    result = []

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank, cache)
            for way in suffix_ways:
                target_ways = [word, *way]
                result.append([*target_ways])

    cache[target] = result
    return result


print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(all_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))