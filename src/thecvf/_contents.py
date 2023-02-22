import json


class Contents(object):

    def __init__(self, name, year, location, type_, topic, title, abstract, author, citation, url):
        self.name: str = name
        self.year: str = year
        self.location: str = location
        self.type: int = type_
        self.topic: str = topic
        self.title: str = title
        self.abstract: str = abstract
        self.author: str = author
        self.citation: str = citation
        self.url: str = url

    def json(self):
        return {
            'name': self.name,
            'year': self.year,
            'location': self.location,
            'type': self.type,
            'topic': self.topic,
            'title': self.title,
            'abstract': self.abstract,
            'author': self.author,
            'citation': self.citation,
            'url': self.url,
        }

    def __str__(self):
        return json.dumps({
            'name': self.name,
            'year': self.year,
            'location': self.location,
            'type': self.type,
            'topic': self.topic,
            'title': self.title,
            'abstract': self.abstract,
            'author': self.author,
            'citation': self.citation,
            'url': self.url,
        })

    def __repr__(self):
        return self.__str__()
