class node:
    def __init__(self,data):
        self.data=data
        self.nextt=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        temp=node(data)
        temp.nextt=self.head
        self.head=temp
    def delatbeg(self):
        temp=self.head
        if(temp!=None):
            self.head=self.head.nextt
            temp.nextt=None
        else:
            print("no elements to print")
    def insertatend(self,data):
        temp=node(data)
        if self.head==None:
            self.head=temp
            return
        last=self.head
        while(last.nextt):
            last=last.nextt
        last.nextt=temp

    def delatend(self):
        temp=self.head
        if(temp!=None):
            if temp.nextt==None:
                self.head=temp=None
            else:
                prev=temp
                if(temp.data!=None):
                    while(temp.nextt!=None):
                        prev=temp
                        temp=temp.nextt
                    prev.nextt=None
            
        else:
            print("no elements to print")

    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.nextt
sl1=sll()
#sl1.head=node("None")
ch=0
while ch!=6:
    print("1.insertion at beginning,2.deletion at beginning , 3.display, 4.insertion at end,5.deletion at end ,6.exit")
    ch=int(input())
    if ch==1:
        print("enter the value to insert")
        data=input()
        sl1.insertatbeg(data)
        sl1.display()
    elif ch==2:
        sl1.delatbeg()
        sl1.display()
    elif ch==3:
        sl1.display()
    elif ch==4:
        print("enter the value to insert")
        data=input()
        sl1.insertatend(data)
        sl1.display()
    elif ch==5:
        sl1.delatend()
        sl1.display()
    
    
