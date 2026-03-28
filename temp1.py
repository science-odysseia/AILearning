import torch, numpy as np
x_train = torch.tensor(np.arange(1, 5)).float().view(-1, 1)
print(x_train)