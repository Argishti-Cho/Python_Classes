

# text = [15, 73, -4, 8, 52, 10, 23]
text = (input())
texts = [float(num) for num in text.split()]
for i in range(len(texts)):
    for j in range(i +  1, len(texts)):
        if texts[i] > texts[j]:
            texts[i], texts[j] = texts[j], texts[i]
print(texts)

# for i in range(len(text)):
#     for j in range(i +  1, len(text)):
#         if text[i] > text[j]:
#             text[i], text[j] = text[j], text[i]
# print(text)

