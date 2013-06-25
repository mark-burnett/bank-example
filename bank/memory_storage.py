import uuid


class MemoryStorage(object):
    def __init__(self, objects):
        self.objects = objects

    def save_object(self, obj):
        key = uuid.uuid4().hex
        self.objects[key] = obj
        return key

    def load_object(self, key):
        return self.objects[key]
