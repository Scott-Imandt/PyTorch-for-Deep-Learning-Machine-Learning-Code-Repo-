import torch;

# https://www.learnpytorch.io/00_pytorch_fundamentals/

# https://pytorch.org/docs/stable/tensors.html

#tensor are created using torch.tensor()

#Typical writing format is to do lowercase for vetor and scalars as lowercase and MATRIX and TENSOR as uppercase

#-----------------------------------------------Scalar-----------------------------------------------

# Scalar Tensors: has zero dementions and holds a single value

scalar = torch.tensor(7)

print(scalar.ndim) # Get the number of dimentions of a tensor

print(scalar.item()) #Get Scalar tensor as python number

# -----------------------------------------------Vector-----------------------------------------------
# Vector: more the n one number in one dimenstions
#   Number of square brakects can help reveial dimention

vector = torch.tensor([7,7])

print(vector.ndim) # 1D

# Shape would be the number of emements

print(vector.shape) # shape == 2

# -----------------------------------------------MATRIX-----------------------------------------------

MATRIX = torch.tensor([[7,8], [9,10]])

print(MATRIX.ndim) # 2D

print(MATRIX.shape) # [2,2] elements

# get elements
print(MATRIX[0][0])

#-----------------------------------------------Tensor-----------------------------------------------

# TENSOR

TENSOR = torch.tensor([[[ 1,2,3 ],
                        [ 4,5,6 ],
                        [ 7,8,9 ]]])

print(TENSOR)

print(TENSOR.ndim) # 3d

print(TENSOR.shape) # [1,3,3] : 1 of shape 3x3 (numbers in each bracket first number 1 has one inside, the second bracket has 3 and the third has 3 elemets)


#-----------------------------------------------Practice-----------------------------------------------

# make a tensor of shape 2,4,4

TENSOR = torch.tensor([[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]])

print(TENSOR.shape)# shape is 2 4x4