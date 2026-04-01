from pawpal_system import Task, Pet, Owner, Scheduler


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


def test_sort_by_time():
    owner = Owner("Jordan")
    pet = Pet("Mochi", "dog", 3)
    pet.add_task(Task("Evening Walk", "18:00", 30, "daily", "high"))
    pet.add_task(Task("Feeding", "07:30", 10, "daily", "high"))
    pet.add_task(Task("Playtime", "12:00", 20, "daily", "medium"))
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()
    times = [t.time for t in sorted_tasks]
    assert times == sorted(times)


def test_recurring_creates_new_task():
    owner = Owner("Jordan")
    pet = Pet("Mochi", "dog", 3)
    pet.add_task(Task("Feeding", "07:30", 10, "daily", "high"))
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    assert len(pet.get_tasks()) == 1
    scheduler.mark_task_complete(pet.get_tasks()[0])
    assert len(pet.get_tasks()) == 2


def test_detect_conflicts():
    owner = Owner("Jordan")
    pet = Pet("Luna", "cat", 2)
    pet.add_task(Task("Playtime", "10:00", 20, "daily", "medium"))
    pet.add_task(Task("Grooming", "10:00", 15, "once", "low"))
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    warnings = scheduler.detect_conflicts()
    assert len(warnings) == 1
    assert "10:00" in warnings[0]
