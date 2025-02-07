import pandas as pd
from pandasql import sqldf

# Open and read the JSON file
flexjson = pd.read_json('balancesheet.json',orient='index')
flexjsondf = pd.DataFrame(flexjson)

print(flexjsondf)