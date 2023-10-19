def can_construct(target, word_bank):
    if target == '':

        return True

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct(suffix, word_bank):
                return True

    return False


print(can_construct('abcdef', ['abcd', 'ef']))
print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'boar', 'sk']))
print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
# print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'f']) will not work


def can_construct1(target, word_bank, cache=None):
    if cache is None:
        cache = {}
    if target in cache:
        return cache[target]
    if target == '':
        return True

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct1(suffix, word_bank, cache):
                cache[target] = True
                return True
    cache[target] = False
    return False


print(can_construct1('eeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'f']))
