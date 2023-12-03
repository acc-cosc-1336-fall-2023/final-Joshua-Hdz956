import question_a
stock_dict = question_a.get_stock_list("stocklist.txt")

while True:
    print("\tMenu")
    print("1 - Display stock purchase history")
    print("2 - Exit")
    option = str(input("Select option 1 or 2: "))
    while option not in ('1','2'):
        option = str(input("Invalid, Select option 1 or 2: "))
    if option == '1':
        print("\nStock Purchase History")
        print("Symbol\tCompany Name")
        for symbol, stocks in stock_dict.items():
            print(f"{str(stocks.get_symbol()).ljust(8)}{stocks.get_company_name()}")
        print("")
    elif option == '2':
        print("Exiting Program")
        break