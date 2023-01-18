# Neural-Network for vision

### 딥러닝 논문 리뷰
* https://docs.google.com/presentation/d/1CT5-f7GyvARWMjpn3UQABDwPGjEFK_1_50eHGObPUto/edit#slide=id.p


### 개요
* CNN과 Faster R-CNN에 대한 전반적인 공부와 실습
* 농업용 이미지 데이터를 활용하여 Neural-Network를 학습
* 농산물 품질 분류 및 생산량 확인

### CNN
* Bing image downloader를 이용한 이미지 데이터 확보 - https://github.com/gurugaurav/bing_image_downloader
* ResNet 18모델 적용
* 간단한 레이어 구성을 통한 과일 품질 분류(classification)
* 사용자의 사진을 이용한 분류 test 제공

### Faster R-CNN
* 직접 구득한 이미지 데이터 활용
* ResNet50 FPN 모델 적용
* 과일의 객체 인식(Detection)
* Labelme를 이용한 클래스 어노테이션 진행 후 학습 - https://github.com/wkentaro/labelme

### Why CNN (Convolutional Neural Network)
* 기존의 컴퓨터 비전(CV)의 경우현장 과일 탐지 작업에서 과일이나 단풍 색상, 조명, 카메라 시야각 및 카메라의 변화와 같은 교정 조건에 대한 일련의 조건 밖에서 사용할 때 재설계가 필요했다.


* “머신러닝을 기반으로 한 방법은 초기 이미지 처리 기술보다 더 나은 결과를 산출하지만, 더 많은 계산 자원과 훈련을 위해 더 많은 라벨이 지정된 데이터가 필요하다.”
“최근 몇 년 동안 고성능 GPU를 사용할 수 있게 되었고, 자유롭게 사용할 수 있는 그래픽 라벨링 툴(ex; labelme)의 출현으로 이미지에서 객체를 라벨링하는 작업이 더 쉬워졌다.”


* “Faster Regional Convolutional Neural Network (Faster R-CNN), Single Shot multibox Detector (SSD), You Only Look Once (YOLO) 와 같은 많은 최첨단 딥 러닝 프레임워크로 이어졌다.”


* “과일 분류 및 등급에 사용하기 위해 머신러닝 알고리즘을 리뷰한 결과, K-Nearest Neighbour (KNN), Artificial Neural Network (ANN) 및 Convolutional Neural Network (CNN)은 머신러닝 (ANN 및 딥 러닝 포함)에 대한 개요와 수확량 예측 및 잡초의 탐지/분류, 작물 품질 및 질병과 같은 농업 영역에서의 적용을 제시했다.”


* “컨볼루션 네트워크(convNets)를 사용한 딥 러닝은 convNets이 translational invariant patterns를 학습하여 이미지의 모든 곳에서 물체를 감지할 수 있으며 점점 더 복잡해지는 패턴의 계층 구조를 감지하여 복잡한 시각적 개념을 추출할 수 있기 때문에 이미지 처리 작업에 널리 사용된다.”


* “딥 러닝의 혁명은 AlexNet이 2012 ImageNet Large Scale Visual Recognition Challenge에서 전통적인 지원 벡터 머신 분류기(SVM)를 큰 차이로 우승했을 때 시작되었다. 1995 이후 몇 년 동안 우승한 출품작은 모두 딥 러닝을 사용하였다. 그러나, 훈련과 테스트 오류는 깊이에 따라 증가하여 더 깊은 모델을 훈련하기 어렵게 만들었지만(ex: 'vanishing gradient'), 이 문제는 skip connection과 결과 residual networks를 사용하여 해결하였다.”


### About ResNet
* “ResNet은 더 깊은 (최대 152 layers) 네트워크에 대한 효율적인 학습을 위해 residual learning 프레임워크를 사용했다. ResNet은 더 깊은 네트워크에서 정보가 손실되지 않고 (vanishing gradient 없이) 흐를 수 있도록 'identity shortcut connection'을 특징으로 하는 residual blocks을 사용했다.”


<img src="https://user-images.githubusercontent.com/93086581/211189863-39d2df3e-53ee-4f60-8a58-543d8128b324.png">


### About RCNN
* “R-CNN은 2012년에 출시된 object detection을 위해 heuristic region proposal - selective search와 Convolutional Network (ConvNet) 을 결합한 모델이다.”


* “Fast R-CNN(Girshick, 2015)에서 SPP 레이어는 fixed size region of interest pooling (ROIPooling) layer로 대체되어 R-CNN보다 속도를 높일 수 있었다.”


* “Faster R-CNN은 Fast R-CNN의 selective search(heuristic region proposal)을 region proposal net- work (RPN)으로 대체했으며 end-to-end 훈련이 가능했다.”


<img src='https://user-images.githubusercontent.com/93086581/211190047-edce6a7e-1b03-4775-9ba2-06365cc5b229.png'>



### 이후 목표
* 이미지의 meta 정보 이용
* 비파괴 생육조사 시스템 개발
