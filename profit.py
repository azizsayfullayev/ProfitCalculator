import pandas as pd
from tabulate import tabulate

# ANSI color escape codes
RED = '\033[31m'     # Red text
GREEN = '\033[32m'   # Green text
YELLOW = '\033[33m'  # Yellow text
RESET = '\033[0m'    # Reset to default color

def calculate_profit_by_date(csv_path):
    # Load the CSV file
    df = pd.read_csv(csv_path)
    
    # Parse dates from the 'Close Time' column and create a new date column
    df['Date'] = pd.to_datetime(df['Close Time'], format='%d/%m/%y, %H:%M').dt.date
    
    # Extract the 'Profit' column, remove currency symbols, and convert to float
    df['Profit'] = df['Profit'].replace('[\$,]', '', regex=True).astype(float)

    # Group by the new 'Date' column
    grouped = df.groupby('Date')

    # Prepare the headers for the table
    headers = ["Date", "Jami topilgan summa", "Komissiya", "Sof foyda", "Foyda foizda"]

    # This will store all rows of the table
    table_rows = []
    overall_total_profit = 0
    overall_profit_25_percent = 0
    overall_profit_75_percent = 0

    # Iterate over each group, calculate financial metrics, and prepare the table row
    for date, group in grouped:
        total_profit = group['Profit'].sum()
        profit_25_percent = total_profit * 0.25
        profit_75_percent = total_profit * 0.75

        # Accumulate overall totals
        overall_total_profit += total_profit
        overall_profit_25_percent += profit_25_percent
        overall_profit_75_percent += profit_75_percent

        # Format the date in '8-May 2024' style, compatible across platforms
        formatted_date = date.strftime('%d-%b %Y').lstrip('0')

        # Prepare the row for this date
        row = [
            f"{formatted_date}",
            f"${total_profit:.2f}",
            f"${profit_25_percent:.2f}",
            f"${profit_75_percent:.2f}",
            f"{((profit_75_percent) / 50) * 100:.2f}%"
        ]
        table_rows.append(row)

    # Calculate overall percentage increase for the accumulated profit_75_percent
    overall_percentage_increase = ((overall_profit_75_percent) / 50) * 100

    # Add a summary row for all dates
    summary_row = [
        "Overall",
        f"{YELLOW}${overall_total_profit:.2f}{RESET}",
        f"{RED}${overall_profit_25_percent:.2f}{RESET}",
        f"{GREEN}${overall_profit_75_percent:.2f}{RESET}",
        f"{GREEN}{overall_percentage_increase:.2f}%{RESET}"
    ]
    table_rows.append(summary_row)

    # Print the results in a table format
    print(tabulate(table_rows, headers=headers, tablefmt='grid'))

# Example usage, replace 'path_to_your_file.csv' with your actual CSV file path
calculate_profit_by_date(r"")
