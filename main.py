import CryptRsa
import algorthym

# Создаем сессию класса с путем – исходный файл
root = "test.txt"
session = CryptRsa.RSA(input_file=root)

# Генерируем массив простых чисел для полу
gen_list = algorthym.GenerateSimpleNumbers()
mass_simple_numbers = gen_list.GenerateList(count_number=100, start_number=17)
simple_numbers = gen_list.GenerateList(count_number=1000, start_number=3)

"""
# Генерация ключей
session.Generate_PP_keys(
    simple_numbers_list=mass_simple_numbers,
    bloc_simple_numbers=simple_numbers
)

# Кодирование файла
session.EncodeFile(
    root_public_key= "public key.txt"
)

# Создаем сессию класса с путем – закодированный файл
root = "encode.txt"
session = CryptRsa.RSA(input_file=root)

# Декодирование файла 
session.DecodeFile(
    root_privite_key="privite key.txt"
)
"""
session.DigitalSignature(
    privite_key_root="privite key.txt"
)