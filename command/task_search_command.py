from dataclasses import dataclass

from flask import json


@dataclass
class TaskSearchCommand:
    description: str
    tags: []

    @classmethod
    def from_request(cls, request_data):
        return cls(
            description=request_data['description'],
            tags=request_data['tags'].split(' ') if request_data['tags'] else []
        )
