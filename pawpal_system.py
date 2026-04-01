from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Task:
    description: str
    time: str               # "HH:MM"
    duration_minutes: int
    frequency: str          # "once", "daily", "weekly"
    priority: str           # "low", "medium", "high"
    pet_name: str = ""
    is_complete: bool = False

    def mark_complete(self):
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        pass

    def get_tasks(self) -> List[Task]:
        pass


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        pass

    def get_all_tasks(self) -> List[Task]:
        pass


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def sort_by_time(self) -> List[Task]:
        pass

    def filter_tasks(self, pet_name: Optional[str] = None, status: Optional[bool] = None) -> List[Task]:
        pass

    def detect_conflicts(self) -> List[str]:
        pass

    def handle_recurring(self, task: Task):
        pass
