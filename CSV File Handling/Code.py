import csv


def rows_data():
    data_list=[]
    print("Enter number of rows you would like to define: ")
    row_limt=int(input("> "))
    for i in range(row_limt):
        print("Enter row{}data: ".format(i+1))
        row_data=input("> ").split()
        data_list.append(row_data)
    return data_list

def write_row(data):

    with open("prac.csv","w",newline="") as file:
        writer=csv.writer(file)
        writer.writerow(data)

def write_rows(data):

    with open("prac.csv","w",newline="") as file:
        writer=csv.writer(file)
        writer.writerows(data)

def read_rows():
    with open("prac.csv","r",newline="") as file:
        content_obj=csv.reader(file)
        for row in content_obj:
            print(row)

def append_rows(data):
    with open("prac.csv","a",newline="") as file:
        writer_obj=csv.writer(file)
        writer_obj.writerows(data)

def append_row(data):
    with open("prac.csv","a",newline="") as file:
        writer_obj=csv.writer(file)
        writer_obj.writerow(data)

print("What would you like to do: ")
print("1) Read\n2) Write\n3) Append")
choice=input("> ")
if choice.lower()=="read":
    read_rows()

elif choice.lower()=="write":
    print("Would you like to write a row or write rows?")
    write_choice=input("> ")
    if write_choice.lower()=="row":
        print("Enter data: ")
        data=input("> ").split()
        write_row(data)
    elif write_choice.lower()=="rows":
        data_list= rows_data()
        write_rows(data_list)


elif choice.lower()=="append":
    print("Would you like to append a row or append rows?")
    append_choice=input("> ")
    if append_choice.lower()=="row":
        print("Enter data: ")
        data=input("> ").split()
        append_row(data)
    elif append_choice.lower()=="rows":
        data_list=rows_data()
        append_rows(data_list)

