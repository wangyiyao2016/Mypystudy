def recv(maxsize, *, block):
    'Receives a message'
    pass

rv = recv(1,block=True)

def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

rv = minimum(1, 5, 2, -5, 10) # Returns -5
print(rv)
rv = minimum(1, 5, 2, -5, 10, clip=0) # Returns 0
print(rv)