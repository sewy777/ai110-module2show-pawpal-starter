from pawpal_system import Task, Pet


def test_mark_complete():
    task = Task("Morning Walk", "08:00", 30, "daily", "high")
    assert task.is_complete == False
    task.mark_complete()
    assert task.is_complete == True


def test_add_task_increases_count():
    pet = Pet("Mochi", "dog", 3)
    assert len(pet.get_tasks()) == 0
    pet.add_task(Task("Morning Walk", "08:00", 30, "daily", "high"))
    assert len(pet.get_tasks()) == 1
