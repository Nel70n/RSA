class GenerateSimpleNumbers:
    def __init__(self, count_number : int, start_number : int):    
        self.number = start_number
        self.return_list = []
        while len(self.return_list) != count_number:
            flag = True

            for divisor in range(2, int(self.number**0.5)+1):
                if self.number % divisor == 0:
                    flag = False
                    break
            if flag:
                self.return_list.append(self.number)
            self.number += 1

        return self.return_list
