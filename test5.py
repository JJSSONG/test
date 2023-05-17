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

# 정규화 규칙 설정
threshold = 125  # 임계값 설정

for i in range(height):
    for j in range(width):
        r, _, _ = image[i, j]
        
        # 정규화 규칙 적용
        if r < threshold:
            note = "도"
        else:
            note = "레"
        
        # 주파수 계산
        frequency = ord(note)  # ASCII 값으로 주파수 매핑
        
        sound_data += np.sin(2 * np.pi * frequency * t)

        # print('i : ' + str(i) + ' j : '+str(j)+' frequency : '+str(frequency))
        print('i : ' + str(i) + ' j : '+str(j)+' sound_data : '+str(sound_data))


# 소리 재생
sd.play(sound_data, sample_rate)
sd.wait()