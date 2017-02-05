"""QuizQuestions API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class QuizQuestionsAPI(BaseCanvasAPI):
    """QuizQuestions API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for QuizQuestionsAPI."""
        super(QuizQuestionsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.QuizQuestionsAPI")

    def list_questions_in_quiz_or_submission(self, quiz_id, course_id, quiz_submission_attempt=None, quiz_submission_id=None):
        """
        List questions in a quiz or a submission.

        Returns the list of QuizQuestions in this quiz.
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
        # OPTIONAL - quiz_submission_id
        """If specified, the endpoint will return the questions that were presented
        for that submission. This is useful if the quiz has been modified after
        the submission was created and the latest quiz version's set of questions
        does not match the submission's.
        NOTE: you must specify quiz_submission_attempt as well if you specify this
        parameter."""
        if quiz_submission_id is not None:
            params["quiz_submission_id"] = quiz_submission_id
        # OPTIONAL - quiz_submission_attempt
        """The attempt of the submission you want the questions for."""
        if quiz_submission_attempt is not None:
            params["quiz_submission_attempt"] = quiz_submission_attempt

        self.logger.debug("GET /api/v1/courses/{course_id}/quizzes/{quiz_id}/questions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/questions".format(**path), data=data, params=params, all_pages=True)

    def get_single_quiz_question(self, id, quiz_id, course_id):
        """
        Get a single quiz question.

        Returns the quiz question with the given id
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
        # REQUIRED - PATH - id
        """The quiz question unique identifier."""
        path["id"] = id

        self.logger.debug("GET /api/v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id}".format(**path), data=data, params=params, single_item=True)

    def create_single_quiz_question(self, quiz_id, course_id, question_answers=None, question_correct_comments=None, question_incorrect_comments=None, question_neutral_comments=None, question_points_possible=None, question_position=None, question_question_name=None, question_question_text=None, question_question_type=None, question_quiz_group_id=None, question_text_after_answers=None):
        """
        Create a single quiz question.

        Create a new quiz question for this quiz
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
        # OPTIONAL - question[question_name]
        """The name of the question."""
        if question_question_name is not None:
            data["question[question_name]"] = question_question_name
        # OPTIONAL - question[question_text]
        """The text of the question."""
        if question_question_text is not None:
            data["question[question_text]"] = question_question_text
        # OPTIONAL - question[quiz_group_id]
        """The id of the quiz group to assign the question to."""
        if question_quiz_group_id is not None:
            data["question[quiz_group_id]"] = question_quiz_group_id
        # OPTIONAL - question[question_type]
        """The type of question. Multiple optional fields depend upon the type of question to be used."""
        if question_question_type is not None:
            self._validate_enum(question_question_type, ["calculated_question", "essay_question", "file_upload_question", "fill_in_multiple_blanks_question", "matching_question", "multiple_answers_question", "multiple_choice_question", "multiple_dropdowns_question", "numerical_question", "short_answer_question", "text_only_question", "true_false_question"])
            data["question[question_type]"] = question_question_type
        # OPTIONAL - question[position]
        """The order in which the question will be displayed in the quiz in relation to other questions."""
        if question_position is not None:
            data["question[position]"] = question_position
        # OPTIONAL - question[points_possible]
        """The maximum amount of points received for answering this question correctly."""
        if question_points_possible is not None:
            data["question[points_possible]"] = question_points_possible
        # OPTIONAL - question[correct_comments]
        """The comment to display if the student answers the question correctly."""
        if question_correct_comments is not None:
            data["question[correct_comments]"] = question_correct_comments
        # OPTIONAL - question[incorrect_comments]
        """The comment to display if the student answers incorrectly."""
        if question_incorrect_comments is not None:
            data["question[incorrect_comments]"] = question_incorrect_comments
        # OPTIONAL - question[neutral_comments]
        """The comment to display regardless of how the student answered."""
        if question_neutral_comments is not None:
            data["question[neutral_comments]"] = question_neutral_comments
        # OPTIONAL - question[text_after_answers]
        """no description"""
        if question_text_after_answers is not None:
            data["question[text_after_answers]"] = question_text_after_answers
        # OPTIONAL - question[answers]
        """no description"""
        if question_answers is not None:
            data["question[answers]"] = question_answers

        self.logger.debug("POST /api/v1/courses/{course_id}/quizzes/{quiz_id}/questions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/questions".format(**path), data=data, params=params, single_item=True)

    def update_existing_quiz_question(self, id, quiz_id, course_id, question_answers=None, question_correct_comments=None, question_incorrect_comments=None, question_neutral_comments=None, question_points_possible=None, question_position=None, question_question_name=None, question_question_text=None, question_question_type=None, question_quiz_group_id=None, question_text_after_answers=None):
        """
        Update an existing quiz question.

        Updates an existing quiz question for this quiz
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id
        # REQUIRED - PATH - quiz_id
        """The associated quiz's unique identifier."""
        path["quiz_id"] = quiz_id
        # REQUIRED - PATH - id
        """The quiz question's unique identifier."""
        path["id"] = id
        # OPTIONAL - question[question_name]
        """The name of the question."""
        if question_question_name is not None:
            data["question[question_name]"] = question_question_name
        # OPTIONAL - question[question_text]
        """The text of the question."""
        if question_question_text is not None:
            data["question[question_text]"] = question_question_text
        # OPTIONAL - question[quiz_group_id]
        """The id of the quiz group to assign the question to."""
        if question_quiz_group_id is not None:
            data["question[quiz_group_id]"] = question_quiz_group_id
        # OPTIONAL - question[question_type]
        """The type of question. Multiple optional fields depend upon the type of question to be used."""
        if question_question_type is not None:
            self._validate_enum(question_question_type, ["calculated_question", "essay_question", "file_upload_question", "fill_in_multiple_blanks_question", "matching_question", "multiple_answers_question", "multiple_choice_question", "multiple_dropdowns_question", "numerical_question", "short_answer_question", "text_only_question", "true_false_question"])
            data["question[question_type]"] = question_question_type
        # OPTIONAL - question[position]
        """The order in which the question will be displayed in the quiz in relation to other questions."""
        if question_position is not None:
            data["question[position]"] = question_position
        # OPTIONAL - question[points_possible]
        """The maximum amount of points received for answering this question correctly."""
        if question_points_possible is not None:
            data["question[points_possible]"] = question_points_possible
        # OPTIONAL - question[correct_comments]
        """The comment to display if the student answers the question correctly."""
        if question_correct_comments is not None:
            data["question[correct_comments]"] = question_correct_comments
        # OPTIONAL - question[incorrect_comments]
        """The comment to display if the student answers incorrectly."""
        if question_incorrect_comments is not None:
            data["question[incorrect_comments]"] = question_incorrect_comments
        # OPTIONAL - question[neutral_comments]
        """The comment to display regardless of how the student answered."""
        if question_neutral_comments is not None:
            data["question[neutral_comments]"] = question_neutral_comments
        # OPTIONAL - question[text_after_answers]
        """no description"""
        if question_text_after_answers is not None:
            data["question[text_after_answers]"] = question_text_after_answers
        # OPTIONAL - question[answers]
        """no description"""
        if question_answers is not None:
            data["question[answers]"] = question_answers

        self.logger.debug("PUT /api/v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id}".format(**path), data=data, params=params, single_item=True)

    def delete_quiz_question(self, id, quiz_id, course_id):
        """
        Delete a quiz question.

        <b>204 No Content</b> response code is returned if the deletion was successful.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id
        # REQUIRED - PATH - quiz_id
        """The associated quiz's unique identifier"""
        path["quiz_id"] = quiz_id
        # REQUIRED - PATH - id
        """The quiz question's unique identifier"""
        path["id"] = id

        self.logger.debug("DELETE /api/v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id}".format(**path), data=data, params=params, no_data=True)


