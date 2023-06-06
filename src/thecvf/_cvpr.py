from ._base import TheCVF


class CVPR(TheCVF):

    def __init__(self):
        super(CVPR, self).__init__()
        self.conference_parser = {
            '2013': self.paper_list,
            '2014': self.paper_list,
            '2015': self.paper_list,
            '2016': self.paper_list,
            '2017': self.paper_list,
            '2018': self.conference_menu,
            '2019': self.conference_menu,
            '2020': self.conference_menu,
            '2021': self.conference_menu,
            '2022': self.conference_menu,
            '2023': self.conference_menu,
        }

        self.workshop_parser = {
            '2013': self.conference_menu,
            '2014': self.conference_menu,
            '2015': self.conference_menu,
            '2016': self.conference_menu,
            '2017': self.conference_menu,
            '2018': self.conference_menu,
            '2019': self.conference_menu,
            '2020': self.conference_menu,
            '2021': self.conference_menu,
            '2022': self.conference_menu,
            '2023': self.conference_menu,
        }
        self.demo_parser = {
            '2022': self.paper_list,
        }


