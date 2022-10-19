import csv

csvpath = "Resources/budget_data.csv"

rows = 0
total = 0
profit_loss = []
profit_change = {}

with open(csvpath, encoding='utf-8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    for i, row in enumerate(csvreader):
        rows += 1
        total += int(row[1])
        profit_loss.append(int(row[1]))
        if i > 0:
            profit_change[row[0]] = int(row[1]) - int(prev_row[1])
        prev_row  = row
        
# Find the average change over the entire period
average_change = round((profit_loss[-1] - profit_loss[0]) / (rows -1), 2)

# Find the greatest increase in profits (date and amount) over the entire period
# Credit: https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
bestday = max(profit_change, key=profit_change.get)
alpha = profit_change.values()
increase = max(alpha)
# Find the greatest decrease in profits (date and amount) over the entire period
worstday = min(profit_change, key=profit_change.get)
decrease = min(alpha)

# Print Results
print("Financial Analysis")
print("----------------------------------")
print(f"Total Months: {rows}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {bestday} ${increase}")
print(f"Greatest Decrease in Profits: {worstday} ${decrease}")

# Write output analysis to text file

output = f"""Financial Analysis
----------------------------------
Total Months: {rows}
Total: ${total}
Average Change: ${average_change}
Greatest Increase in Profits: {bestday} ${increase}
Greatest Decrease in Profits: {worstday} ${decrease}"""

with open("pybank_analysis.txt", "w") as f:
    f.write(output)