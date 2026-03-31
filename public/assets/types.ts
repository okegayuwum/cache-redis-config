// types.ts

import { RedisConfig } from './redis-config';

/**
 * CacheConfig interface
 */
export interface CacheConfig {
  host: string;
  port: number;
  db: number;
  password?: string;
}

/**
 * RedisConfig interface
 */
export interface RedisConfig {
  host: string;
  port: number;
  db: number;
  password?: string;
}

/**
 * RedisOptions interface
 */
export interface RedisOptions {
  host: string;
  port: number;
  db: number;
  password?: string;
  prefix?: string;
  logger?: { [key: string]: any };
}

/**
 * RedisConfigFactory interface
 */
export interface RedisConfigFactory {
  createRedisConfig(): RedisConfig;
}

// Types
type RedisConfigFactoryFunction = () => RedisConfig;
type RedisConfigFactoryObject = { createRedisConfig: RedisConfigFactoryFunction };