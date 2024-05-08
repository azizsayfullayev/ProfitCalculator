# Trading Platform Profit Calculator

## Overview
This Python script calculates trading profits on platforms that do not offer built-in calculators. It's designed to help traders efficiently analyze their financial performance through an automated system.

## Features
- **Data Parsing**: Reads trading data from CSV files.
- **Daily Profit Analysis**: Groups transactions by date to calculate daily profits.
- **Profit Calculations**: Computes total profits, 25% commission fees, and 75% net profits for each trading day.
- **Summary Output**: Provides cumulative financial metrics and displays them in a color-coded table for clarity and quick reference.

## Purpose
Created for personal use, this script bridges the functionality gap in trading platforms lacking native profit calculation tools. It simplifies financial tracking and enhances decision-making for traders.

## How to Use
1. Place your trading data in a CSV file.
2. Ensure the data includes a 'Close Time' and 'Profit' column.
3. Run the script with the path to your CSV file:
   ```bash
   python profit_calculator.py <path_to_your_csv_file>
