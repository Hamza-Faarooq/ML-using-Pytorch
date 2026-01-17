import torch.nn as nn

model = nn.Linear(10, 1)
x = torch.randn(5, 10)
model(x)


# this is a very basic model, just to get the gist of the basic code utilising pytorch
