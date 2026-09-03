import csv
import os

def create_file(name,type):
    with open(f"{name}.{type}","w"):
        pass

def rows_data():
    data_list=[]
    print("Enter number of rows you would like to define: ")
    row_limt=int(input("> "))
    for i in range(row_limt):
        print("Enter row{} data: ".format(i+1))
        row_data=input("> ").split()
        data_list.append(row_data)
    return data_list

def write_rows(data,destination,extension):
    with open(destination,"w",newline="") as file:
        if extension.lower()=="csv":
            writer=csv.writer(file)
            writer.writerows(data)
        elif extension.lower()=="txt":
            file.writelines(data)

def append_rows(data,destination,extension):
    with open(destination,"a",newline="") as file:
        if extension.lower()=="csv":
            writer_obj=csv.writer(file)
            writer_obj.writerows(data)
        elif extension.lower()=="txt":
            #text file code pending...
            pass

def read_rows(destination,extension):
    with open(destination,"r",newline="") as file:
        if extension.lower()=="csv":
            content_obj=csv.reader(file)
            for row in content_obj:
                print(row)
        elif extension.lower()=="txt":
            #text reader is pending..
            pass


def operation_create():
    print("Name of the file: ")
    file_name=input("> ")
    print("File extension(png,jpeg,txt,csv): ")
    file_extension=input("> ")
    create_file(file_name,file_extension)

def operation_manage():
    print("What would you like to do: ")
    print("1) Read\n2) Write\n3) Append")
    choice=input("> ")
    print("which file would you like to edit: ")
    file_name=input("> ")
    file_extension=file_name.split(".")[1]

    if choice.lower()=="read":
        read_rows(file_name,file_extension)
    elif choice.lower()=="write":
        data_list= rows_data()
        write_rows(data_list,file_name,file_extension)
    elif choice.lower()=="append":
        print("Would you like to append a row or append rows?")
        append_choice=input("> ")
        data_list=rows_data()
        append_rows(data_list,file_name,file_extension)



print("What file action do you want to perform?(create/manage)")
operation = input("> ")
if operation.lower()=="create":
    operation_create()

elif operation.lower()=="manage":
    operation_manage()

