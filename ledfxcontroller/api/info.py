from ledfxcontroller.api import RestEndpoint
from aiohttp import web
import logging
import json
from ledfxcontroller.consts import PROJECT_VERSION

_LOGGER = logging.getLogger(__name__)

class InfoEndpoint(RestEndpoint):

    ENDPOINT_PATH = "/api/info"

    async def get(self) -> web.Response:
        response = {
            'url': 'http://placeholder',
            'name': 'LedFx (Placeholder)',
            'version': PROJECT_VERSION
        }

        return web.Response(text=json.dumps(response), status=200)
