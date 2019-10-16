import os

from npyscreen import NPSAppManaged, setTheme
from npyscreen.npysThemes import ElegantTheme

from gitlab_ui.deployment_service import DeploymentService
from gitlab_ui.status_form import StatusForm


class GitlabApp(NPSAppManaged):

    def onStart(self):
        setTheme(ElegantTheme)

        host = os.environ.get('GITLAB_HOST', 'gitlab.com')
        token = os.environ.get('GITLAB_TOKEN')
        deployment_service = DeploymentService(host=host, token=token)
        self.registerForm("MAIN", StatusForm(name='DEV', deployments=deployment_service))
