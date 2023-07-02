from dataclasses import dataclass
from dataclasses import fields as get_fields

@dataclass
class LineNode:
    coordinates: list[tuple[float, float]]
    size: float
    color: str
    is_eraser: bool


@dataclass
class RectangleNode:
    coordinates: list[tuple[float, float]]
    outline_size: float
    outline_color: str
    fill_color: str


@dataclass
class EllipseNode:
    coordinates: list[tuple[float, float]]
    outline_size: float
    outline_color: str
    fill_color: str


@dataclass
class PolygonNode:
    coordinates: list[tuple[float, float]]
    outline_size: float
    outline_color: str
    fill_color: str


@dataclass
class ImageNode:
    coordinate: tuple[float, float]
    size: tuple[float, float]
    hash: str


def node_from_data(node: LineNode | RectangleNode | EllipseNode | PolygonNode | ImageNode, data: dict) -> LineNode | RectangleNode | EllipseNode | PolygonNode | ImageNode:
    fields = {f.name for f in get_fields(node) if f.init}
    filtered_args = {k : v for k, v in data.items() if k in fields}
    return node(**filtered_args)