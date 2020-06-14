n = [
    1, 2.34, 'abc', None, False, ('abc', 'abc'),
    {'a': 'b', 'c': 'd'}, [1, 2], {'a', 'b', 'c'}
]
for id, item in enumerate(n,1):
    print(f"{id}: {item} - {type(item)}")
