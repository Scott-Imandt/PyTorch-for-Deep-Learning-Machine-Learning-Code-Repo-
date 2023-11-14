#https://youtu.be/V_xro1bcAuA?t=6843

#1:54:03

#NOTE tensor datatype is one of the three big errors when doing deep learning
#   tensor not right datatype
#   tensor not right shape
#   tensor not correct device

import torch

# Float 32 tensor

float_32_tensor = torch.tensor([3.0,6.0,9.0], dtype=torch.float32,    # datatype of the tensor  (Float32(single precition), float16, int64 ... etc)   datatype is the data presison of a numeric precision
                                              device="cpu",  # default is CPU or cuda for gpu acceleration
                                              requires_grad=False) # if you want pytorch to track gradients of the tensore when i enters calculation

print(float_32_tensor.dtype)


# can also create a tensore based on another and change the type
float_16_tensor = float_32_tensor.type(torch.float16)
print(float_16_tensor.dtype)



