# CSV_DataFilter: Data Filtering and Organization Script

## Project Overview

The primary goal of this script is to automate the process of segmenting a marketing campaign dataset. It reads a tab-separated CSV file, extracts relevant date information (year and month of customer acquisition), and then creates separate CSV files for each unique combination of year, month, and education level. This organized output makes it easier to analyze specific customer segments.

## Features

-   **Data Loading**: Safely loads data from a specified CSV file.
-   **Data Transformation**:
    -   Converts a customer acquisition date column (`Dt_Customer`) to datetime objects.
    -   Extracts `Cus_year` and `Cus_month` from the `Dt_Customer` column.
-   **Directory Creation**: Automatically creates nested directories for storing filtered data based on year and month.
-   **Data Filtering and Export**: Filters the dataset by year, month, and education level, saving each filtered subset into its own CSV file.
-   **Null Row Handling**: Removes rows that are entirely null after filtering to ensure clean output.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:
-   Python 3.x
-   pandas library

### Installation

1.  Clone the repository (or download the script):
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```
    *(Replace `your-username` and `your-repo-name` with your actual GitHub details.)*

2.  Install the required Python libraries:
    ```bash
    pip install pandas
    ```

### Usage

1.  **Place your data file**:
    Make sure your marketing campaign data file (e.g., `marketing_campaign.csv`) is in the same directory as the `main.py` script, or update the `file_path` variable in `main.py` to point to its correct location. The script expects a tab-separated CSV file.

2.  **Run the script**:
    ```bash
    python main.py
    ```
    The script will print messages to the console indicating its progress, including data loading, transformation, and the saving of filtered files.

## Code Structure

The `main.py` script is organized into several functions:

-   `load_data(file_path)`:
    -   Loads data from the specified `file_path` into a pandas DataFrame.
    -   Handles potential errors during file loading.
    -   **Parameters**: `file_path` (str) - The path to the CSV file.
    -   **Returns**: `pd.DataFrame` or `None`.

-   `transform_data(data)`:
    -   Takes a pandas DataFrame as input.
    -   Prints the initial row and column counts.
    -   Converts the `Dt_Customer` column to datetime objects.
    -   Extracts `Cus_year` and `Cus_month` as new columns.
    -   **Parameters**: `data` (pd.DataFrame) - The DataFrame to transform.
    -   **Returns**: `pd.DataFrame`.

-   `Create_dir(nested_path)`:
    -   Creates nested directories if they do not already exist.
    -   Handles `FileExistsError` gracefully.
    -   **Parameters**: `nested_path` (str) - The path to create.
    -   **Returns**: `None`.

-   `Filter_data(data)`:
    -   Takes the transformed pandas DataFrame.
    -   Identifies unique years, months, and education levels present in the data.
    -   Iterates through each unique combination and filters the DataFrame.
    -   Removes rows where all columns are null (`dropna(how='all')`).
    -   Saves the filtered data to a CSV file within a structured directory.
    -   **Parameters**: `data` (pd.DataFrame) - The DataFrame to filter.
    -   **Returns**: `str` - A success message.

-   `if __name__ == "__main__":`:
    -   The main execution block of the script.
    -   Defines the `file_path` for the input CSV.
    -   Calls `load_data`, `transform_data`, and `Filter_data` in sequence.
    -   Prints status messages throughout the process.

## Output Structure

The filtered CSV files will be saved in a directory structure like this:

```
Filtered_Data/
├── 2012/
│   ├── 10/
│   │   ├── Graduation.csv
│   │   └── Master.csv
│   └── 11/
│       ├── PhD.csv
│       └── Basic.csv
└── 2013/
    └── 01/
        ├── 2n Cycle.csv
        └── Graduation.csv
    ...
```
> **Note**: The base output path is currently hardcoded in the `Filter_data` function (e.g., `D:\Tasks\Record_Filter\Filtered_Data`). For better portability, you may want to make this configurable.

## Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, please feel free to:
1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add new feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

## License

This project is open-sourced under the MIT License. See the `LICENSE` file for more details.
