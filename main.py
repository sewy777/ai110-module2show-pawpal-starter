from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Jordan")

mochi = Pet("Mochi", "dog", 3)
luna = Pet("Luna", "cat", 2)

# Tasks added out of order to demonstrate sorting
mochi.add_task(Task("Evening Walk", "18:00", 30, "daily", "high"))
mochi.add_task(Task("Feeding", "07:30", 10, "daily", "high"))
mochi.add_task(Task("Morning Walk", "08:00", 30, "daily", "high"))
luna.add_task(Task("Playtime", "10:00", 20, "daily", "medium"))
luna.add_task(Task("Evening Meds", "19:00", 5, "daily", "high"))
# Conflict: two tasks at the same time
luna.add_task(Task("Grooming", "10:00", 15, "once", "low"))

owner.add_pet(mochi)
owner.add_pet(luna)

scheduler = Scheduler(owner)

# Sorted schedule
print("=== Today's Schedule (sorted) ===")
for task in scheduler.sort_by_time():
    status = "done" if task.is_complete else "todo"
    print(f"[{status}] {task.time} | {task.pet_name:<6} | {task.description} ({task.duration_minutes} min) [{task.priority}]")

# Filtering by pet
print("\n=== Mochi's Tasks Only ===")
for task in scheduler.filter_tasks(pet_name="Mochi"):
    print(f"  {task.time} | {task.description}")

# Filtering by status
print("\n=== Incomplete Tasks ===")
for task in scheduler.filter_tasks(status=False):
    print(f"  {task.time} | {task.pet_name} | {task.description}")

# Conflict detection
print("\n=== Conflict Check ===")
conflicts = scheduler.detect_conflicts()
if conflicts:
    for warning in conflicts:
        print(f"WARNING: {warning}")
else:
    print("No conflicts found.")

# Recurring task demo
print("\n=== Recurring Task Demo ===")
feeding = mochi.get_tasks()[1]  # Feeding task
print(f"Before: {feeding.description} | complete={feeding.is_complete} | total Mochi tasks={len(mochi.get_tasks())}")
scheduler.mark_task_complete(feeding)
print(f"After:  {feeding.description} | complete={feeding.is_complete} | total Mochi tasks={len(mochi.get_tasks())}")
