import orjson

import storage.painting_nodes as painting_nodes

from pathlib import Path

from storage.painting_nodes import node_from_data
from storage.templates import PAINT_TEMPLATE
from storage.images import Registry

def get_paint_path(iid: str) -> None:
    return Path(f"./data/paint/paint_{iid}.json")


def _parse_paint_data(data: dict) -> dict:
    return {
        key: node_from_data(
            getattr(painting_nodes, value["type"]), value["value"]
        )
        for key, value in data.items()
    }


def load_paint(iid: str) -> dict:
    with open(get_paint_path(iid), encoding="utf-8") as data_file:
        data = orjson.loads(data_file.read())

    return _parse_paint_data(data)


def load_paint_raw(data) -> dict:
    return _parse_paint_data(data)


def save_paint(iid: str, paint: dict) -> None:
    with open(Path(get_paint_path(iid)), "wb") as data_file:
        new = {
            str(key): {"value": value, "type": type(value).__name__}
            for key, value in paint.items()
        }
        data_file.write(orjson.dumps(new))


def create_new_paint(iid: str) -> None:
    with open(Path(get_paint_path(iid)), "wb") as data_file:
        data_file.write(orjson.dumps(PAINT_TEMPLATE))


def delete_paint(iid: str) -> None:
    Registry().unregister_all_from_iid(iid, load_paint(iid))
    Path(get_paint_path(iid)).unlink()