from pathlib import Path
from jinja2 import Template

def get_dict_path(path):
    command = "['"
    for key in path.split("."):
        command += f"{key}']['"

    return command[:-2]


def get_function_type_hint(types):
    type_hint = ""
    if len(types) > 1:
        for type in types:
            type_hint += f"{'None' if type == 'NoneType' else type} | "

        type_hint = type_hint[:-3]

    else:
        type_hint = types[0]

    return type_hint


def get_isinstance_type_check_arg(types):
    if len(types) > 1:
        arg = "("
        for type in types:
            arg += f"{type},"

        arg = arg[:-1]
        arg += ")"

    else:
        arg = types[0]

    return arg


entries_specification = [
    ["parent", ["str"], "parent"],
    ["id", ["str"], "id"],
    ["is_open", ["bool"], "is_open"],
    ["text", ["str"], "text"],

    ["activated_paint_mode", ["str"], "paint_tab.activated_mode"],
    ["eraser_size", ["int"], "paint_tab.eraser.size"],
    ["line_size", ["int"], "paint_tab.line.line_size"],
    ["line_color", ["str"], "paint_tab.line.line_color"],
    ["shape_fill_color", ["str"], "paint_tab.shape.fill_color"],
    ["shape_outline_color", ["str"], "paint_tab.shape.outline_color"],
    ["shape_outline_size", ["int"], "paint_tab.shape.outline_size"],

    ["position", ["int"], "position"],
    ["creation_time", ["str"], "times.creation_time"],
    ["modification_time", ["str"], "times.modification_time"],
    ["tags", ["list"], "tags"],
    ["name_text", ["str"], "name.text"],
    ["name_color", ["str"], "name.color"],
]

settings_specification = [
    # main settings
    ["background_image", ["int"], "background_image"],
    ["background_color", ["str"], "background_color"],
    ["background_acryl", ["bool"], "background_acryl"],
    ["background_mode", ["str"], "background_mode"],
    ["language", ["str"], "language"],
    ["active_entry", ["str", "NoneType"], "active_entry"],
    ["active_tab", ["int"], "active_tab"],
    ["vertical_scrollbar_value", ["int"], "vertical_scrollbar_value"],
    ["horizontal_scrollbar_value", ["int"], "horizontal_scrollbar_value"],
    ["search_category", ["str"], "search_tab.category"],
    ["color_chooser_custom_colors", ["list"], "color_chooser_custom_colors"],
]

def main():
    paths = list(Path("./src/jinja2_templates").glob("*.j2"))
    if not paths:
        print("Can't find templates.")

    for path in paths:
        with open(path, encoding="utf-8") as template_file:
            template = Template(template_file.read())

        if path.name == "entries.py.j2":
            generated_code = template.render(
                entries_specification=entries_specification,
                get_dict_path=get_dict_path,
                get_function_type_hint=get_function_type_hint,
                get_isinstance_type_check_arg=get_isinstance_type_check_arg
            )

        if path.name == "settings.py.j2":
            generated_code = template.render(
                specification=settings_specification,
                get_dict_path=get_dict_path,
                get_function_type_hint=get_function_type_hint,
                get_isinstance_type_check_arg=get_isinstance_type_check_arg
            )

        with open(Path("./src/storage_generated/", "".join(path.name[:-3])), "w", encoding="utf-8") as code_file:
            code_file.write(generated_code)

if __name__ == "__main__":
    main()