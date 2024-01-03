import json
import requests
from bs4 import BeautifulSoup

max_page_url = "https://quotes.toscrape.com/page/10/"
min_page_url = "https://quotes.toscrape.com/page/1/"
base_url = 'http://quotes.toscrape.com'
page_link_template = f"/page/{1}/"


def scrapping_authors():
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    pages = soup.find("ul", attrs={"class": "pager"})
    page_link = pages.find("a").get("href")
    pages_list_urls = []
    authors_list = []

    try:
        for page in range(1, 11):
            pages_list_urls.append(f"{base_url}/page/{page}/")
    except ValueError as e:
        print(f"Error processing: {e}")

    for page in pages_list_urls:
        response = requests.get(page)
        soup = BeautifulSoup(response.text, 'html.parser')

        for author in soup.find_all('small', attrs={'class': 'author'}):
            author_dict = {"fullname": None, "born_date": None, "born_location": None, "description": None}
            author.get("href")
            author_url = author.find_next_sibling("a").get("href")
            response_author = requests.get(base_url + author_url)
            soup = BeautifulSoup(response_author.text, 'html.parser')
            author_title = soup.find('h3', class_='author-title')
            burn_date = author_title.find('span', attrs={'class': 'author-born-date'}).text
            location = author_title.find("span", attrs={"class": "author-born-location"}).text
            description = author_title.find('div', class_='author-description').text.strip()
            author_name = author_title.get_text(strip=True).split(':')[0]
            author_dict["fullname"] = author_name
            author_dict["born_date"] = burn_date
            author_dict["born_location"] = location
            author_dict["description"] = description
            if author_dict not in authors_list:
                authors_list.append(author_dict)
                print(f"added author {author_name}...")
    return authors_list


def scrapping_quotes():
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    pages = soup.find("ul", attrs={"class": "pager"})
    page_link = pages.find("a").get("href")
    pages_list_urls = []
    quotes_list = []

    try:
        for page in range(1, 11):
            pages_list_urls.append(f"{base_url}/page/{page}/")
    except ValueError:
        print("The amount of pages was changed by service owner!")

    for page in pages_list_urls:
        response = requests.get(page)
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all("span", class_="text")
        authors = soup.find_all('small', class_='author')
        tags = soup.find_all('div', class_='tags')
        for i in range(0, len(quotes)):
            quotes_dict = {"tags": None, "author": None, "quote": None}
            quote = quotes[i].text
            author = authors[i].text
            tags_for_quote = tags[i].find_all('a', class_='tag')
            tags_list = []
            for tag in tags_for_quote:
                text_tag = tag.get_text()
                tags_list.append(text_tag)
            quotes_dict["author"] = author
            quotes_dict["quote"] = quote
            quotes_dict["tags"] = tags_list
            print(f"added quote for author {author}...")
            quotes_list.append(quotes_dict)
    return quotes_list


if __name__ == '__main__':
    with open('authors.json', 'w', encoding='utf-8') as fh:
        json.dump(scrapping_authors(), fh)

    with open('quotes.json', 'w', encoding='utf-8') as fh:
        json.dump(scrapping_quotes(), fh)
