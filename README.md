# CSV to SQL Importer (Python)

A CLI tool to convert any CSV file into a series of SQL `INSERT` statements.

## Features

-   **Auto-Schema**: Infers column names from the CSV header.
-   **Safe Quoting**: Handles strings, numbers, and NULLs properly.
-   **Custom Table**: Specify the target table name.

## Installation

1.  **Clone the repository**
2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

```bash
python run_importer.py --csv input.csv --table users
```

This will output:
```sql
INSERT INTO users (id, name, email) VALUES (1, 'John Doe', 'john@example.com');
...
```

To save to a file:
```bash
python run_importer.py --csv input.csv --table users > output.sql
```

## Contact

Developed for Anunzio International by Anzul Aqeel.
Contact +971545822608 or +971585515742.

## License

MIT


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
