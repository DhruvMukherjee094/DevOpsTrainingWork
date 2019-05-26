# Your security team said every  username contains 1 didgit
# for example above user list is not valid we have to loop through the list and digit for the same
users=["user1","user2","user3","user4"]
num = "123"
  #traditional way 
for i in range(0,len(users)):
  users[i]= users[i] + num
print (users)
  
users = [u+num for u in users]
print (users)
  