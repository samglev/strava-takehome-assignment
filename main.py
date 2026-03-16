"""
A simple program to parse and analyze logging data obtained from an API query

Author: Sam Lev
3/16/26
"""

import argparse
import sys
import json
import analyze
import fetcher

def main():
    #provided starter code for parsing command-line arguments
    parser = argparse.ArgumentParser(description="Process index data.")
    parser.add_argument("--endpoint", type=str, default="",
                        help="Logging endpoint")
    parser.add_argument("--debug", action="store_true",
                        help="Debug flag used to run locally")
    parser.add_argument("--days", type=int, default=7,
                        help="Number of days of data to parse")
    args = parser.parse_args()

    data = None

    if args.debug:
        try:
            data = get_data_from_file("data/indexes.json")
        except Exception as err:
            sys.exit("Error reading data from file. Error: " + str(err))
    else:
        try:
            data = fetcher.get_data_from_server(args.endpoint, args.days)
        except Exception as err:
            sys.exit("Error reading data from API endpoint. Error: " + str(err))

    data = analyze.pre_process(data)
    analyze.print_largest_indexes(data)
    analyze.print_most_shards(data)
    analyze.print_least_balanced(data)

def get_data_from_file(filename):
    """
    returns a list of dictionaries containing data from JSON file
    """
    with open(filename) as f:
        data_dict = json.load(f)
    return data_dict


if __name__ == '__main__':
    main()
