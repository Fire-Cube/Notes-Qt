from PIL import Image, ImageEnhance
from pathlib import Path

# for path in Path("src/designer/resources").glob("*.png"):
#     if str(path.name)[0].islower():
#         print(str(path.name)[0])
#         img = Image.open(path)
#         enhancer = ImageEnhance.Brightness(img)
#         img = enhancer.enhance(0.95)
#         img.save(f"{str(path).split('.')[0]}Hover.png")

path = Path("src/designer/resources/url.png")
img = Image.open(path)
enhancer = ImageEnhance.Brightness(img)
img = enhancer.enhance(0.95)
img.save(f"{str(path).split('.')[0]}Hover.png")