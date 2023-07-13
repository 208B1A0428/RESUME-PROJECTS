class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node
    
class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        
        #Remove pass and copy the code you had written to add an element.
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node
            
    def insert(self,data,data_before):
        new_data=Node(data)
        if(data_before is None):
            new_data.set_next(self.__head)
            self.__head=new_data
            if(new_data.get_next() is None):
                self.__tail=new_node
        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                
                new_data.set_next(node_before.get_next())
                node_before.set_next(new_data)
                if(new_data.get_next() is None):
                    self.__tail=new_data
            else:
                print("There is no  data belongs to data_before in LinkedList",data_before)
    
    
    def display(self):
        
        #Remove pass and copy the code you had written to display the element(s).
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()
            
    
    def find_node(self,data):
        
        #Remove pass and write the logic to find the node and return the node if found or return None.
        temp=self.__head
        while(temp is not None):
            if(data==temp.get_data()):
                return temp
            temp=temp.get_next()
        return None
        

    def delete(self,data):
        node=self.find_node(data)
        if(node):
            if(node==self.__head):
                if(self.__head==self.__tail):
                    self.__head=self.__tail=None
                self.__head=node.get_next()
            else:
                temp=self.__head
                while(temp):
                    if(temp.get_next()==node):
                        temp.set_next(node.get_next())
                        if(node==self.__tail):
                            self.__tail=temp
                        node.set_next(None)
                        break
                    temp=temp.get_next()
        else:
            print(data,"is not present in Linked list") 
        
                                   
                                           
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return(msg)


def Quick_sort(list1,left,right):
    if(left<right):
        parition_pos=partition(list1,left,right)
        Quick_sort(list1,left,parition_pos-1)
        Quick_sort(list1,parition_pos+1)
        
def partition(list1,left,right):
    i=left
    j=right-1
    temp=list1.get_head()
    z=0
    while(temp):
        z+=1
        if(z==right):
            pivot=temp.get_data()
        temp=temp.get_next()
    while(i<j):
        l=i
        temp=list1.get_head()
        while(temp):
            if(i==l):
                low=temp.get_data()
            temp=temp.get_next()
        while(i<right and low<pivot):
            i+=1
            l+=1
            temp=list1.get_head()
            while(temp):
                if(i==l):
                    low=temp.get_data()
                temp=temp.get_next()
        h=j
        temp=list1.get_head()
        while(temp):
            if(i==h):
                high=temp.get_data()
            temp=temp.get_next()
        while(j>left and high>=pivot):
            j-=1
            h-=1
            temp=list1.get_head()
            while(temp):
                if(h==j):
                    high=temp.get_data()
                temp=temp.get_next()
        if(i<j):
            
    #return i
                
        








#Add all the required element(s)
#Search for the required node
list1=LinkedList()
list1.add(4)
list1.add(2)
list1.add(32)
list1.add(245)
list1.add(77)
temp=list1.get_head()
c=0
while(temp):
    c+=1
    temp=temp.get_next()
Quick_sort(list1,0,c-1)
print(list1)

    