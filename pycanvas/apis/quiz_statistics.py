"""QuizStatistics API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class QuizStatisticsAPI(BaseCanvasAPI):
    """QuizStatistics API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for QuizStatisticsAPI."""
        super(QuizStatisticsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.QuizStatisticsAPI")

    def fetching_latest_quiz_statistics(self, quiz_id, course_id, all_versions=None):
        """
        Fetching the latest quiz statistics.

        This endpoint provides statistics for all quiz versions, or for a specific
        quiz version, in which case the output is guaranteed to represent the
        _latest_ and most current version of the quiz.
        
        <b>200 OK</b> response code is returned if the request was successful.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id
        # REQUIRED - PATH - quiz_id
        """ID"""
        path["quiz_id"] = quiz_id
        # OPTIONAL - all_versions
        """Whether the statistics report should include all submissions attempts."""
        if all_versions is not None:
            params["all_versions"] = all_versions

        self.logger.debug("GET /api/v1/courses/{course_id}/quizzes/{quiz_id}/statistics with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/statistics".format(**path), data=data, params=params, no_data=True)


class Quizstatisticsquestionstatistics(BaseModel):
    """Quizstatisticsquestionstatistics Model.
    Statistics for submissions made to a specific quiz question."""

    def __init__(self, responses=None, answers=None):
        """Init method for Quizstatisticsquestionstatistics class."""
        self._responses = responses
        self._answers = answers

        self.logger = logging.getLogger('pycanvas.Quizstatisticsquestionstatistics')

    @property
    def responses(self):
        """Number of students who have provided an answer to this question. Blank or empty responses are not counted."""
        return self._responses

    @responses.setter
    def responses(self, value):
        """Setter for responses property."""
        self.logger.warn("Setting values on responses will NOT update the remote Canvas instance.")
        self._responses = value

    @property
    def answers(self):
        """Statistics related to each individual pre-defined answer."""
        return self._answers

    @answers.setter
    def answers(self, value):
        """Setter for answers property."""
        self.logger.warn("Setting values on answers will NOT update the remote Canvas instance.")
        self._answers = value


class Quizstatistics(BaseModel):
    """Quizstatistics Model."""

    def __init__(self, id, quiz_id, question_statistics=None, links=None, multiple_attempts_exist=None, url=None, html_url=None, submission_statistics=None, generated_at=None, includes_all_versions=None):
        """Init method for Quizstatistics class."""
        self._question_statistics = question_statistics
        self._links = links
        self._multiple_attempts_exist = multiple_attempts_exist
        self._url = url
        self._html_url = html_url
        self._submission_statistics = submission_statistics
        self._generated_at = generated_at
        self._quiz_id = quiz_id
        self._includes_all_versions = includes_all_versions
        self._id = id

        self.logger = logging.getLogger('pycanvas.Quizstatistics')

    @property
    def question_statistics(self):
        """Question-specific statistics for each question and its answers."""
        return self._question_statistics

    @question_statistics.setter
    def question_statistics(self, value):
        """Setter for question_statistics property."""
        self.logger.warn("Setting values on question_statistics will NOT update the remote Canvas instance.")
        self._question_statistics = value

    @property
    def links(self):
        """JSON-API construct that contains links to media related to this quiz statistics object. 
NOTE: AVAILABLE ONLY IN JSON-API REQUESTS."""
        return self._links

    @links.setter
    def links(self, value):
        """Setter for links property."""
        self.logger.warn("Setting values on links will NOT update the remote Canvas instance.")
        self._links = value

    @property
    def multiple_attempts_exist(self):
        """Whether there are any students that have made mutliple submissions for this quiz."""
        return self._multiple_attempts_exist

    @multiple_attempts_exist.setter
    def multiple_attempts_exist(self, value):
        """Setter for multiple_attempts_exist property."""
        self.logger.warn("Setting values on multiple_attempts_exist will NOT update the remote Canvas instance.")
        self._multiple_attempts_exist = value

    @property
    def url(self):
        """The API HTTP/HTTPS URL to this quiz statistics."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def html_url(self):
        """The HTTP/HTTPS URL to the page where the statistics can be seen visually."""
        return self._html_url

    @html_url.setter
    def html_url(self, value):
        """Setter for html_url property."""
        self.logger.warn("Setting values on html_url will NOT update the remote Canvas instance.")
        self._html_url = value

    @property
    def submission_statistics(self):
        """Question-specific statistics for each question and its answers."""
        return self._submission_statistics

    @submission_statistics.setter
    def submission_statistics(self, value):
        """Setter for submission_statistics property."""
        self.logger.warn("Setting values on submission_statistics will NOT update the remote Canvas instance.")
        self._submission_statistics = value

    @property
    def generated_at(self):
        """The time at which the statistics were generated, which is usually after the occurrence of a quiz event, like a student submitting it."""
        return self._generated_at

    @generated_at.setter
    def generated_at(self, value):
        """Setter for generated_at property."""
        self.logger.warn("Setting values on generated_at will NOT update the remote Canvas instance.")
        self._generated_at = value

    @property
    def quiz_id(self):
        """The ID of the Quiz the statistics report is for. 
