"""OutcomeResults API Tests for Version 1.0.

This is a testing template for the generated OutcomeResultsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.outcome_results import OutcomeResultsAPI
from pycanvas.apis.outcome_results import Outcomeresult
from pycanvas.apis.outcome_results import Outcomerolluplinks
from pycanvas.apis.outcome_results import Outcomepathpart
from pycanvas.apis.outcome_results import Outcomerollupscorelinks
from pycanvas.apis.outcome_results import Outcomealignment
from pycanvas.apis.outcome_results import Outcomerollupscore
from pycanvas.apis.outcome_results import Outcomerollup
from pycanvas.apis.outcome_results import Outcomepath


class TestOutcomeResultsAPI(unittest.TestCase):
    """Tests for the OutcomeResultsAPI."""

    def setUp(self):
        self.client = OutcomeResultsAPI(secrets.instance_address, secrets.access_token)

    def test_get_outcome_results(self):
        """Integration test for the OutcomeResultsAPI.get_outcome_results method."""
        course_id = None  # Change me!!

        r = self.client.get_outcome_results(course_id, include=None, outcome_ids=None, user_ids=None)

    def test_get_outcome_result_rollups(self):
        """Integration test for the OutcomeResultsAPI.get_outcome_result_rollups method."""
        course_id = None  # Change me!!

        r = self.client.get_outcome_result_rollups(course_id, aggregate=None, include=None, outcome_ids=None, user_ids=None)

