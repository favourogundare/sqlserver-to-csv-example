from source_db import SourceDB
from target_csv import TargetCSV

## Scenerio 1

## initialize the source database
source_db = SourceDB()

## get the columns
incident_parties_columns = source_db.get_columns('INCIDENT_PARTIES_SOURCE')

## 1. initialize the target csv with auto name and set header using the columns
my_csv = TargetCSV().autoname().set_head(incident_parties_columns)

## 2. iterate over the table and append the rows
for row in source_db.iterate_table('INCIDENT_PARTIES_SOURCE'):

    ## manipudated_row TODO: do your manipulation here
    manipulated_row = {}
    manipulated_row = row

    ## add the row to the csv
    my_csv.append_row(manipulated_row)

## 3. save the csv
my_csv.save()

## close the source database
source_db.close()

## Scenerio 2

## initialize the source database
source_db = SourceDB()

## get the columns
incident_parties_columns = source_db.get_columns('INCIDENT_PARTIES_SOURCE')

## 1. initialize the target csv with specific name and set header using the columns
my_csv = TargetCSV('my_target.csv').set_head(incident_parties_columns)

## 2. iterate over the table and append the rows
for row in source_db.iterate_table('INCIDENT_PARTIES_SOURCE'):
    ## manipudated_row TODO: do your manipulation here
    manipulated_row = {}
    manipulated_row = row

    ## add the row to the csv
    my_csv.append_row(manipulated_row)

## 3. save the csv
my_csv.save()

## close the source database
source_db.close()