import smtplib
def service(Id, mobile):
    global rooms_type
    global rooms_booked
    global rooms_status
    if rooms_booked == 4:
        print("oops ! All rooms are booked")
        return
    if rooms_booked < 4:
        for i in rooms_status:
            print(i, "=", rooms_type[i])
        select = int(input("enter which room you want : "))
        if rooms_status[select] == 1:
        # consider they will pay money when they checkout
            details = "NAME : {}\nMOBILE : {}\nROOM NO : {}\n ".format(Id, mobile, rooms_status[select])
            user_file = open('Hotel_register.txt', 'a')
            user_file.write(details)
            user_file.close()
            gmail=smtplib.SMTP_SSL("smtp.gmail.com",465)
            gmail.login("quizarre2k21@gmail.com","18MTL127")
            gmail.sendmail("quizarre2k21@gmail.com","sathish19062001@gmail.com","message from hotel python hi {} you booked room no {} {} room".format(Id,select,rooms_type[select]))
            gmail.quit()
            print("your room successfully booked now its all yours")
            rooms_status[select] = 0
            rooms_booked += 1
        else:
            print("sorry sir , room you chose currently engaged")
            return


def new_admin():
    print("enter the admin detail")
    name = input("name OR user id : ")  # should greater than 18
    age = int(input("age : "))
    phone = input("contact info : ")
    print("passcode minimum 6 chars")
    password: str = input("give your passcode : ")
    details = "\nNAME : {}\nAGE :{}\nCONTACT : {}\nPASSWORD : {}\n".format(name, age, phone, password)
    admin_file = open('Admin_details.txt', 'a')
    admin_file.write(details)
    admin_file.close()


def admin_login():
    print("welcome to admin login page")
    print("just follow few steps you will get all you need")
    Id = input("enter your user id : ")
    passcode = input("passcode : ")
    file=open('Admin_details.txt', 'r')
    af=file.read()
    if (Id in af) and (passcode in af):
            print("Login successfully now you will redirected to user page")
            file.close()
            admin_permission()
    else:
        file.close()
        print("sorry , your id or passcode invalid")
        option = (input("do you want to continue Y/N : "))[0]
        if option == 'y' or option == 'Y':
            return admin_login()
        else:
                return


def new_user():
    print("thanks for choosing HOTEL python")
    print("enter you detail")
    name = input("name OR user id : ")  # should greater than 18
    age = int(input("age : "))
    phone = input("contact info : ")
    print("passcode minimum 6 chars")
    password: str = input("give your passcode : ")
    details = "\nNAME : {}\nAGE :{}\nCONTACT : {}\nPASSWORD : {}\n".format(name, age, phone, password)
    user_file = open('user_details.txt', 'a+')
    if (name not in user_file.read()) and (password not in user_file.read()):
        user_file.write(details)
        return
    else:
        user_file.close()
        print("name and pass word already in the file")
        return new_user()



def user_login():
    print("good to see you again ")
    print("just follow few steps you will get all you need")
    Id = input("enter your user id : ")
    passcode = input("passcode : ")
    file=open('user_details.txt', 'r')
    uf=file.read()
    if (Id in uf) and (passcode in uf):
        mobile = input("enter your mobile number : ")
        print("Login successfully now you will redirected to user page")
        file.close()
        service(Id, mobile)
    else:
        file.close()
        print("sorry , your id or passcode invalid")
        option = (input("do you want to continue Y/N : "))[0]
        if option == 'y' or option == 'Y':
            return user_login()
        else:
            return


def admin_permission():
   while(1):
        global rooms_booked
        global rooms_status
        admin_choice = int(input("1->add user\n2->add admin\n3->booking details\n4->cancel_rooms\n5->return"))
        if admin_choice == 1:
            new_user()
        elif admin_choice == 2:
            new_admin()
        elif admin_choice == 3:
            print("\nno of rooms booked\n", rooms_booked)
        elif admin_choice == 4:
            for i in rooms_status:
                if rooms_status[i] == 0:
                    rooms_status[i]=0
                    rooms_booked-=1
        elif admin_choice == 5:
            return




rooms_booked = 0
rooms_type = {
    1: 'single bed non AC',
    2: 'double bed non Ac',
    3: 'single bed with AC',
    4: 'double bed with AC'

}
rooms_status = {
    1: 1,
    2: 1,
    3: 1,
    4: 1
}  # 1 means available 0 means already booked
while (1):
    print("HI , WELCOME TO HOTEL PYTHON")
    print("enter your choice\n1->Login as Admin\n2->Login as regular user\n3->new user")
    choice = int(input())
    if choice == 1:
        admin_login()
    elif choice == 2:
        user_login()
    elif choice == 3:
        new_user()
