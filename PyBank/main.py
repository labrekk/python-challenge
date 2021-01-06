
#   * The total number of months included in the dataset

#   * The net total amount of "Profit/Losses" over the entire period

#   * The average of the changes in "Profit/Losses" over the entire period

#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period

#first, I input os and csv so I can access the budget and election .csv files

import os
import csv

# determining path to collect data from the resources folder. found out to use single . instead of .. based on where i moved the csv 
budget_csv = os.path.join('.', 'resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_csv, newline='') as csvfile:

    # Split the data on commas (taken from class activity)
    csvreader = csv.reader(csvfile, delimiter=',')
    #skipping the header row of the csv (Date, Profit/Loss)
    csv_header = next(csvfile)
    
    #create empty lists and my variables to store data in

    months = 0
    netprofit = 0
    lastmonth_profit = 0
    change = 0
    avg_change = 0
    #list for monthly_changes, needed for max/min/avg functions
    monthly_changes = []

    #loop dataset
    for row in csvreader:
        #what is the total # of months? will take months variable defined above and just add 1 for every row in csvreader
        months = months + 1
        #what is the net total amount of "Profit/Losses" over the entire period?
        #new variable will be equal to row[1] (Profit/Losses column in .csv file)
        profitslosses = float(row[1])
        netprofit = netprofit + profitslosses

        #using the empty monthly_changes list for code below - i want to figure out what profitlosses - lastmonth_profit =,
        #then append that value into my list. i think this should work.

        change = profitslosses - lastmonth_profit
        monthly_changes.append(change)
        #Redefine lastmonth_profit variable since it is now going to be = profitlosses.
        lastmonth_profit = profitslosses

    #* The average of the changes in "Profit/Losses" over the entire period
        #NOTE TO SELF: Does this belong in for loop??
        #Citation: https://careerkarma.com/blog/python-average/#:~:text=We%20can%20find%20the%20average,a%20common%20task%20in%20Python.

    avg_change = ((sum(monthly_changes))/(len(monthly_changes)))

    #https://www.tutorialspoint.com/python/list_max.htm

    max = max(monthly_changes)
    #i assumed the function would be along the same lines for min.
    min = min(monthly_changes)


    #print financial analysis - it should look like the next several lines below:
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
    print ("Financial Analysis")
    print ("----------------------------")
    print (f"Total Months: {months}")
    print (f"Net profit for period = $ {netprofit}")
    print (f"The average change month to month = $ {avg_change}")
    print (f"Greatest Increase in Profits: $ {max}")
    print (f"Greatest decrease in profits: $ {min}")

#https://www.guru99.com/reading-and-writing-files-in-python.html
f = open("analysis.txt", "w+")

#Source for \n bits:
#https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/#:~:text=The%20new%20line%20character%20in%20Python%20is%20%5Cn%20.,used%20to%20separate%20the%20lines.
f.write("Financial Analysis\n")
f.write ("----------------------------\n")
f.write (f"Total Months: {months}\n")
f.write (f"Net profit for period = $ {netprofit}\n")
f.write (f"The average change month to month = $ {avg_change}\n")
f.write (f"Greatest Increase in Profits: $ {max}\n")
f.write (f"Greatest decrease in profits: $ {min}\n")

f.close()   




    

