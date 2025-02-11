from src.data_preprocessing import load_data, clean_data

# Function that will use the preprocessing functions
def run_data_processing():
    df = load_data("data/raw_data.csv")  # Ensure correct path to the raw data file
    cleaned_df = clean_data(df)  # Clean the data using the function defined in data_preprocessing.py
    cleaned_df.to_csv("data/cleaned_data.csv", index=False)  # Save the cleaned data
    print("Data Preprocessing Completed!")

if __name__ == "__main__":
    run_data_processing() # This will call the main function when the script is executed