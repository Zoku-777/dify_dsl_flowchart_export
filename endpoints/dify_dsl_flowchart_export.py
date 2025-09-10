import json
import logging
from typing import Any, Mapping

import requests
import yaml
from dify_plugin import Endpoint
from dify_plugin.plugin import plugin_logger_handler
from markdown import markdown
from werkzeug import Request, Response

from const import HTML_TEMPLATE
from dify_dsl_convertor import DifyDSLConvertor

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(plugin_logger_handler)


class DifyDslFlowchartExportEndpoint(Endpoint):
    def _invoke(self, r: Request, values: Mapping, settings: Mapping) -> Response:
        """
        Invokes the endpoint with the given request.
        """

        host = settings.get("dify_console_api_domain")
        if not host:
            host = "localhost"
        app_id = settings.get("app").get("app_id")
        access_token = settings.get("dify_access_token")
        flowchat_direction = settings.get("flowchart_direction")
        language_setting = r.cookies.get("locale")
        if not language_setting:
            language_setting = "en_US"

        try:
            logger.info(
                f"AppInfoInput: host={host}, app_id={app_id}, language_setting={language_setting}"
            )
            dsl_data = self.__get_app_dsl_data(host, app_id, access_token)
        except DifyAppDslExportError:
            logger.error(f"Dify App DSL Export faild")
            return Response(
                "Dify App DSL Export Error", status=500, content_type="text/html"
            )

        flowchart_str = DifyDSLConvertor.convert_dsl(
            dsl_data, flowchat_direction, language_setting
        )

        mardown_str = f"""
```txt
{flowchart_str}
```
"""

        html_content = markdown(mardown_str, extensions=["fenced_code"])

        html_template = HTML_TEMPLATE.format(
            flowchart_str=flowchart_str, html_content=html_content
        )

        return Response(html_template, status=200, content_type="text/html")

    def __get_app_dsl_data(
        self, host: str, app_id: str, accsess_token: str
    ) -> dict[str, Any]:
        url = f"http://{host}/console/api/apps/{app_id}/export"
        headers = {"Authorization": "Bearer {}".format(accsess_token)}
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            dsl_data = yaml.safe_load(json.loads(response.text)["data"])
            print("App DSL exported successfully")
            return dsl_data
        else:
            print(
                f"App DSL export API error: {response.status_code} - {response.reason}"
            )
        raise DifyAppDslExportError("App DSL export failed")


class DifyAppDslExportError(Exception):
    pass
