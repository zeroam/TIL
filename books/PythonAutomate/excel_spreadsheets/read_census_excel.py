"""read_census_excel.py
스프레드시트에서 데이터 읽기
"""
import openpyxl
import pprint

print("Opening workbook...")
wb = openpyxl.load_workbook("censuspopdata.xlsx")
sheet = wb["Population by Census Tract"]
country_data = {}

# Fill in country_data with each country's population and tracts
print("Reading rows...")
for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract
    state = sheet[f"B{row}"].value
    country = sheet[f"C{row}"].value
    pop = sheet[f"D{row}"].value

    # Make sure the key for this state exists
    country_data.setdefault(state, {})
    # Make sure the key for this country in this state exists
    country_data[state].setdefault(country, {"tracts": 0, "pop": 0})

    # Each row represents one census tract, so increment by one
    country_data[state][country]["tracts"] += 1
    # Increase the country pop by the pop in this census tract
    country_data[state][country]["pop"] += int(pop)

# Open a new text file and write the contents of country_data to it
print("Writing resutls...")
result_file = open("census2010.py", "w")
result_file.write("all_data = " + pprint.pformat(country_data))
result_file.close()
print("Done")
