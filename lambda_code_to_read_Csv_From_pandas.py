import boto3
import pandas as pd
from io import BytesIO

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    print(event)
    try:
        bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
        s3_file_name = event["Records"][0]["s3"]["object"]["key"]
        print(bucket_name)
        print(s3_file_name)
        req_data = s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)
        print(req_data['Body'])
        df_s3_data = pd.read_csv(req_data['Body'], sep=',')
        print(df_s3_data.head())
    except Exception as err:
        print(err)
    # # TODO implement
    # bucket = s3.Bucket('first-asw-s3-bucket')
    # print(bucket.objects.all())
    # print("=========================")
    # for obj in bucket.objects.all():
    #     key = obj.key
    #     print(key)
