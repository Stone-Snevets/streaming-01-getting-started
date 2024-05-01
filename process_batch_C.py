"""
Batch Process C: Third transformation

Read from a file, transform, write to a new file.
In this case, covert degree K to degree F.

Kelvin to Fahrenheit calculation
Fahrenheit = ((Kelvin - 273.15) * 1.8) + 32


Note: 
This is a batch process, but the file objects we use are 
often called 'file-like objects' or 'streams'.
Streaming differs in that the input data is unbounded.

Use logging, very helpful when working with batch and streaming processes. 

"""

# Import from Python Standard Library

import csv
import logging

# Set up basic configuration for logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Declare program constants

INPUT_FILE_NAME = "batchfile_2_kelvin.csv"
OUTPUT_FILE_NAME = "batchfile_3_farenheit.csv"

# Define program functions (bits of reusable code)
# Use docstrings - and indentation matters!


def convert_k_to_f(temp_k):
    """ Convert Kelvin to Fahrenheit
    Use built-in round() to round the answer to 2 decimal places
    Use built-in float() to convert the string input to a float
    """
    logging.debug(f'Calling convert_k_to_f with {temp_k}.')

    # Convert the temperature to degrees Fahrenheit
    temp_f = round(((float(temp_k) - 273.15) * 1.8) + 32, 2)

    logging.debug(f'Converted {temp_k}K to {temp_f}F.')

    # Return the Fahnreheit temperature
    return temp_f


def process_rows(input_file_name, output_file_name):
    """ Read in a file, Convert the temperature, Write to a new file"""
    logging.info(f'Calling process_rows(): {input_file_name} to {output_file_name}.')

    # Open the input file to Read
    with open(input_file_name, 'r') as input_file:
        logging.info(f'Opened for reading: {input_file_name}')

        # Create a CSV reader object
        reader = csv.reader(input_file, delimiter=',')

        # Grab the original header row to skip
        header = next(reader)
        logging.info(f'Skipped header row: {header}')

        # Create an output file to write our converted temperatures to
        #-> Set the newline character to ' ' to avoid unnecessary newlines
        with open(output_file_name, 'w', newline='') as output_file:
            logging.info(f'Create output file: {output_file_name}.')

            # Create a csv writer object
            writer = csv.writer(output_file, delimiter=',')

            # Write a new header row
            writer.writerow(['Year', 'Month', 'Day', 'Time', 'TempF'])

            # For each row of elements in input_file's list
            for row in reader:
                # Assign each measurement to its respective element in the row
                Year, Month, Day, Time, TempK = row

                # Call convert_k_to_f() to convert the Kelvin temperature to Fahrenheit
                TempF = convert_k_to_f(TempK)

                # Write the measurements in the output file
                writer.writerow([Year, Month, Day, Time, TempF])

    # Exit the function
    return


# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        logging.info("===============================================")
        logging.info("Starting batch process C.")
        process_rows(INPUT_FILE_NAME, OUTPUT_FILE_NAME)
        logging.info("Processing complete! Check for new file.")
        logging.info("===============================================")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
