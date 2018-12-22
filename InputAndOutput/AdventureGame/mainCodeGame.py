import shelve

loc = '1'
exits = shelve.open('exits')
locations = shelve.open('location')
vocabulary = shelve.open('vocabulary')

while True:
    if loc is not '0':
        availableExits = ', '.join(exits[loc].keys())
        # availableExits = ''
    # for direction in exits[loc].keys() :
    #     availableExits += direction + ' '

    print(locations[loc])

    if loc == '0':
        break

    print('Available exits are '+availableExits, end=' ')
    direction = input().lower()
    print()

    if len(direction) > 0:
        tempList = direction.split()
        # it will split the sentence wherever the space is found .
        for word in tempList:
            # now we are iterating through the user input
            # which is negligible unlike the previous example .
            if word in vocabulary.keys():
                direction = vocabulary[word]

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print('You cannot go in that location')
