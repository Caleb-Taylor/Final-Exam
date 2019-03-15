''''
#Caleb Taylor
#3.7.19
This program tells basketball players how many shots they shoot
'''

name = input('What is your name?:')  # name and how many shots they take
shots = input('How many shots do you take?:')


def question(hooper, shots):
    print('\n'+hooper, 'shoots', shots, ) #Call the name and shot number


question(name, shots)#this defines the variable


def list():  # define my list of questions
    name = input('What is your name?:')  # name and shot number

    shots = input('How many shots do you take?:')
    print(name, 'shots', shots+'\n')


i = int(input('\n'"how many hoopers are you asking for: "))  # how many people are you asking for

for i in range(i):  # run my questions until the user is done
    list()

while_attempt = input('if you would like to add more hoopers type "yes":')  # ask if you want to do another hooper
'''

the point of the while loop is to see if the user is gonna enter another hooper
'''
if while_attempt == 'yes':  # if they said yes keep it going
    while True:
        list()
        stop = input('would you like to be done then type done if not type no: ')
        if stop == 'done': break