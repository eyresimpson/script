import chardet

# chardet可以自动猜测目标的编码类型

text = "一个字符串"
encoding = chardet.detect(text.encode())["encoding"]
decoded_text = text.encode(encoding)

print(encoding)
print(decoded_text)
