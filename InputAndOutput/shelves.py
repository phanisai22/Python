import shelve

# with shelve.open('shelveTest') as fruit:
#     fruit['banana'] = 'my fav fruit'
#     fruit['apple'] = 'an apple a day keeps the doc away'
#     fruit['grapes'] = 'they grow in bunches'
#     fruit['oranges'] = 'a citrus fruit , good for skin'
#
#     print(fruit['apple'])
#     print(fruit['banana'])
#
#     print(fruit)

# fruit = shelve.open('shelveTest')
# fruit['banana'] = 'my fav fruit'
# fruit['apple'] = 'an apple a day keeps the doc away'
# fruit['grapes'] = 'they grow in bunches'
# fruit['oranges'] = 'a citrus fruit , good for skin'
#
# print(fruit['banana'])
# print(fruit['grapes'])
#
# fruit['grapes'] = 'also citrus .'
#
# for item in fruit:
#     print(item + ':' + fruit[item])
#
# fruit.close()


# friedRice = ['eggs', 'onions', 'refined oil', 'chicken powder', 'rice']
# noodles = ['eggs', 'onions', 'refined oil', 'chicken powder', 'noodles']
# tomato = ['tomato', 'onions', 'refined oil', 'chicken powder']
# tea = ['tea powder', 'sugar', 'milk']

with shelve.open('recipe', writeback=True) as recipes:
    # recipes['fried Rice'] = friedRice
    # recipes['noodles'] = noodles
    # recipes['tomato'] = tomato
    # recipes['tea'] = tea
    recipes['fried Rice'].append('hmmmm')
    # updating the data.
    del recipes['fried Rice']
    for items in recipes:
        print(items, recipes[items])
