import CryptRsa
import algorthym
root = "test.txt"
session = CryptRsa.RSA(input_file=root)

mass_simple_numbers = algorthym.GenerateSimpleNumbers.GenerateList(count_number=100, start_number=17)
print(mass_simple_numbers)