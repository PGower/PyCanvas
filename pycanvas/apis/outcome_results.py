"""OutcomeResults API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class OutcomeResultsAPI(BaseCanvasAPI):
    """OutcomeResults API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for OutcomeResultsAPI."""
        super(OutcomeResultsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.OutcomeResultsAPI")

    def get_outcome_results(self, course_id, include=None, outcome_ids=None, user_ids=None):
        """
        Get outcome results.

        Gets the outcome results for users and outcomes in the specified context.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # OPTIONAL - user_ids
        """If specified, only the users whose ids are given will be included in the
        results. SIS ids can be used, prefixed by "sis_user_id:".
        It is an error to specify an id for a user who is not a student in
        the context."""
        if user_ids is not None:
            params["user_ids"] = user_ids

        # OPTIONAL - outcome_ids
        """If specified, only the outcomes whose ids are given will be included in the
        results. it is an error to specify an id for an outcome which is not linked
        to the context."""
        if outcome_ids is not None:
            params["outcome_ids"] = outcome_ids

        # OPTIONAL - include
        """[String, "alignments"|"outcomes"|"outcomes.alignments"|"outcome_groups"|"outcome_links"|"outcome_paths"|"users"]
        Specify additional collections to be side loaded with the result.
        "alignments" includes only the alignments referenced by the returned
        results.
        "outcomes.alignments" includes all alignments referenced by outcomes in the
        context."""
        if include is not None:
            params["include"] = include

        self.logger.debug("GET /api/v1/courses/{course_id}/outcome_results with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/outcome_results".format(**path), data=data, params=params, no_data=True)

    def get_outcome_result_rollups(self, course_id, aggregate=None, include=None, outcome_ids=None, user_ids=None):
        """
        Get outcome result rollups.

        Gets the outcome rollups for the users and outcomes in the specified
        context.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # OPTIONAL - aggregate
        """If specified, instead of returning one rollup for each user, all the user
        rollups will be combined into one rollup for the course that will contain
        the average rollup score for each outcome."""
        if aggregate is not None:
            self._validate_enum(aggregate, ["course"])
            params["aggregate"] = aggregate

        # OPTIONAL - user_ids
        """If specified, only the users whose ids are given will be included in the
        results or used in an aggregate result. it is an error to specify an id
        for a user who is not a student in the context"""
        if user_ids is not None:
            params["user_ids"] = user_ids

        # OPTIONAL - outcome_ids
        """If specified, only the outcomes whose ids are given will be included in the
        results. it is an error to specify an id for an outcome which is not linked
        to the context."""
        if outcome_ids is not None:
            params["outcome_ids"] = outcome_ids

        # OPTIONAL - include
        """[String, "courses"|"outcomes"|"outcomes.alignments"|"outcome_groups"|"outcome_links"|"outcome_paths"|"users"]
        Specify additional collections to be side loaded with the result."""
        if include is not None:
            params["include"] = include

        self.logger.debug("GET /api/v1/courses/{course_id}/outcome_rollups with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/outcome_rollups".format(**path), data=data, params=params, no_data=True)


class Outcomeresult(BaseModel):
    """Outcomeresult Model.
    A student's result for an outcome"""

    def __init__(self, score=None, percent=None, id=None, links=None, submitted_or_assessed_at=None):
        """Init method for Outcomeresult class."""
        self._score = score
        self._percent = percent
        self._id = id
        self._links = links
        self._submitted_or_assessed_at = submitted_or_assessed_at

        self.logger = logging.getLogger('pycanvas.Outcomeresult')

    @property
    def score(self):
        """The student's score."""
        return self._score

    @score.setter
    def score(self, value):
        """Setter for score property."""
        self.logger.warn("Setting values on score will NOT update the remote Canvas instance.")
        self._score = value

    @property
    def percent(self):
        """score's percent of maximum points possible for outcome, scaled to reflect any custom mastery levels that differ from the learning outcome."""
        return self._percent

    @percent.setter
    def percent(self, value):
        """Setter for percent property."""
        self.logger.warn("Setting values on percent will NOT update the remote Canvas instance.")
        self._percent = value

    @property
    def id(self):
        """A unique identifier for this result."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def links(self):
        """Unique identifiers of objects associated with this result."""
        return self._links

    @links.setter
    def links(self, value):
        """Setter for links property."""
        self.logger.warn("Setting values on links will NOT update the remote Canvas instance.")
        self._links = value

    @property
    def submitted_or_assessed_at(self):
        """The datetime the resulting OutcomeResult was submitted at, or absent that, when it was assessed."""
        return self._submitted_or_assessed_at

    @submitted_or_assessed_at.setter
    def submitted_or_assessed_at(self, value):
        """Setter for submitted_or_assessed_at property."""
        self.logger.warn("Setting values on submitted_or_assessed_at will NOT update the remote Canvas instance.")
        self._submitted_or_assessed_at = value


class Outcomerolluplinks(BaseModel):
    """Outcomerolluplinks Model."""

    def __init__(self, course=None, section=None, user=None):
        """Init method for Outcomerolluplinks class."""
        self._course = course
        self._section = section
        self._user = user

        self.logger = logging.getLogger('pycanvas.Outcomerolluplinks')

    @property
    def course(self):
        """If an aggregate result was requested, the course field will be present. Otherwise, the user and section field will be present (Optional) The id of the course that this rollup applies to."""
        return self._course

    @course.setter
    def course(self, value):
        """Setter for course property."""
        self.logger.warn("Setting values on course will NOT update the remote Canvas instance.")
        self._course = value

    @property
    def section(self):
        """(Optional) The id of the section the user is in."""
        return self._section

    @section.setter
    def section(self, value):
        """Setter for section property."""
        self.logger.warn("Setting values on section will NOT update the remote Canvas instance.")
        self._section = value

    @property
    def user(self):
        """(Optional) The id of the user that this rollup applies to."""
        return self._user

    @user.setter
    def user(self, value):
        """Setter for user property."""
        self.logger.warn("Setting values on user will NOT update the remote Canvas instance.")
        self._user = value


class Outcomepathpart(BaseModel):
    """Outcomepathpart Model.
    An outcome or outcome group"""

    def __init__(self, name=None):
        """Init method for Outcomepathpart class."""
        self._name = name

        self.logger = logging.getLogger('pycanvas.Outcomepathpart')

    @property
    def name(self):
        """The title of the outcome or outcome group."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value


