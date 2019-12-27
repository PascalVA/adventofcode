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
    layers.append(l)

img = [2] * 150
for layer in reversed(layers):
    for i, p in enumerate(layer):
        img[i] = p if p != 2 else img[i]

output = ""
for i, p in enumerate(img):
    if i % 25 == 0:
        output += "\n"
    if p == 0:
        output += " "
    if p == 1:
        output += "#"

print(output)
