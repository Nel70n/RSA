class GenerateSimpleNumbers:
    def GenerateList(self, count_number : int, start_number : int):    
        self.number = start_number
        self.return_list = []
        self.bro = count_number
        while len(self.return_list) != self.bro:
            self.flag = True

            for divisor in range(2, int(self.number**0.5)+1):
                if self.number % divisor == 0:
                    self.flag = False
                    break
            if self.flag:
                self.return_list.append(self.number)
            self.number += 1

        return self.return_list
