prices = [57.8, 46.51, 97, 65.84, 334.95, 781.06, 85.45, 99.99, 12.06, 25.84]
# вывести цены через запятую в одну строку, в виде 00 руб 00 коп
price = []
for i in prices:
    rub = int(i)
    kop = round((i - rub)*100)
    price.append(f'{rub} руб {kop:02d} коп')
print(", ".join(price))
#отсортировать по возрастанию, не создавая новый список
prices.sort()
print(prices)
#отсортировать по убыванию
prices.reverse()
print(prices)
#вывести цены пяти самых дорогих товоров
print(prices[:5])