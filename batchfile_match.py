"""
Determine if temperatures were converted correctly

batchfile_0_farenheit and batchfile_3_farenheit both read the temperature in fahrenheit.
-> Both should have the same outputs

Basic Steps:
1. Open both files
2. Read in one file and store it in a list
3. Read in other file
4. Check if each row in 2nd file matches respective row in created list
5. Count the number of rows that don't match

NOTE: The temperatures in batchfile_0_farenheit are read as integers.
      The temperatures in batchfile_3_farenheit are read as floating point numbers.
      Both are actually strings

Use logging to record process
"""

# Imports
import csv, logging

# Set up basic logger
logging.basicConfig(level=logging.INFO,
                    format= "%(asctime)s - %(levelname)s - %(message)s"
                    )

# Declare the two files we want to observe
ORIGINAL_FILE = 'batchfile_0_farenheit.csv'
NEW_FILE = 'batchfile_3_farenheit.csv'


# Define a function to check similarity
def identical_file(og_file, new_file):
    """
    Function to read in two files and
    check if their contents are identical.
    """
    logging.info(f'Calling identical_file(): {og_file}, {new_file}')

    # Assign a variable to count the number of non-matches
    #-> Start at zero
    num_non_match = 0

    # Assign an index variable
    #-> Start at negative one
    #-> It gets incremented before we do anything with it
    index = -1

    # Open and read the first file
    with open(og_file, 'r') as file_1:
        reader_1 = csv.reader(file_1, delimiter=',')

        logging.info(f'Opened file {og_file}')

        # Skip the header
        header_1 = next(reader_1)

        logging.info(f'Skipped header row {header_1}')

        # Create an empty list
        reader_1_list = []

        # For each row in the first file
        for row_1 in reader_1:
            # Create variables
            Year, Month, Day, Time, TempF = row_1

            # Concatinate a ".0" to the end of the temperature
            TempF = TempF + '.0'

            # Reassign row_1 with the new information
            row_1 = Year, Month, Day, Time, TempF

            # Assign the row to the list
            #-> Make sure each row is itself a list
            reader_1_list.append(list(row_1))

        logging.info('List of elements in reader_1 created.')

        # Open and read the second file
        with open(new_file, 'r') as file_2:
            reader_2 = csv.reader(file_2, delimiter=',')

            logging.info(f'Opened file {new_file}')

            # Skip the header row
            header_2 = next(reader_2)

            logging.info(f'Skipped header row: {header_2}')

            # For each row in the second file
            for row_2 in reader_2:
                # Increment our index variable
                index += 1

                # Check if the rows match
                if row_2 != reader_1_list[index]:
                    # If not, increment the number of errors
                    num_non_match += 1

    # Return the number of misses
    return num_non_match




# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        logging.info("===============================================")
        logging.info("Starting batchfile_match.")

        num_misses = identical_file(ORIGINAL_FILE, NEW_FILE)

        logging.info("Processing complete!")
        logging.info(f'Number of misses: {num_misses}')

        if num_misses == 0:
            logging.info('A Perfect Match!')
        else:
            logging.info('Not quite identical.')
        logging.info("===============================================")
    except Exception as e:
        logging.error(f"An error occurred: {e}")