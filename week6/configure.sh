#xport env variables
export OUTPUT_FILE_PATTERN="s3://nyc-duration/out/{year:04d}-{month:02d}.parquet"
export INPUT_FILE_PATTERN="s3://nyc-duration/in/{year:04d}-{month:02d}.parquet"
export S3_ENDPOINT_URL="http://localhost:4566"

#start s3 service
docker-compose up -d

sleep 10

#create s3 bucket
aws --endpoint-url=${S3_ENDPOINT_URL} s3 mb s3://nyc-duration