def lookup_key(data, value):
    keys = list()
    for k, v in data.items():
      if v == value:
       keys.append(k)
    return keys


 


print(lookup_key({'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}, 2))