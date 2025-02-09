def migrate(data) -> tuple[dict, bool]:
    if not data == {}:
        if next(iter(data.items()))[1]["value"].get("z_order") is None:
            for key, value in data.items():
                value["value"]["z_order"] = 0

            changed = True

        else:
            changed = False

    else:
        changed = False
    
    return data, changed