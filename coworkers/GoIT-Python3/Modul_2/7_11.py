def first(size, *numbers):
    return size + len(numbers)
    


def second(size, **comments):
  return size + len(comments)


print(first(1, "Alex", "Boris"))
print(second(3, comment_one="first", comment_two="second", comment_third="third"))