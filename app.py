from flask import Flask
from redis import Redis
import os

app = Flask(__name__)

# Connect to Redis
# Host is 'redis' because that will be the service name in docker-compose
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    # Increment the counter in the database
    redis.incr('hits')
    counter = str(redis.get('hits'), 'utf-8')
    return "This site has been visited " + counter + " times!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
