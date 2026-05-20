from DataLoader import DataLoader


def main():
    # Get the Data File Name
    fileName = "Retail_Transactions_Dataset.csv"

    try:
        #Load and prepare the data
        dataLoader = DataLoader(file_name=fileName)
        loadedData = dataLoader.load_and_prepare_data()


    except FileNotFoundError as fnf_error:
        print(f"\n[Configuration Error]: {fnf_error}", file=sys.stderr)
    except Exception as runtime_error:
        print(f"\n[Unexpected Execution Exception]: {runtime_error}", file=sys.stderr)

if __name__ == "__main__":
    main()