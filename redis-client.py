from datetime import datetime

import redis

r = redis.Redis(host='localhost', port=6379, db=0, password='mTfVgqgKXxH38uhseDZfeL9r')
# r = redis.Redis(host='10.0.0.50', port=6379, db=0, password='mTfVgqgKXxH38uhseDZfeL9r')


def datetime_from(key: bytes) -> datetime:
    dt = key.decode().split('-')[0]
    return datetime.fromtimestamp(int(dt))


def main():
    # entries = {key: r.get(key) for key in r.keys('*')}
    # [print(datetime_from(key), key, entries.get(key)) for key in sorted(entries.keys())]
    keys = r.keys('*')
    print(keys)
    values = r.mget(keys)
    print(values)
    print(len(values))


if __name__ == '__main__':
    main()
    # r.flushdb()
