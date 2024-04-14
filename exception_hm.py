
result = []
try:
  def divider(a, b):
    try:
      if a < b:
        raise ValueError
      if b > 100:
        raise IndexError
    except (ValueError,IndexError) as err:
      print(err)
    return a/b
  data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
  for key in data:
    res = divider(key, data[key])
    result.append(res)
except :
  print("Error")
print(result)