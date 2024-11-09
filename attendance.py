import openpyxl
import json
from datetime import datetime
import pathlib
from icecream import ic

# Load data from JSON files
with open("public/names.json", "r") as file:
    names_data = json.load(file)

with open("data/data.json", "r") as file:
    attendance_data = json.load(file)

# Get the current date and month
today = datetime.today()
current_day = today.day
month_days = 31  # Modify this based on the current month

# Extract names from both JSON files
names_from_json = {person['name'] for person in names_data}  # Set for names in names.json
names_in_data = {person['name'] for person in attendance_data}  # Set for names in data.json

date_string = attendance_data[0]["day"]
ic(date_string)

directory = pathlib.Path("data")
xlsx_files = list(directory.glob('*.xlsx'))

if not xlsx_files:
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Attendance"
    ws.cell(row=1, column=1, value="Names")
    for i in range(1, month_days + 1):
        ws.cell(row=1, column=i + 1, value=str(i))
    
    for i, name in enumerate(names_from_json, start=2):
        ws.cell(row=i, column=1, value=name)

    wb.save(f"data/attendance_sheet_Nov.xlsx")
    
else:

    wb = openpyxl.load_workbook(f"data/attendance_sheet_Nov.xlsx")
    ws = wb.active
    for row in ws.iter_rows(min_row=2, min_col=1):
        name_cell = row[0]
        if name_cell.value in names_in_data:
            for cell in row[1:]:
                #day = cell.column - 1
                for data in attendance_data:
                    date_string = data["day"]
                    day = datetime.fromisoformat(date_string.replace("Z", "+00:00"))
                    day = day.day
                    ic(day)
                    if day == current_day:
                        ic(current_day)
                        cell.value = "✓"

    wb.save(f"data/attendance_sheet_Nov.xlsx")

#print("Excel file has been generated as attendance_sheet.xlsx.")

