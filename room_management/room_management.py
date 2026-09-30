room_no = [101,102,103,104,105]
room = [["type:duplex","prize:500","floor:1"],["type:duplex","prize:500","floor:1"],["type:duplex","prize:600","floor:2"],["type:duplex","prize:600","floor:3"],["type:single shear","prize:700","floor:4"]]
def rooms():
    for i in range(len(room_no)):
        print(f"{i+1}.room_no:{room_no[i]}")
        print("-"*10)
        for j in room[i]:
            print(' ',j)
        print()
l = []
from datetime import date
def registration():
    global l
    while True:
        name = input("enter name:")
        if name.isalpha():
            break
        else:
            print("name must be alphabets")
    while True:
        ph_no = input("phone number:")
        if ph_no.isdigit():
            if len(ph_no) == 10:
                break
            else:
                print("invalid mobile number")
        else:
            print("number not charectors")        
    while True:
        id_proof = input("id_proof:")
        if id_proof.isalnum():
            if len(id_proof) == 12:
                break
            else:
                print("invalid id proof")
        else:
            print("invalid")
    entity ={
        
            "name" : name,
            "ph_no" : ph_no,
            "id_proof": id_proof,
            "data":str(date.today())
            }
    l.append(entity)
    print(l)
cus_r =[]
number_hr ={}
def check_in():
    cus_r1 = []
    rooms()
    length_1 = len(room_no)
    while True:
        a = input("enter how many rooms you want:")
        if int(a) <= len(room_no):
            if a.isdigit():
                r = int(a)
                if r <= length_1:       
                    for i in range(r):
                        while True :
                            a_user = input()
                            if a_user.isdigit():
                                serial_no = ["1","2","3","4","5"]
                                if a_user in serial_no:
                                    break
                                else :
                                    print("invalid input:")
                            else :
                                print("invalid input:")
                        while True:
                            user_stay= input("enter stay time:")
                            if user_stay.isdigit():
                                break
                            else:
                                print("invali input")
                        cus_r1.append(int(a_user))
                        a = length_1 -r
                    for i in cus_r1:
                        if i in serial_no:
                            serial_no.remove(i)
                    cus_r11 = set(cus_r1)
                    res = [val for i, val in enumerate(room_no,start =1) if i in cus_r11]
                    for i in res:
                        key = i
                        cus_r.append(i)
                        if key in cus_r:
                            number_hr[key] = user_stay
                    res4 = [val for i, val in enumerate(room_no,start =1) if i in cus_r11]
                    for i in res4:
                        print(f"room_no:{i}")
                    for i in cus_r:
                        if i in room_no:
                            room_no.remove(i)
                    if a >0:
                        print("*"*10)
                        print("avalibe rooms")
                        print("*"*10)
                        res1 = [val for i, val in enumerate(room,start =0) if i not in cus_r11] 
                        res2 =[val for i, val in enumerate(room_no,start =0) if i not in cus_r11]
                    
                        for i in range(len(res2)):
                            print(f"room_no:{res2[i]}")
                            for j in room[i]:
                                print(j)
                        break
                    else :
                        print("-"*17)
                        print("no avalible rooms")
                        break
                else :
                    print(f"number of room avalible :{length_1}")
            else :
                print("invalid input")
        else :
            print("no rooms avalible")
            break
