# dashboard.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Dashboard:

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def generateDashboard(self, outputFilename: str = 'retail_analytics_dashboard.png'):

        print("Dashboarding and Visualization")

        sns.set_theme(style="whitegrid")
        plt.figure(figsize=(16, 12))

        #Bar plot of the number of transactions per city
        plt.subplot(2, 2, 1)
        city_counts = self.df['City'].value_counts().sort_values(ascending=False)
        sns.barplot(x=city_counts.values, y=city_counts.index, palette='viridis', hue=city_counts.index, legend=False)
        plt.title('Number of Transactions per City', fontsize=13, fontweight='bold')
        plt.xlabel('Transaction Count')
        plt.ylabel('City')

        #Pie chart showing distribution of payment methods
        plt.subplot(2, 2, 2)
        payment_counts = self.df['Payment_Method'].value_counts()
        plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', startangle=140,
                colors=sns.color_palette('pastel'))
        plt.title('Distribution of Payment Methods', fontsize=13, fontweight='bold')

        #Line chart of monthly revenue trends (grouped by year if applicable)
        plt.subplot(2, 2, 3)
        monthly_revenue = self.df.groupby(['Txn_Year', 'Txn_Month'])['Total_Cost'].sum().reset_index()
        sns.lineplot(data=monthly_revenue, x='Txn_Month', y='Total_Cost', hue='Txn_Year', marker='o', linewidth=2.5,
                     palette='tab10')
        plt.title('Monthly Revenue Trends by Year', fontsize=13, fontweight='bold')
        plt.xlabel('Month (1-12)')
        plt.ylabel('Total Sales Revenue ($)')
        plt.xticks(range(1, 13))

        #Heatmap or stacked bar showing revenue by season and customer category
        plt.subplot(2, 2, 4)
        pivot_heatmap = self.df.pivot_table(index='Season', columns='Customer_Category', values='Total_Cost',
                                            aggfunc='sum')
        sns.heatmap(pivot_heatmap, annot=True, fmt=',.0f', cmap='YlGnBu', cbar_kws={'label': 'Revenue ($)'})
        plt.title('Revenue by Season and Customer Category', fontsize=13, fontweight='bold')
        plt.xlabel('Customer Category')
        plt.ylabel('Season')
        plt.tight_layout()
        plt.savefig(outputFilename, dpi=300)
        plt.close()

        print(f"Visualization Dashboard generated to: '{outputFilename}'")