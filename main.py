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
    print(f'The total sales across all {len(total_sales)} months were {sum(total_sales)}.')
    return len(total_sales), sum(total_sales)

# Calculate total expenditures from the spreadsheet
def calculate_expenses(data):
    total_expenses = []
    for row in data:
        monthly_expenses = row['expenditure']
        total_expenses.append(int(monthly_expenses))
    return sum(total_expenses)

# Calculate the average quantities
def calculate_average(data):
    sales = []
    expenses = []
    for row in data:
        sales.append(int(row['sales']))
        expenses.append(int(row['expenditure']))

    average_sales = round(sum(sales) / len(sales), 2)
    average_expenses = round(sum(expenses) / len(expenses), 2)

    print(f"The average sales was {average_sales} \nThe average expenditure was {average_expenses}")
    return average_sales, average_expenses

# Calculate the months with the highest and lowest sales
def calculate_min_max_sales(data):
    min_and_max_sales = []

    for row in data:
        min_and_max_sales.append(int(row['sales']))

    #print(min_and_max_sales)
    min_sale = min(min_and_max_sales)
    max_sale = max(min_and_max_sales)

    print(f"The highest sale was {max_sale}")
    print(f"The lowest sale was {min_sale}")
    return min_sale, max_sale

# Calculate monthly changes as a percentage
# formula = (new_value-old_value)/old_value
def monthly_changes(data):
    listChanges = []
    for i in range(1, len(data)):
        previous_month = int(data[i-1]['sales'])
        current_month = int(data[i]['sales'])
        change_as_percentage = round(((current_month - previous_month) / previous_month) * 100, 2)
        listChanges.append(change_as_percentage )
    print(f"The monthly changes as percentage are {listChanges}")


def ask_data_by_month(data):
    month = input("Please enter the 3 first letters of a month to show data (eg. apr)").lower()

    for i in range(0, len(data)):
        if month == data[i]['month']:
            print(f"The sale in {month} was {data[i]['sales']}")
            print(f"The expenditure in {month} was {data[i]['expenditure']}")

def run():
    data = read_data()
    calculate_sales(data)
    calculate_average(data)
    calculate_min_max_sales(data)
    monthly_changes(data)
    ask_data_by_month(data)



run()