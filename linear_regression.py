X = torch.randn(100, 1)
y = 3*X + 2 + 0.1*torch.randn(100, 1)

w = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)

for _ in range(100):
    y_hat = w*X + b
    loss = ((y_hat - y)**2).mean()
    loss.backward()
    with torch.no_grad():
        w -= 0.1*w.grad
        b -= 0.1*b.grad
        w.grad.zero_()
        b.grad.zero_()

w, b

