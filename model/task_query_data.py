from dataclasses import dataclass

from command.task_search_command import TaskSearchCommand


@dataclass
class TaskQueryData:
    description: str
    tags: []

    @classmethod
    def from_command(cls, command: TaskSearchCommand):
        return cls(
            description=command.description,
            tags=command.tags
        )
