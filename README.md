# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Testing PawPal+

Run the test suite with:

```bash
python -m pytest
```

The tests cover:
- **Task completion** — `mark_complete()` correctly flips the task status
- **Task addition** — adding a task to a pet increases its task count
- **Sorting correctness** — tasks are returned in chronological order regardless of the order they were added
- **Recurrence logic** — marking a daily task complete automatically creates a new task for the next occurrence
- **Conflict detection** — the Scheduler correctly flags two tasks scheduled at the same time

**Confidence Level: ⭐⭐⭐⭐ (4/5)** — all core behaviors are tested and passing. The main gap is duration-overlap conflicts (e.g., a 30-min task at 10:00 overlapping a task at 10:15), which aren't covered yet.

---

## Smarter Scheduling

PawPal+ includes algorithmic logic to make scheduling more intelligent:

- **Sorting by time** — tasks are automatically ordered chronologically using a lambda on the `HH:MM` time field
- **Filtering** — tasks can be filtered by pet name or completion status
- **Conflict detection** — the Scheduler flags any two tasks scheduled at the exact same time with a warning message
- **Recurring tasks** — when a daily or weekly task is marked complete, the Scheduler automatically creates the next occurrence using Python's `timedelta`

---

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.
