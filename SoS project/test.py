import torch
print(torch.cuda.is_available())         # ✅ Should be True
print(torch.cuda.get_device_name(0))     # ✅ Should show your GPU name (like RTX 4050)
