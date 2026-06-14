import gspread
import pandas as pd

gc = gspread.service_account(
    filename="credentials/d912-498923-cff34531ec87.json"
)

sheet = gc.open(
    "D912 Database"
)

inventario = sheet.worksheet(
    "Inventario"
)

df = pd.DataFrame(
    inventario.get_all_records()
)

print(df.head())
print(df.columns.tolist())