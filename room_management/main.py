from room_management import *
def function():

    print("_"*33)
    a = "WELCOME TO OUR MAWA BRO's ROOMs"
    print(a)
    print("_"*len(a))
    print("1. Avalible rooms")
    print("2. custmor registation")
    print("3. check in")
    print("4. food services")
    print("5. bill payment")
    print("6. booking history")
    print("7. check out")
    print("8. exit")
    while True:
        user = input("enter:")
        if user.isdigit():
            list1 = ["1","2","3","4","5","6","7","8"]
            if user in list1:
                break
            else:
                print("invalid option:")
        else:
            print("input only numbers")

    if user == "1":
        rooms()
        function()
    elif user == "2":
        registration()
        function()
    elif user == "3":
        check_in()
        function()
    elif user  == "4":
        food_service()
        function()
    elif user == "5":
        generate_bill()
        function()
    elif user == "6":
        view_booking_history()
        function()
    elif user == "7":
        check_out()
        function()
    else :
        print("exit")
function()
        
        
