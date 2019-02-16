# Jalil Douglas
#DSCI 1530--Computational Thinking and Programming
#Program No.0
#Name of Program -- Program Assignment 2 Program No.2
#Student's grade
# Due 2/15/2019

#What was the lowest grade you could've possibly get
lowGrade = float(input ("\nWhat was the lowest grade on the test? \n\n"))
#What was the grade you recieved
yourGrade = float(input ("\nWhat was your original grade? \n\n"))
#
topGrade = float(input("\nWhat is the highest grade on the test you can recieve?\n\n"))
curve = (topGrade - lowGrade) / 4
curvedGrade = yourGrade + curve
topCurvedGrade = topGrade + curve

if curvedGrade < 60:
 print ("\nAre you serious right not? You're going to tutoring. How do you get a 'F.' Your curved grade is",
curvedGrade, "no child of mine is going to fail highschool.")
elif curvedGrade < 70:
 print ("\nYea bud you're definetly not getting into harvard with a", curvedGrade, ". You got a 'D.'")
elif curvedGrade < 80:
 print ("Your curved grade is", curvedGrade, " -- You can do better than this 'C'.")
elif curvedGrade < 90:
 print ("\nDo Better-- a curved grade of", curvedGrade, ", just a 'B' and not an 'A.' If you want to get into college you need to get higher grades")
elif curvedGrade < 100:
 print ("\nYour curved grade is ", curvedGrade, " -- an 'A.' well well well looks like you might actually get an 'A' in this course.")

elif curvedGrade > 100 and curvedGrade < topCurvedGrade:
 print ("You recieved the highest score in the class. Your grade is", curvedGrade, " and you've earned an A+.")

