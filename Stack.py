class Stacks:
    def __init__(self):
        self.list=[]
    def appendd(self):
        a="Hello"
        for i in a:
            self.list.append(i)
        return self.list
    
        """self.list.append("H")
        self.list.append("e")
        self.list.append("l")
        self.list.append("l")
        self.list.append("o")
        return self.list"""
        
    def reverse(self):
        s1=[]
        for i in range(len(self.list)):
            s1.append(self.list.pop())
        return s1
s=Stacks()
print(s.appendd())
print(s.reverse())
