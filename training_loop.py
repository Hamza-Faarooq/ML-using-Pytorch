optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
criterion = nn.MSELoss()

for epoch in range(3):
    optimizer.zero_grad()
    preds = model(x)
    loss = criterion(preds, torch.randn(5, 1))
    loss.backward()
    optimizer.step()
    print(loss.item())
