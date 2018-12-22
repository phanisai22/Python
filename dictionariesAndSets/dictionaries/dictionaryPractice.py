 #      ---->      5 forest
 #     |             ^
 #     |             |
 #     |             v
 #     v                                                  n
 # 2 hill  <--   1 road  <-->   3 building              w-|-e
 #     ^           ^                                      s
 #     |           |
 #     |           v
 #     -------- 4 valley

# locations = {
#     0: 'you are at your seat learning python .',
#     1: 'you are at the road .',
#     2: 'you are up above the hill , be careful .',
#     3: 'you are in the building .',
#     4: 'you are in a valley .',
#     5: 'you are in a forest .'
# }
#
# exits = {
#     0: {"q": 0},
#     1: {'e': 3, 'w': 2, 'n': 5, 's': 4, 'q': 0},
#     2: {'n': 5, 'q': 0},
#     3: {'w': 1, 'q': 0},
#     4: {'n': 1, 'w': 2, 'q': 0},
#     5: {'s': 1, 'w': 2, 'q': 0}
# }
#
# vocabulary = {
#     'south': 's',
#     'north': "n",
#     'west': 'w',
#     'east': 'e',
#     'quit': 'q'
# }
#
#
# loc = 1
#
# while True:
#     availableExits = ', '.join(exits[loc].keys())
#     # for direction in exits[loc].keys() :
#     #     availableExits += direction + ' '
#
#     print(locations[loc])
#
#     if loc == 0:
#         break
#
#     print('Available exits are '+availableExits, end=' ')
#     direction = input().lower()
#     print()
#
#     # if len(direction) > 0:
#     #     #if a word is entered .
#     #     for key in vocabulary:
#     #         #iterating through the dict .
#     #         #it will take more time to iterate if the list is big .
#     #         if key in direction:
#     #             #checking if the key in the vocabulary dict matches the
#     #             #direction entered .
#     #             direction = vocabulary[key]
#
#     if len(direction) > 0:
#         tempList = direction.split()
#         #it will split the sentence wherever the space is found .
#         for word in tempList:
#             #now we are iterating through the user input
#             #which is negligible unlike the previous example .
#             if word in vocabulary.keys():
#                 direction = vocabulary[word]
#
#     if direction in exits[loc]:
#         loc = exits[loc][direction]
#     else:
#         print('You cannot go in that location')


#---------------------------------------------------------------------------------

fruits = {
    'banana': 'mmmm, my fav',
    'apple': 'good for health',
    'orange': 'it is a citrus fruit',
    'grapes': 'grows in bunchs'
}

# print(fruits)

veg = {
    'tamato': 'we indians consider it as a vegetable',
    'cabbage': 'its a anti cancer veg',
    'onions': 'common for all receips'
}
#
# print(veg)
#
# veg.update(fruits)
#
# print(veg)

niceAndNasty = fruits.copy()
niceAndNasty.update(veg)

fruits['apple'] = 'aapple a day keeps the doctor away'

niceAndNasty.update(fruits)

print(niceAndNasty)