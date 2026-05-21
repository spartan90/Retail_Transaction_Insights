import sys

from Dashboard import Dashboard
from DataLoader import DataLoader
from Analyzer import DataAnalyzer


def main():
    # Get the Data File Name
    fileName = "Retail_Transactions_Dataset.csv"

    try:
        #Load and prepare the data
        print("Going for Validation/cleanup and processing of file")
        dataLoader = DataLoader(file_name=fileName)
        ##return dataframe object
        loadedData = dataLoader.load_and_prepare_data()

        #Perform analytics on the dataframe
        analyzer = DataAnalyzer(dataframe=loadedData)
        analyzer.analyze()

        #Dashboard..
        dashboard = Dashboard(dataframe=loadedData)
        dashboard.generateDashboard(outputFilename='retail_analytics_dashboard.png')

    except FileNotFoundError as error:
        print(f"\n[Error]: {error}", file=sys.stderr)
    except Exception as runtime_error:
        print(f"\n[Exception]: {runtime_error}", file=sys.stderr)

if __name__ == "__main__":
    main()