import csv
import os

#Initialize variables
Total_months = 0
Total_change = 0
Avg_change = 0 
list_of_change = []
list_of_months = []
prev_total = 0
Most_Profit = 0
Most_Loss = 0
max = 0
min = 0
max_month = ""
min_month = ""

#Import the file
Budget_csv = os.path.join("Resources" , "budget_data.csv")

#Read in the file
with open (Budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")

    #Read in header
    csv_header = next(csv_file)

    #Take in the data and analyze
    for line in csv_reader:
        Total_months += 1
        Total_change += int(line[1])
        list_of_change.append(int(line[1]) - prev_total)
        prev_total = int(line[1])
        list_of_months.append(line[0])

    #Looking for max and mins of the list
    for value in list_of_change:
        if value > max:
            max = value
            max_month = list_of_months[list_of_change.index(value)]
        if value < min:
            min = value
            min_month = list_of_months[list_of_change.index(value)]

    #Clean up some values and print the results
    list_of_change.pop(0)
    avg_change = sum(list_of_change) / len(list_of_change)
    avg_change =  round(avg_change, 2)
    print(f"Financial Analysis")
    print(f"Total Months: {Total_months}")
    print(f"Total: ${Total_change}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {max_month} ${max}")
    print(f"Greatest Increase in Profits: {min_month} ${min}")
# Write the output
analysis = os.path.join("analysis", "Analysis.txt")
with open (analysis, 'w') as file:
    file.write(f"Financial Analysis")
    file.write(f"\nTotal Months: {Total_months}")
    file.write(f"\nTotal: ${Total_change}")
    file.write(f"\nAverage Change: ${avg_change}")
    file.write(f"\nGreatest Increase in Profits: {max_month} ${max}")
    file.write(f"\nGreatest Increase in Profits: {min_month} ${min}")