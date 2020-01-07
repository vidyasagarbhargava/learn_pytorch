import torch
import torchvision
#print(torch.cuda.is_available())
#1 -dimensional tensor :- list
a = torch.tensor([2,2,1])
print(a)

b = torch.tensor([[1,2,3], [1,2,3], [33,3,4], [2, 3, 2]])
print(b)

print(a.size())
print(b.shape)
print(b)
x = b.view(-1,2)
print(x.size())
