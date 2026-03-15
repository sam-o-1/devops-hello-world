import time
import redis
import boto3  # New: AWS SDK
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

# New: S3 Client Configuration
s3 = boto3.client(
    's3',
    endpoint_url='http://localstack:4566',  # Talking to your LocalStack container
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    
    # New: Every time someone visits, we log it to our "Cloud" bucket
    try:
        s3.put_object(
            Bucket='soham-devops-project-bucket', 
            Key='logs.txt', 
            Body=f'Total hits so far: {count}'
        )
        s3_status = "Success: Logged to S3"
    except Exception as e:
        s3_status = f"Failed: S3 Error {e}"

    return f'Hello! I have been seen {count} times. S3 Status: {s3_status}\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
