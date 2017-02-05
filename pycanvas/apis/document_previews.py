"""DocumentPreviews API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI



class DocumentPreviewsAPI(BaseCanvasAPI):
    """DocumentPreviews API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for DocumentPreviewsAPI."""
        super(DocumentPreviewsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.DocumentPreviewsAPI")

