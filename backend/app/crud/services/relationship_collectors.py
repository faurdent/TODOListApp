def collect_tasks(weekdays: list):
    tasks = []
    for weekday in weekdays:
        tasks.extend(weekday.tasks)

    return tasks
