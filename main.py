import csv

# 1. Read the data from the spreadsheet
def read_data():
    data = []

    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data

#2. Collect all of the sales from each month into a single list
def calculate_sales(data):
    total_sales = []
    for row in data:
        monthly_sales = row['sales']
        total_sales.append(int(monthly_sales))
    # 3. Output the total sales across all months , f string
    print(f'The total sales across all {len(total_sales)} months are {sum(total_sales)}.')
    return len(total_sales), sum(total_sales)

# Calculate total expenditures from the spreadsheet
def calculate_expenses(data):
    total_expenses = []
    for row in data:
        monthly_expenses = row['expenditure']
        total_expenses.append(int(monthly_expenses))
    return sum(total_expenses)

def ask_data_by_month(data):
    month = input("Please enter the 3 first letters of a month to show data (eg. apr)").lower()

    for i in range(0, len(data)):
        if month == data[i]['month']:
            print(f"The sale in {month} was {data[i]['sales']}")
            print(f"The expenditure in {month} was {data[i]['expenditure']}")

def run():
    data = read_data()
    calculate_sales(data)
    ask_data_by_month(data)

run()