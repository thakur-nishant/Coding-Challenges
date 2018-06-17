def identifyTriangle(a,b,c):
    if a == b and b == c:
        return "Equilateral"

    if a+b > c and b+c > a and a+c > b:
        if a == b or b == c or c == a:
            return "Isosceles"
        else:
            return "None of these"

print(identifyTriangle(2,2,1))
print(identifyTriangle(3,3,3))
print(identifyTriangle(3,4,5))
print(identifyTriangle(1,1,3))
print(identifyTriangle(3,5,3))
