import time

start_time = time.time()

d = {}

for i in range(10):
    d[f"{i}"] = i * 10
# print(d)
# print(d.items())
# print(d.keys())
print(eval("1+2"))
# print(list(map(lambda a, b: a + b, lambda x: x[1], d.values())))
end_time = time.time()
print("time:", end_time - start_time)
