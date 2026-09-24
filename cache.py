import redis

cache = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

cache.ping()

print("Redis connected!")

def get_cache(key):
    return cache.get(key)

def set_cache(key,value):
    cache.set(key,value, ex=300)
