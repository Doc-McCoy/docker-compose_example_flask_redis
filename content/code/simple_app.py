from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return '<b>Welcome do Docker Compose!</b><br><br>You have visited this site {} times.\n'.format(count)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
