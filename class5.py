
#Format() Method
words="My name is {} and I am {} years old.".format("shazia", 25) #posiion formating
print(words)


words="My name is {1} and I am {0} years old.".format(25, "shazia") #index formating
print(words)


words="My name is {name} and I am {age} years old.".format(name="shazia", age=25)#parameters
print(words)


words="My name is {name:^25} and I am {age} years old.".format(name="shazia", age=25)
print(words)
