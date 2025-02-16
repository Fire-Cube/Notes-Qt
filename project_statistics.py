from pathlib import Path

jinja2_templates = [
    "jinja2_templates/entries.py.j2",
    "jinja2_templates/settings.py.j2"
]

jinja2_generated = [
    "storage_generated/entries.py",
    "storage_generated/settings.py"
]

ui_generated = [
    "ui_generated/MainWindow.py",
    "ui_generated/AskTagDialog.py",
    "ui_generated/SettingsDialog.py"
]

ui_resources_generated = [
    "ui_generated/main_window_resources.py",
    "ui_generated/settings_dialog_resources.py"
]

python = [
    "storage/migrations/__init__.py",
    "storage/migrations/paint_add_z_order.py",
    "storage/helpers.py",
    "storage/images.py",
    "storage/paint.py",
    "storage/painting_nodes.py",
    "storage/paths.py",
    "storage/templates.py",
    "core/context_managers.py",
    "core/event_filters.py",
    "core/random_id.py",
    "core/shared_functions.py",
    "core/special_logging.py",
    "ui/custom_objects.py",
    "ui/custom_widgets.py",
    "ui/dialogs.py",
    "ui/main_window.py",
    "constants.py",
    "main.py"
]

tools = [
    "../render_jinja_templates.py",
    "../project_statistics.py",
    "../make_darker.py"
]

def title(title):
    print(f"{title}\n{'-' * len(title)}")


def count_file_code_lines(path):
    lines_counter = 0
    with open(Path("src", path), encoding="utf-8") as input_file:
        for line in input_file.read().splitlines():
            if len(line.replace(" ", "")) > 0:
                lines_counter += 1

    return lines_counter


def count_category_lines(category, paths):
    lines_counter = 0
    title(category)
    for path in paths:
        lines_number = count_file_code_lines(path)
        lines_counter += lines_number
        print(f"- {path}: {lines_number}")

    print(f"sum: {lines_counter}\n")

    return lines_counter


def count_images():
    title("used images")
    print(len([path for path in Path("src/designer/resources").glob("*.png") if path.is_file()]), "\n")


def print_requirements():
    title("requirements")
    with open("requirements.txt", encoding="utf-8") as input_file:
        for module in input_file.read().split("\n"):
            print(f"- {module}")


count_category_lines("jinja2 templates", jinja2_templates)
count_category_lines("jinja2 generated", jinja2_generated)
count_category_lines("UI generated", ui_generated)
count_category_lines("UI resources generated", ui_resources_generated)
count_category_lines("python", python)

count_category_lines("tools", tools)

count_images()

print_requirements()