import pandas as pd
import json

# ✅ 1. Set your file paths
input_excel = 'Uber Trip Details.xlsx'   # Update with your file name
output_json = 'Uber_Trips.json'          # Desired output file name

# ✅ 2. Read the Excel file (specify sheet if needed)
df = pd.read_excel(input_excel, sheet_name='Trip Details')

# ✅ 3. Convert to JSON (list of records)
json_data = df.to_dict(orient='records')

# ✅ 4. Save JSON to file
with open(output_json, 'w') as f:
    json.dump(json_data, f, indent=4, default=str)  # default=str to handle datetimes

print(f"✅ JSON file saved as: {output_json}")
