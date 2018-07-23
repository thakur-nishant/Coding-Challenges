def getSpreadsheetNotation(n):
    row = n // 702 + 1
    col = n % 702
    if col == 0:
        return str(row-1)+"ZZ"
    A_to_Z = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

    result = ""
    while col > 0:
        col -= 1
        r = col % 26
        col = col // 26
        result = str(A_to_Z[r]) + result

    return str(row)+result

n = 702
print(getSpreadsheetNotation(n))
