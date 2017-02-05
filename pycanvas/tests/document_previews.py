"""DocumentPreviews API Tests for Version 1.0.

This is a testing template for the generated DocumentPreviewsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.document_previews import DocumentPreviewsAPI


class TestDocumentPreviewsAPI(unittest.TestCase):
    """Tests for the DocumentPreviewsAPI."""

    def setUp(self):
        self.client = DocumentPreviewsAPI(secrets.instance_address, secrets.access_token)

