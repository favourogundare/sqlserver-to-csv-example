# SQL Server to CSV example
This example shows how to use the SQL Server connector to read data from a SQL Server database and write it to a CSV file.

## Prerequisites
- [SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
- [SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15)
- [SQL Server JDBC Driver](https://docs.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server?view=sql-server-ver15)
- [Python 3.11+](https://www.python.org/downloads/)

## Setup environment
1. Install the SQL Server JDBC Driver
2. Create virtual environment
```
python -m venv venv
```

3. Activate virtual environment
```
venv\Scripts\activate
```

4. Install dependencies
```
pip install -r requirements.txt
```

## Setup environment variables
1. Create a `.env` file in the root directory of the project using .env.example as a template.
2. Fill in the environment variables in the `.env` file.
```
DATABASE_DRIVER=
DATABASE_HOST=
DATABASE_NAME=
TRUSTED_CONNECT='yes'
```

## Run the example
```
python usage.py
```

## Expected output
The usage.py script will create a CSV file in the root directory of the project called `my_target.csv` and a csv with {datetime}.csv as the name. 

## Thanks

Follow me on Twitter [@mohsin_rizz](https://twitter.com/mohsin_rizz)