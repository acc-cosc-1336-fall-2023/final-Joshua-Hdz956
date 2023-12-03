#add import
import question_b

while True:
    print("\tMenu")
    print("1 - Create Multiplication Table")
    print("2 - Exit")
    option = str(input("Select option 1 or 2: "))
    while option not in ('1','2'):
        option = input("Invalid option, Select 1 or 2: ")
    if option == '1':
        while True:
            while True:
                try:
                    row = int(input("Select number of rows for your table: "))
                    break
                except:
                    print("Invalid, not a whole number!")
            while True:
                try:
                    column = int(input("Select number of columns for your table: "))
                    break
                except:
                    print("Invalid, not a whole number!")
            table = question_b.create_multiplication(row, column)
            question_b.display_table(table)
            exit_option = str(input("If you would to create another table press Y. Otherwise enter any other key to exit: ")).lower()
            print("")
            if exit_option not in ('y','yes'):
                print("Exiting Program")
                break
        break
    if option == '2':
        print("Exiting Program")
        break