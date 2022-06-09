import datetime
from dateutil.relativedelta import relativedelta
today = datetime.today()
train_month = today - relativedelta(month=-2)
val_month = today - relativedelta(month=-1)

train_path = f'./data/fhv_tripdata_{train_month.strftime("%Y-%m")}.parquet'
val_path = f'./data/fhv_tripdata_{val_month.strftime("%Y-%m")}.parquet'
print(train_path, val_path)