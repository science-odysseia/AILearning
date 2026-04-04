파이썬 문법

[Python](/python_기초문법.ipynb)

AI학습

[AI](/AI기초.ipynb)

## GPU 초기 설정
<details>
<summary> <h3> Ubuntu </h3> </summary>

### Ubuntu

1. 그래픽 드라이버 설치

``` bash
# 시스템 업데이트 및 드라이버 자동 권장 버전 확인
sudo apt update
ubuntu-drivers devices

# 가장 적합한 드라이버 자동 설치 (보통 추천 버전 설치)
sudo ubuntu-drivers autoinstall

# 이후 재부팅
sudo reboot
```

2. 가상환경 생성

``` bash
# venv 패키지 설치 (안 되어 있을 경우)
sudo apt update
sudo apt install python3-venv

# 가상환경 생성 및 활성화
python3 -m venv "가상환경 이름"
source "가상환경 이름"/bin/activate
```

3. pytorch 설치

``` bash
# pip 최신화
pip install --upgrade pip

# CUDA 12.1 버전용 PyTorch 설치
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

</details>
