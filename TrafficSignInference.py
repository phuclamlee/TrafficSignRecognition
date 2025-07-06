from sahi import AutoDetectionModel
import pandas as pd
from sahi.predict import  get_sliced_prediction
from constants import FONT_PATH, IMAGE_URL, MODEL_PATH, SAVE_PATH
from utils import draw_bboxes_with_labels_pil

#yolo v8 + sahi
detection_model = AutoDetectionModel.from_pretrained(
    model_type = 'yolov8',
    model_path = MODEL_PATH,
    confidence_threshold = 0.5,
    device = 'cuda:0'
)
# kết quả
result = get_sliced_prediction(
    IMAGE_URL,
    detection_model = detection_model,
    slice_height = 256,
    slice_width = 256,
    overlap_height_ratio = 0.2,
    overlap_width_ratio = 0.2,
)

#Đọc file TrafficSignCodeAndName
df = pd.read_excel("TrafficSignCodeAndName.xlsx")
#chuyển đổi thành dictionary: {code: name}
TRAFFIC_SIGN_MAP = dict(zip(df['Code'], df['Name']))

# vẽ kết quả lên màn hình
predictions = []
for idx, object_prediction in enumerate(result.object_prediction_list):
    code = object_prediction.category.name
    real_name = TRAFFIC_SIGN_MAP.get(code, code)
    score = object_prediction.score.value
    bbox = object_prediction.bbox.to_xyxy()
    predictions.append({
        'bbox': bbox,
        'label': real_name
    })
draw_bboxes_with_labels_pil(
    image_path=IMAGE_URL,
    predictions=predictions,
    save_path= SAVE_PATH,
    font_path=FONT_PATH,
    font_size=30
)



