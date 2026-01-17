attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
x = torch.randn(10, 2, 512)
attn(x, x, x)[0].shape
