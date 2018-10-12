def dnaComplement(s):
    invertor = {
        'A' : 'T',
        'C' : 'G',
        'T' : 'A',
        'G' : 'C'
    }
    result = ''
    s = s[::-1]
    for char in s:
        result += invertor[char]

    return result




s = "ACCGGGTTTT"
test = dnaComplement(s)
print(test)


