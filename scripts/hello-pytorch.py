# https://colab.research.google.com/drive/1ac0K9_aa46c77XEeYtaMAfSOfmH1Bl9L#scrollTo=V1odfZpGFoBi
import torch
import torch.nn as nn

## our data in tensor form
x = torch.tensor([[-1.0],  [0.0], [1.0], [2.0], [3.0], [4.0]], dtype=torch.float)
y = torch.tensor([[-3.0], [-1.0], [1.0], [3.0], [5.0], [7.0]], dtype=torch.float)

## neural network with 1 hidden layer
layer1 = nn.Linear(1,1, bias=False)
model = nn.Sequential(layer1)

## loss function
criterion = nn.MSELoss()

## optimizer algorithm
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

## training
for ITER in range(150):
    model = model.train()
    output = model(x)
    loss = criterion(output, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    model.eval()

## test the model
sample = torch.tensor([10.0], dtype=torch.float)
predicted = model(sample)
print(predicted.detach().item())
