import argparse
import pandas as pd

def clean_data(input1, input2, output):
    # Load data from input files
    data1 = pd.read_csv(input1)
    data2 = pd.read_csv(input2)

    # Merge the two input data files based on ID value
    merged_data = pd.merge(data1, data2, left_on="respondent_id", right_on="id")

    # Drop rows with missing values
    merged_data = merged_data.dropna()

    # Drop rows with "insurance" or "Insurance" in the job column
    merged_data = merged_data[~merged_data["job"].str.contains('insurance|Insurance')]

    # Remove redundant key column after merging
    merged_data = merged_data.drop(columns=["id"])

    # Save cleaned data to the output file
    merged_data.to_csv(output, index=False)
    # Print the shape of the output file
    output_data = pd.read_csv(output)
    print("Output file shape:", output_data.shape)

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Data cleaning script")
    parser.add_argument("input1", help="Path to respondent_contact.csv file")
    parser.add_argument("input2", help="Path to respondent_other.csv file")
    parser.add_argument("output", help="Path to output file")


    args = parser.parse_args()


    clean_data(args.input1, args.input2, args.output)