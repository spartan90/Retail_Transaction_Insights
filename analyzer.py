import pandas as pd
import ast

class DataAnalyzer:

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def analyze(self):
        ##Data exploration results

        total_transactions = self.df.shape
        total_unique_customers = self.df['Customer_Name'].nunique()

        print(f"Total Transactions Count : {total_transactions}")
        print(f"Total Unique Customers  : {total_unique_customers}")

        # Unpack literal strings of product lists
        def parseProducts(products):
            try:
                return ast.literal_eval(products)
            except (ValueError, SyntaxError):
                return []

        self.df['Clean_Product_List'] = self.df['Product'].apply(parseProducts)
        all_individual_products = self.df['Clean_Product_List'].explode()

        print("\nTop 5 Most Common Products Sold:")
        print(all_individual_products.value_counts().head(5).to_string())

        print("\nTop Cites having highest number of transactions:")
        print(self.df['City'].value_counts().head(5).to_string())
        print("\n")

        print("Customer categories spend the most on average:")
        avg_spend = self.df.groupby('Customer_Category')['Total_Cost'].mean().sort_values(ascending=False)
        print(avg_spend.round(2).to_string())



