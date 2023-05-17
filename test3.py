import cv2

# 이미지 파일 경로
image_path = "./image.jpg"

# 이미지 파일 불러오기
image = cv2.imread(image_path)

# 이미지의 너비와 높이 구하기
height, width, _ = image.shape

# 이미지의 픽셀 값을 배열로 받기
pixels = image.reshape((height * width, 3))

# 픽셀 값 출력
for pixel in pixels:
    print(pixel)