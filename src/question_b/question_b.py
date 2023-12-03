#write functions here, don't add input('') statements here!
def create_multiplication(x,y):
    table = []
    for i in range(1,x+1):
        row = []
        i * 1
        for j in range(1,y+1):
            product = i*j
            row.append(product)
        table.append(row)
    return table

def display_table(table):
     for i in range(len(table)):
          print('')
          for j in range(len(table[i])):
               print(str(table[i][j]).ljust(4), end = ' ')
     print("")
