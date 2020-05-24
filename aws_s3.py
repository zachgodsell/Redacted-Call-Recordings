import boto3
import json


# returns a list of wav files from s3 bucket
def list_files():
    s3 = boto3.client('s3')
    objects = s3.list_objects(Bucket='axelsolutions')
    data = objects['Contents']
    count = 0
    wav = []
    for files in data:
        if '.wav' in files['Key']:
            data = files['Key']
            wav.append(data)
    return wav


def download(bucket_name, object_name, file_name):
    try:
        s3 = boto3.client('s3')
        s3.download_file(bucket_name, object_name, file_name)
        print(f'Download of {file_name} was successful')
    except Exception as e:
        print(f'Download of {file_name} was not succesful. Error: {e}')



def upload(bucket_name, file_name, object_name):
    try:
        s3 = boto3.client('s3')
        with open(file_name, "rb") as f:
            s3.upload_fileobj(f, bucket_name, object_name)
        print(f'Upload of {object_name} was successful')
    except Exception as e:
        print(f'Upload of {object_name} was not successful Error: {e}')

