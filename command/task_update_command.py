from dataclasses import dataclass

from flask import json


@dataclass
class TaskUpdateCommand:
    description: str

    @classmethod
    def from_json_str(cls, json_str):
        parsed_data = json.loads(json_str)
        return cls(description=parsed_data['description'])