food_details={}
breakfast ={"idly":40,"dosa":35,"egg dosa":45,"onion dosa":40,"vada":30,"upma dosa":50}
lunch = {"nonvegmeal":180,"vegmeal":120,"biriyani":280,"familybriyani":750,"firedrice":110,"nudies":90,"chickenfiredrice":160}
dinner = {"nonvegmeal":180,"vegmeal":120,"biriyani":280,"familybriyani":750,"firedrice":110,"nudies":90,"chickenfiredrice":160}
price = 0
total_cost =0
def food_service():
    global total_cost
    list1 =["1.Breakfast","2.Lunch","3.Dinner"]
    for i in list1:
        print(i)
    while True:
        n = input("enter your option")
        if n.isdigit():
            if n in ["1","2","3"]:
                pass
                break
            else:
                print("invalid input")
        else:
            print("enter valid option")
    if int(n) == 1:
        b="Breakfast item list:"
        print(b)
        print("-"*len(b))
        for i in breakfast:
            print(f"{i.title():10} :${breakfast[i]}")
        while True:
            user11 = input("enter room number")
            if user11.isdigit():
                if int(user11) in cus_r:
                    def food_selection():
                        global total_cost
                        while True:
                            select_food = input("enter food:")
                            if select_food.isalpha():
                                break
                            else:
                                print("invalid food")
                        while True:
                            quantity = input("enter quantity:")
                            if quantity.isdigit():
                                break
                            else:
                                print("invalid quantity")
                        cost = breakfast[select_food]
                        t = cost * int(quantity)
                        total_cost += t
                    food_selection()
                    while True:
                        user = input("you want one more food(yes/no):")
                        if user.lower() =="no":
                            break
                        else:
                            food_selection()
                    food_details[user11] = total_cost
                    break
                elif int(user11) not in cus_r:
                    print("enter correct room number is not occuried")
                    print("go and check in first ")
                    break
            else:
                print("room number must be digits")
        
        
        
            
        
    
        
            
                
    elif int(n) == 2:
        l="lunch item list:"
        print(l)
        print("-"*len(l))
        for i in lunch:
            print(f"{i.title() :10} :${lunch[i]}")
        while True:
            user11 = input("enter room number")
            if user11.isdigit():
                if int(user11) in cus_r:
                    if user11 in food_details.keys():
                        def food_selection():
                            global total_cost
                            global food_details
                            while True:
                                select_food = input("enter food:")
                                if select_food.isalpha():
                                    break
                                else:
                                    print("invalid food")
                            while True:
                                quantity = input("enter quantity:")
                                if quantity.isdigit():
                                    break
                                else:
                                    print("invalid quantity")
                            cost = lunch[select_food]
                            t1 = cost * int(quantity)
                            total_cost += t1
                        food_selection()
                        while True:
                            user = input("you want one more food(yes/no):")
                            if user.lower() =="no":
                                break
                            else:
                                food_selection()
                        food_details[user11] = total_cost
                        break
                    else:
                        def food_selection():
                            global price
                            while True:
                                select_food = input("enter food:")
                                if select_food.isalpha():
                                    break
                                else:
                                    print("invalid food")
                            while True:
                                quantity = input("enter quantity:")
                                if quantity.isdigit():
                                    break
                                else:
                                    print("invalid quantity")
                            cost = lunch[select_food]
                            t = cost * int(quantity)
                            price += t
                        food_selection()
                        while True:
                            user = input("you want one more food(yes/no):")
                            if user.lower() =="no":
                                break
                            else:
                                food_selection()
                        food_details[user11] = price
                        break
                elif int(user11) not in cus_r:
                    print("enter correct room number is not occuried")
                    print("check in first!")
                    break
            else:
                print("room number must be digits")
                    
            





                
    elif int(n) == 3:
        d="dinner item list:"
        print(d)
        print("-"*len(d))
        for i in dinner:
            print(f"{i.title() :10} :${dinner[i]}")
        while True:
            user11 = input("enter room number")
            if user11.isdigit():
                if int(user11) in cus_r:
                    if user11 in food_details.keys():
                        def food_selection():
                            global total_cost
                            global food_details
                            while True:
                                select_food = input("enter food:")
                                if select_food.isalpha():
                                    break
                                else:
                                    print("invalid food")
                            while True:
                                quantity = input("enter quantity:")
                                if quantity.isdigit():
                                    break
                                else:
                                    print("invalid quantity")
                            cost = dinner[select_food]
                            t1 = cost * int(quantity)
                            total_cost += t1
                        food_selection()
                        while True:
                            user__1 = input("you want one more food(yes/no):")
                            if user__1.lower() == "no":
                                break
                            else:
                                food_selection()
                        food_details[user11] = total_cost
                        break
                    else:
                        def food_selection():
                            global price
                            while True:
                                select_food = input("enter food:")
                                if select_food.isalpha():
                                    break
                                else:
                                    print("invalid food")
                            while True:
                                quantity = input("enter quantity:")
                                if quantity.isdigit():
                                    break
                                else:
                                    print("invalid quantity")
                            cost = dinner[select_food]
                            t = cost * int(quantity)
                            price += t
                        food_selection()
                        while True:
                            user = input("you want one more food(yes/no):")
                            if user.lower() =="no":
                                break
                            else:
                                food_selection()
                        food_details[user11] = price
                        break
                elif int(user11) not in cus_r:                    
                    print("enter correct room number is not occuried")
                    print("check in first")
                    break
            else:
                print("room number must be digits")
