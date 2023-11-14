import torch

# int_32_tensor = torch.tensor([3,6,9], dtype=torch.long)

float_32_tensor = torch.tensor([3.0, 6.0, 9.0], dtype=torch.float32)
print(float_32_tensor)

# print(int_32_tensor * float_32_tensor)

# how to get datatype form a tensor (.dtype)
print(float_32_tensor.dtype)

# to get shape of a tensor we can use (.shape)
print(float_32_tensor.shape)

# to get device we can use (.device)
print(float_32_tensor.device)

#https://youtu.be/V_xro1bcAuA?t=7749