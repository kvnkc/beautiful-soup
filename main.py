from bs4 import BeautifulSoup
import requests
# import lxml <-- if html.parser doesnt work

response = requests.get('https://news.ycombinator.com/')
page_source = response.text

soup = BeautifulSoup(page_source, 'html.parser')
articles = soup.find_all(name='span', class_='titleline')

article_texts = []
article_links = []

for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get('href')
    article_links.append(article_links)

article_upvotes = [int(score.getText().split()[0])
                   for score in soup.find_all(name='span', class_='score')]
a = 0
for num in article_upvotes:
    if num > a:
        a = num
print(article_upvotes)
print(a)

# with open('website.html', encoding='utf-8') as file:
#     contents = file.read()


# soup = BeautifulSoup(contents, 'html.parser')

# returns a list of all elements in the html you are looking for
# all_anchor_tags = soup.find_all(name='a')

# Loops through all anchor tags in html document
# for tag in all_anchor_tags:
# print(tag.getText())
# print(tag.get('href'))

# print(all_anchor_tags)

# Looks for a specific heading with the id 'name'
# heading = soup.find(name='h1', id='name')
# print(heading)

# Looks for a specific section where the class is 'heading'
# section_heading = soup.find(name='h3', class_='heading')
