from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime, timedelta


@dataclass
class Task:
    """Represents a single pet care activity."""
    description: str
    time: str               # "HH:MM"
    duration_minutes: int
    frequency: str          # "once", "daily", "weekly"
    priority: str           # "low", "medium", "high"
    pet_name: str = ""
    is_complete: bool = False

    def mark_complete(self):
        """Mark this task as done."""
        self.is_complete = True


@dataclass
class Pet:
    """Represents a pet with a list of care tasks."""
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet and tag it with the pet's name."""
        task.pet_name = self.name
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        return self.tasks


class Owner:
    """Manages multiple pets and their tasks."""

    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        """Add a pet to this owner's list."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        """Return every task across all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    """Organizes and manages tasks across all pets for an owner."""

    def __init__(self, owner: Owner):
        self.owner = owner

    def sort_by_time(self) -> List[Task]:
        """Return all tasks sorted chronologically by time."""
        return sorted(self.owner.get_all_tasks(), key=lambda t: t.time)

    def filter_tasks(self, pet_name: Optional[str] = None, status: Optional[bool] = None) -> List[Task]:
        """Filter tasks by pet name and/or completion status."""
        tasks = self.owner.get_all_tasks()
        if pet_name:
            tasks = [t for t in tasks if t.pet_name == pet_name]
        if status is not None:
            tasks = [t for t in tasks if t.is_complete == status]
        return tasks

    def detect_conflicts(self) -> List[str]:
        """Return warnings for any two tasks scheduled at the same time."""
        tasks = self.owner.get_all_tasks()
        seen = {}
        warnings = []
        for task in tasks:
            if task.time in seen:
                warnings.append(
                    f"Conflict at {task.time}: '{seen[task.time]}' and '{task.description}'"
                )
            else:
                seen[task.time] = task.description
        return warnings

    def mark_task_complete(self, task: Task):
        """Mark a task complete and auto-schedule the next occurrence if it recurs."""
        task.mark_complete()
        if task.frequency in ("daily", "weekly"):
            self.handle_recurring(task)

    def handle_recurring(self, task: Task):
        """Create the next occurrence of a recurring task after it's completed."""
        if task.frequency == "daily":
            next_date = datetime.now() + timedelta(days=1)
        elif task.frequency == "weekly":
            next_date = datetime.now() + timedelta(weeks=1)
        else:
            return None

        new_task = Task(
            description=task.description,
            time=task.time,
            duration_minutes=task.duration_minutes,
            frequency=task.frequency,
            priority=task.priority,
            pet_name=task.pet_name,
        )
        for pet in self.owner.pets:
            if pet.name == task.pet_name:
                pet.add_task(new_task)
                break
        return new_task
