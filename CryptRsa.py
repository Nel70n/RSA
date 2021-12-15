import random

class RSA:
    """
    В классе реализуется ряд заданий, необходимых для сдалчи нам лабы по крипте:
    1. Генерация ключей
    2. Кодирование и декодирование файла
    3. Подписывание файла приватной экспонентой 
    4. Првоерка подписи документа
    """
    def __init__(self, input_file : str):
        self.file_session = open(input_file, encoding='UTF-8')
        self.string_from_file = ""
        for line in self.file_session:
            self.string_from_file += line.replace('\n', '').replace(' ', '').lower()

    def gcd_extended(self, num1, num2):
        """
        
        """
        if num1 == 0:
            return (num2, 0, 1)
        else:
            div, x, y = self.gcd_extended(num2 % num1, num1)
        return (div, y - (num2 // num1) * x, x)

    # TODO: #3 разобраться, какого хуя не работает encode/decode по-человечески.
    def ControlSum(self, message : str):
        self.bin_message = message.encode("utf-8")
        self.resuls_control = 0
        print(self.bin_message)
        for i in range(len(self.bin_message)):
            print(self.bin_message[i], end="")
            self.resuls_control += self.bin_message[i]
        print(self.resuls_control)
        self.resuls_control %= 2
        print(self.resuls_control)
        return self.resuls_control


    def GeneratePPkeys(self, simple_numbers_list : list, bloc_simple_numbers : list):
        """
        
        """
        self.p = 0
        self.q = 0
        while self.p == self.q:
            self.p = simple_numbers_list[random.randint(0,len(simple_numbers_list))]
            self.q = simple_numbers_list[random.randint(0,len(simple_numbers_list))]
        
        self.n = self.p * self.q
        self.phi = (self.p - 1)*(self.q - 1)
        for num in bloc_simple_numbers:
            if self.gcd_extended(self.phi, num)[0] == 1:
                self.e = num
                break
        
        self.d = pow( self.e, -1,  self.phi )
        self.pr_key = open("privite key.txt", "w", encoding="UTF-8")
        self.pu_key = open("public key.txt", "w", encoding="UTF-8")

        self.pu_key.write(str(self.e) + ' ' + str(self.n))
        self.pr_key.write(str(self.d) + ' ' + str(self.n))
        self.pu_key.close()
        self.pr_key.close()
        
    def EncodeFile(self, root_public_key : str):
        """
        
        """
        self.enc_file = open(root_public_key, "r", encoding='UTF-8')
        self.e , self.n = map(int,self.enc_file.readline().split(" "))
        self.enc_message = pow(int(self.string_from_file), self.e, self.n)
        self.enc_message_root = open("encode.txt", "w", encoding="UTF-8")
        self.enc_message_root.write(str(self.enc_message))
        self.enc_message_root.close()
        
    def DecodeFile(self,root_privite_key : str):
        """
        
        """
        self.dec_file = open(root_privite_key, "r", encoding='UTF-8')
        self.d , self.n = map(int,self.dec_file.readline().split(" "))
        self.dec_message = pow(int(self.string_from_file), self.d, self.n)
        self.dec_message_root = open("decode.txt", "w", encoding="UTF-8")
        self.dec_message_root.write(str(self.dec_message))
        self.dec_message_root.close()

    # TODO: #2 доделать так, чтобы подпись высчитывалась по контрольной сумме.
    def DigitalSignature(self, privite_key_root : str):
        self.file_privite = open(privite_key_root)
        self.message_encod = self.ControlSum(self.string_from_file)
        self.d , self.n = map(int,self.file_privite.readline().split(" "))
        # self.s = pow(self.string_from_file, self.d, self.n)

