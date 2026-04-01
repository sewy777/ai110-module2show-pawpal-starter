from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Jordan")

mochi = Pet("Mochi", "dog", 3)
luna = Pet("Luna", "cat", 2)

mochi.add_task(Task("Feeding", "07:30", 10, "daily", "high"))
mochi.add_task(Task("Morning Walk", "08:00", 30, "daily", "high"))
luna.add_task(Task("Playtime", "10:00", 20, "daily", "medium"))
luna.add_task(Task("Evening Meds", "19:00", 5, "daily", "high"))

owner.add_pet(mochi)
owner.add_pet(luna)

scheduler = Scheduler(owner)
schedule = scheduler.sort_by_time()

print("=== Today's Schedule ===")
for task in schedule:
    status = "done" if task.is_complete else "todo"
    print(f"[{status}] {task.time} | {task.pet_name:<6} | {task.description} ({task.duration_minutes} min) [{task.priority}]")
