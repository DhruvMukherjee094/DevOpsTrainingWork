#!/usr/local/bin/python3.6
users = ["user1","user2","user3"]
print (users[0])
#Accessing last element in list
print (users[len(users)-1])
print (users[-1])
print (users[-2])
users[1]= "jdoe"
users.append('peter')
print(users)
print (sorted(users))



#Add or move elements in the list
users[1] = "jeff"
print (users)
users.append("peter")
print (users)
 
users=[]
users.append("mahesh")
print(users)
 
 #insert add an item at specific index
users.insert(1,"mary")
users.remove("mahesh")
 
print (users)
 
 ###########################Looping####################################
users =[]
users.append("ahmad")
users.append("john")
users.append("linda")
users.insert(1,"mary")
users.append("john")
print (users)
#Sorting a list
#users.sort() #This will sort a list
sorted_users = sorted(users)
print (sorted_users)
print (users)
