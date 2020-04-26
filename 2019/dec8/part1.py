#!/usr/bin/env python3
with open('input.txt') as f:
    pixels = [int(p) for p in f.read().strip()]

# layers
img_size = 25 * 6
img_layers = int(len(pixels) / img_size)

layers = []
for i in range(0, img_layers):
    s = i * img_size
    e = i * img_size + img_size
    l = pixels[s:e]
    layers.append((l.count(0), l))

res_layer = sorted(layers, key=lambda s: s[0])[0][1]
print(res_layer.count(1) * res_layer.count(2))
