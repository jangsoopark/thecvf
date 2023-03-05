from tqdm import tqdm
import argparse
import logging
import json
import os

import thecvf

project_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(description='The CVF')
parser.add_argument('--title', type=str, default='wacv', help='conference name')
parser.add_argument('--year', type=str, default='2023', help='conference year')
parser.add_argument('--type', type=str, default='main', help='main, workshop, demo')
args = parser.parse_args()


def main():
    conference = {
        'cvpr': thecvf.CVPR(),
        'wacv': thecvf.WACV(),
    }[args.title]
    _p = {
        'main': conference.conference_parser,
        'workshop': conference.workshop_parser,
    }[args.type]

    if args.title == 'cvpr' and args.year == '2022':
        _p.update({'demo': conference.demo_parser})

    main_menu = conference.parse_main_menu()

    papers = []
    common = dict()
    for e in main_menu:
        if e['year'] != args.year:
            continue
        common = e

    name = common['name']
    year = common['year']

    paper_url_list = _p[year](args.type, **common)
    for p in tqdm(paper_url_list):
        topic, url = p
        _paper_info = conference.paper(url)
        papers.append(thecvf.Contents(
            name=common['name'],
            year=common['year'],
            location=common['location'],
            type_=thecvf.common.index(args.type),
            topic=topic.strip(),
            title=_paper_info['title'].strip(),
            abstract=_paper_info['abstract'].strip(),
            author=_paper_info['author'].strip(),
            citation=_paper_info['citation'].strip(),
            url=_paper_info['url'],
        ).json())

    with open(os.path.join(project_root, 'assets', f'{name}-{year}-{args.type}.json'), mode='w', encoding='utf-8') as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
