city_map = {}

cities1 = ['Calgary', 'Vancouver', 'Toronto']
city_map['Canada'] = []
city_map['Canada'] += cities1
city_map['USA'] = []
cities2 = ['New York', 'Austin', 'Seattle']
city_map['USA'] += cities2
city_map['England'] = []
cities3 = ['London', 'Manchester']
city_map['England'] += cities3

print(city_map)

city_list = city_map.values()
print(*city_list, sep=',')

for city in city_list:
    print(*city, sep=',')