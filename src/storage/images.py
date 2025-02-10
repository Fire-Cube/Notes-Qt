import hashlib
import orjson
import lzma

from PIL import Image
from pathlib import Path

from storage.painting_nodes import ImageNode
from storage.paths import IMAGES_DIR_PATH, IMAGES_REGISTRY_FILE_PATH

BUFFER_SIZE = 64000

def get_hash_from_image(path: Path) -> str:
    hasher = hashlib.sha512()
    with open(path, "rb") as file:
        buffer = file.read(BUFFER_SIZE)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = file.read(BUFFER_SIZE)

    return hasher.hexdigest()


def get_cache_path(image_hash: str) -> Path:
    return Path(IMAGES_DIR_PATH, image_hash)


def import_image(path: Path) -> str:
    image = Image.open(path)
    image.convert("RGBA")
    with lzma.open(get_cache_path(f"{get_hash_from_image(path)}_image"), "wb") as image_file:
        image_file.write(image.tobytes("raw", "RGBA"))

    with open(get_cache_path(f"{get_hash_from_image(path)}_size"), "wb") as size_file:
        size_file.write(orjson.dumps(image.size))


def remove_image(image_hash: str) -> None:
    get_cache_path(f"{image_hash}_image").unlink()
    get_cache_path(f"{image_hash}_size").unlink()


def get_image(image_hash: str) -> tuple[bytes, tuple[int, int]]:
    with lzma.open(f"{get_cache_path(image_hash)}_image", "rb") as image_file:
        with open(get_cache_path(f"{image_hash}_size"), "rb") as size_file:
            return image_file.read(), orjson.loads(size_file.read())


class Registry:
    def __init__(self) -> None:
        with open(IMAGES_REGISTRY_FILE_PATH, mode="rb") as registry_file:
            self.registry = orjson.loads(registry_file.read())


    def register_image(self, image_hash: str) -> None:
        self.registry[image_hash] = []
        self.save()


    def register_image_usage(self, image_hash: str, iid: str) -> None:
        self.registry[image_hash].append(iid)
        self.save()


    def unregister_image_usage(self, image_hash: str, iid: str) -> None:
        self.registry[image_hash].remove(iid)
        if not self.registry[image_hash]:
            del self.registry[image_hash]
            self.save()

            remove_image(image_hash)


    def unregister_all_from_iid(self, iid: str, paint_data: dict) -> None:
        for node in paint_data.values():
            if isinstance(node, ImageNode):
                self.unregister_image_usage(node.hash, iid)


    def is_image_imported(self, path: Path) -> bool:
        return get_hash_from_image(path) in self.registry


    def save(self) -> None:
        with open(IMAGES_REGISTRY_FILE_PATH, mode="wb") as registry_file:
            registry_file.write(orjson.dumps(self.registry))