import http
import logging

from typing import List, Any

import http3


class DeploymentService:

    def __init__(self, host: str, token: str) -> None:
        self._token = token
        self._host = host

    def get_project_deployments(self, project_id: int) -> List[Any]:
        response = http3.get(f'https://{self._host}/api/v1/projects/{project_id}/deployments/')
        if response.status_code != http.HTTPStatus.OK:
            logging.warning("Can't connect to gitlab host: %s", self._host)

        deployments = response.json()
        return deployments
