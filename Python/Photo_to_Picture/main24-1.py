# 라이브러리 소개
import numpy as np
# numpy : 행렬이나 일반적으로 대규모 다차원 배열을 쉽게 처리할 수 있도록 지원하는 파이썬의 라이브러리이다. 여기서는 이미지 파일을 numpy배열로 불러오기 위해 사용함.
import cv2 
# OpenCV(Open Source Computer Vision)은 실시간 컴퓨터 비전을 목적으로 한 프로그래밍 라이브러리이다.  실시간 이미지 프로세싱에 중점을 둔 라이브러리이다


# 이미지 불러오기
ff=np.fromfile(r'C:\Users\user\Desktop\Study\Python\Photo_to_Picture\cake.jpg', np.uint8 )
# 1. numpy.savetxt(), numpy.loadtxt()   텍스트 파일로 Numpy배열 저장및 로드 .txt
# 2. numpy.tofile(), numpy.fromfile()   이진 파일로 Numpy배열 저장및 로드 .dat(이미지도!)
# 3. numpy.save(), numpy.load()         Numpy배열 파일 저장및 로드 .npy
# python에서 string 앞에 r 을 표기해 주는 것은 해당 string literal을 raw string 으로 만들어 주기 위함이다.  즉 \\이 아닌 \ 쓰기 위함이다.
# numpy의 데이터타입 불리언 boolean, 정수형 int8~64, 양의 정수형 uint8~64, 부동소수형 float16~64,
# 복소수형 complex64~128, 문자형 string_ 
# uint8: 0~255
# 이미지 전처리
# img = cv2.imencode(ext, src[, params])  -> ext: 출력파일 확장자, src:압축할 이미지, params: ImwriteFlags
# img =cv2.cv.imdecode(buf, flags) -> buf:인코딩된 배열, flags:ImreadModes
img =cv2.imdecode(ff, -1)
# cv2.IMREAD_COLOR : 이미지 파일을 Color로 읽어들입니다. 투명한 부분은 무시되며, Default값입니다.   1
# cv2.IMREAD_GRAYSCALE : 이미지를 Grayscale로 읽어 들입니다. 실제 이미지 처리시 중간단계로 많이 사용합니다. 0
# cv2.IMREAD_UNCHANGED : 이미지파일을 alpha channel(RGB값 이외의 데이터)까지 포함하여 읽어 들입니다.  -1


img =cv2.resize(img, dsize=(0,0), fx=0.5,fy=0.5, interpolation=cv2.INTER_AREA)
# cv2.resize(src, dsize, dst=None, fx=None, fy=None, interpolation=None)
# src:입력이미지, desize: 결과 영상크기(w,h) 둘다 0이면 fx(x방향 스케일비율),fy(y방향 스케일비율)로 이용하여 결정 interpolation: 보간법 지정. 기본값은 cv2.INTER_LINEAR
# cv2.INTER_NEAREST - 최근방 이웃 보간법: 가장 빠르지만 퀄리티가 많이 떨어집니다. 따라서 잘 쓰이지 않습니다.
# cv2.INTER_LINEAR - 양선형 보간법(2x2 이웃 픽셀 참조) :4개의 픽셀을 이용합니다. 효율성이 가장 좋습니다. 속도도 빠르고 퀄리티도 적당합니다.
# cv2.INTER_CUBIC - 3차회선 보간법(4x4 이웃 픽셀 참조) 16개의 픽셀을 이용합니다. cv2.INTER_LINEAR 보다 느리지만 퀄리티는 더 좋습니다.
# cv2.INTER_LANCZOS4 - Lanczos 보간법 (8x8 이웃 픽셀 참조) 64개의 픽셀을 이용합니다. 좀더 복잡해서 오래 걸리지만 퀄리티는 좋습니다.
# cv2.INTER_AREA - 영상 축소시 효과적 영역적인 정보를 추출해서 결과 영상을 셋팅합니다. 영상을 축소할 때 이용합니다.
cartoon_img = cv2.stylization(img, sigma_s=100, sigma_r=0.1)
# cv2.stylization(img, sigma_s=(0~200), sigma_r=(0~1))
# sigma_s: 이미지가 부드럽게 되는 정도 값이 클수록 이미지가 부드러워지지만 계산이 느려집니다.
# sigma_r: 이미지를 부드럽게 하면서 가장자리를 유지하려는 경우 중요합니다. 작은 sigma_r은 매우 유사한 색상만 평균화(즉, 매끄럽게 함)하는 반면 많이 다른 색상은 그대로 유지됩니다.  
cv2.imshow('cartoon view', cartoon_img)
# 화면출력

cv2.waitKey(0)
#cv2.waitKey() 는 keyboard입력을 대기하는 함수로 0이면 key입력까지 무한대기이며 특정 시간동안 대기하려면 milisecond값을 넣어주면 됩니다.
cv2.destroyAllWindows()
# cv2.destroyAllWindows() 는 화면에 나타난 윈도우를 종료합니다. 일반적으로 위 3개는 같이 사용됩니다.