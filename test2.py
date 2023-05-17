import cv2
import numpy as np
import winsound

# 이미지 파일 경로
image_path = "./image.jpg"

# 이미지 파일 불러오기
image = cv2.imread(image_path)

# 이미지를 그레이스케일로 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이미지 크기 설정
height, width = gray_image.shape

# 소리 데이터로 변환
sound_data = gray_image.flatten() / 255.0 * 2 - 1  # 이미지 값을 [-1, 1] 범위로 정규화

# WAV 파일로 저장
wav_file = "output.wav"
scaled_sound_data = np.int16(sound_data * 32767)  # 데이터 스케일링 (-32768 ~ 32767 사이의 값으로 변환)
winsound.write(wav_file, 44100, scaled_sound_data)

# WAV 파일 재생
winsound.PlaySound(wav_file, winsound.SND_FILENAME)