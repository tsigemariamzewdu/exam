def number1program():
    newlist=[]
    newdict={}
    newlist1=[]
    
    numbers=input("enter the elements:")
    target=int(input("which element are you searchingn for : "))
    newnum=numbers.split(",")
    for i in newnum:
        newlist.append(int(i))
    for i in newlist:
        count=0
        
        if i==target:
            count += 1
    return count     
        

number1program()