def get_fullname(first_name, last_name, middle_name=None):
      if middle_name == None:
            return f'{first_name} {last_name}'
      elif middle_name != None:
            return f'{first_name} {middle_name} {last_name}'


print(get_fullname('Vlad', 'Babenko', 'Yrievich'))

