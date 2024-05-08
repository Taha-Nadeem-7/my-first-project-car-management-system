#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import time
while True:
    print()
    print("Car Show Management System")
    print("Press '1' to Add Car in inventory")
    print("Press '2' to View Cars in inventory")
    print("Press '3' to Sell Car")
    print("Press '4' to add employee detail")
    print("Press '5' to see employee detail")
    print("Press '6' to see details sales and about car that have been sold")
    print("Press '7' to Sign out")
    choice = input("Enter your choice: ")
    print()
    try:
        if choice=="1":
            print("-------Adding Car to Inventory-------")
            print()
            car_id = input("Enter the ID of the car to add: ")

            # Check if the car ID is already used
            infile = open("carrrrrrssssss.txt", "r+")
            lines = infile.readlines()
            infile.close()
            existing_ids = [eval(detail)[5] for detail in lines]
            if car_id in existing_ids:
                print("This Car ID is already used. Please enter a new ID.")
                break

            make = input("Enter car make: ")
            model = input("Enter car model: ")
            year = int(input("Enter car year: "))
            price = float(input("Enter car price: "))
            color = input("Enter car color: ")
            feature = input("Enter car features using commas (e.g., feature1,feature2): ")
            features = feature.split(",")

            # Create a new car entry
            new_car = [make, model, year, price, color, car_id, features]

            # Append the new car data to the file
            with open("carrrrrrssssss.txt", "a") as outfile:
                outfile.write(str(new_car) + "\n")

            print("-------Car has been Added Successfully-------")

        elif choice=="2":
            print("-------Detail of car in inventory-------")
            print()
            count=1
            def veiw_car(filename):
                infile= open(filename, "r+")
                lines=infile.readlines()
                infile.close
                if lines=="":
                    print("No cars found!")
                print("--- Available Cars ---")
                for detail in lines:
                    detail_car0=detail.replace("\n","")
                    detail_car=eval(detail_car0)
                    len_detail_car=len(detail_car)
                    print("Make: ", detail_car[0])
                    print("Model:", detail_car[1])
                    print("Year: " ,detail_car[2])
                    print("Price:PKR",detail_car[3])
                    print("Color: " ,detail_car[4])
                    print("Car_ID:",detail_car[5])
                    features =detail_car[6]
                    feature_1=""
                    for feature in features:
                        feature_1=feature_1+","+feature
                    feature_2=feature_1.replace(feature_1[0],"")
                    if feature=="":
                        print("Features: There are no special features available")
                    else:
                        print("Features:", feature_2)
                    print()
                print("-------END-------")
                print()
            veiw_car("carrrrrrssssss.txt")

        elif choice == "3":
            print("-------Sell Car-------")
            print()
            car_id = input("Enter the ID of the car to sell: ")
            print()
            infile = open("car.txt", "r")
            lines = infile.readlines()
            infile.close()
            new_lines = []
            for detail in lines:
                car_id0 =eval(detail)
                car_id1=car_id0[5]
                car_id2=car_id1.replace("'", "")
                if car_id != car_id2:
                    new_lines.append(detail)
                else:
                    print(detail)
                    infile = open("Detail of Car Sold.txt", "a")
                    csd=infile.write(str(detail))
                    csd=infile.write("\n")
                    infile.close
            if new_lines == lines: 
                print("Car not found in inventory!")
            else:
                infile = open("car.txt", "w")
                for line in new_lines:
                    infile.write(line)
                infile.close()
                customer_name = input("Enter customer name: ")
                car_sale_detail = [car_id, customer_name, time.strftime( '%A %b/%d/%y %I:%M %p', time.localtime( )) ]
                outfile = open("sales.txt", "a")
                str_car_sale_detail=str(car_sale_detail) + "\n"
                outfile.write(str_car_sale_detail)
                outfile.close()
                print("-------Car sold successfully!-------")

        elif choice=="4":
            print("-------Adding Employee Detail-------")
            print()
            employee_id=input("Enter Employee ID:")
            employee_name=input("Enter Employee Full Name:")
            employee_position=input("Enter Employee Position:")
            employee_salary=input("Enter Employee Salary:")
            employee_detail=[employee_id,employee_name,employee_position,employee_salary]
            infile=open("Employee detail.txt","a")
            text=infile.write(str(employee_detail))
            text1=infile.write("\n")
            infile.close
            print("-------Employee details added successfully!-------")
            
        elif choice == "5":
            print("-------View Employee Detail-------")
            print()
            def veiw_empolyee_detail(filename):
                infile=open(filename,"r")
                lines=infile.readlines()
                infile.close
                for line in lines:
                    detail_=line.replace("\n","")
                    detail_employee=eval(line)
                    print("Employee ID: ", detail_employee[0])
                    print("Employee Full Name: ", detail_employee[1])
                    print("Enter Employee Position: " ,detail_employee[2])
                    print("Employee Salary:PKR ",detail_employee[3])
                    print()
                print("-------END-------")
                print()
            veiw_empolyee_detail("Employee detail.txt")

        elif choice == "6":
            print("-------------View Details about sales and Cars sold.-------------")
            print()
            infile = open("sales.txt", "r")
            line=infile.readlines()
            infile.close
            for sale in line:
                sale1=sale.replace("\n","")
                sale2=eval(sale)
                print("Car ID of Car sold: ",sale2[0])
                print("Name of Customer ",sale2[1])
                print("Time and date on which car was sold",sale2[2])
                print()
            while True:
                print("Do you want detail of any car sold.Type 'yes' or 'no':")
                ans=input()
                if ans.lower()=="yes":
                    id_ans=input("Please Enter Car ID ")
                    infile = open("Detail of Car Sold.txt", "r")
                    dcs=infile.readlines()
                    infile.close
                    for dcs_1 in dcs:
                        dcs_2=dcs_1.replace("\n","")
                        dcs_3=eval(dcs_2)
                        if id_ans in dcs_3:
                            print(dcs_3)
                    print()
                elif ans.lower()=="no":
                    break
                    print()
                else:
                    print("please answer in 'yes' or 'no' ")
                    print()
                print("-------END-------")
                print()
                 
        elif choice == "7":
            print("GoodBye")
            break
        
        else:
            raise ValueError("Please enter a Number in between 1-7")
    except (TypeError,ValueError):
        print("Invalid input")
