import csv
from datetime import datetime

class TargetCSV:
    def __init__(self, filename='target.csv'):
        self.filename = filename
        self.head = []
        self.rows = []
    
    def autoname(self):
        now = datetime.now()
        self.filename = now.strftime("%Y%m%d_%H%M%S") + '.csv'
        return self

    def set_head(self, head):
        self.head = head
        return self
    
    def append_row(self, dict_row):
        ## check if the row has all the columns
        if len(dict_row.keys()) != len(self.head):
            raise Exception('Row does not have all the columns')

        ## check if the row has all the columns
        for key in dict_row.keys():
            if key not in self.head:
                raise Exception('Row has extra columns')
        
        ## append the row
        self.rows.append(dict_row)

    def save(self):
        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.head)
            writer.writeheader()
            for row in self.rows:
                writer.writerow(row)
        return self