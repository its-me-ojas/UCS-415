# def compare(basket, toSearch):
#     result = []
#     for item in basket:
#         if toSearch == item.lower():
#             result.append(item)
#     return result
#
#
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# basket = set(basket)
#
# toSearch = input("Enter the fruit to search: ")
# result = compare(basket, toSearch.lower())
# print(result)

# a = set('acads')
# b = set('institute')
# print(a)
# print(b)
# print(a - b)
# print(a | b)
# print(a & b)

# capital = {'India': 'New Delhi', 'USA': 'Washington', 'UK': 'London'}
# print(capital.keys())
# print(capital.values())
# print(capital['India'])

players=open("players","r")
# players.write("Sachin\n")
# players.write("Saurav\n")
# players.write("Dravid\n")
print(players.read())
players.close()
