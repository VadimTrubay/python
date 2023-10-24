from jinja2 import Template

a = [1, 2, 3, 4, 5, 6]

link = "{{ a | sum }}"


t = Template(link)
res = t.render(a=a)
print(res)