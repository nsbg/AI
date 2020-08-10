## 사이킷런/텐서플로우 설치  
(Anaconda 배포판 설치 시 사이킷런이 포함이기 때문에 추가 설치 필요 X)  
---
  
1. python -c "import sklearn; print(sklearn.__version__)"  
=> 사이킷런 설치 확인
  
2. pip install tensorflow==2.0.0  

3. python -c "import tensorflow as tf; print(tf.__version__)"  
=> 텐서플로우 설치 확인  
  
4. conda env create -f environment.yml  
=> **파일 속성 확인 후 .txt를 완전히 지우고 .yml로 확장자 변경**  
  
5. conda activate(비활성화는 deactivate) python-ml  
=> 설치 후 자동으로 콘다 환경 생성 & 텐서플로우와 필요한 다른 패키지 설치  
  

## Jupyter notebook/Google Colab  
(Google Colab : 구글에서 제공하는 주피터 노트북 환경)
---
  
✔ 주피터 노트북 파일 확장자 : ipynb  
  
✔ 주피터 노트북은 다른 사이트 참고해서 더 공부할 것  
  

##### "머신 러닝 교과서 with 파이썬, 사이킷런, 텐서플로" 책에서 발췌