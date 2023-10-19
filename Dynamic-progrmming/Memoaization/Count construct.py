def count_construct(target, word_bank, cache=None):
    if cache is None:
        cache = {}
    if target in cache:
        return cache[target]
    if target == '':
        return 1

    total_count = 0
    for word in word_bank:
        if target.startswith(word):
            num_ways_for_rest = count_construct(target[len(word):], word_bank, cache)
            total_count += num_ways_for_rest

    cache[target] = total_count
    return total_count


print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))