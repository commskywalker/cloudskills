"""This script creates a private AWS S3 bucket using Boto3 client.
   It expects user input for bucket name (must be globally unique)
   Note: In order to properly execute, the AWS CLI must be configured -> aws configure"""

import sys
import logging
import boto3

try:
    def main():
        """Main function"""
        create_s3bucket(bucket_name)

except SyntaxError as synterr:
    logging.exception(synterr)

def create_s3bucket(b_name):
    """Initializes boto3 client, creates an s3 bucket and prints bucket info"""
    s3_bucket=boto3.client(
        's3',
    )

    bucket = s3_bucket.create_bucket(
        Bucket=b_name,
        ACL='private',
    )

    print(bucket)

bucket_name = sys.argv[1]

if __name__ == '__main__':
    main()
