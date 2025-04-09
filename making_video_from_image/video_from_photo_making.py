import cv2
import os
import time
from tqdm import tqdm

start_time = time.time()
input_folder = 'D:/Projects/dataset_hight_calibration/calibrated_dataset_tt/images'
fps = 15
output_folder = 'OUT_VIDEO'
current_time = time.strftime("%Y-%m-%d_%H-%M")
os.makedirs(output_folder, exist_ok=True)

output_video = os.path.join(output_folder, f'output_video_{fps}_fps_{current_time}.mp4')
#output_video = os.path.join(output_folder, f'output_video_{fps}_fps.mp4')
images = [img for img in os.listdir(input_folder) if img.lower().endswith(".png")]
images.sort()

if not images:
    print("В папке нет PNG-файлов")
    exit()
print(f"Найдено файлов: {len(images)}")

first_image_path = os.path.join(input_folder, images[0])
frame = cv2.imread(first_image_path)
if frame is None:
    print(f"Ошибка: не удалось загрузить изображение {first_image_path}")
    exit()

height, width, layers = frame.shape
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))
for image in tqdm(images, desc="Создание видео"):
    image_path = os.path.join(input_folder, image)
    frame = cv2.imread(image_path)
    if frame is None:
        print(f"Ошибка: не удалось загрузить изображение {image_path}")
        continue
    video.write(frame)

video.release()
print(f"Видео сохранено как {output_video}/nВремя на обработку: {(time.time()- start_time)} sec")