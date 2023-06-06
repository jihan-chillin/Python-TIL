import pandas
house = pandas.read_csv('Boston.csv')

print(house)
print(house.head(2))

print(house.describe())