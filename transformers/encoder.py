encoder_layer = nn.TransformerEncoderLayer(d_model=512, nhead=8)
encoder = nn.TransformerEncoder(encoder_layer, num_layers=6)
encoder(x).shape
