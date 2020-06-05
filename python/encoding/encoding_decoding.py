print("Encoding".center(20, "="))
print("résumé".encode("utf-8"))
print("El Niño".encode("utf-8"))

print("Decoding".center(20, "="))
print(b"r\xc3\xa9sum\xc3\xa9".decode("utf-8"))
print(b"El Ni\xc3\xb1o".decode("utf-8"))
