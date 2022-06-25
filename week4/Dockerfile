FROM agrigorev/zoomcamp-model:mlops-3.9.7-slim

COPY . .

RUN pip install pipenv

RUN pipenv install --system --deploy --ignore-pipfile

CMD ["python","starter.py","2021","4"]