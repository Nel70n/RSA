class RSA:

    def __init__(self, input_file : str):
        self.file_session = open(input_file)
        self.string_from_file = ""
        for line in self.file_session:
            self.string_from_file += line.replace('\n', '').replace(' ', '').lower()
        