def Welcome():
        Menu=open("Menu.txt","a")
        Menu.write("--------------------*********Welcome Home Foods Restaurent*************-----------------------------------------")
        Menu.close()

def Menu_starters():
        Menu=open("Menu.txt","a")
        Serail_no=input("Enter a Number :")
        Food_item=input("Enter a Food item :")
        Price=int(input("Enter a Price of item :"))
        Menu.write(Serail_no+" : "+Food_item+" : "+str(Price))


def Menu_Biryani():
        Menu=open("Menu.txt","a")
        Serail_no = input("Enter a Numnber :")
        Food_item = input("Enter a Food item :")
        Price = int(input("Enter a Price of item :"))
        Menu.write(Serail_no + " : " + Food_item + " : " + str(Price))



def Menu_Pizza():
        Menu=open("Menu.txt","a")
        Serail_no = input("Enter a Numnber :")
        Food_item = input("Enter a Food item :")
        Price = int(input("Enter a Price of item :"))
        Menu.write(Serail_no + " : " + Food_item + " : " + str(Price))

def Menu_Sandwich():
        Menu = open("Menu.txt", "a")
        Serail_no = input("Enter a Numnber :")
        Food_item = input("Enter a Food item :")
        Price = int(input("Enter a Price of item :"))
        Menu.write(Serail_no + " : " + Food_item + " : " + str(Price))


def Menu_Deserts():
        Menu = open("Menu.txt", "a")
        Serail_no = input("Enter a Numnber :")
        Food_item = input("Enter a Food item :")
        Price = int(input("Enter a Price of item :"))
        Menu.write(Serail_no + " : " + Food_item + " : " + str(Price))


def Menu_Burger():
        Menu = open("Menu.txt", "a")
        Serail_no = input("Enter a Numnber :")
        Food_item = input("Enter a Food item :")
        Price = int(input("Enter a Price of item :"))
        Menu.write(Serail_no + " : " + Food_item + " : " + str(Price))

def Menu_Drinks():
        Menu = open("Menu.txt", "a")
        Serail_no = input("Enter a Numnber :")
        Food_item = input("Enter a Food item :")
        Price = int(input("Enter a Price of item :"))
        Menu.write(Serail_no + " : " + Food_item + " : " + str(Price))

def review_of_items(Menu):
        if Serail_no == 1 :
            print(Price)

