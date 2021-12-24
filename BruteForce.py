import algorthym
TRUE_MESSAGE     = 1558
ENCODE_MESSAGE   = 33960

def gcd_extended(num1, num2):
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return (div, y - (num2 // num1) * x, x)

def GeneratePK(p, q):
    n = q * p
    phi = (p - 1)*(q - 1)
    for num in simple_numbers:
        if gcd_extended(phi, num)[0] == 1:
            e = num
            break
        
    d = pow(e, -1, phi)
    theory_decode = pow(ENCODE_MESSAGE, d, n)
    if theory_decode == TRUE_MESSAGE:
        print(f'Key was founded!\nIs: {d}, {n}')

 
session = algorthym.GenerateSimpleNumbers()
simple_numbers = session.GenerateList(count_number=1000, start_number=3)
number_list = session.GenerateList(count_number=100, start_number=17)

for p in number_list:
    for q in number_list[number_list.index(p):]:
        if p == q:
            continue
        GeneratePK(p=p, q=q)

