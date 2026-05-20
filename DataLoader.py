
import pandas as pd
from pathlib import Path


class DataLoader:
    """Read and validate the file"""

    def __init__(self, file_name: str):
        self.filePath = Path("resources") / file_name

    def load_and_prepare_data(self) -> pd.DataFrame:
        """Validation :- check file path"""
        print(f"Verifying file path: {self.filePath.resolve()}")

        if not self.filePath.exists() or not self.filePath.is_file():
            raise FileNotFoundError(f"File not found at {self.filePath}")

        print("File verified. Reading excel....")
        df = pd.read_csv(self.filePath)

        #drop empty rows if any
        df = df.dropna(subset=['Date']).copy()

        #parse different date format
        df['Formatted_Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True)

        print("Extracting time-series")
        df['Txn_Year'] = df['Formatted_Date'].dt.year
        df['Txn_Month'] = df['Formatted_Date'].dt.month
        df['Txn_Day_Of_Week'] = df['Formatted_Date'].dt.day_name()

        print("Update boolean values...")
        if df['Discount_Applied'].dtype == 'object':
            df['Discount_Applied'] = df['Discount_Applied'].astype(str).str.upper().map({'TRUE': True, 'FALSE': False})

        print("--- DataLoad completed ---\n")
        return df