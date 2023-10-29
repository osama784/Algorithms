# mine:

arr = []
with open('../nyc_weather.csv', 'r') as file:
    for line in file:
        tokens = line.split(',')
        try:
            temp = int(tokens[1])
            arr.append(temp)
        except:
            pass

print(arr[8])
print(arr[3])


# Origin:
weather_dict = {}

with open("../nyc_weather.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        try:
            temperature = int(tokens[1])
            weather_dict[day] = temperature
        except:
            pass

print(weather_dict['Jan 9'])

print(weather_dict['Jan 4'])