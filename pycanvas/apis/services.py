"""Services API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI



class ServicesAPI(BaseCanvasAPI):
    """Services API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for ServicesAPI."""
        super(ServicesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.ServicesAPI")

    def get_kaltura_config(self):
        """
        Get Kaltura config.

        Return the config information for the Kaltura plugin in json format.
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("GET /api/v1/services/kaltura with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/services/kaltura".format(**path), data=data, params=params, no_data=True)

    def start_kaltura_session(self):
        """
        Start Kaltura session.

        Start a new Kaltura session, so that new media can be recorded and uploaded
        to this Canvas instance's Kaltura instance.
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("POST /api/v1/services/kaltura_session with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/services/kaltura_session".format(**path), data=data, params=params, no_data=True)

