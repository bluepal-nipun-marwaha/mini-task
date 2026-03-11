import uuid
import datetime


def generate_task_id():
    return str(uuid.uuid4())


def get_timestamp():
    return datetime.datetime.utcnow().isoformat()
