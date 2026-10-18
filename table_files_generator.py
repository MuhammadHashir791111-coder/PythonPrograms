def generateTable(a):
    table = "" #initially, there is no table
    for b in range(1, 11):
        table += f"{a} X {b} = {a*b}\n" #table of n is created
    
    with open(f"tables/table_{a}.txt", "w") as f: #table_n.txt is opened in the folder tables
        f.write(table) #table of n is written

for a in range(2, 21):
    generateTable(a)
