def heron(a, b, c):
    perimeter = a + b + c 
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

def desempacota(params):
    return heron(*params)

triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37)
]

print(list(map(desempacota, triangulos)))