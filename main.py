import CryptRsa
import algorthym
root = "test.txt"
session = CryptRsa.RSA(input_file=root)

mass_simple_numbers = algorthym.GenerateSimpleNumbers()
mass_simple_numbers = mass_simple_numbers.GenerateList(count_number=10000, start_number=17)
print(len(mass_simple_numbers))