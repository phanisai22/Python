pp, ch = tuple(map(float, input().split(";")))
coin_value = {
    'PENNY': .01,
    'NICKEL': .05,
    'DIME': .10,
    'QUARTER': .25,
    'HALF DOLLAR': .50,
    'ONE': 1.00,
    'TWO': 2.00,
    'FIVE': 5.00,
    'TEN': 10.00,
    'TWENTY': 20.00,
    'FIFTY': 50.00,
    'ONE HUNDRED': 100.00
}
if ch < pp:
    print("ERROR")
elif ch == pp:
    print("ZERO")
else:
    r = ch - pp

    result = []

    while r > 0:
        r = round(r, 2)
        temp = ''
        temp_val = 0
        for key, value in coin_value.items():
            if value == r:
                result.append(key)
                r -= value
                break;
            elif value > r:
                result.append(temp)
                r -= temp_val
                break
            else:
                temp = key
                temp_val = value

    result.sort()
    print(";".join(result))
