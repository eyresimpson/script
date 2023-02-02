import redis
#
r = redis.StrictRedis(host="localhost", port=6379, db=0)
r.set("keys", "Values")
print(r.keys("*"))
print(r.get("keys"))
