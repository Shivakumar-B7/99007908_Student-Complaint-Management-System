class complaint:

   #Student Complaint/Queries Management System
  print("**** WELCOME STUDENTS ******")
print("-----------")
name = input("Enter Your Name: ")
print(" Hi " + name)

print(" -----------")
print("1.Complaint about subjects\n2.Complaint about food\n3.Complaint about hostel")
option = int(input(" Select a option: "))
if option == 1 :
    result = "1.Complaint about subjects"
    print("You have selected", result)
    print(" -----------")

    print("1.Kannada\n2.English\n3.Hindi\n4.Mathematics\n5.Science")
    option = int(input(" Select the Subject: "))
    if option == 1:
       result = "Kannada"
       print("You have selected ", result)
       print(" -----------")
       option = str(input("Enter your Compliant/Quarry :"))
       print("Noted")
       print(" -----------")

    elif option == 2:
      result = "English"
      print("You have selected ", result)
      print(" -----------")
      option = str(input("Enter your Compliant/Quarry :"))
      print("Noted")

    elif option == 3:
      result = "Hindi"
      print("You have selected ", result)
      print(" -----------")
      option = str(input("Enter your Compliant/Quarry :"))
      print("Noted")

    elif option == 4:
      result = "Mathematics"
      print("You have selected ", result)
      print(" -----------")
      option = str(input("Enter your Compliant/Quarry :"))
      print("Noted")

    elif option == 5:
      result = "scince"
      print("You have selected ", result)
      print(" -----------")
      option = str(input("Enter your Compliant/Quarry :"))
      print("Noted")

    else:
       print("Incorrect option\nChoose the correct option")

elif option == 2:
  result = "2.Complaint about food"
  print("You have selected ", result)
  print(" -----------")
  option = str(input("Enter your Compliant/Quarry :"))
  print("Noted")

elif option == 3:
  result = "3.Complaint about hostel"
  print("You have selected ", result)
  print(" -----------")
  option = str(input("Enter your Compliant/Quarry :"))
  print("Noted")

else:
  print("Incorrect option")
  print(" -----------")

 # print("1.Register new complaint\n2.Close")
  option = int(input(" Select a option: "))
  if option == 1:
    class complaint():

        if option == 2:
            print("******Exit******")


