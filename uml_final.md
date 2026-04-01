# PawPal+ Final UML Diagram

Updated to reflect final implementation. `mark_task_complete()` was added to Scheduler during Phase 4 to connect task completion with recurring task logic.

```mermaid
classDiagram
    class Task {
        +str description
        +str time
        +int duration_minutes
        +str frequency
        +str priority
        +str pet_name
        +bool is_complete
        +mark_complete()
    }

    class Pet {
        +str name
        +str species
        +int age
        +List tasks
        +add_task(task)
        +get_tasks()
    }

    class Owner {
        +str name
        +List pets
        +add_pet(pet)
        +get_all_tasks()
    }

    class Scheduler {
        +Owner owner
        +sort_by_time()
        +filter_tasks(pet_name, status)
        +detect_conflicts()
        +mark_task_complete(task)
        +handle_recurring(task)
    }

    Pet "1" --> "many" Task : has
    Owner "1" --> "many" Pet : owns
    Scheduler "1" --> "1" Owner : manages
```

> To export as PNG, paste the Mermaid code above into https://mermaid.live and use the Export button.
