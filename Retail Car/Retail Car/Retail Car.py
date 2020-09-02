cars=["mercedes","wolkswagen","bmw"]

mercedes=[   ["A180","2019",[4,120]]   ]
bmw=[  ["3.18","2018",[9,140]]  ,  ["5.20","2017",[3,210]]   ]
wolkswagen=[  ["Passat","2014",[3,120]]   ]

print("Welcome to our Car Rental Firm")
print("Our Car Brands: ",cars)
true_value=0

def cost_of_rent(car_brand,car_model,rent_days):
   
    if car_model==car_brand[0][0]:
        return car_brand[0][2][1]*rent_days

    elif car_model==car_brand[1][0]:
        return car_brand[1][2][1]*rent_days 

def rent(brand):
    model=input("Which model do you want: ")
    day=int(input("How mand days do you rent this car: "))
    print("Cost of rent: ",cost_of_rent(brand,model,day))


while true_value==0:

    brand=input("Enter your selection: ")
    
    if brand=="mercedes":
        true_value=1
        print("Model:{} Year:{}".format(mercedes[0][0],mercedes[0][1]))
        rent(mercedes)
      

    elif brand=="wolkswagen":
        true_value=1
        print("Model:{} Year:{}".format(wolkswagen[0][0],wolkswagen[0][1]))
        rent(wolkswagen)
        

    elif brand=="bmw":
        true_value=1
        for i in range(2):
            print("Model:{} Year:{}".format(bmw[i][0],bmw[i][1]))
        rent(bmw)

    elif brand=="exit":
        true_value=1
        print("")
    
    else:
        print("Please enter valid value")