NOTE: AVAILABLE ONLY IN NON-JSON-API REQUESTS."""
        return self._quiz_id

    @quiz_id.setter
    def quiz_id(self, value):
        """Setter for quiz_id property."""
        self.logger.warn("Setting values on quiz_id will NOT update the remote Canvas instance.")
        self._quiz_id = value

    @property
    def includes_all_versions(self):
        """In the presence of multiple attempts, this field describes whether the statistics describe all the submission attempts and not only the latest ones."""
        return self._includes_all_versions

    @includes_all_versions.setter
    def includes_all_versions(self, value):
        """Setter for includes_all_versions property."""
        self.logger.warn("Setting values on includes_all_versions will NOT update the remote Canvas instance.")
        self._includes_all_versions = value

    @property
    def id(self):
        """The ID of the quiz statistics report."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value


class Quizstatisticsanswerpointbiserial(BaseModel):
    """Quizstatisticsanswerpointbiserial Model.
    A point-biserial construct for a single pre-defined answer in a Multiple-Choice or True/False question."""

    def __init__(self, point_biserial=None, distractor=None, correct=None, answer_id=None):
        """Init method for Quizstatisticsanswerpointbiserial class."""
        self._point_biserial = point_biserial
        self._distractor = distractor
        self._correct = correct
        self._answer_id = answer_id

        self.logger = logging.getLogger('pycanvas.Quizstatisticsanswerpointbiserial')

    @property
    def point_biserial(self):
        """The point biserial value for this answer. Value ranges between -1 and 1."""
        return self._point_biserial

    @point_biserial.setter
    def point_biserial(self, value):
        """Setter for point_biserial property."""
        self.logger.warn("Setting values on point_biserial will NOT update the remote Canvas instance.")
        self._point_biserial = value

    @property
    def distractor(self):
        """Convenience attribute that denotes whether this is a distractor answer and not the correct one. This is mutually exclusive with the `correct` value."""
        return self._distractor

    @distractor.setter
    def distractor(self, value):
        """Setter for distractor property."""
        self.logger.warn("Setting values on distractor will NOT update the remote Canvas instance.")
        self._distractor = value

    @property
    def correct(self):
        """Convenience attribute that denotes whether this is the correct answer as opposed to being a distractor. This is mutually exclusive with the `distractor` value."""
        return self._correct

    @correct.setter
    def correct(self, value):
        """Setter for correct property."""
        self.logger.warn("Setting values on correct will NOT update the remote Canvas instance.")
        self._correct = value

    @property
    def answer_id(self):
        """ID of the answer the point biserial is for."""
        return self._answer_id

    @answer_id.setter
    def answer_id(self, value):
        """Setter for answer_id property."""
        self.logger.warn("Setting values on answer_id will NOT update the remote Canvas instance.")
        self._answer_id = value


