"""
create function for creating a new instance
"""


# def func(number: int, name: str):
#     """ Create function for creating a new instance
#     :number: that is the number
#     """
#     print(number, name)
# func(5, "vad")

# import unittest
#
# def multiply_numbers(x: int, y: int):
#     return x * y
#
# class TestMulti(unittest.TestCase):
#     def test_multiply_numbers(self):
#         result = multiply_numbers(2, 2)
#         self.assertEqual(result, 4)
#
#
# if __name__ == "__main__":
#     unittest.main()


# a = 1
# b = 2
# assert a == b

# def testfunc():
#     """
#     The testfunc function is a test function.
#
#     :return: None
#     :doc-author: Trelent
#     """
#     print('ok')
#
#
# print(testfunc.__doc__)
# print(testfunc.__hash__())


from datetime import datetime, timedelta

def get_date_range(user_input):
    delta = timedelta(days=user_input)
    current_date = datetime.now()
    end_date = current_date
    date_range = [(end_date - timedelta(days=x)).strftime("%d.%m.%Y") for x in range(delta.days)]
    return delta.days, date_range

# Пример использования:
input_days = 10  # Введите количество дней назад
days_count, date_list = get_date_range(input_days)
print(f"Days count: {days_count}")
print("Date List:", date_list)




