class firstclass:
    def __init__(self):
        self.text = ""  

    def get_string(self):
        self.text = input()  

    def print_string(self):
        print(self.text.upper())  

obj = firstclass()
obj.get_string()  
obj.print_string()