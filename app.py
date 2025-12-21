from flask import Flask
from redis import Redis
import os

app = Flask(__name__)

# Connect to Redis (using the environment variable for flexibility)
redis_host = os.environ.get('REDIS_HOST', 'redis')
redis = Redis(host=redis_host, port=6379)

@app.route('/')
def hello():
    try:
        redis.incr('hits')
        counter = str(redis.get('hits'), 'utf-8')
    except Exception:
        counter = "Error connecting to Redis"

    # HTML with a RED background to prove the update worked
    html = f"""
    <div style="background-color: #e74c3c; color: white; padding: 50px; font-family: sans-serif; text-align: center;">
        <h1>🔥 CI/CD Pipeline Success! 🔥</h1>
        <p>This update was deployed automatically by GitHub Actions.</p>
        <br>
        <h2>Visitor Count: {counter}</h2>
    </div>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
