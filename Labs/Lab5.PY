print("Hello Nani keep doing your great work")

print("I know you're busy but is it okay if i can get some information about you")

print("How many years old are you?")
birthyear = int(input("year: "))
print("What day you born")
birthdate = int(input("date: "))
print("Can you also tell me what month you were born")
birthmonth = int(input("month: "))


seconds = birthyear * 24 * 60 * 60 * 365 + birthmonth * 30 * 60 + birthdate * 60

print ("you are about" , seconds , "seconds old") 