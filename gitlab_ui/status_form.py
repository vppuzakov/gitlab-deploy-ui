from typing import List

from npyscreen import FormMultiPage

from gitlab_ui.color_grid import ColorGrid
from gitlab_ui.deployment_service import DeploymentService


class StatusForm(FormMultiPage):

    def __init__(self, deployments: DeploymentService, projects: List[int], *args, **keywords) -> None:
        self._deployments = deployments
        self._projects = projects
        super().__init__(*args, **keywords)

    def create(self):
        gd = self.add(ColorGrid)
        for project_id in self._projects:
            deployments = self._deployments.get_project_deployments(project_id)
            deployments_map = {deployment['env']: deployment for deployment in deployments}

            gd.values = []
            for x in range(1):
                row = [deployments_map.get('dev')]
                gd.values.append(row)
