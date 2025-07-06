from PIL import Image, ImageDraw, ImageFont

def draw_bboxes_with_labels_pil(
        image_path,
        predictions,  # List các dict/object: {'bbox': (x_min, y_min, x_max, y_max), 'label': 'string'}
        save_path,
        font_path,
        font_size=18,
        box_color=(0, 255, 0),
        text_color=(255, 0, 0),
        outline=True
):
    """
    Vẽ bbox và nhãn lên ảnh sử dụng Pillow.

    - image_path: Đường dẫn ảnh gốc.
    - predictions: List dict/object với keys: 'bbox' (tuple), 'label' (str)
    - save_path: Đường dẫn lưu ảnh kết quả.
    - font_path: Đường dẫn tới file .ttf font.
    - font_size: Cỡ chữ.
    - box_color: Màu bbox.
    - text_color: Màu chữ.
    - outline: Có viền chữ không (True: có, False: không).
    """
    img = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)

    for pred in predictions:
        x_min, y_min, x_max, y_max = map(int, pred['bbox'])
        label = str(pred['label'])

        # Vẽ bbox
        draw.rectangle([x_min, y_min, x_max, y_max], outline=box_color, width=2)

        # Tính kích thước text và vị trí
        bbox = font.getbbox(label)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        text_x = x_max + 4  # Thêm 4px padding sang phải cho đẹp
        text_y = y_min

        # Vẽ nền cho chữ (cho dễ nhìn)
        # draw.rectangle([text_x, text_y, text_x + text_width, text_y + text_height], fill=(255, 255, 255))

        # Viền chữ (optional)
        if outline:
            # Viền đen 1px quanh text
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx != 0 or dy != 0:
                        draw.text((text_x + dx, text_y + dy), label, font=font, fill=(0, 0, 0))
        # Vẽ chữ
        draw.text((text_x, text_y), label, font=font, fill=text_color)

    img.save(save_path)
