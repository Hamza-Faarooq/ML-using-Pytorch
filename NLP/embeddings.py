emb = nn.Embedding(10000, 768)
tokens = torch.randint(0, 10000, (2, 5))
emb(tokens)
