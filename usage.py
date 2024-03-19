from source_db import SourceDB
from target_csv import TargetCSV


## initialize the source database
source_db = SourceDB()

## get the columns
incident_parties_columns = source_db.get_columns('Raw_SourceNames')

## 1. initialize the target csv with specific name and set header using the columns
my_csv = TargetCSV('Raw_SourceNames.csv').set_head([
    'PERSONID',
    'FULLNAME',
    'DOB',
    'SSN'
])

## 2. iterate over the table and append the rows
for row in source_db.iterate_table('Raw_SourceNames'):
    ## manipudated_row TODO: do your manipulation here
    manipulated_row = {}
    manipulated_row['PERSONID'] = row['personid']
    manipulated_row['FULLNAME'] = row['fullname']
    if row['dob']:
        manipulated_row['DOB'] = row['dob'].strftime('%Y-%m-%d')
    manipulated_row['SSN'] = row['ssn']

    ## add the row to the csv
    my_csv.append_row(manipulated_row)

## 3. save the csv
my_csv.save()

## close the source database
source_db.close()