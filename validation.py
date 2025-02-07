import json
from core.extent_table import ExtentTable
from core.table_maker import TableMaker

with open('balancesheet.json','r') as flexjsonraw:
    flexjson = json.load(flexjsonraw)

print(flexjson)

