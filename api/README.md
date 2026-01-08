"""
cache-redis-config

A simple Python package for configuring Redis as a caching layer.

Installation
------------

To install this package, run the following command:

    pip install cache-redis-config

Usage
-----

To use this package, import the `Config` class and create an instance:

    from cache_redis_config import Config

    config = Config(
        host='localhost',
        port=6379,
        password=None,
        db=0
    )

    # Get the connection URL
    url = config.get_url()

    # Perform Redis operations using the URL
    # ...

Dependency
-----------

*   `redis`: The Redis client library.

License
-------

This package is licensed under the MIT License.

Author
------

[Your Name]
"""

import redis

class Config:
    def __init__(self, host, port, password, db):
        self.host = host
        self.port = port
        self.password = password
        self.db = db
        self.redis_client = self._create_client()

    def _create_client(self):
        return redis.Redis(host=self.host, port=self.port, password=self.password, db=self.db)

    def get_url(self):
        return f'redis://{self.host}:{self.port}/'

if __name__ == '__main__':
    config = Config('localhost', 6379, None, 0)
    print(config.get_url())