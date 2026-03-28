import torch

# --- 가상의 모델 출력값과 정답 (수정 불필요) ---
# outputs: 모델이 예측한 확률 (0~1 사이)
outputs = torch.tensor([0.1, 0.9, 0.4, 0.7])
# labels: 실제 정답 (0 또는 1)
labels = torch.tensor([0.0, 1.0, 1.0, 1.0])

print(torch.sigmoid(outputs))

print(outputs > 0.5)
