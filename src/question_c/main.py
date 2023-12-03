import question_c

while True:
    print("Menu")
    print("1 - Display stock purchase history")
    print("2 - Exit")
    option = str(input("Select option 1 or 2: "))
    while option not in ('1','2'):
        option = str(input("Invalid, Select option 1 or 2: "))
    
    if option == '1':
        question_c.stock_purchase_history()

    elif option == '2':
        print("Exiting Program")
        break