def backspace_compare(S, T):
    p1 = len(S) - 1
    p2 = len(T) - 1

    while p1 >= 0 or p2 >= 0:
        if S[p1] == '#' or T[p2] == '#':
            if S[p1] == '#':
                backspace = 2
                while (backspace > 0):
                    p1 -= 1
                    backspace -= 1
                    if p1 > -1 and S[p1] == '#':
                        backspace += 2
            if T[p2] == '#':
                backspace = 2
                while (backspace > 0):
                    p2 -= 1
                    backspace -= 1
                    if p2 > -1 and T[p2] == '#':
                        backspace += 2

        else:
            if S[p1] != T[p2]:
                return 'false'
            else:
                p1 -= 1
                p2 -= 1

    return 'true'

# def backspace(S):
#     L = []
#     for letter in S:
#         if letter != '#':
#             L.append(letter)
#         elif len(L) > 0:
#             L.pop()

#     return ''.join(L)

# def backspace_compare(S, T):
#     return 'true' if backspace(S) == backspace(T) else 'false'


if __name__ == "__main__":
    print(backspace_compare("a#c", "b"))
    # print(backspace_compare("ab#z", "az#z"))
    # print(backspace_compare("ab##", "c#d#"))
