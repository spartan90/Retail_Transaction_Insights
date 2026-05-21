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

        print("\nCustomer categories spend the most on average:")
        avg_spend = self.df.groupby('Customer_Category')['Total_Cost'].mean().sort_values(ascending=False)
        print(avg_spend.round(2).to_string())

        print("\nDo certain customer categories prefer specific payment methods:")
        payment_matrix = pd.crosstab(self.df['Customer_Category'], self.df['Payment_Method'])
        print(payment_matrix.to_string())

        print("\nWhat is the average number of items bought per transaction per store type:")
        avg_items = self.df.groupby('Store_Type')['Total_Items'].mean().sort_values(ascending=False)
        print(avg_items.round(2).to_string())
        print("\n")

        print("What is the average cost of transactions where a discount was applied vs not applied?")
        avg_cost_discount = self.df.groupby('Discount_Applied')['Total_Cost'].mean()
        print(avg_cost_discount.round(2).to_string())

        self.df['Promotion_Cleaned'] = self.df['Promotion'].fillna('No Promo')

        print("\nCompare the average number of items purchased for different promotion types")
        avg_items_promo = self.df.groupby('Promotion_Cleaned')['Total_Items'].mean().sort_values(ascending=False)
        print(avg_items_promo.round(2).to_string())

        print("\nWhich promotion type seems to be most effective in terms of increasing total cost? ")
        promo_effectiveness = self.df.groupby('Promotion_Cleaned')['Total_Cost'].mean().sort_values(ascending=False)
        print(promo_effectiveness.round(2).to_string())
        print("\n")

        print("Which season has the highest total revenue? ")
        total_revenue_season = self.df.groupby('Season')['Total_Cost'].sum().sort_values(ascending=False)
        for season, gross_sales in total_revenue_season.items():
            print(f"  {season:<12} : ${gross_sales:,.2f}")

        print("\nAre there seasonal preferences for certain store types or product categories? ")
        seasonal_store = self.df.groupby(['Season', 'Store_Type']).size().unstack(fill_value=0)
        print(seasonal_store.to_string())
        print("\n")