from datetime import date
def generate_bill():
    global t
    while True:
        user = input("how many roomsr")
        if user.isdigit():
            break
        else:
            print("invalid input")
    for i in range(int(user)):
        while True:
            n = input("enter room number:")
            if int(n) in cus_r:
                a = "mawa bro's bills"
                print("*"*30)
                print(f"Room no:{cus_r[i]}{" "*5}date:{date.today()}")
                print("*"*30)
                print(f"details:{" "*9} amount")
                print("-"*30)
                hr = int(number_hr[int(n)])
                print(f"number_hr:{hr:12}")
                for idx, i in enumerate(room,start =1):
                    if int(user) == idx:
                        price = i[1].split(":")[1]
                        print(f"room_rent:{" "*8} {price :1}")
                if n in food_details.keys():
                    food =food_details[n]
                    print(f"food_amount:{food:9}")
                else:
                    food_cost = 0
                    print(f"food_amount:{food_cost:8}")
                print("-"*30)
                service_charges = 80
                gst = 30
                maintanace =100
                print(f"service_charges:{service_charges:5}")
                print(f"gst:{gst :17}")
                print(f"maintences:{maintanace:11}")
                print("-"*30)
                total_amount = (int(hr)*int(price))+food+service_charges+gst+maintanace
                t+=total_amount
                print(f"total_amount:{t:10}")
                print("")
                break
            elif n not in cus_r:
                print(f"{n } is not check in state")
                print("go to check in option!")

                break
            else:
                print("invalid input:")
from datetime import date
t = 0
def view_booking_history():
    global t
    while True:
        user = input("how many roomsr")
        if user.isdigit():
            break
        else:
            print("invalid input")
    for i in range(1,int(user)+1):
        while True:
            n = input()
            if n.isdigit():
                if int(n) in cus_r:
                    print("")
                    print("view_booking_history")
                    print("-"*30)
                    print(f"room_no:{n}{" "*10}data:{date.today()}")
                    print("-"*30)
                    a = number_hr[int(n)]
                    print(f"number of hr:{" "*6}{a}")
                    if n in food_details.keys():
                        food =food_details[n]
                        print(f"food_amount:{food:9}")
                    else:
                        food_cost = 0
                        print(f"food_amount:{food_cost:8}")
                    for idx, i in enumerate(room,start =1):
                        if int(user) == idx:
                            price = i[1].split(":")[1]
                            print(f"room_rent:{" "*8} {price :1}")
                    print("-"*30)
                    service_charges = 80
                    gst = 30
                    maintanace =100
                    print(f"service_charges:{service_charges:5}")
                    print(f"gst:{gst :17}")
                    print(f"maintences:{maintanace:11}")
                    print("-"*30)
                    total_amount = (int(a)*int(price))+food+service_charges+gst+maintanace
                    t+=total_amount
                    print(f"total_amount:{t:10}")
                    print("")
                     
                    break
                elif int(n) not in cus_r:
                    print(f"{n } is not check in state")
                    print("go to check in option!")
                    break
                else:
                    print("invalid input")
            else:
                print("invalid input")
def check_out():
    while True:
        n = input("enter room numberr:")
        if n.isdigit():
            if int(n) in cus_r:
                cus_r.remove(int(n))
                if int(n) in number_hr:
                    del number_hr[int(n)]
                if n in food_details.keys():
                    del food_details[n]
                print("records deleted sucessfully:")
                break
            elif int(n) not in cus_r:
                print(f"{n } is not check in state")
                print("go to check in option!")
                break
            else:
                print("invalid input")
        else:
            print("invalid input:")
def check_out():
    while True:
        n = input("enter room numberr:")
        if n.isdigit():
            if int(n) in cus_r:
                cus_r.remove(int(n))
                if int(n) in number_hr:
                    del number_hr[int(n)]
                if n in food_details.keys():
                    del food_details[n]
                print("records deleted sucessfully:")
                break
            elif int(n) not in cus_r:
                print(f"{n } is not check in state")
                print("go to check in option!")
                break
            else:
                print("invalid input")
        else:
            print("invalid input:")
    
