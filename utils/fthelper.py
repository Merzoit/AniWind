from PIL import Image, ImageDraw
from io import BytesIO

def create_empty_field():
    img = Image.new('RGB', (800, 600), color='green')
    draw = ImageDraw.Draw(img)
    for row in range(2):
        for col in range(3):
            left = 10 + col * 260
            top = 10 + row * 290
            right = left + 250
            bottom = top + 280
            draw.rectangle([left, top, right, bottom], outline="black")

    # Вместо сохранения изображения в файл, сохраняем в BytesIO
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr

def add_card_to_field(field_image_bytes, card_image_path, position):
    field_image = Image.open(field_image_bytes)
    card_image = Image.open(card_image_path).resize((250, 280))
    field_image.paste(card_image, position)

    # Возвращаем измененное поле как BytesIO
    img_byte_arr = BytesIO()
    field_image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr
