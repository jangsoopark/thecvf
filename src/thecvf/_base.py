from bs4 import BeautifulSoup
from urllib import parse
import requests
import copy


class TheCVF(object):

    def __init__(self):
        self.host = 'https://openaccess.thecvf.com'

    def get(self, uri=''):
        response = requests.get(f'{self.host}/{uri}')
        return response.text

    def parse_main_menu(self):
        html = self.get('menu')
        bs = BeautifulSoup(html, 'html.parser')
        content = bs.find('div', {'id': 'content'})
        main_menu = content.find_all('dd')

        menu = []
        for e in main_menu:
            title, meta = e.text.split(',')
            name, year = title.split()
            name = name.lower()
            if name != self.__class__.__name__.lower():
                continue

            location = meta.split('[')[0].strip()

            conference_type = self.parse_conference_type(e.find_all('a'))
            menu.append({
                'name': name,
                'year': year,
                'location': location,
                'conference_type': conference_type
            })
        return menu

    def paper(self, uri):
        html = self.get(uri)
        bs = BeautifulSoup(html, 'html.parser')
        content = bs.find('dl')
        title = content.find('div', {'id': 'papertitle'}).text
        citation = content.find('div', {'id': 'authors'}).text

        author = citation.split(';')[0]
        abstract = content.find('div', {'id': 'abstract'}).text

        return {
            'title': title,
            'author': author,
            'citation': citation,
            'abstract': abstract,
            'url': f'{self.host}/{uri}'
        }

    def paper_list(self, type_, topic='', **params):
        html = self.get(params['conference_type'][type_])
        bs = BeautifulSoup(html, 'html.parser')
        content = bs.find('div', {'id': 'content'})
        _menu = content.find_all('dt', {'class': 'ptitle'})

        _paper_list = []
        for e in _menu:
            link = e.find_all('a').pop()['href']
            _paper_list.append((topic, link))
        return _paper_list

    def conference_menu(self, type_, **params):
        html = self.get(params['conference_type'][type_])
        bs = BeautifulSoup(html, 'html.parser')
        content = bs.find('div', {'id': 'content'})
        _menu = content.find_all('dd')

        topic_list = []
        for e in _menu:
            if 'back' in e.text.lower():
                continue
            if 'all' in e.text.lower():
                continue
            # print(e.find('a')['href'])
            link = e.find('a')['href']
            topic = e.text
            topic_list.append((
                topic if type_ == 'workshop' else '',
                link
            ))

        _paper_list = []
        for topic, link in topic_list:
            _params = copy.deepcopy(params)
            _params['conference_type'][type_] = link
            if type_ == 'workshop':
                ws = params['conference_type'][type_].split('/')[1]
                if ws not in link:
                    _params['conference_type'][type_] = f'{ws}/{link}'

            _paper_list.extend(self.paper_list(type_, topic, **_params))

        return _paper_list

    @staticmethod
    def parse_conference_type(elements):
        conference_type = {}
        for a in elements:
            if 'main' in a.text.lower():
                conference_type['main'] = a['href']
                continue
            if 'workshop' in a.text.lower():
                conference_type['workshop'] = a['href']
                continue
            if 'demo' in a.text.lower():
                conference_type['demo'] = a['href']
                continue

        return conference_type
