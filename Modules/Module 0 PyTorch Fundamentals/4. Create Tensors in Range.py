import torch;

# https://www.learnpytorch.io/00_pytorch_fundamentals/

# https://pytorch.org/docs/stable/tensors.html

# arange doc: https://pytorch.org/docs/stable/generated/torch.arange.html

# Create a range od tensors and tensors-like

# use torch.range() This will be depricated in a future release

print(torch.range(0,10))

# arange is the proper way to make tensors with ranges
print(torch.arange(0,10))# 0-9 (end - 1)

# more advanced

print(torch.arange(start=0, end=1001, step=1))

#-----------------------Create tensor like------------------------
#Create a tensor of similar shape using input

one_to_ten = torch.arange(start=1, end=11, step=1)
print(one_to_ten)

ten_zeroes = torch.zeros_like(input=one_to_ten)
print(ten_zeroes)