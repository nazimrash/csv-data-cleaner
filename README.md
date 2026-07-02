# CSV Data Cleaner

A Python project that cleans messy CSV files using pandas.

## Features

- Removes duplicate rows
- Fills missing values
- Removes extra spaces
- Saves cleaned data into a new CSV file

## Technologies Used

- Python
- pandas
=======
## 📌 Overview

This project is a Python application that automatically cleans messy CSV files using the pandas library.

It is designed to perform common data-cleaning tasks that businesses often require before analyzing their data.

---

## 🚀 Features

- Reads CSV files
- Removes duplicate records
- Removes extra spaces
- Fills missing Age values using the average age
- Fills missing Salary values using the average salary
- Replaces missing City values with "Unknown"
- Saves a cleaned CSV file

---

## 🛠 Technologies Used

- Python 3.13
- pandas

---

## 📂 Project Structure

```
csv-data-cleaner/
│
├── data/
│   └── messy_data.csv
│
├── output/
│   └── cleaned_data.csv
│
├── clean_data.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

Install pandas

```bash
pip install pandas
```

Run the project

```bash
python clean_data.py
```

---

## 📥 Input

A messy CSV file containing:

- Duplicate records
- Missing values
- Extra spaces

---

## 📤 Output

A cleaned CSV file stored in

```
output/cleaned_data.csv
```

---

## 👨‍💻 Author

Nazim Rasheed
>>>>>>> ba073cfef9c751d794ed647166a36357ab49c70d
