import os
os.system('cls')

print "Welcome to the launch pad!"
print
print "Let's prepare for launch."
print

def countdown(n):
    if n == 0:
        print "BLASTOFF!"
    else:
        print n
        print
        pause = raw_input()
        countdown(n-1)

prompt = "How long is the countdown? "
x = input(prompt)
countdown(x)
