class node:
    def __init__(self,data):
        self.data=data
        self.address=None
class sll:
    def __init__(self):
        self.head=None
sl1=sll()
sl1.head=node("d")
n2=node("h")
n3=node("a")
sl1.head.address=n2
n2.address=n3
temp=sl1.head
while temp!=None:
    print(temp.data)
    temp=temp.address
