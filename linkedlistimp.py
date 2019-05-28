class node:
    def __init__(self,data):
        self.data=data
        self.nextt=None
class sll:
    def __init__(self):
        self.head=None
        
    def createnode(self):
        val=input("Enter data value for node:")
        temp=node(val)
        if(self.head==None):
            self.head=temp
            return
        a=self.head
        while(a!=0):
            a=a.nextt
        a.nextt=temp
        
    def insertatbeg(self):
        val=input("Enter data value for node:")
        temp=node(val)
        temp.nextt=self.head
        self.head=temp
        
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.nextt

    def deleteatbeg(self):
        temp=self.head
        self.head=self.head.nextt
        temp.nextt=None
        
    def deleteatend(self):
        if temp.nextt==None:
            remove(temp.data)
            prev=None
        else:
            temp=temp.nextt
obj=sll()
j=int(input("enter num of nodes to be created:"))
for i in range(j):
    obj.createnode()


                
