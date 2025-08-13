import os
import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path, sep='\t', encoding='utf-8')
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    
# handle missing values
def handle_missing_values(data):
    """
    Handle missing values in the DataFrame.
    
    Parameters:
    data (pd.DataFrame): The DataFrame to process.
    
    Returns:
    pd.DataFrame: DataFrame with missing values handled.
    """
    # Fill missing values in 'Income' with the mean
    if 'Income' in data.columns:
        data['Income'].fillna(data['Income'].mean(), inplace=True)
    
    # Fill missing values in 'Complain' with 0
    if 'Complain' in data.columns:
        data['Complain'].fillna(0, inplace=True)
    
    # Fill missing values in 'Dt_Customer' with a placeholder date
    if 'Dt_Customer' in data.columns:
        data['Dt_Customer'].fillna('1900-01-01', inplace=True)
    
    return data
    
# Transform the data if necessary
def transform_data(data):
    # Count the number of rows and columns
    Row_Count, Column_Count = data.shape
    print(f"Row Count: {Row_Count}, Column Count: {Column_Count}")

    # Convert the 'date_col' to datetime
    data['Dt_Customer'] = pd.to_datetime(data['Dt_Customer'], errors='coerce')

    # Extract year and month from 'Dt_Customer'
    data['Cus_year'] = data['Dt_Customer'].dt.year.astype('Int64')
    data['Cus_month'] = data['Dt_Customer'].dt.month.astype('Int64')

    return data


def Create_dir(nested_path):
    try:
        os.makedirs(nested_path)
        print(f"Nested directories '{nested_path}' created successfully.")
    except FileExistsError:
        print(f"Nested directories '{nested_path}' already exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def Filter_data(data):

    # Extract Unique values for years, months, and education levels
    Years = data['Cus_year'].unique().tolist()
    Months = data['Cus_month'].unique().tolist()
    Education = data['Education'].unique().tolist()
    print("Years of Customer:", Years)
    print("Months of Customer", Months)
    print("Education levels:", Education)

    for year in Years:
        for month in Months:
            for education in Education:
                _filter1 = data["Cus_year"]==year
                _filter2 = data["Cus_month"]==month
                _filter3 = data["Education"]==education
                try:
                    # Create directory structure for each year, month
                    Create_dir(f"D:\\Tasks\\Record_Filter\\Filtered_Data\\{year}\\{month}")

                    d1 = data.where(_filter1 & _filter2 & _filter3, inplace=False)
                    # Remove rows only if ALL columns in that row are null
                    d1 = d1.dropna(how='all')
                    d1.to_csv(f"D:\\Tasks\\Record_Filter\\Filtered_Data\\{year}\\{month}\\{education}.csv", index=False)

                    print(f"Filtered data for {year}-{month} with education {education} saved.")
                except Exception as e:
                    continue
    return "Data filtered and saved successfully."



if __name__ == "__main__":
    # Define the path to the CSV file
    file_path = os.path.join(os.getcwd(), "marketing_campaign.csv")
    # Load the data
    data = load_data(file_path)
    if data is not None:
        print("Data loaded successfully:")
        print(data.head())
    else:
        print("Failed to load data.")

    # Transform the data
    data = transform_data(data)
    if data is not None:
        print("Data transformed successfully.")
    else:
        print("Failed to transform data.")

    # Filter the data
    Result = Filter_data(data)
    print(Result)


    