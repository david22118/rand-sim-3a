from csv_manager import CSV_Manager
from manipulator import Manipulator
import json

def filter_CSV(filter_field, value):
    reader = CSV_Manager("./articles.csv")
    articles = reader.get_csv_as_dicts()
    manipulator = Manipulator(articles)
    filtered = manipulator.filter_by(filter_field, value)
    return list(filtered)
def count_articles(filter_field,value):
    filtered = filter_CSV(filter_field, value)
    return len(filtered)
def is_article(filter_field,value):
    return count_articles(filter_field,value)>0
def longest_article(filter_field,value):
    filtered = filter_CSV(filter_field, value)
    max = 0
    for a in filtered:
        if(int(a['pages'])>max):
            max = int(a['pages'])
            article=a
    return article

    

reader = CSV_Manager("./articles.csv")
articles = reader.get_csv_as_dicts()

print(reader.to_obj(articles))