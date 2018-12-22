#
# farmAnimals = {'cow', 'ox', 'goat', 'cow'}
# for animals in farmAnimals:
#     print(animals)
#
# print('='*10)
#
# wildAnimals = set(['tiger', 'lion', 'cheetas', 'black panther', 'elephant'])
#
# print(wildAnimals)
#
# for animals in wildAnimals:
#     print(animals)
#
# evenNumbers = set(range(0,20,2))
# print(evenNumbers)
# print(len(evenNumbers))
# squareTuple = (1,4,9,16)
# squareNumbers = set(squareTuple)
# print(squareNumbers)
# print(squareNumbers)
#
# print('the difference is {} '.format(evenNumbers.difference(squareNumbers)))
# print(len(evenNumbers.difference(squareNumbers)))
# print('the intersection is {}'.format(evenNumbers.intersection(squareNumbers)))
# print(len(evenNumbers.intersection(squareNumbers)))
# print('the union is {}'.format(evenNumbers.union(squareNumbers)))
# print(len(evenNumbers.union(squareNumbers)))

#-----------------------------------------------------------------------------
#CHALLENGE
#
# sentence = input("Enter the sentence : ").lower()
# vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
# sentenceSet = set(sentence)
# # print(sentenceSet)
# sentenceSet.difference_update(vowels)
# #sentence = list(sentenceSet)    you cannot do that.
# printingList = ''.join(sentenceSet)
# print(printingList)
