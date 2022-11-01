import csv

csvpath = "Resources/election_data.csv"

rows = 0
candidates = []
stockham = 0
degette = 0
doane = 0

with open(csvpath, encoding='utf-8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    for row in csvreader:
        rows += 1
        candidates.append(row[2])
        if row[2] == "Charles Casper Stockham":
            stockham += 1
        if row[2] == "Diana DeGette":
            degette += 1
        if row[2] == "Raymon Anthony Doane":
            doane += 1

percent_stockham = round(((stockham / rows) * 100), 3)
percent_degette = round(((degette / rows) * 100), 3)
percent_doane = round(((doane / rows) * 100), 3)

# Find the candidate who won with the most votes
# https://stackoverflow.com/questions/1518522/find-the-most-common-element-in-a-list
def winner(candidates):
    return max(set(candidates), key=candidates.count)

victor = winner(candidates)

print()
print("Election Results")
print("----------------------------------")
print(f"Total Votes: {rows}")
print("----------------------------------")
print(f"Charles Casper Stockham: {percent_stockham}% ({stockham})")
print(f"Diana DeGette: {percent_degette}% ({degette})")
print(f"Raymon Anthony Doane: {percent_doane}% ({doane})")
print("----------------------------------")
print(f"Winner: {victor}")
print("----------------------------------")

# Write output analysis to text file

output = f"""Election Results
----------------------------------
Total Votes: {rows}
----------------------------------
Charles Casper Stockham: {percent_stockham}% ({stockham})
Diana DeGette: {percent_degette}% ({degette})
Raymon Anthony Doane: {percent_doane}% ({doane})
----------------------------------
Winner: {victor}
----------------------------------"""

with open("pypoll_analysis.txt", "w") as f:
    f.write(output)