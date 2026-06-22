# Write your solution here
def create_tuple(x: int, y: int, z: int):
    minm = min(x,y,z)
    maxm = max(x,y,z)
    result = (minm, maxm, x + y + z)
    return result
