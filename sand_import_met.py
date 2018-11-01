import requests
from io import StringIO
import pandas as pd

def name (y):
    met_file = {           
    "Waikerie":"24018",
    "Carwarp":"76005",
    "Ouyen":"76047",
    "Karoonda":"25006",
    "Murlong":"18046",
    "Yenda":"75079",
    "Lameroo":"25509",
    "Bute":"21012",
    "Brimpton Lake":"18005",
    "Cadgee":"26099"
    }
    
    x = (met_file[y])
    
       
    params = {
        'apikey': "Kvsj6LwGthiRRUoxGazEDLikHvDxh5kOJDvbRZp4",
        'format': 'csv', 
        'station': x,
        'start': '20160101',
        'finish': '20160112',
        'variables': 'daily_rain'
        }
    

    r = requests.get('https://siloapi.longpaddock.qld.gov.au/pointdata', params=params)
    met_data_csv = r.text 
    

    point_data_csv = StringIO(met_data_csv)

    # Import data into a Pandas dataframe
    point_data_csv_df = pd.read_csv(point_data_csv,names=["station",                 # Strings for our column headings
                                    "date", 
                                    "daily_rain",
                                    "daily_rain_source"], skiprows=1,
                               parse_dates=[1])               
                             
    
    return(point_data_csv_df)