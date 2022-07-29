import pandas as pd
from datetime import datetime
import os 

def dt(hour, minute, second=0):
    return datetime(2021, 1, 1, hour, minute, second)

data = [
        (None, None, dt(1, 2), dt(1, 10)),
        (1, 1, dt(1, 2), dt(1, 10)),
        (1, 1, dt(1, 2, 0), dt(1, 2, 50)),
        (1, 1, dt(1, 2, 0), dt(2, 2, 1)),        
    ]

columns = ['PUlocationID', 'DOlocationID', 'pickup_datetime', 'dropOff_datetime']
df = pd.DataFrame(data, columns=columns)

options = {
    'client_kwargs': {
        'endpoint_url': os.getenv("S3_ENDPOINT_URL")
    }
}

year = 2021
month = 1
input_file = os.getenv("INPUT_FILE_PATTERN")
input_file = input_file.format(year=year, month=month)


df.to_parquet(
    input_file,
    engine='pyarrow',
    compression=None,
    index=False,
    storage_options=options
)