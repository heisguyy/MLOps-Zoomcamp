import batch
import pandas as pd
from datetime import datetime


def dt(hour, minute, second=0):
    return datetime(2021, 1, 1, hour, minute, second)

def test_prepare_data():
    data = [
        (None, None, dt(1, 2), dt(1, 10)),
        (1, 1, dt(1, 2), dt(1, 10)),
        (1, 1, dt(1, 2, 0), dt(1, 2, 50)),
        (1, 1, dt(1, 2, 0), dt(2, 2, 1)),        
    ]

    columns = ['PUlocationID', 'DOlocationID', 'pickup_datetime', 'dropOff_datetime']
    df = pd.DataFrame(data, columns=columns)


    expected_output = [
        ("-1","-1",dt(1,2),dt(1,10),8.000000000000002),
        ("1","1",dt(1,2),dt(1,10),8.000000000000002)
    ]
    columns.append("duration")
    expected_df = pd.DataFrame(expected_output,columns=columns)

    result = batch.prepare_data(df)

    assert expected_df.equals(result)