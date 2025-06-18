#roman to integer
roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
s = "MCMXCIV"
n = len(s)
i = 0
int = 0
while i<n:
    if i+1<n and roman[s[i]]<roman[s[i+1]]:
        int+=roman[s[i+1]]-roman[s[i]]
        i+=2
    else: 
        int+=roman[s[i]]
        i+=1
print (int)

#integer to roman
int_to_roman = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}

def int_to_roman_fn(num):
    res = ''
    for val in int_to_roman:
        while num >= val:
            res += int_to_roman[val]
            num -= val
    return res

print (int_to_roman_fn(1994)) 