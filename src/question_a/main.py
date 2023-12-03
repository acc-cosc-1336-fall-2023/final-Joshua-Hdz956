import question_a
question_a.write_stock_file("stocklist.txt")
stock_dict = question_a.get_stock_list("stocklist.txt")
bold = '\033[1m'
underline = '\033[4m'
normal = "\033[0;0m"
while True:
    print("\tMenu")
    print("1 - Display stock purchase history")
    print("2 - Exit")
    option = str(input("Select option 1 or 2: "))
    while option not in ('1','2'):
        option = str(input("Invalid, Select option 1 or 2: "))
    if option == '1':
        print(bold+"\nStock Purchase History")
        print(underline+"Stock\t"+normal+"      "+underline+bold+"Report"+normal)
        for symbol, stocks in stock_dict.items():
            print(f"{str(stocks.get_company_name()).ljust(14)}{stocks.get_symbol()}")
        print("")
    elif option == '2':
        print("Exiting Program")
        break