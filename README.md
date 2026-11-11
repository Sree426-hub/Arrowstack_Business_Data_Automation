# Business Data Automation Toolkit

## Project Overview
This repository contains a modular Python-based automation script built during my Python Development Internship at Arrowstack Technologies. The system automates data ingestion from CSV source files, performs comprehensive record validations, and generates detailed exception reports for operational visibility.

## Technical Framework & Implementation
- **Core Technology:** Python 3.x
- **Data Source Handling:** Automated processing of localized relational datasets (`employees.csv`)
- **Validation Engine:** Integrated Regular Expressions (`re` module) for structure verification and robust syntax matching
- **Error Control:** Modular try-except architectures to isolate edge cases without interrupting workflow pipelines

## Features Implemented
- **Automated Data Ingestion:** Reads structured corporate files reliably.
- **Dynamic Input Validation:** Checks for structural data faults, empty records, and non-numeric salary metrics.
- **Exception Logging:** Captures formatting issues dynamically into an external text file (`exception_report.txt`).

## Execution Instructions
1. Clone or download the files into a single localized directory.
2. Open your system terminal or command prompt inside the workspace.
3. Run the automation program executing:
   ```bash
   python data_automation.py
   ```
4. Check the directory for the automatically populated `exception_report.txt` file.
