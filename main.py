import csv

def read_data():
    data = []

    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data

# Collect all of the sales from each month into a single list
def calculate_sales(data):
    total_sales = []
    for row in data:
        monthly_sales = row['sales']
        total_sales.append(int(monthly_sales))

    print(f'The total sales across all {len(total_sales)} months are {sum(total_sales)}.')
    return len(total_sales), sum(total_sales)

def run():
    data = read_data()
    calculate_sales(data)

run()