class Outcomerollupscorelinks(BaseModel):
    """Outcomerollupscorelinks Model."""

    def __init__(self, outcome=None):
        """Init method for Outcomerollupscorelinks class."""
        self._outcome = outcome

        self.logger = logging.getLogger('pycanvas.Outcomerollupscorelinks')

    @property
    def outcome(self):
        """The id of the related outcome."""
        return self._outcome

    @outcome.setter
    def outcome(self, value):
        """Setter for outcome property."""
        self.logger.warn("Setting values on outcome will NOT update the remote Canvas instance.")
        self._outcome = value


class Outcomealignment(BaseModel):
    """Outcomealignment Model.
    An asset aligned with this outcome"""

    def __init__(self, id=None, html_url=None, name=None):
        """Init method for Outcomealignment class."""
        self._id = id
        self._html_url = html_url
        self._name = name

        self.logger = logging.getLogger('pycanvas.Outcomealignment')

    @property
    def id(self):
        """A unique identifier for this alignment."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def html_url(self):
        """(Optional) A URL for details about this alignment."""
        return self._html_url

    @html_url.setter
    def html_url(self, value):
        """Setter for html_url property."""
        self.logger.warn("Setting values on html_url will NOT update the remote Canvas instance.")
        self._html_url = value

    @property
    def name(self):
        """The name of this alignment."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value


class Outcomerollupscore(BaseModel):
    """Outcomerollupscore Model."""

    def __init__(self, count=None, score=None, links=None):
        """Init method for Outcomerollupscore class."""
        self._count = count
        self._score = score
        self._links = links

        self.logger = logging.getLogger('pycanvas.Outcomerollupscore')

    @property
    def count(self):
        """The number of alignment scores included in this rollup."""
        return self._count

    @count.setter
    def count(self, value):
        """Setter for count property."""
        self.logger.warn("Setting values on count will NOT update the remote Canvas instance.")
        self._count = value

    @property
    def score(self):
        """The rollup score for the outcome, based on the student alignment scores related to the outcome. This could be null if the student has no related scores."""
        return self._score

    @score.setter
    def score(self, value):
        """Setter for score property."""
        self.logger.warn("Setting values on score will NOT update the remote Canvas instance.")
        self._score = value

    @property
    def links(self):
        """links."""
        return self._links

    @links.setter
    def links(self, value):
        """Setter for links property."""
        self.logger.warn("Setting values on links will NOT update the remote Canvas instance.")
        self._links = value


class Outcomerollup(BaseModel):
    """Outcomerollup Model."""

    def __init__(self, name=None, links=None, scores=None):
        """Init method for Outcomerollup class."""
        self._name = name
        self._links = links
        self._scores = scores

        self.logger = logging.getLogger('pycanvas.Outcomerollup')

    @property
    def name(self):
        """The name of the resource for this rollup. For example, the user name."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def links(self):
        """links."""
        return self._links

    @links.setter
    def links(self, value):
        """Setter for links property."""
        self.logger.warn("Setting values on links will NOT update the remote Canvas instance.")
        self._links = value

    @property
    def scores(self):
        """an array of OutcomeRollupScore objects."""
        return self._scores

    @scores.setter
    def scores(self, value):
        """Setter for scores property."""
        self.logger.warn("Setting values on scores will NOT update the remote Canvas instance.")
        self._scores = value


class Outcomepath(BaseModel):
    """Outcomepath Model.
    The full path to an outcome"""

    def __init__(self, parts=None, id=None):
        """Init method for Outcomepath class."""
        self._parts = parts
        self._id = id

        self.logger = logging.getLogger('pycanvas.Outcomepath')

    @property
    def parts(self):
        """an array of OutcomePathPart objects."""
        return self._parts

    @parts.setter
    def parts(self, value):
        """Setter for parts property."""
        self.logger.warn("Setting values on parts will NOT update the remote Canvas instance.")
        self._parts = value

    @property
    def id(self):
        """A unique identifier for this outcome."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

