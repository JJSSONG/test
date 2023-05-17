import cv2
import numpy as np
import sounddevice as sd

# 이미지 파일 경로
image_path = "./image.jpg"

# 이미지 파일 불러오기
image = cv2.imread(image_path)

# 이미지 크기 설정
height, width, _ = image.shape

# 샘플링 주파수와 재생 시간 설정
sample_rate = 44100  # 예시로 44100Hz 사용
duration = 1.0  # 예시로 1초 사용

# 소리 데이터 생성
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
sound_data = np.zeros_like(t)

# 2옥타브 도~시 계이름과 주파수 매핑
octave_notes = {
    "도": 261.63,
    "도#": 277.18,
    "레": 293.66,
    "레#": 311.13,
    "미": 329.63,
    "파": 349.23,
    "파#": 369.99,
    "솔": 392.00,
    "솔#": 415.30,
    "라": 440.00,
    "라#": 466.16,
    "시": 493.88,
    "도+": 523.25,
    "도#+": 554.37
}

for i in range(height):
    for j in range(width):
        r, _, _ = image[i, j]

        # 정규화 규칙 적용
        normalized_r = r / 255.0
        note_index = int(normalized_r * len(octave_notes))
        note = list(octave_notes.keys())[note_index]

        # 주파수 계산
        frequency = octave_notes[note]

        sound_data += np.sin(2 * np.pi * frequency * t)

# 소리 재생
sd.play(sound_data, sample_rate)
sd.wait()