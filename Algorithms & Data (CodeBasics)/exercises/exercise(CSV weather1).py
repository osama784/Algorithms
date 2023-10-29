arr = []

with open('../nyc_weather.csv', 'r') as file:
    for line in file:
        tokens = line.split(',')
        try:
            temperature = int(tokens[1])
            arr.append(temperature)

        except:  # to not print the empty lines or anything not an int
            pass

print(sum(arr[0:7]) / len(arr[0:7]))

print(max(arr[0:10]))
