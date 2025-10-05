# FILE NAME - compliment_01.py

# NAME: isiah osborn 
# DATE: 2025-10-05
# BRIEF DESCRIPTION:
#   Read a single line of input. If it's exactly "yes" (lowercase),
#   print a compliment. Always print "Thank you for playing." afterward.


########## ENTER YER CODE BELOW THIS LINE ##########


response = input("Would you like a compliment? ")
if response == "yes":
    print("You have wonderful eyes.")
print("Thank you for playing.")




########### END YER CODE ABOVE THIS LINE ###########



########################################
#          SAMPLE OUTPUT
########################################

'''
Would you like a compliment? yes
You have wonderful eyes.
Thank you for playing.
'''


'''
Would you like a compliment? y
Thank you for playing.
'''


'''
Would you like a compliment? Yes
Thank you for playing.
'''


'''
Would you like a compliment? no
Thank you for playing.
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. On a scale of 1 to 10 (where 10 is the hardest), how would you rate this lab?
2/10

2. What was the hardest part of this lab?
Making sure the behavior matched the sample output exactly—only printing the compliment when the input is exactly "yes" (lowercase), and always printing "Thank you for playing." regardless of the answer. Also paying attention to the prompt text and spacing so the outputs line up.

'''
