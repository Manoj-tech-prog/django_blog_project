array = [{'name':20,'manoj':25,'john':32}]

arr = dict(sorted(array[0].items(), key=lambda q:q[1]))

print(arr)