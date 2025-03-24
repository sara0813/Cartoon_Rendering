import cv2
import numpy as np

# 이미지 읽기
img = cv2.imread('test1.jpg')  # 파일 경로를 실제 이미지 파일로 변경하세요

# 이미지를 그레이스케일로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 그레이스케일 이미지를 블러링
gray_blurred = cv2.medianBlur(gray, 5)

# 엣지 검출
edges = cv2.adaptiveThreshold(gray_blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# 색상 필터링
color = cv2.bilateralFilter(img, 9, 300, 300)

# 엣지와 색상을 결합하여 만화 스타일 이미지 생성
cartoon = cv2.bitwise_and(color, color, mask=edges)

# 원본 이미지와 카툰화 이미지 합치기
merged_image = cv2.hconcat([img, cartoon])

# 결과 이미지 보기
cv2.imshow("Original and Cartoonified Images", merged_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 결과 이미지 저장
cv2.imwrite('merge_test1.jpg', merged_image)
