import requests


print ("Hello World !");

#print "comments";

'''
print "xyz"
print "abc"
'''

name = "Venu"

print "Hi "+name

quote = "You are welcome and remember you are unique";

print ("Arrey %s How are you." %name);

grocery_list = ["banana","juice","tomatoes","yogurt"]

print grocery_list[2]


number1 = 400; number2=500;

if(number1 + number2 == 900) :
    print "number is in the range"
elif (number1 <400 and number2>300 ):
    print "number is not in the range"
else: print "not a number"

# how to end the for loop
'''
for x in range(0, 2):
    print ("number =", x)
'''
for x in range(0, 2):
    print ("number =", x)

print ("number =")





def addNumbers(num1, num2):
            sumNum = num1 + num2
            return sumNum

print ('total = ',addNumbers(20,3))
#print sumNum

name1="Venu"
print ("This is an example of format. My name is {}".format(name1))
print ("This is an example of . My name is %s" %name1)


r = requests.get("https://api.github.com/events")

print ("status_code = ", r.url())