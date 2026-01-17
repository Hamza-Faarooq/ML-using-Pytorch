lstm = nn.LSTM(input_size=50, hidden_size=128, batch_first=True)
x = torch.randn(4, 10, 50)
out, (h, c) = lstm(x)
out.shape
