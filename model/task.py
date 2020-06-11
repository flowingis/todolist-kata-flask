import uuid
from dataclasses import dataclass

from command.task_add_command import TaskAddCommand


@dataclass
class Task:
    uuid: str
    description: str
    done: int
    tags: []

    @classmethod
    def create(cls, description: str, tags=None):
        if tags is None:
            tags = []
        return cls(
            uuid=str(uuid.uuid4()),
            description=description,
            done=0,
            tags=tags
        )

    @classmethod
    def from_command(cls, command: TaskAddCommand):
        return cls(
            uuid=str(uuid.uuid4()),
            description=command.description,
            done=0,
            tags=command.tags
        )
