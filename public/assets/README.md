# cache-redis-config

## Table of Contents

* [Overview](#overview)
* [Installation](#installation)
* [Usage](#usage)
* [API](#api)
* [Contributing](#contributing)
* [License](#license)

## Overview

This project provides a configuration file for Redis to be used as a cache layer.

## Installation

To install the cache-redis-config, run the following command:

```bash
npm install cache-redis-config
```

## Usage

To use the cache-redis-config, create a new instance and pass the configuration options:

```javascript
const CacheRedisConfig = require('cache-redis-config');

const config = new CacheRedisConfig({
  host: 'localhost',
  port: 6379,
  db: 0
});

config.connect();
```

## API

### CacheRedisConfig(options)

Creates a new instance of the CacheRedisConfig class.

#### Options

* `host` - The Redis host to connect to.
* `port` - The Redis port to connect to.
* `db` - The Redis database to use.

### connect()

Establishes a connection to the Redis server.

### disconnect()

Closes the connection to the Redis server.

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for details.

## License

This project is licensed under the MIT License.