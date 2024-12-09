from ._base import TheCVF


class ACCV(TheCVF):

    def __init__(self):
        super(ACCV, self).__init__()
        self.conference_parser = {
            '2020': self.paper_list,
            '2022': self.paper_list,
            '2024': self.paper_list,
        }

        self.workshop_parser = {
            '2020': self.conference_menu,
            '2022': self.conference_menu,
            '2024': self.conference_menu,
        }


