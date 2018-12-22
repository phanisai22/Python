import shelve

with shelve.open('location') as locations:
    locations['0'] = 'you are at your seat learning python .'
    locations['1'] = 'you are at the road .'
    locations["2"] = 'you are up above the hill , be careful .'
    locations['3'] = 'you are in the building .'
    locations['4'] = 'you are in a valley .'
    locations['5'] = 'you are in a forest .'

with shelve.open('exits') as exits:
    exits['0'] = {"q": '0'},
    exits['1'] = {'e': '3', 'w': '2', 'n': '5', 's': '4', 'q': '0'}
    exits['2'] = {'n': '5', 'q': '0'}
    exits['3'] = {'w': '1', 'q': '0'}
    exits['4'] = {'n': '1', 'w': '2', 'q': '0'}
    exits['5'] = {'s': '1', 'w': '2', 'q': '0'}

with shelve.open('vocabulary') as vocabulary:
    vocabulary['south'] = 's'
    vocabulary['north'] = "n"
    vocabulary['west'] = 'w'
    vocabulary['east'] = 'e'
    vocabulary['quit'] = 'q'