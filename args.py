def display(length, breadth, height=20, color='black') : #required arguments should be first from left
	print " the length is ", length
	print " the dimension in lXbXh ", length,"X",breadth,"X", height
	print "color",color
	


display(52,96) # atleast have to give the requied arguments if we call display() it will show error
display(1,1,1,"red")