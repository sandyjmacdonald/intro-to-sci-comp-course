#!/usr/bin/env python3

# Import the Python libraries that will be used.
import argparse
import pandas as pd

# Set up command line arguments for the input and output files.
parser = argparse.ArgumentParser()

# Each argument has a short and a long version, i.e. -i and --input,
# in this case. The help text is displayed along with the various
# command line arguments when you type "python3 parse-weather-data.py -h"

# Input file argument
parser.add_argument(
    "-i",
    "--input",
    type=str,
    help="input file (comma-separated) from which the data should be read",
)

# Output file argument
parser.add_argument(
    "-o",
    "--output",
    type=str,
    help="output file (comma-separated) to which the data should be written",
)

# We can access the data associated with each argument by using, e.g.
# "args.input" to see the input argument's value.
args = parser.parse_args()

# We'll use the Pandas Python library, which is used to read and process
# tabular data. It has a specific function just for reading in CSV files,
# which our data are.
df = pd.read_csv(args.input)

# The timestamp (in the first column) for each row of data is a combined
# data and time separated by a space. Because we want to group the values
# by date, we'll split the date and time into new columns, using the
# space " " to split them.
df[["date", "time"]] = df["time"].str.split(" ", expand=True)

# We'll group the rows of data by date and then get the mean of the
# "temperature" column, and save the result to a new variable called
# daily_means
daily_means = df.groupby("date")["temperature"].mean().reset_index()

# Finally, we'll write the resulting daily mean temperatures to the output
# file passed in as an argument, i.e. args.output.
daily_means.to_csv(args.output, index=False)
