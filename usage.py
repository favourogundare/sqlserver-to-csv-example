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

## Scenerio 3

'''
1. iterate over table `FILE_MAPPING_SOURCE` and get the `LEGACY_INCIDENT_ID` and `FILENAME` and `FILETYPE`
2. change FILETYPE to 'application/pdf' if FILETYPE is 'pdf', 'image/jpeg' if FILETYPE is 'jpg' or 'jpeg', 'image/png' if FILETYPE is 'png'
3. save into target csv `FILE_MAPPING_TARGET` with columns `LEGACY_INCIDENT_ID` and `FILENAME` and `FILETYPE`
'''

def get_filetype_map(filetype):
    file_type = filetype.lower().replace('.', '')
    filetype_map = {
        'pdf': 'application/pdf',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'mp4': 'video/mp4',
        'mp3': 'audio/mpeg',
        'zip': 'application/zip',
    }
    return filetype_map[file_type]

## initialize the source database
source_db = SourceDB()

## get the columns
file_mapping_columns = source_db.get_columns('FILE_MAPPING_SOURCE')

## 1. initialize the target csv with specific name and set header using the columns
my_csv = TargetCSV('new_my_target.csv').set_head([
    'LEGACY_INCIDENT_ID',
    'FILENAME',
    'FILETYPE'
])

## 2. iterate over the table and append the rows
for row in source_db.iterate_table('FILE_MAPPING_SOURCE'):
    ## manipudated_row TODO: do your manipulation here
    manipulated_row = {}
    manipulated_row['LEGACY_INCIDENT_ID'] = row['LEGACY_INCIDENT_ID']
    manipulated_row['FILENAME'] = row['FILENAME']
    manipulated_row['FILETYPE'] = get_filetype_map(row['FILETYPE'])

    ## add the row to the csv
    my_csv.append_row(manipulated_row)

## 3. save the csv
my_csv.save()

## close the source database
source_db.close()