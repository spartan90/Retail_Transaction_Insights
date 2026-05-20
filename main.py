from DataLoader import DataLoader
from analyzer import DataAnalyzer


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

    except FileNotFoundError as fnf_error:
        print(f"\n[Configuration Error]: {fnf_error}", file=sys.stderr)
    except Exception as runtime_error:
        print(f"\n[Unexpected Execution Exception]: {runtime_error}", file=sys.stderr)

if __name__ == "__main__":
    main()