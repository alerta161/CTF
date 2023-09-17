from PIL import Image
from PIL.ExifTags import TAGS


image_path = 'airport.jpg'
image = Image.open(image_path)


exif_data = image._getexif()


if exif_data:
    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        print(f"{tag_name}: {value}")
else:
    print("Метаданные не найдены в данном изображении.")
