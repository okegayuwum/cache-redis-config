import os
import redis
from dotenv import load_dotenv

load_dotenv()

class RedisConfig:
    def __init__(self):
        self.host = os.getenv('REDIS_HOST', 'localhost')
        self.port = int(os.getenv('REDIS_PORT', 6379))
        self.password = os.getenv('REDIS_PASSWORD', None)
        self.db = int(os.getenv('REDIS_DB', 0))

    def get_redis_connection(self):
        return redis.Redis(
            host=self.host,
            port=self.port,
            password=self.password,
            db=self.db,
            decode_responses=True
        )

def main():
    redis_config = RedisConfig()
    redis_client = redis_config.get_redis_connection()

    try:
        redis_client.ping()
        print("Connected to Redis successfully!")
    except redis.ConnectionError as e:
        print(f"Failed to connect to Redis: {e}")

if __name__ == "__main__":
    main()