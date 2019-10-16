from npyscreen import NPSAppManaged, setTheme
from npyscreen.npysThemes import ElegantTheme

from gitlab_ui.status_form import StatusForm


class GitlabApp(NPSAppManaged):

    def onStart(self):
        setTheme(ElegantTheme)

        self.registerForm("MAIN", StatusForm(name='DEV'))
