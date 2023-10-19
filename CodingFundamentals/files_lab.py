#import csv

#companies = []
#sales = []

#with open
#    reader = csv.reader(*filename*)
        #skip for first line
#    for loop;
#    appending to companies
#    append sales date to sales - (int just the sales data, want a list of tuples as final outcome)

#monthly_sum (zip) - use to unpack tuples from list
#yearly_sum use a for loop - put into a dict

#print monthly
#print yearly print as dict with method and .items()

import csv

companies = []
sales = []

with open("output.csv", "w") as file:
    next(file)

    for i in file:
        companies.append(row[0])
        sales.append(row[1])