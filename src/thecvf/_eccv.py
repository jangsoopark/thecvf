from ._base import TheCVF


class ECCV(TheCVF):

    def __init__(self):
        super(ECCV, self).__init__()
        self.conference_parser = {
            '2018': self.paper_list,
            # '2020': self.paper_list,
        }

        self.workshop_parser = {
            '2018': self.conference_menu,
            # '2020': self.conference_menu,
        }


