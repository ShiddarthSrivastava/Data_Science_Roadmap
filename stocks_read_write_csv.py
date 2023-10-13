import csv
with open('stocks.csv',mode='r') as file:
    csv_file=csv.reader(file)
    next(file)
    with open("ouput.csv","w") as output:
        output.write("Company Name, PE Ratio, PB Ratio\n")
        for line in csv_file:

            Stocks=line[0]
            PE_Ratio=round(float(line[1])/float(line[2]),2)
            PB_Ratio=round(float(line[1])/float(line[3]),2)
            output.write(f"{Stocks},{PB_Ratio},{PE_Ratio}\n")
            print(PE_Ratio,PB_Ratio)
