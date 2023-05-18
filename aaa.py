import cv2
import numpy as np
from music21 import stream, note, duration

def rgb_to_hsi(rgb):
    r, g, b = rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0
    hsi = np.zeros(3)

    num = 0.5 * ((r - g) + (r - b))
    den = np.sqrt((r - g) ** 2 + (r - b) * (g - b))

    theta = np.arccos(num / (den + 1e-5))
    h = theta if b <= g else 2 * np.pi - theta

    min_rgb = min(r, g, b)
    s = 1 - 3 * min_rgb / (r + g + b + 1e-5)

    i = (r + g + b) / 3

    hsi[0] = h
    hsi[1] = s
    hsi[2] = i

    return hsi

def generate_note_from_hsi(hue, saturation, intensity):
    # 정규화 룰 설정
    note_mapping = {
        (0.0, 0.0, 0.0): "C4",
        (0.2, 0.5, 0.5): "D4",
        (0.4, 1.0, 0.7): "E4",
        (0.6, 0.8, 0.8): "F4",
        (0.8, 0.3, 0.6): "G4",
        (1.0, 0.6, 0.4): "A4",
    }

    key = (hue, saturation, intensity)
    if key in note_mapping:
        return note_mapping[key]
    else:
        return "C4"

def generate_melody_from_image(image_path):
    # 이미지 로드
    img = cv2.imread(image_path)
    img_hsi = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # 이미지 크기 조정
    img_hsi = cv2.resize(img_hsi, (100, 100))

    # HSI 값을 추출하여 음표 생성
    melody_stream = stream.Stream()
    for row in img_hsi:
        for pixel in row:
            h, s, i = pixel
            code = generate_note_from_hsi(h, s, i)
            
            n = note.Note()
            n.pitch.nameWithOctave = code
            n.duration.quarterLength = 0.5  # 음표의 길이 설정
            
            melody_stream.append(n)

    return melody_stream

# 이미지 경로 설정
image_path = "./image.jpg"

# 이미지에서 멜로디 생성
melody = generate_melody_from_image(image_path)

# MIDI 파일로 저장
output_file = "melody_from_image.mid"
melody.write("midi", fp=output_file)
print(f"MIDI 파일이 저장되었습니다: {output_file}")
