cnn = nn.Sequential(
    nn.Conv2d(3, 16, 3),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Flatten(),
    nn.Linear(16*15*15, 10)
)

img = torch.randn(1, 3, 32, 32)
cnn(img)
