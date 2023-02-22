from tqdm import tqdm
import argparse
import logging
import json
import os

import thecvf

project_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(description='The CVF')
parser.add_argument('--title', type=str, default='cvpr', help='conference name')
parser.add_argument('--year', type=str, default='2013', help='conference year')
parser.add_argument('--type', type=str, default='main', help='main, workshop, demo')
args = parser.parse_args()


def main():
    cvpr = thecvf.CVPR()
    main_menu = cvpr.parse_main_menu()

    papers = []
    common = dict()
    for e in main_menu:
        if e['year'] != args.year:
            continue

        common = e
        break
    name = common['name']
    year = common['year']
    paper_url_list = cvpr.conference_parser[year](args.type, **common)

    for p in tqdm(paper_url_list):
        _paper_info = cvpr.paper(p)
        papers.append(thecvf.Contents(
            name=common['name'],
            year=common['year'],
            location=common['location'],
            type_=thecvf.common.index(args.type),
            topic='',
            title=_paper_info['title'],
            abstract=_paper_info['abstract'],
            author=_paper_info['author'],
            citation=_paper_info['citation'],
        ).json())

    with open(os.path.join(project_root, 'assets', f'{name}-{year}-{args.type}.json'), mode='w', encoding='utf-8') as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
