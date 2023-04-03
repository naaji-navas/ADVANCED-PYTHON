def process(x):
    i = 0
    while i<x:
        yield i * 2
        i += 1
for i in process(100):
    # print(i)
    pass