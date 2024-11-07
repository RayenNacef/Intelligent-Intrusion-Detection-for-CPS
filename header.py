import pandas as pd
# Load the Excel file without headers
df = pd.read_excel(r"C:\Users\dell\Desktop\SCPS\ListAttacks.xlsx", header=None)

# Inspect the first row to verify the structure
print("First row (for header analysis):")
print(df.iloc[0])

# Define your column names explicitly if there are exactly 9 columns
column_names = [
    "Date", "Start Time", "End Time", "Component", "Current State", 
    "Action Taken", "Successful Action", "Immediate Impact", "Extended Impact"
]

# Assign the column names if they match the number of columns in `df`
if len(column_names) == df.shape[1]:
    df.columns = column_names
    print("okaay")
else:
    print(f"Error: Expected 9 columns but found {df.shape[1]}. Adjust `column_names` list.")
    # You may need to debug further based on the output

# Drop the first row if it contains header data
df = df.drop(0).reset_index(drop=True)

# Save to a new Excel file or inspect
print(df.head())
df.to_excel("Cleaned_ListAttacks.xlsx", index=False)