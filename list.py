# list of strings
list = ["balaji", "ravi", "ram"]

#get the list size
n = len(list)

i=0

#loop starts
while i < n :
	print list[i]
	i = i+1
#loop ends

print "\n list after mutable \n"
#list is mutable where as string is immutable

# assign ravi to ravikumar
list[1] = "ravikumar"

print list