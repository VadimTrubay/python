''' Разработайте функцию get_str_date(date), которая будет преобразовывать дату из базы данных
 в формате ISO "2021-05-27 17:08:34.149Z" в строковое представление
 "Thursday 27 May 2021" — день недели, число, месяц и год.
 Преобразованное значение функция должна вернуть при вызове. '''



from datetime import datetime

def get_str_date(date):
    dt = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%fZ')
    return dt.strftime('%A %d %B %Y')


print(get_str_date("2021-05-27 17:08:34.149Z"))