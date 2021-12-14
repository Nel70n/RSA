from os import stat_result
import random

class RSA:

    def __init__(self, input_file : str):
        self.file_session = open(input_file)
        self.string_from_file = ""
        for line in self.file_session:
            self.string_from_file += line.replace('\n', '').replace(' ', '').lower()

    # TODO: #1 Написать генерацию публичного и приватного ключа 

    def gcd_extended(self, num1, num2):
        if num1 == 0:
            return (num2, 0, 1)
        else:
            div, x, y = self.gcd_extended(num2 % num1, num1)
        return (div, y - (num2 // num1) * x, x)

    def Generate_PP_keys(self, simple_numbers_list : list, bloc_simple_numbers : list):
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
        

