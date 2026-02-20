class mathematicsClass:

    def __init__(self,first_num=3,second_num=4):
        self.first_num = first_num 
        self.second_num =second_num

    def addition(self):
        return self.first_num + self.second_num
    
c=mathematicsClass(1,2)
print(c.addition())