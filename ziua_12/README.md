# Personal Finance Tracker

A command-line application written in Python to track personal income and expenses, offering persistent storage, categorization, and financial reporting.

## Description
This project manages personal finances by tracking income and expenditures. It allows users to add financial transactions, view balances, filter expenses by category, view top spending records, and automatically serialize data into a local JSON file.

## Features
- **Transaction Management:** Add income (with custom sources) and expenses (categorized).
- **Data Persistence:** Automatic saving and loading of transactions using JSON storage (`date.json`).
- **Financial Insights:** Real-time calculation of total income, total expenses, and current balance.
- **Categorization & Analytics:** View expenses broken down by category.
- **Filters & Sorting:** Search expenses by specific category or view the top N highest expenses.
- **Error Handling & Input Validation:** Built-in decorators and input safety checks to prevent crashes.

## How to Run
Ensure you have Python 3 installed. Open a terminal in the project directory and run:

```bash
python main.py