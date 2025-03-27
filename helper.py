import boto3
import os

def upload_to_s3(file_path, bucket_name, s3_key, aws_access_key=None, aws_secret_key=None, region_name="us-east-1"):
    try:
        if aws_access_key and aws_secret_key:
            s3_client = boto3.client(
                's3'
            )
        else:
            s3_client = boto3.client('s3', region_name=region_name)

        s3_client.upload_file(file_path, bucket_name, s3_key)
        print(f"✅ File '{file_path}' uploaded successfully to 's3://{bucket_name}/{s3_key}'")
        return True
    except Exception as e:
        print(f"❌ Failed to upload '{file_path}' to S3: {e}")
        return False

if __name__ == "__main__":
    file_to_upload = "template.txt"  
    bucket = "s3employees"
    s3_object_name = os.path.basename(file_to_upload)

    upload_to_s3(file_to_upload, bucket, s3_object_name)