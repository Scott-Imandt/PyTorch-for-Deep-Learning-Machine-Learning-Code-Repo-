import torch;

# https://www.learnpytorch.io/00_pytorch_fundamentals/

# https://pytorch.org/docs/stable/tensors.html


# Create a tensor of all zeros (usefull when creating a mask)

zeros = torch.zeros(3,4)

print(zeros)




# Create a tensor of all ones

ones = torch.ones(3,4)

print(ones)

# Default data type == dtype Default is torch.float32