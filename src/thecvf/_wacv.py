from ._base import TheCVF


class WACV(TheCVF):

    def __init__(self):
        super(WACV, self).__init__()
        self.conference_parser = {
            '2020': self.paper_list,
            '2021': self.paper_list,
            '2022': self.paper_list,
            '2023': self.paper_list,
        }

        self.workshop_parser = {
            '2020': self.conference_menu,
            '2021': self.conference_menu,
            '2022': self.conference_menu,
            '2023': self.conference_menu,
        }


