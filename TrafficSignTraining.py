#from roboflow import Roboflow
import shutil

#Tải Dataset
# rf = Roboflow(api_key="3hkuTgRp6MLCk0Hnglqw")
# project = rf.workspace("phuclamle-p6er2").project("vietnam-traffic-sign-detection-2i2j8-5j5xt")
# version = project.version(1)
# dataset = version.download("yolov5")

# Đổi lại vị trí dường dẫn(phù hợp với file data.yaml)
shutil.move("trafficSignDataSet/train",
"trafficSignDataSet/trafficSignDataSet/train",
)
shutil.move("trafficSignDataSet/test",
"trafficSignDataSet/trafficSignDataSet/test",
)
shutil.move("trafficSignDataSet/valid",
"trafficSignDataSet/trafficSignDataSet/valid",
)

#câu lệnh training: yolo task=detect mode=train model=models/yolov8m.pt data=trafficSignDataSet/data.yaml epochs=25 imgsz=640