class Answer(BaseModel):
    """Answer Model."""

    def __init__(self, answer_text, answer_weight, text_after_answers=None, answer_match_left=None, answer_comments=None, margin=None, matching_answer_incorrect_matches=None, approximate=None, start=None, answer_match_right=None, precision=None, numerical_answer_type=None, end=None, blank_id=None, exact=None, id=None):
        """Init method for Answer class."""
        self._text_after_answers = text_after_answers
        self._answer_match_left = answer_match_left
        self._answer_comments = answer_comments
        self._margin = margin
        self._matching_answer_incorrect_matches = matching_answer_incorrect_matches
        self._approximate = approximate
        self._start = start
        self._answer_text = answer_text
        self._answer_weight = answer_weight
        self._answer_match_right = answer_match_right
        self._precision = precision
        self._numerical_answer_type = numerical_answer_type
        self._end = end
        self._blank_id = blank_id
        self._exact = exact
        self._id = id

        self.logger = logging.getLogger('pycanvas.Answer')

    @property
    def text_after_answers(self):
        """Used in missing word questions.  The text to follow the missing word."""
        return self._text_after_answers

    @text_after_answers.setter
    def text_after_answers(self, value):
        """Setter for text_after_answers property."""
        self.logger.warn("Setting values on text_after_answers will NOT update the remote Canvas instance.")
        self._text_after_answers = value

    @property
    def answer_match_left(self):
        """Used in matching questions.  The static value of the answer that will be displayed on the left for students to match for."""
        return self._answer_match_left

    @answer_match_left.setter
    def answer_match_left(self, value):
        """Setter for answer_match_left property."""
        self.logger.warn("Setting values on answer_match_left will NOT update the remote Canvas instance.")
        self._answer_match_left = value

    @property
    def answer_comments(self):
        """Specific contextual comments for a particular answer."""
        return self._answer_comments

    @answer_comments.setter
    def answer_comments(self, value):
        """Setter for answer_comments property."""
        self.logger.warn("Setting values on answer_comments will NOT update the remote Canvas instance.")
        self._answer_comments = value

    @property
    def margin(self):
        """Used in numerical questions of type 'exact_answer'. The margin of error allowed for the student's answer."""
        return self._margin

    @margin.setter
    def margin(self, value):
        """Setter for margin property."""
        self.logger.warn("Setting values on margin will NOT update the remote Canvas instance.")
        self._margin = value

    @property
    def matching_answer_incorrect_matches(self):
        """Used in matching questions. A list of distractors, delimited by new lines (
) that will be seeded with all the answer_match_right values."""
        return self._matching_answer_incorrect_matches

    @matching_answer_incorrect_matches.setter
    def matching_answer_incorrect_matches(self, value):
        """Setter for matching_answer_incorrect_matches property."""
        self.logger.warn("Setting values on matching_answer_incorrect_matches will NOT update the remote Canvas instance.")
        self._matching_answer_incorrect_matches = value

    @property
    def approximate(self):
        """Used in numerical questions of type 'precision_answer'.  The value the answer should equal."""
        return self._approximate

    @approximate.setter
    def approximate(self, value):
        """Setter for approximate property."""
        self.logger.warn("Setting values on approximate will NOT update the remote Canvas instance.")
        self._approximate = value

    @property
    def start(self):
        """Used in numerical questions of type 'range_answer'. The start of the allowed range (inclusive)."""
        return self._start

    @start.setter
    def start(self, value):
        """Setter for start property."""
        self.logger.warn("Setting values on start will NOT update the remote Canvas instance.")
        self._start = value

    @property
    def answer_text(self):
        """The text of the answer."""
        return self._answer_text

    @answer_text.setter
    def answer_text(self, value):
        """Setter for answer_text property."""
        self.logger.warn("Setting values on answer_text will NOT update the remote Canvas instance.")
        self._answer_text = value

    @property
    def answer_weight(self):
        """An integer to determine correctness of the answer. Incorrect answers should be 0, correct answers should be non-negative."""
        return self._answer_weight

    @answer_weight.setter
    def answer_weight(self, value):
        """Setter for answer_weight property."""
        self.logger.warn("Setting values on answer_weight will NOT update the remote Canvas instance.")
        self._answer_weight = value

    @property
    def answer_match_right(self):
        """Used in matching questions. The correct match for the value given in answer_match_left.  Will be displayed in a dropdown with the other answer_match_right values.."""
        return self._answer_match_right

    @answer_match_right.setter
    def answer_match_right(self, value):
        """Setter for answer_match_right property."""
        self.logger.warn("Setting values on answer_match_right will NOT update the remote Canvas instance.")
        self._answer_match_right = value

    @property
    def precision(self):
        """Used in numerical questions of type 'precision_answer'. The numerical precision that will be used when comparing the student's answer."""
        return self._precision

    @precision.setter
    def precision(self, value):
        """Setter for precision property."""
        self.logger.warn("Setting values on precision will NOT update the remote Canvas instance.")
        self._precision = value

    @property
    def numerical_answer_type(self):
        """Used in numerical questions.  Values can be 'exact_answer', 'range_answer', or 'precision_answer'."""
        return self._numerical_answer_type

    @numerical_answer_type.setter
    def numerical_answer_type(self, value):
        """Setter for numerical_answer_type property."""
        self.logger.warn("Setting values on numerical_answer_type will NOT update the remote Canvas instance.")
        self._numerical_answer_type = value

    @property
    def end(self):
        """Used in numerical questions of type 'range_answer'. The end of the allowed range (inclusive)."""
        return self._end

    @end.setter
    def end(self, value):
        """Setter for end property."""
        self.logger.warn("Setting values on end will NOT update the remote Canvas instance.")
        self._end = value

    @property
    def blank_id(self):
        """Used in fill in multiple blank and multiple dropdowns questions."""
        return self._blank_id

    @blank_id.setter
    def blank_id(self, value):
        """Setter for blank_id property."""
        self.logger.warn("Setting values on blank_id will NOT update the remote Canvas instance.")
        self._blank_id = value

    @property
    def exact(self):
        """Used in numerical questions of type 'exact_answer'.  The value the answer should equal."""
        return self._exact

    @exact.setter
    def exact(self, value):
        """Setter for exact property."""
        self.logger.warn("Setting values on exact will NOT update the remote Canvas instance.")
        self._exact = value

    @property
    def id(self):
        """The unique identifier for the answer.  Do not supply if this answer is part of a new question."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value


class Quizquestion(BaseModel):
    """Quizquestion Model."""

    def __init__(self, id, quiz_id, question_text=None, neutral_comments=None, points_possible=None, question_name=None, answers=None, question_type=None, correct_comments=None, incorrect_comments=None, position=None):
        """Init method for Quizquestion class."""
        self._question_text = question_text
        self._neutral_comments = neutral_comments
        self._points_possible = points_possible
        self._question_name = question_name
        self._answers = answers
        self._question_type = question_type
        self._correct_comments = correct_comments
        self._incorrect_comments = incorrect_comments
        self._position = position
        self._quiz_id = quiz_id
        self._id = id

        self.logger = logging.getLogger('pycanvas.Quizquestion')

    @property
    def question_text(self):
        """The text of the question."""
        return self._question_text

    @question_text.setter
    def question_text(self, value):
        """Setter for question_text property."""
        self.logger.warn("Setting values on question_text will NOT update the remote Canvas instance.")
        self._question_text = value

    @property
    def neutral_comments(self):
        """The comments to display regardless of how the student answered."""
        return self._neutral_comments

    @neutral_comments.setter
    def neutral_comments(self, value):
        """Setter for neutral_comments property."""
        self.logger.warn("Setting values on neutral_comments will NOT update the remote Canvas instance.")
        self._neutral_comments = value

    @property
    def points_possible(self):
        """The maximum amount of points possible received for getting this question correct."""
        return self._points_possible

    @points_possible.setter
    def points_possible(self, value):
        """Setter for points_possible property."""
        self.logger.warn("Setting values on points_possible will NOT update the remote Canvas instance.")
        self._points_possible = value

    @property
    def question_name(self):
        """The name of the question."""
        return self._question_name

    @question_name.setter
    def question_name(self, value):
        """Setter for question_name property."""
        self.logger.warn("Setting values on question_name will NOT update the remote Canvas instance.")
        self._question_name = value

    @property
    def answers(self):
        """An array of available answers to display to the student."""
        return self._answers

    @answers.setter
    def answers(self, value):
        """Setter for answers property."""
        self.logger.warn("Setting values on answers will NOT update the remote Canvas instance.")
        self._answers = value

    @property
    def question_type(self):
        """The type of the question."""
        return self._question_type

    @question_type.setter
    def question_type(self, value):
        """Setter for question_type property."""
        self.logger.warn("Setting values on question_type will NOT update the remote Canvas instance.")
        self._question_type = value

    @property
    def correct_comments(self):
        """The comments to display if the student answers the question correctly."""
        return self._correct_comments

    @correct_comments.setter
    def correct_comments(self, value):
        """Setter for correct_comments property."""
        self.logger.warn("Setting values on correct_comments will NOT update the remote Canvas instance.")
        self._correct_comments = value

    @property
    def incorrect_comments(self):
        """The comments to display if the student answers incorrectly."""
        return self._incorrect_comments

    @incorrect_comments.setter
    def incorrect_comments(self, value):
        """Setter for incorrect_comments property."""
        self.logger.warn("Setting values on incorrect_comments will NOT update the remote Canvas instance.")
        self._incorrect_comments = value

    @property
    def position(self):
        """The order in which the question will be retrieved and displayed."""
        return self._position

    @position.setter
    def position(self, value):
        """Setter for position property."""
        self.logger.warn("Setting values on position will NOT update the remote Canvas instance.")
        self._position = value

    @property
    def quiz_id(self):
        """The ID of the Quiz the question belongs to."""
        return self._quiz_id

    @quiz_id.setter
    def quiz_id(self, value):
        """Setter for quiz_id property."""
        self.logger.warn("Setting values on quiz_id will NOT update the remote Canvas instance.")
        self._quiz_id = value

    @property
    def id(self):
        """The ID of the quiz question."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

