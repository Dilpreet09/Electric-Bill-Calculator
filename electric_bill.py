print ("Electric Bill Calculator ---> Made by Dilpreet Singh Kohli\n")            #Header

print ("--Electricity Per Unit Charges--\n")

print ("1 to 100 units   -  10rs/Unit")
print ("100 to 200 units -  15rs/unit")
print ("200 to 300 units -  20rs/unit")
print ("Above 300 units  -  25rs/unit\n")

unit = int(input("Please Enter Your Units : "))                              #Unit

if unit <= 100:                                                              #unit less than equal to 100
    output = unit * 10
    print (f"You units is {unit} and total electric bill is {output}rs.")
elif unit in range(101,201):                                                 #unit in range 101-200
    subtract = unit - 100
    add = (unit - subtract)*10 + (subtract)*15
    print(f"You units is {unit} and total electric bill is {add}rs.")
elif unit in range(201,301):                                                  #unit in range 201-300
    subtract = unit - 200
    add_1 = 100 * 10
    add_2 = 100 * 15
    output = (100 * 10) + (100 * 15) + (subtract)*20
    print(f"You units is {unit} and total electric bill is {output}rs.")
elif unit >= 300:                                                              #unit more than 300
    subtract = unit - 300
    output = (100 * 10) + (100 * 15) + (100 * 20) + (subtract)*25
    print(f"You units is {unit} and total electric bill is {output}rs.")


