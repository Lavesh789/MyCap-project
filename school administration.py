# project 1: Basic school administration tool
import csv

def write_into_csv(info_list):
  with open('Student_info.csv','a', newline='') as csv_file:
    writer = csv.write(csv_file)
    
    if csv_file.tell() == 0:
        Writer.writerow(["Name", "Age", "Contact Number", "E-mail ID"])
    
    Write.writerow(info_list)
    
if __name__ == '__main__':
    condition = True
    student_num = 1 

    While(Condition):
    Student_info = input("Enter student information for the student #{} in the following format (Name Age Contact_Number E-mail_ID): ".format(student_num))
   
    #Spilt
    Student_Info_list = student_info.split('')
          
    print("\nThe Entered information is -\nName: {}\nAge: {} \ncontact_Number: {}\nE-mail_ID: {}"
          .format(Student_Info_list[0], student_info_list[1], student_info_list[2], student_info_list[2]) 
          
    choice_check = input("Is the entered information correct? (Yes/No): ")
       
    if choice_check == "Yes":
       Write_info_csv(Student_info_list)
          
   condition_Check = input("Enter (Yes/No) if you want to enter information for another student: ")
   if condition_Chek == "yes":
          condition = True
          student_num = student_num + 1
   elif condition_check == "No":
          Condition = False
   elif choice_check == "No":
          print("\nPlease re-enter the value!")
