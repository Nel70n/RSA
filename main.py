import CryptRsa
import GenerateSimpleNumber
root = "test.txt"
session = CryptRsa.RSA(input_file=root)

mass_simple_numbers = GenerateSimpleNumber.GenerateSimpleNumbers(100, 17)
print(mass_simple_numbers)