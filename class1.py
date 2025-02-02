class MyClass:
    def __init__(self):
        self.text = ""  

    def get_string(self):
        self.text = input()  

    def print_string(self):
        print(self.text.upper())  

obj = MyClass()
obj.get_string()  
obj.print_string()