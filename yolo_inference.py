from ultralytics import YOLO

model = YOLO('yolov8m')
result = model.predict('input_vedeos/game.png', save=True)

print(result)
print("boxes:")
for box in result[0].boxes:
    print(box)