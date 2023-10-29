word_count = {}

with open('../poem.txt', 'r') as file:
    for line in file:
        tokens = line.split(' ')
        for token in tokens:
            token = token.replace('\n', '')
            count1 = tokens.count(token)
            if token in word_count:
                word_count[token] += 1
            else:
                word_count[token] = 1

print(word_count)
