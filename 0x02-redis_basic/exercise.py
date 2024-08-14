#!/usr/bin/env python3
"""0. Writing strings to Redis """
import typing
import redis
import uuid


class Cache:
    """
        basic functionalities for storing and retrieving strings in a Redis instance.
    """
    def __init__(self):
        """
            Initializes a new Cache instance.
            Connects to the default Redis instance and clears the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """Stores a string in Redis and returns a unique ID.

            Args:
                data: The string to store.

            Returns:
                A UUID string representing the key for the stored data.
        """

        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id
