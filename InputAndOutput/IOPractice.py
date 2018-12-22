#Reading

# with open('sample.txt', 'r') as jabber:
#     for line in jabber:
#         if "jab" in line.lower():
#             print(line, end='')
#
# jabber.close()
#
# with open('sample.txt','r') as jabber:
#     lines = jabber.readlines()  #note: to use the readlines(self,hint)
#     #this will work as an array of lines.
# print(lines)    #run this u can see an array of lines .
#
# for line in lines[::-1]:
#     print(line, end='')

#Writing
#
# companies = ['Google', 'windows', 'amazon', 'infosys', 'facebook', 'media tech'
#              , 'tech mahendra', 'apple']
#
# with open('companies.txt','w') as phani:
#     for company in companies:
#         print(company,file=phani)



# companies = []
#
# with open('companies.txt','r') as phani:
#     for company in phani:
#         companies.append(company.strip('\n'))
#         # .strip('\n') removes the \n from the importing .txt file.
#         #the .strip only removes the charaters from the beggining or from the end .
#
# print(companies)
#
# for company in companies:
#     print(company)



# edShereen = ('ed shereen', '2018',
#        ((1, 'sick boy'), (2, 'shape of you'), (3, 'flower market')))
#
# with open('music.txt', 'w') as music:
#     print(edShereen, file=music)

# with open('music.txt', 'r') as music:
#     content = music.readline()
#     #.readlines() will throw an error .
#
# edShereen = eval(content)
#
# artist, year, tracks = edShereen
#
# print('{} \n {} \n {} \n'.format(artist, year, tracks))


#challenge

# with open('sample.txt', 'a') as tableFile:
#     for i in range(0,13):
#         for j in range(0,13):
#             print('{:2} times {:2} is {:2} '.format(i,j,(i*j)), file=tableFile)
#         print('-'*20, file=tableFile)

