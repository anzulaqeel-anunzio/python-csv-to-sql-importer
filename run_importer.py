# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
from importer.converter import csv_to_sql

def main():
    parser = argparse.ArgumentParser(description="Convert CSV to SQL INSERT statements.")
    parser.add_argument("--csv", required=True, help="Path to input CSV file")
    parser.add_argument("--table", required=True, help="Target database table name")
    
    args = parser.parse_args()

    statements = csv_to_sql(args.csv, args.table)
    
    for stmt in statements:
        print(stmt)

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
