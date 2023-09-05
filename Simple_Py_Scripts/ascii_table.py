#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# source: http://stackoverflow.com/a/5910078/5909792
def ascii_table(rows):
    headers = rows[0]
    lens = list()
    for i in range(len(rows[0])):
        lens.append(
            len(
                max(
                    [str(x[i]) for x in rows] + [headers[i]],
                    key=lambda x: len(str(x))
                )
            )
        )

    formats = ["%%-%ds" % col_len for col_len in lens]

    pattern = " | ".join(formats)
    hpattern = " | ".join(formats)
    separator = "-+-".join(['-' * n for n in lens])

    text_lines = [hpattern % tuple(headers), separator]
    for line in rows[1:]:
        text_lines.append(pattern % tuple(t for t in line))

    return '\n'.join(text_lines)


if __name__ == '__main__':
    columns = ['id', 'url', 'name', 'short_name', 'birthday', 'job', 'department', 'photo', 'work_phone', 'mobile_phone', 'email']
    rows = [['#1', 'http://amiller.example.com', 'Andrew Miller', 'amiller', '11 December', 'Testing Engineer', 'CD, Product Support Service', 'amiller.jpg', '888888888888', '', 'amiller@example.com'], ['#2', 'http://ataylor.example.com', 'Anthony Taylor', 'ataylor', '17 July', 'Software Engineer', 'CD, Product Support Service', 'ataylor.jpg', '', '', 'ataylor@example.com'], ['#3', 'http://dmoore.example.com', 'Daniel Moore', 'dmoore', '2 March', 'Testing Engineer', 'CD, Product Support Service', 'dmoore.jpg', '', '', 'dmoore@example.com'], ['#4', 'http://dsmith.example.com', 'David Smith', 'dsmith', '5 January', 'Testing Engineer', 'Processing Services Division', 'dsmith.jpg', '', '', 'dsmith@example.com'], ['#5', 'http://awilson.example.com', 'Alexander Wilson', 'awilson', '11 April', 'Software Engineer', 'CD, Product Support Service', 'awilson.jpg', '', '', 'awilson@example.com'], ['#6', 'http://asmith.example.com', 'Alexander Smith', 'asmith', '3 November', 'Testing Engineer', 'CD, Product Support Service', 'asmith.jpg', '', '', 'asmith@example.com'], ['#7', 'http://jdavis.example.com', 'Jayden Davis', 'jdavis', '10 April', 'Shift Engineer', 'BSD, Presale Solution Bureau', 'jdavis.jpg', '', '', 'jdavis@example.com'], ['#8', 'http://jdavis.example.com', 'Jacob Davis', 'jdavis', '5 July', 'Shift Engineer', 'DD, Technical Translation Bureau', 'jdavis.jpg', '', '', 'jdavis@example.com'], ['#9', 'http://ejones.example.com', 'Ethan Jones', 'ejones', '14 September', 'Software Engineer', 'BSD, Presale Solution Bureau', 'ejones.jpg', '', '', 'ejones@example.com'], ['#10', 'http://abrown.example.com', 'Angel Brown', 'abrown', '15 April', 'Testing Engineer', 'Processing Services Division', 'abrown.jpg', '', '', 'abrown@example.com'], ['#11', 'http://dwilliams.example.com', 'David Williams', 'dwilliams', '23 November', 'Application Developer', 'DD, Technical Translation Bureau', 'dwilliams.jpg', '', '', 'dwilliams@example.com'], ['#12', 'http://ddavis.example.com', 'Daniel Davis', 'ddavis', '5 September', 'Shift Engineer', 'DD, Technical Translation Bureau', 'ddavis.jpg', '', '', 'ddavis@example.com'], ['#13', 'http://ntaylor.example.com', 'Nathan Taylor', 'ntaylor', '16 February', 'Shift Engineer', 'BSD, Presale Solution Bureau', 'ntaylor.jpg', '', '', 'ntaylor@example.com'], ['#14', 'http://dtaylor.example.com', 'Daniel Taylor', 'dtaylor', '10 March', 'Application Developer', 'DD, Technical Translation Bureau', 'dtaylor.jpg', '', '', 'dtaylor@example.com'], ['#15', 'http://jbrown.example.com', 'Jayden Brown', 'jbrown', '1 January', 'Software Engineer', 'DD, Technical Translation Bureau', 'jbrown.jpg', '', '', 'jbrown@example.com'], ['#16', 'http://asmith.example.com', 'Andrew Smith', 'asmith', '9 August', 'Software Engineer', 'CD, Product Support Service', 'asmith.jpg', '', '', 'asmith@example.com'], ['#17', 'http://jsmith.example.com', 'Jayden Smith', 'jsmith', '8 April', 'Testing Engineer', 'BSD, Presale Solution Bureau', 'jsmith.jpg', '', '', 'jsmith@example.com'], ['#18', 'http://asmith.example.com', 'Alexander Smith', 'asmith', '7 November', 'Shift Engineer', 'Processing Services Division', 'asmith.jpg', '', '', 'asmith@example.com'], ['#19', 'http://dbrown.example.com', 'David Brown', 'dbrown', '20 October', 'Shift Engineer', 'Processing Services Division', 'dbrown.jpg', '', '', 'dbrown@example.com'], ['#20', 'http://nwilliams.example.com', 'Nathan Williams', 'nwilliams', '9 March', 'Shift Engineer', 'CD, Product Support Service', 'nwilliams.jpg', '', '', 'nwilliams@example.com'], ['#21', 'http://dtaylor.example.com', 'Daniel Taylor', 'dtaylor', '5 April', 'Shift Engineer', 'CD, Product Support Service', 'dtaylor.jpg', '', '', 'dtaylor@example.com'], ['#22', 'http://nmoore.example.com', 'Nathan Moore', 'nmoore', '14 July', 'Testing Engineer', 'DD, Technical Translation Bureau', 'nmoore.jpg', '', '', 'nmoore@example.com'], ['#23', 'http://ewilson.example.com', 'Ethan Wilson', 'ewilson', '7 September', 'Software Engineer', 'CD, Product Support Service', 'ewilson.jpg', '', '', 'ewilson@example.com'], ['#24', 'http://awilson.example.com', 'Angel Wilson', 'awilson', '5 December', 'Application Developer', 'BSD, Presale Solution Bureau', 'awilson.jpg', '', '', 'awilson@example.com'], ['#25', 'http://abrown.example.com', 'Angel Brown', 'abrown', '21 October', 'Shift Engineer', 'BSD, Presale Solution Bureau', 'abrown.jpg', '', '', 'abrown@example.com']]

    rows.insert(0, columns)
    print(ascii_table(rows))
