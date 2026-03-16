# Strava Take-Home Assignment
*Sam Lev*

*March 16, 2026*

This is my solution to the take-home coding problem for Strava's summer 2026 software engineering internship application. It parses JSON input, analyzes the data, and prints stats and recommendations!

# Instructions
- To run the program locally, with data from `./data/indexes.json`, use `python3 main.py --debug`

- To run the program dynamically, with data from a live API server, use `python3 main.py --endpoint <ENDPOINT>` with the API endpoint. Optionally, you may add the `--days` flag followed by an integer to pull a specific number of days' worth of data. If the `--days` flag is not provided, the program will default to 7 days. The program will pull the previous XX days' worth of data from the API, including today.

# Notes
This program uses a binary base when converting from bytes to GB, *i.e.*,
$1$ GB is equal to $2^{30} = 1024^3$ bytes.