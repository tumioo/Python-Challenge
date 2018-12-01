import csv

# declare input file
bank_data_in = "budget_data.csv"
bank_data_out = "Bank_Analysis.txt"

# Declare lists to be filled with data for calculations and final report
Bank_tot_net = 0
Bank_months = 0
Bank_month_of_change = []
Net_change_values = []
max_increase = ["", 0]
max_decrease = ["", 9999999999999999999]


# convert csv to a dictionary with key: Month and value: Profit/loss
with open(bank_data_in) as Bank_data:
    reader = csv.reader(Bank_data)

    # establish first line as header and not actionable data
    header = next(reader)

    # pre loop skip first month since it has no prior period comparison
    # iterates through month and profit/loss value
    # establish prior month comparison criteria
    first_row = next(reader)
    Bank_months = Bank_months + 1
    Bank_tot_net = Bank_tot_net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        # counter to track cumulative number of months and cumulative net change
        Bank_months = Bank_months + 1
        Bank_tot_net = Bank_tot_net + int(row[1])

        # counter to track cumulative values of net change
        # generates data to fill lists(net change list, month of change) established pre loop
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        Net_change_values = Net_change_values + [net_change]
        Bank_month_of_change = Bank_month_of_change + [row[0]]

        # Calculate the greatest increase
        if net_change > max_increase[1]:
            max_increase[0] = row[0]
            max_increase[1] = net_change

        # Calculate the greatest decrease
        if net_change < max_decrease[1]:
            max_decrease[0] = row[0]
            max_decrease[1] = net_change

# Calculate the Average Net Change s
net_monthly_avg = sum(Net_change_values) / len(Net_change_values)

# Generate Output Summary
output = (
    f"\nBank Financial Report\n"
    f"----------------------------\n"
    f"Total Months: {Bank_months}\n"
    f"Total: ${Bank_tot_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})\n"
    f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})\n")

# Print the output
print(output)

# Export the results to text file
with open(bank_data_out, "w") as Financial_Report:
    Financial_Report.write(output)
