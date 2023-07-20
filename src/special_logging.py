LOG_ENTRY_CHANGES = 0
LOG_HIERARCHICAL_VIEW_UPDATES = 1
LOG_CHOOSEN_COLOR = 2
LOG_PROFILING = 3

DISABLED_CATEGORYS = ()

def log(message, category):
    if category not in DISABLED_CATEGORYS:
        print(f"INFO: {message}")