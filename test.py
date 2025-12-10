a = ["a", "b", "c"]
b = [1, 2, 3]
print(",".join([str(e) for e in b]))
print({str(e): e for e in b if e % 2})