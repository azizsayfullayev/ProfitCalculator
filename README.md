# Trading Platform Profit Calculator

## Overview
This Python script calculates trading profits on platforms that do not offer built-in calculators. It's designed to help traders efficiently analyze their financial performance through an automated system.

## Features
- **Data Parsing**: Reads trading data from CSV files.
- **Daily Profit Analysis**: Groups transactions by date to calculate daily profits.
- **Profit Calculations**: Computes total profits, commissions, and net profits for each trading day.
- **Summary Output**: Provides cumulative financial metrics and displays them in a color-coded table for clarity and quick reference.

## Customization
- **Commission Rates**: Users can modify the script to include different commission rates based on their specific agreements or trading conditions.
- **Initial Investment Tracking**: Add the amount of initial investment at the start of the trading period to monitor overall financial growth.
- **Investment Balance**: Calculate and track the remaining balance of the investment after each trading day or at the end of the trading period.
  
## Purpose
Created for personal use, this script bridges the functionality gap in trading platforms lacking native profit calculation tools. It simplifies financial tracking and enhances decision-making for traders.

## How to Use
1. Place your trading data in a CSV file.
2. Ensure the data includes 'Close Time' and 'Profit' columns.
3. Modify the script parameters to reflect your commission rate and initial investment.
4. Run the script with the path to your CSV file:
   ```bash
   python profit_calculator.py <path_to_your_csv_file>
