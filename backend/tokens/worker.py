import json
from json import JSONEncoder
from backend.enums import FactionEncoder


class Worker:
    def __repr__(self):
        return f"{self.faction} worker"

    def __init__(self, faction):
        self.faction = faction


class WorkerEncoder(JSONEncoder):
    def default(self, worker):
        if not isinstance(worker, Worker):
            return super().default(worker)
        return {"f": json.dumps(worker.faction, cls=FactionEncoder)}
