import torch;

# https://www.learnpytorch.io/00_pytorch_fundamentals/

# https://pytorch.org/docs/stable/tensors.html


##-----------------------------------------------Random Tensor-----------------------------------------------

# Why create random tensors????
#Radom of tensors are important because the way that many neural networks learn is that they start with tensors full of random numbers and then adjust those random number to then better represent the data
#   Start with random number -> look at data -> Update Random numbers -> look at data -> update random numbers (Typical work flow)

# https://pytorch.org/docs/stable/generated/torch.rand.html

# Create random tensor of size (3,4)

random_tensor = torch.rand(3,4)

print(random_tensor)

print(random_tensor.ndim) #2d

print(random_tensor.shape) #[3,4]

# create a random tensor with similar shape to an image tensor

# Size is the default so torch.rand(224,224,3) would work as well
random_image_tensor = torch.rand(size=(224, 224, 3))# height, width, color channels(RGB) (Color channels can go before or after height (3,224,224) or (224,224,3))

print(random_image_tensor.shape)# [224, 224, 3]

print(random_image_tensor.ndim)# [3]

