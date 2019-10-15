from npyscreen import NPSAppManaged

from gitlab_ui.status_form import StatusForm


class GitlabApp(NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", StatusForm(name='DEV'))
