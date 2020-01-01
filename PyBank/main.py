# Importing modules os and csv

import os
import csv

# Defining the variables / lists

months = 0
revenue_total = 0
list_revenue = []
revenue_chng = 0
revenue_prev = 0
decrease = ["",""]
increase=["",""]
revenue_start = 0
revenue_end = 0
revenue_avg = 0


# Opening the file and getting this show on the road!
with open('budget_data.csv', newline = '') as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
    print(csvreader)
    csv_header = next(csvreader)
    for row in csvreader:

        # Increasing month by 1 per row

        months += 1
    
        # Adding to the total revenue by pulling from the profit/losses column
        # Setting up a list for each entry in profits/losses column

        revenue_total = revenue_total + int(row[1])
        list_revenue.append(int(row[1]))

        # Calculating change for use in greatest increase and decrease in profits
        # Important note: instructions were unclear as to the timeframe to be used
        # After trial and error, it was determined that the change was to be calculated
        # per month, not per year or quarter

        revenue_chng = int(row[1]) - int(revenue_prev)
        revenue_prev = int(row[1])

        # If no data is in the increase or decrease list at the start, it will pull the 
        # first record as a baseline
        # Otherwise, it will compare the revenue change vs. the increase or decrease 
        # and determine if it is higher or lower (respectively) than the existing 
        # record and adjust accordingly

        if increase[0] == "":
            increase[0] = row[0]
            increase[1] = row[1]
        elif int(revenue_chng) > int(increase[1]):
            increase[0] = row[0]
            increase[1] = int(revenue_chng)

        if decrease[0] == "":
            decrease[0] = row[0]
            decrease[1] = row[1]
        elif int(revenue_chng) < int(decrease[1]):
            decrease[0] = row[0]
            decrease[1] = int(revenue_chng)
        
    # Grabbing the starting and ending revenue totals from the list
    revenue_start = int(list_revenue[0])
    revenue_end = int(list_revenue[-1])

    # Calculating the average overall with the starting and ending revenue totals
    # Dividing by total number of months - 1 to get the final average of changes 
    # over the entire date range
    revenue_avg = (int(list_revenue[-1]) - int(list_revenue[0])) / (int(months) - 1 )

# Generating the text file

with open('pybank.txt','w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write("Total Months: " + str(months)+"\n")
    file.write("Total: $" + str(revenue_total)+"\n")
    file.write("Average Change: $" + str(round(revenue_avg,2))+"\n")
    file.write("Greatest Increase in Profits: " + str(increase[0]) + " ($" + str(increase[1]) + ")\n")
    file.write("Greatest Decrease in Profits: " + str(decrease[0]) + " ($" + str(decrease[1]) + ")\n")

# Printing to terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months))
print("Total: $" + str(revenue_total))
print("Average Change: $" + str(round(revenue_avg,2)))
print("Greatest Increase in Profits: " + str(increase[0]) + " ($" + str(increase[1]) + ")")
print("Greatest Decrease in Profits: " + str(decrease[0]) + " ($" + str(decrease[1]) + ")")