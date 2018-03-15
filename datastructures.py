# function accepts variable, list, map(dictionaries)


def display(name, *languagesknown, **skillsets) :

	print "Welcome ",name, "!!!"
	print "\n Languages known\n"
	
	for i in languagesknown : 
		print i
	
	print"\n Skill sets\n"
	
	keys = sorted(skillsets.keys())
	
	for i in keys :
		print i, " : " , skillsets[i]
	

display("balaji",
	"English","Malayalam","Tamil",
		java="spring,spring boot, grails",
		dotnet="WCF,WPF,C#",
		javascript="angular,dojo")