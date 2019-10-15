import random

from npyscreen import Form, TitleText

from gitlab_ui.color_grid import ColorGrid


class StatusForm(Form):

    def __init__(self, *args, **keywords) -> None:
        super().__init__(*args, **keywords)

    def create(self):
        gd = self.add(ColorGrid)

        gd.values = []
        for x in range(3):
            row = []
            for y in range(4):
                if bool(random.getrandbits(1)):
                    row.append("PASS")
                else:
                    row.append("FAIL")
            gd.values.append(row)
