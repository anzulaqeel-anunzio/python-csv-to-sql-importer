# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import csv
import sys

def csv_to_sql(csv_file, table_name):
    try:
        with open(csv_file, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader, None)
            
            if not headers:
                return ["-- Error: Empty CSV file"]

            columns = ", ".join(headers)
            statements = []

            for row in reader:
                values = []
                for val in row:
                    if val is None or val.strip() == '':
                        values.append("NULL")
                    else:
                        # Escape single quotes
                        safe_val = val.replace("'", "''")
                        # Try to detect numbers to avoid quoting if strictly needed, 
                        # but typically quoting numbers in SQL ('123') works fine for storage.
                        # For simplicity and safety against SQL injection via text, we quote everything.
                        values.append(f"'{safe_val}'")
                
                val_str = ", ".join(values)
                sql = f"INSERT INTO {table_name} ({columns}) VALUES ({val_str});"
                statements.append(sql)

            return statements

    except FileNotFoundError:
        return [f"-- Error: File {csv_file} not found"]
    except Exception as e:
        return [f"-- Error: {str(e)}"]

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
