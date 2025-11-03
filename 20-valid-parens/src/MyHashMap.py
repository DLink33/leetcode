class MyHashMap:
    """
    Separate chaining hash map (int keys/values).
    Collision handling: per-bucket list of (key, value).
    """

    def __init__(self, bucket_count: int = 1024):
        self._n = 0  # number of pairs
        self._m = bucket_count  # number of buckets
        self._buckets: list[list[tuple[int, int]]] = [[] for _ in range(self._m)]
        self._load_factor = 0

    def _hash(self, key: int) -> int:
        """Map key -> bucket index in [0, self._m)."""
        return (key & 0x7FFFFFFF) % self._m

    def put(self, key: int, value: int) -> None:
        """
        Insert or update (key -> value)
        """
        idx: int = self._hash(key)
        bucket: list[tuple[int, int]] = self._buckets[idx]

        for i, (k, _) in enumerate(bucket):
            if key == k:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._n += 1

    def get(self, key: int):
        """
        Return value if found; else -1
        """
        idx: int = self._hash(key)
        bucket: list[tuple[int, int]] = self._buckets[idx]
        for k, v in bucket:
            if key == k:
                return v
        return -1

    def remove(self, key: int) -> None:
        """
        Remove key if present.
        Hint: you can delete by index; order in a bucket doesn't matter.
        """
        idx: int = self._hash(key)
        bucket: list[tuple[int, int]] = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]

    # Optional stretch:
    # def _maybe_resize(self):
    #     """If load factor > 0.75, rehash into 2x buckets."""
    #     # TODO
    #     pass
