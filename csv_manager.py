import csv


class CSV_Manager:
    def __init__(self, filename):
        self.filename = filename

    def get_csv_as_dicts(self):
        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            rows = [row for row in csv_reader]
            return self.to_dict(rows)

    def to_dict(self, rows):
        keys = rows[0]
        all_data = []
        for row in rows: 
            data_dict = {}
            for i in range(0, len(row)):
                data_dict[keys[i]] = row[i]
            all_data.append(data_dict)
        return all_data

    def to_obj(self, data):
        
        all_data={}
        data.pop(0)
        for d in data:
            if( d['author'] in all_data.keys()):
                all_data[d['author']].append(d)
            else: all_data[d['author']]=[d]
        for d in data:
            if(d['category'] in all_data.keys()):
                all_data[d['category']].append(d)
            else : all_data[d['category']]=[d]
        return all_data
    