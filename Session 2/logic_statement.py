print "May I ask your age?"
age = int(raw_input())

if age >= 18 and age < 25:
    print "You can rent a car with extra fee"
elif age >= 25:
    print "You can rent a car"
else:
    print "You cannot rent a car"