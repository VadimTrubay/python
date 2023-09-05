''' Есть список IP адресов:

IP = [
    "85.157.172.253",
    ...
]
Реализуйте две функции. Первая get_count_visits_from_ip с помощью Counter будет возвращать словарь,
 где ключ — это IP, а значение — количество вхождений в указанный список.
Пример:
{
    '85.157.172.253': 2,
    ...
}
Вторая функция get_frequent_visit_from_ip возвращает кортеж с наиболее часто встречаемым в списке IP
и количеством его вхождений в список.
Пример:
('66.50.38.43', 4) '''


from collections import Counter


def get_count_visits_from_ip(ips):
    ip_dict = Counter(ips)
    return ip_dict


def get_frequent_visit_from_ip(ips):
    ip_dict = Counter(ips)
    return ip_dict.most_common(1)[0]
