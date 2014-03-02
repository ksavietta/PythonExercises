numGuesses = 0
low = 0
high = 100
guess = (high+low)/2
reply = "nothing yet"

print "Please think of a number between {0} and {1}!".format(low, high)

while reply != "c":
    guess = int((high + low)/2.0)
    print "Is your secret number {}?".format(str(guess))
    reply = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    numGuesses += 1
    if reply == "c":
        break
    elif reply == "l":
        low = guess
    elif reply == "h":
        high = guess
    else: 
        print "Sorry, I did not understand your input."
    

print "Game over. Your secret number was: {}".format(str(guess))