
#This a program for a chatbot(seven wonders for children)
#Step_1:The bot will start with a greeting and self introduction and ask for the user(child) information like name , age and class etc..
#Step_2:The bot will greet and welcome  the user(child)
#Step_3:Bot will ask what a child want to know about the  seven wonders of the world,it will offer a choice of seven wonders based upon what the bot is designed for.
#Step_4:It will respond to the users input and provides appropriate output.

import datetime
def welcome_user():
    x=datetime.datetime.now()
    if x.hour<12:
        print("Good morning and have a nice day")   #Greeting the user
    elif x.hour==12:
        print("Good afternoon")
    elif x.hour>12 and x.hour<=20:
        print("Good evening")
    else:
        print("Oh,it's late")
welcome_user()
def greetings_user():        #Welcoming and self intro
    print("Hello!,I am neel and welcome to seven wonders.Wow! it's feeling very excited to have you here,i hope you also feeling great.It is a wonderful opportunity")
greetings_user()
def introduce_user():
    print("Enter your name")   #user information
    name=input()
    print("Nice name ")
    print("Enter your current class")
    current_class=input()
    print("Kindly enter your age")
introduce_user()
#1.great wall of china        seven wonders in the world
#2.petra
#3.colosseum
#4.chichn itza
#5.manchu pichu
#6.tajmahal
#7.christ the redeemer
#8.exit
def wonders_describe():         # describe about the wonder
    age=int(input())
    if age<=15:
        print("welcome to wonders")
        while(1):
            print("choose the number ")
            choice=int(input())
            if choice==1:
                print("Welcome to great wall of china.The wall was built to save the country from foreign invasions.",
                "The wall is 13,171 miles long and it tookalmost 2000 years to build and rebuild the wall") 
            elif choice==2:
                print("Welcome to petra.It is situated in the ancient city of jordan in the early nineteenth centuary",
                "More than half of city is carved from one rock.The city is nickednamed as Rose city because it is carved from pink coloured rock") 
            elif choice==3:
                print("Welcome to colosseum.It is an ancient amphitheatre that was built in 80 AD by the great emperor Tiyus Vespasian.It took almost years and 60,000 slaves to complete the structure. In 207 AD a massive fire destroyed the top level of the structure") 
            elif choice==4:
                print("Welcome to chichn itza.Mexico is world famous because of this beautiful city which was built by Mayan civilisation."
                 "The english transalation of the world chichn itza means at the mouth of the well of the itza.The pyramid shaped structure called castillo is the most famous structure") 
            elif choice==5:
                print("Welcome to manchu pichu.It was declared a heritage sitwe in the year 1983 by UNESCO.The city is almost 8000 feet above swa level.")
            elif choice==6:
                print("Welcome to tajmahal.It is built by great Mugal emperor Shah Jehan in the memory of his loving wife,Mumtaz Mahal",
                "The entire structure is made up of marble and 20000 slaves take 20 years to complete the wonder.The original tomb was embellished with precious gemstones,which was looked during the rebellion of 1857 ")
            elif choice==7:
                print("Welcome to christ the redeemer.This is statue of Jesus Christ situated on the Corcovado mountain.If the 22 feet pedastal is excluded,the statue is 125 feet tall.the arms of the strucure are 92 feet wide") 
            elif choice==8:
                print("Bye")
                break
            else:
                print("Select a valid option please..")
    else:
        print("sorry it is designed for kids")
wonders_describe()