class Quizstatisticsanswerstatistics(BaseModel):
    """Quizstatisticsanswerstatistics Model.
    Statistics for a specific pre-defined answer in a Multiple-Choice or True/False quiz question."""

    def __init__(self, text=None, id=None, weight=None, responses=None):
        """Init method for Quizstatisticsanswerstatistics class."""
        self._text = text
        self._id = id
        self._weight = weight
        self._responses = responses

        self.logger = logging.getLogger('pycanvas.Quizstatisticsanswerstatistics')

    @property
    def text(self):
        """The text attached to the answer."""
        return self._text

    @text.setter
    def text(self, value):
        """Setter for text property."""
        self.logger.warn("Setting values on text will NOT update the remote Canvas instance.")
        self._text = value

    @property
    def id(self):
        """ID of the answer."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def weight(self):
        """An integer to determine correctness of the answer. Incorrect answers should be 0, correct answers should be non-negative."""
        return self._weight

    @weight.setter
    def weight(self, value):
        """Setter for weight property."""
        self.logger.warn("Setting values on weight will NOT update the remote Canvas instance.")
        self._weight = value

    @property
    def responses(self):
        """Number of students who have chosen this answer."""
        return self._responses

    @responses.setter
    def responses(self, value):
        """Setter for responses property."""
        self.logger.warn("Setting values on responses will NOT update the remote Canvas instance.")
        self._responses = value


class Quizstatisticslinks(BaseModel):
    """Quizstatisticslinks Model.
    Links to media related to QuizStatistics."""

    def __init__(self, quiz=None):
        """Init method for Quizstatisticslinks class."""
        self._quiz = quiz

        self.logger = logging.getLogger('pycanvas.Quizstatisticslinks')

    @property
    def quiz(self):
        """HTTP/HTTPS API URL to the quiz this statistics describe."""
        return self._quiz

    @quiz.setter
    def quiz(self, value):
        """Setter for quiz property."""
        self.logger.warn("Setting values on quiz will NOT update the remote Canvas instance.")
        self._quiz = value


class Quizstatisticssubmissionstatistics(BaseModel):
    """Quizstatisticssubmissionstatistics Model.
    Generic statistics for all submissions for a quiz."""

    def __init__(self, duration_average=None, score_average=None, score_low=None, incorrect_count_average=None, unique_count=None, score_high=None, scores=None, correct_count_average=None, score_stdev=None):
        """Init method for Quizstatisticssubmissionstatistics class."""
        self._duration_average = duration_average
        self._score_average = score_average
        self._score_low = score_low
        self._incorrect_count_average = incorrect_count_average
        self._unique_count = unique_count
        self._score_high = score_high
        self._scores = scores
        self._correct_count_average = correct_count_average
        self._score_stdev = score_stdev

        self.logger = logging.getLogger('pycanvas.Quizstatisticssubmissionstatistics')

    @property
    def duration_average(self):
        """The average time spent by students while taking the quiz."""
        return self._duration_average

    @duration_average.setter
    def duration_average(self, value):
        """Setter for duration_average property."""
        self.logger.warn("Setting values on duration_average will NOT update the remote Canvas instance.")
        self._duration_average = value

    @property
    def score_average(self):
        """The mean of the student submission scores."""
        return self._score_average

    @score_average.setter
    def score_average(self, value):
        """Setter for score_average property."""
        self.logger.warn("Setting values on score_average will NOT update the remote Canvas instance.")
        self._score_average = value

    @property
    def score_low(self):
        """The lowest submission score."""
        return self._score_low

    @score_low.setter
    def score_low(self, value):
        """Setter for score_low property."""
        self.logger.warn("Setting values on score_low will NOT update the remote Canvas instance.")
        self._score_low = value

    @property
    def incorrect_count_average(self):
        """The mean of the number of questions answered incorrectly by each student."""
        return self._incorrect_count_average

    @incorrect_count_average.setter
    def incorrect_count_average(self, value):
        """Setter for incorrect_count_average property."""
        self.logger.warn("Setting values on incorrect_count_average will NOT update the remote Canvas instance.")
        self._incorrect_count_average = value

    @property
    def unique_count(self):
        """The number of students who have taken the quiz."""
        return self._unique_count

    @unique_count.setter
    def unique_count(self, value):
        """Setter for unique_count property."""
        self.logger.warn("Setting values on unique_count will NOT update the remote Canvas instance.")
        self._unique_count = value

    @property
    def score_high(self):
        """The highest submission score."""
        return self._score_high

    @score_high.setter
    def score_high(self, value):
        """Setter for score_high property."""
        self.logger.warn("Setting values on score_high will NOT update the remote Canvas instance.")
        self._score_high = value

    @property
    def scores(self):
        """A percentile distribution of the student scores, each key is the percentile (ranges between 0 and 100%) while the value is the number of students who received that score."""
        return self._scores

    @scores.setter
    def scores(self, value):
        """Setter for scores property."""
        self.logger.warn("Setting values on scores will NOT update the remote Canvas instance.")
        self._scores = value

    @property
    def correct_count_average(self):
        """The mean of the number of questions answered correctly by each student."""
        return self._correct_count_average

    @correct_count_average.setter
    def correct_count_average(self, value):
        """Setter for correct_count_average property."""
        self.logger.warn("Setting values on correct_count_average will NOT update the remote Canvas instance.")
        self._correct_count_average = value

    @property
    def score_stdev(self):
        """Standard deviation of the submission scores."""
        return self._score_stdev

    @score_stdev.setter
    def score_stdev(self, value):
        """Setter for score_stdev property."""
        self.logger.warn("Setting values on score_stdev will NOT update the remote Canvas instance.")
        self._score_stdev = value

