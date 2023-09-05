import requests
from bs4 import BeautifulSoup
import json


def write_in_json_file(file_name, list_dicts):
    with open(file_name, 'w', encoding='utf-8') as fd:
        json.dump(list_dicts, fd, ensure_ascii=False, indent=4)

def main():
    url = 'https://quotes.toscrape.com/'
    next_page = ''
    all_quotes = []
    all_authors = []
    name_authors = []

    while True:   # page loop -- цикл по сторінках
        url_next_page = url + next_page
        response = requests.get(url_next_page)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes_class = soup.find_all('div', class_ ="quote")    
        # loop through the block of quotes on the page -- цикл по блоку цитат на сторінці
        for qu in quotes_class:
            # search and add a quote -- пошук та додавання цитати
            quote_text = qu.find('span', class_='text').text.strip()
            author_quote = qu.find('small', class_='author').text.strip()
            tags = qu.find('div', class_='tags')
            tagsforquote = tags.find_all('a', class_='tag')
            tags_quote = []
            for tag in tagsforquote:
                tags_quote.append(tag.text.strip())
            
            quote = {
                "tags": tags_quote,
                "author": author_quote,
                "quote": quote_text
            }
            all_quotes.append(quote)
            # search and add an author -- пошук та додавання автора
            if author_quote in name_authors:
                continue
            else:
                name_authors.append(author_quote)
                url_about = url + qu.find('a')['href']
                response = requests.get(url_about)
                soup_about = BeautifulSoup(response.text, 'lxml')
                about_author = soup_about.find('div', class_='author-description').text.strip()
                born_date = soup_about.find('span', class_="author-born-date").text.strip()
                born_location = soup_about.find('span', class_="author-born-location").text.strip()
                author = {
                    "fullname": author_quote,
                    "born_date": born_date,
                    "born_location": born_location,
                    "description": about_author
                }
                all_authors.append(author)
        # next page -- наступна сторінка
        next_p = soup.find('li', class_="next")
        if next_p:
            next_page = next_p.find('a')['href']
            print(next_page.replace('/',' ').strip())
            continue
        else:
            print('finish')
            break
    # writing to json-files -- запис в json-файли
    write_in_json_file('quotes.json', all_quotes)
    write_in_json_file('authors.json', all_authors)


if __name__ == '__main__':
    main()
