# PyBank 

#  add in csv and os
import os
import csv

# path to csv
budget_data_csv = os.path.join("resources", "budget_data.csv")

# opening/reading csv
with open(budget_data_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    # omitting header
    header = next(csv_reader)


    # printing title
    print("Financial Analysis")
    print("-------------------")

    # find ln of csv (months; omit header)
    rowcount = 0
    nettotal = 0
    value = 0
    smallest = 0
    sum = 0

    # going through each row of data
    for row in csv_reader:
        maxVal = row[1]
        # finding total months 
        rowcount+= 1
        # finding net total
        nettotal = nettotal + int(row[1])
        # finding average change
        change = nettotal / rowcount
        # finding min and max


    print(maxVal)
    print(f'Total months: {rowcount}')
    print (f'Total: ${nettotal}')
    print(f'Average change: ${change}')

   
    # variables for the min/max
    profitchange = []
    change = []
    months = []

    # making a loop
    for i in range(1,len(profitchange)):
        change.append(profitchange[i] - profitchange[i-1])
        averagechange = sum(change)/len(change)

        max_change = max(change)
        min_change = min(change)

        max_date = str(months[change.index(max(change))])
        min_date = str(months[change.index(min(change))])

    print(f'Greatest Increase in Profits: {max_date} (${max_change})')
    print(f'Greatest Decrease in Profits: {min_date} (${min_change})')

