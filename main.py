import CryptRsa
import algorthym
root = "test.txt"
# создает сессию класса с путем
session = CryptRsa.RSA(input_file=root)

# Генерируем массив простых чисел для полу
gen_list = algorthym.GenerateSimpleNumbers()
mass_simple_numbers = gen_list.GenerateList(count_number=100, start_number=17)
simple_numbers = gen_list.GenerateList(count_number=1000, start_number=3)

session.Generate_PP_keys(
    simple_numbers_list=mass_simple_numbers,
    bloc_simple_numbers=simple_numbers
)