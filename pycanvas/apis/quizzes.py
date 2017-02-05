"""Quizzes API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class QuizzesAPI(BaseCanvasAPI):
    """Quizzes API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for QuizzesAPI."""
        super(QuizzesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.QuizzesAPI")

    def list_quizzes_in_course(self, course_id, search_term=None):
        """
        List quizzes in a course.

        Returns the list of Quizzes in this course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # OPTIONAL - search_term - The partial title of the quizzes to match and return.
        if search_term is not None:
            params["search_term"] = search_term

        self.logger.debug("GET /api/v1/courses/{course_id}/quizzes with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/quizzes".format(**path), data=data, params=params, all_pages=True)

    def get_single_quiz(self, id, course_id):
        """
        Get a single quiz.

        Returns the quiz with the given id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("GET /api/v1/courses/{course_id}/quizzes/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/quizzes/{id}".format(**path), data=data, params=params, single_item=True)

    def create_quiz(self, course_id, quiz_title, quiz_access_code=None, quiz_allowed_attempts=None, quiz_assignment_group_id=None, quiz_cant_go_back=None, quiz_description=None, quiz_due_at=None, quiz_hide_correct_answers_at=None, quiz_hide_results=None, quiz_ip_filter=None, quiz_lock_at=None, quiz_one_question_at_a_time=None, quiz_one_time_results=None, quiz_published=None, quiz_quiz_type=None, quiz_scoring_policy=None, quiz_show_correct_answers=None, quiz_show_correct_answers_at=None, quiz_show_correct_answers_last_attempt=None, quiz_shuffle_answers=None, quiz_time_limit=None, quiz_unlock_at=None):
        """
        Create a quiz.

        Create a new quiz for this course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - quiz[title] - The quiz title.
        data["quiz[title]"] = quiz_title
        # OPTIONAL - quiz[description] - A description of the quiz.
        if quiz_description is not None:
            data["quiz[description]"] = quiz_description
        # OPTIONAL - quiz[quiz_type] - The type of quiz.
        if quiz_quiz_type is not None:
            self._validate_enum(quiz_quiz_type, ["practice_quiz", "assignment", "graded_survey", "survey"])
            data["quiz[quiz_type]"] = quiz_quiz_type
        # OPTIONAL - quiz[assignment_group_id] - The assignment group id to put the assignment in. Defaults to the top assignment group in the course. Only valid if the quiz is graded, i.e. if quiz_type is "assignment" or "graded_survey".
        if quiz_assignment_group_id is not None:
            data["quiz[assignment_group_id]"] = quiz_assignment_group_id
        # OPTIONAL - quiz[time_limit] - Time limit to take this quiz, in minutes. Set to null for no time limit. Defaults to null.
        if quiz_time_limit is not None:
            data["quiz[time_limit]"] = quiz_time_limit
        # OPTIONAL - quiz[shuffle_answers] - If true, quiz answers for multiple choice questions will be randomized for each student. Defaults to false.
        if quiz_shuffle_answers is not None:
            data["quiz[shuffle_answers]"] = quiz_shuffle_answers
        # OPTIONAL - quiz[hide_results] - Dictates whether or not quiz results are hidden from students. If null, students can see their results after any attempt. If "always", students can never see their results. If "until_after_last_attempt", students can only see results after their last attempt. (Only valid if allowed_attempts > 1). Defaults to null.
        if quiz_hide_results is not None:
            self._validate_enum(quiz_hide_results, ["always", "until_after_last_attempt"])
            data["quiz[hide_results]"] = quiz_hide_results
        # OPTIONAL - quiz[show_correct_answers] - Only valid if hide_results=null If false, hides correct answers from students when quiz results are viewed. Defaults to true.
        if quiz_show_correct_answers is not None:
            data["quiz[show_correct_answers]"] = quiz_show_correct_answers
        # OPTIONAL - quiz[show_correct_answers_last_attempt] - Only valid if show_correct_answers=true and allowed_attempts > 1 If true, hides correct answers from students when quiz results are viewed until they submit the last attempt for the quiz. Defaults to false.
        if quiz_show_correct_answers_last_attempt is not None:
            data["quiz[show_correct_answers_last_attempt]"] = quiz_show_correct_answers_last_attempt
        # OPTIONAL - quiz[show_correct_answers_at] - Only valid if show_correct_answers=true If set, the correct answers will be visible by students only after this date, otherwise the correct answers are visible once the student hands in their quiz submission.
        if quiz_show_correct_answers_at is not None:
            data["quiz[show_correct_answers_at]"] = quiz_show_correct_answers_at
        # OPTIONAL - quiz[hide_correct_answers_at] - Only valid if show_correct_answers=true If set, the correct answers will stop being visible once this date has passed. Otherwise, the correct answers will be visible indefinitely.
        if quiz_hide_correct_answers_at is not None:
            data["quiz[hide_correct_answers_at]"] = quiz_hide_correct_answers_at
        # OPTIONAL - quiz[allowed_attempts] - Number of times a student is allowed to take a quiz. Set to -1 for unlimited attempts. Defaults to 1.
        if quiz_allowed_attempts is not None:
            data["quiz[allowed_attempts]"] = quiz_allowed_attempts
        # OPTIONAL - quiz[scoring_policy] - Required and only valid if allowed_attempts > 1. Scoring policy for a quiz that students can take multiple times. Defaults to "keep_highest".
        if quiz_scoring_policy is not None:
            self._validate_enum(quiz_scoring_policy, ["keep_highest", "keep_latest"])
            data["quiz[scoring_policy]"] = quiz_scoring_policy
        # OPTIONAL - quiz[one_question_at_a_time] - If true, shows quiz to student one question at a time. Defaults to false.
        if quiz_one_question_at_a_time is not None:
            data["quiz[one_question_at_a_time]"] = quiz_one_question_at_a_time
        # OPTIONAL - quiz[cant_go_back] - Only valid if one_question_at_a_time=true If true, questions are locked after answering. Defaults to false.
        if quiz_cant_go_back is not None:
            data["quiz[cant_go_back]"] = quiz_cant_go_back
        # OPTIONAL - quiz[access_code] - Restricts access to the quiz with a password. For no access code restriction, set to null. Defaults to null.
        if quiz_access_code is not None:
            data["quiz[access_code]"] = quiz_access_code
        # OPTIONAL - quiz[ip_filter] - Restricts access to the quiz to computers in a specified IP range. Filters can be a comma-separated list of addresses, or an address followed by a mask Examples: "192.168.217.1" "192.168.217.1/24" "192.168.217.1/255.255.255.0" For no IP filter restriction, set to null. Defaults to null.
        if quiz_ip_filter is not None:
            data["quiz[ip_filter]"] = quiz_ip_filter
        # OPTIONAL - quiz[due_at] - The day/time the quiz is due. Accepts times in ISO 8601 format, e.g. 2011-10-21T18:48Z.
        if quiz_due_at is not None:
            data["quiz[due_at]"] = quiz_due_at
        # OPTIONAL - quiz[lock_at] - The day/time the quiz is locked for students. Accepts times in ISO 8601 format, e.g. 2011-10-21T18:48Z.
        if quiz_lock_at is not None:
            data["quiz[lock_at]"] = quiz_lock_at
        # OPTIONAL - quiz[unlock_at] - The day/time the quiz is unlocked for students. Accepts times in ISO 8601 format, e.g. 2011-10-21T18:48Z.
        if quiz_unlock_at is not None:
            data["quiz[unlock_at]"] = quiz_unlock_at
        # OPTIONAL - quiz[published] - Whether the quiz should have a draft state of published or unpublished. NOTE: If students have started taking the quiz, or there are any submissions for the quiz, you may not unpublish a quiz and will recieve an error.
        if quiz_published is not None:
            data["quiz[published]"] = quiz_published
        # OPTIONAL - quiz[one_time_results] - Whether students should be prevented from viewing their quiz results past the first time (right after they turn the quiz in.) Only valid if "hide_results" is not set to "always". Defaults to false.
        if quiz_one_time_results is not None:
            data["quiz[one_time_results]"] = quiz_one_time_results

        self.logger.debug("POST /api/v1/courses/{course_id}/quizzes with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/quizzes".format(**path), data=data, params=params, single_item=True)

    def edit_quiz(self, id, course_id, quiz_notify_of_update=None):
        """
        Edit a quiz.

        Modify an existing quiz. See the documentation for quiz creation.
        
        Additional arguments:
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - id - ID
        path["id"] = id
        # OPTIONAL - quiz[notify_of_update] - If true, notifies users that the quiz has changed. Defaults to true
        if quiz_notify_of_update is not None:
            data["quiz[notify_of_update]"] = quiz_notify_of_update

        self.logger.debug("PUT /api/v1/courses/{course_id}/quizzes/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/quizzes/{id}".format(**path), data=data, params=params, single_item=True)

    def delete_quiz(self, id, course_id):
        """
        Delete a quiz.

        
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("DELETE /api/v1/courses/{course_id}/quizzes/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/quizzes/{id}".format(**path), data=data, params=params, single_item=True)

    def reorder_quiz_items(self, id, order_id, course_id, order_type=None):
        """
        Reorder quiz items.

        Change order of the quiz questions or groups within the quiz
        
        <b>204 No Content</b> response code is returned if the reorder was successful.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - id - ID
        path["id"] = id
        # REQUIRED - order[id] - The associated item's unique identifier
        data["order[id]"] = order_id
        # OPTIONAL - order[type] - The type of item is either 'question' or 'group'
        if order_type is not None:
            self._validate_enum(order_type, ["question", "group"])
            data["order[type]"] = order_type

        self.logger.debug("POST /api/v1/courses/{course_id}/quizzes/{id}/reorder with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/quizzes/{id}/reorder".format(**path), data=data, params=params, no_data=True)


class Quizpermissions(BaseModel):
    """Quizpermissions Model.
    Permissions the user has for the quiz"""

    def __init__(self, read=None, create=None, manage=None, update=None, submit=None, read_statistics=None, review_grades=None):
        """Init method for Quizpermissions class."""
        self._read = read
        self._create = create
        self._manage = manage
        self._update = update
        self._submit = submit
        self._read_statistics = read_statistics
        self._review_grades = review_grades

        self.logger = logging.getLogger('pycanvas.Quizpermissions')

    @property
    def read(self):
        """whether the user can view the quiz."""
        return self._read

    @read.setter
    def read(self, value):
        """Setter for read property."""
        self.logger.warn("Setting values on read will NOT update the remote Canvas instance.")
        self._read = value

    @property
    def create(self):
        """whether the user may create a new quiz."""
        return self._create

    @create.setter
    def create(self, value):
        """Setter for create property."""
        self.logger.warn("Setting values on create will NOT update the remote Canvas instance.")
        self._create = value

    @property
    def manage(self):
        """whether the user may edit, update, or delete the quiz."""
        return self._manage

    @manage.setter
    def manage(self, value):
        """Setter for manage property."""
        self.logger.warn("Setting values on manage will NOT update the remote Canvas instance.")
        self._manage = value

    @property
    def update(self):
        """whether the user may update the quiz."""
        return self._update

    @update.setter
    def update(self, value):
        """Setter for update property."""
        self.logger.warn("Setting values on update will NOT update the remote Canvas instance.")
        self._update = value

    @property
    def submit(self):
        """whether the user may submit a submission for the quiz."""
        return self._submit

    @submit.setter
    def submit(self, value):
        """Setter for submit property."""
        self.logger.warn("Setting values on submit will NOT update the remote Canvas instance.")
        self._submit = value

    @property
    def read_statistics(self):
        """whether the user may view quiz statistics for this quiz."""
        return self._read_statistics

    @read_statistics.setter
    def read_statistics(self, value):
        """Setter for read_statistics property."""
        self.logger.warn("Setting values on read_statistics will NOT update the remote Canvas instance.")
        self._read_statistics = value

    @property
    def review_grades(self):
        """whether the user may review grades for all quiz submissions for this quiz."""
        return self._review_grades

    @review_grades.setter
    def review_grades(self, value):
        """Setter for review_grades property."""
        self.logger.warn("Setting values on review_grades will NOT update the remote Canvas instance.")
        self._review_grades = value


class Quiz(BaseModel):
    """Quiz Model."""

    def __init__(self, time_limit=None, lock_info=None, one_question_at_a_time=None, points_possible=None, quiz_type=None, shuffle_answers=None, id=None, locked_for_user=None, mobile_url=None, allowed_attempts=None, title=None, show_correct_answers=None, scoring_policy=None, permissions=None, hide_correct_answers_at=None, show_correct_answers_at=None, description=None, all_dates=None, cant_go_back=None, html_url=None, speedgrader_url=None, hide_results=None, lock_explanation=None, quiz_extensions_url=None, question_count=None, ip_filter=None, show_correct_answers_last_attempt=None, version_number=None, unlock_at=None, one_time_results=None, due_at=None, preview_url=None, lock_at=None, assignment_group_id=None, published=None, access_code=None, unpublishable=None):
        """Init method for Quiz class."""
        self._time_limit = time_limit
        self._lock_info = lock_info
        self._one_question_at_a_time = one_question_at_a_time
        self._points_possible = points_possible
        self._quiz_type = quiz_type
        self._shuffle_answers = shuffle_answers
        self._id = id
        self._locked_for_user = locked_for_user
        self._mobile_url = mobile_url
        self._allowed_attempts = allowed_attempts
        self._title = title
        self._show_correct_answers = show_correct_answers
        self._scoring_policy = scoring_policy
        self._permissions = permissions
        self._hide_correct_answers_at = hide_correct_answers_at
        self._show_correct_answers_at = show_correct_answers_at
        self._description = description
        self._all_dates = all_dates
        self._cant_go_back = cant_go_back
        self._html_url = html_url
        self._speedgrader_url = speedgrader_url
        self._hide_results = hide_results
        self._lock_explanation = lock_explanation
        self._quiz_extensions_url = quiz_extensions_url
        self._question_count = question_count
        self._ip_filter = ip_filter
        self._show_correct_answers_last_attempt = show_correct_answers_last_attempt
        self._version_number = version_number
        self._unlock_at = unlock_at
        self._one_time_results = one_time_results
        self._due_at = due_at
        self._preview_url = preview_url
        self._lock_at = lock_at
        self._assignment_group_id = assignment_group_id
        self._published = published
        self._access_code = access_code
        self._unpublishable = unpublishable

        self.logger = logging.getLogger('pycanvas.Quiz')

    @property
    def time_limit(self):
        """quiz time limit in minutes."""
        return self._time_limit

    @time_limit.setter
    def time_limit(self, value):
        """Setter for time_limit property."""
        self.logger.warn("Setting values on time_limit will NOT update the remote Canvas instance.")
        self._time_limit = value

    @property
    def lock_info(self):
        """(Optional) Information for the user about the lock. Present when locked_for_user is true."""
        return self._lock_info

    @lock_info.setter
    def lock_info(self, value):
        """Setter for lock_info property."""
        self.logger.warn("Setting values on lock_info will NOT update the remote Canvas instance.")
        self._lock_info = value

    @property
    def one_question_at_a_time(self):
        """show one question at a time?."""
        return self._one_question_at_a_time

    @one_question_at_a_time.setter
    def one_question_at_a_time(self, value):
        """Setter for one_question_at_a_time property."""
        self.logger.warn("Setting values on one_question_at_a_time will NOT update the remote Canvas instance.")
        self._one_question_at_a_time = value

    @property
    def points_possible(self):
        """The total point value given to the quiz."""
        return self._points_possible

    @points_possible.setter
    def points_possible(self, value):
        """Setter for points_possible property."""
        self.logger.warn("Setting values on points_possible will NOT update the remote Canvas instance.")
        self._points_possible = value

    @property
    def quiz_type(self):
        """type of quiz possible values: 'practice_quiz', 'assignment', 'graded_survey', 'survey'."""
        return self._quiz_type

    @quiz_type.setter
    def quiz_type(self, value):
        """Setter for quiz_type property."""
        self.logger.warn("Setting values on quiz_type will NOT update the remote Canvas instance.")
        self._quiz_type = value

    @property
    def shuffle_answers(self):
        """shuffle answers for students?."""
        return self._shuffle_answers

    @shuffle_answers.setter
    def shuffle_answers(self, value):
        """Setter for shuffle_answers property."""
        self.logger.warn("Setting values on shuffle_answers will NOT update the remote Canvas instance.")
        self._shuffle_answers = value

    @property
    def id(self):
        """the ID of the quiz."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def locked_for_user(self):
        """Whether or not this is locked for the user."""
        return self._locked_for_user

    @locked_for_user.setter
    def locked_for_user(self, value):
        """Setter for locked_for_user property."""
        self.logger.warn("Setting values on locked_for_user will NOT update the remote Canvas instance.")
        self._locked_for_user = value

    @property
    def mobile_url(self):
        """a url suitable for loading the quiz in a mobile webview.  it will persiste the headless session and, for quizzes in public courses, will force the user to login."""
        return self._mobile_url

    @mobile_url.setter
    def mobile_url(self, value):
        """Setter for mobile_url property."""
        self.logger.warn("Setting values on mobile_url will NOT update the remote Canvas instance.")
        self._mobile_url = value

    @property
    def allowed_attempts(self):
        """how many times a student can take the quiz -1 = unlimited attempts."""
        return self._allowed_attempts

    @allowed_attempts.setter
    def allowed_attempts(self, value):
        """Setter for allowed_attempts property."""
        self.logger.warn("Setting values on allowed_attempts will NOT update the remote Canvas instance.")
        self._allowed_attempts = value

    @property
    def title(self):
        """the title of the quiz."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value

    @property
    def show_correct_answers(self):
        """show which answers were correct when results are shown? only valid if hide_results=null."""
        return self._show_correct_answers

    @show_correct_answers.setter
    def show_correct_answers(self, value):
        """Setter for show_correct_answers property."""
        self.logger.warn("Setting values on show_correct_answers will NOT update the remote Canvas instance.")
        self._show_correct_answers = value

    @property
    def scoring_policy(self):
        """which quiz score to keep (only if allowed_attempts != 1) possible values: 'keep_highest', 'keep_latest'."""
        return self._scoring_policy

    @scoring_policy.setter
    def scoring_policy(self, value):
        """Setter for scoring_policy property."""
        self.logger.warn("Setting values on scoring_policy will NOT update the remote Canvas instance.")
        self._scoring_policy = value

    @property
    def permissions(self):
        """Permissions the user has for the quiz."""
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """Setter for permissions property."""
        self.logger.warn("Setting values on permissions will NOT update the remote Canvas instance.")
        self._permissions = value

    @property
    def hide_correct_answers_at(self):
        """prevent the students from seeing correct answers after the specified date has passed. only valid if show_correct_answers=true."""
        return self._hide_correct_answers_at

    @hide_correct_answers_at.setter
    def hide_correct_answers_at(self, value):
        """Setter for hide_correct_answers_at property."""
        self.logger.warn("Setting values on hide_correct_answers_at will NOT update the remote Canvas instance.")
        self._hide_correct_answers_at = value

    @property
    def show_correct_answers_at(self):
        """when should the correct answers be visible by students? only valid if show_correct_answers=true."""
        return self._show_correct_answers_at

    @show_correct_answers_at.setter
    def show_correct_answers_at(self, value):
        """Setter for show_correct_answers_at property."""
        self.logger.warn("Setting values on show_correct_answers_at will NOT update the remote Canvas instance.")
        self._show_correct_answers_at = value

    @property
    def description(self):
        """the description of the quiz."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn("Setting values on description will NOT update the remote Canvas instance.")
        self._description = value

    @property
    def all_dates(self):
        """list of due dates for the quiz."""
        return self._all_dates

    @all_dates.setter
    def all_dates(self, value):
        """Setter for all_dates property."""
        self.logger.warn("Setting values on all_dates will NOT update the remote Canvas instance.")
        self._all_dates = value

    @property
    def cant_go_back(self):
        """lock questions after answering? only valid if one_question_at_a_time=true."""
        return self._cant_go_back

    @cant_go_back.setter
    def cant_go_back(self, value):
        """Setter for cant_go_back property."""
        self.logger.warn("Setting values on cant_go_back will NOT update the remote Canvas instance.")
        self._cant_go_back = value

    @property
    def html_url(self):
        """the HTTP/HTTPS URL to the quiz."""
        return self._html_url

    @html_url.setter
    def html_url(self, value):
        """Setter for html_url property."""
        self.logger.warn("Setting values on html_url will NOT update the remote Canvas instance.")
        self._html_url = value

    @property
    def speedgrader_url(self):
        """Link to Speed Grader for this quiz. Will not be present if quiz is unpublished."""
        return self._speedgrader_url

    @speedgrader_url.setter
    def speedgrader_url(self, value):
        """Setter for speedgrader_url property."""
        self.logger.warn("Setting values on speedgrader_url will NOT update the remote Canvas instance.")
        self._speedgrader_url = value

    @property
    def hide_results(self):
        """let students see their quiz responses? possible values: null, 'always', 'until_after_last_attempt'."""
        return self._hide_results

    @hide_results.setter
    def hide_results(self, value):
        """Setter for hide_results property."""
        self.logger.warn("Setting values on hide_results will NOT update the remote Canvas instance.")
        self._hide_results = value

    @property
    def lock_explanation(self):
        """(Optional) An explanation of why this is locked for the user. Present when locked_for_user is true."""
        return self._lock_explanation

    @lock_explanation.setter
    def lock_explanation(self, value):
        """Setter for lock_explanation property."""
        self.logger.warn("Setting values on lock_explanation will NOT update the remote Canvas instance.")
        self._lock_explanation = value

    @property
    def quiz_extensions_url(self):
        """Link to endpoint to send extensions for this quiz."""
        return self._quiz_extensions_url

    @quiz_extensions_url.setter
    def quiz_extensions_url(self, value):
        """Setter for quiz_extensions_url property."""
        self.logger.warn("Setting values on quiz_extensions_url will NOT update the remote Canvas instance.")
        self._quiz_extensions_url = value

    @property
    def question_count(self):
        """the number of questions in the quiz."""
        return self._question_count

    @question_count.setter
    def question_count(self, value):
        """Setter for question_count property."""
        self.logger.warn("Setting values on question_count will NOT update the remote Canvas instance.")
        self._question_count = value

    @property
    def ip_filter(self):
        """IP address or range that quiz access is limited to."""
        return self._ip_filter

    @ip_filter.setter
    def ip_filter(self, value):
        """Setter for ip_filter property."""
        self.logger.warn("Setting values on ip_filter will NOT update the remote Canvas instance.")
        self._ip_filter = value

    @property
    def show_correct_answers_last_attempt(self):
        """restrict the show_correct_answers option above to apply only to the last submitted attempt of a quiz that allows multiple attempts. only valid if show_correct_answers=true and allowed_attempts > 1."""
        return self._show_correct_answers_last_attempt

    @show_correct_answers_last_attempt.setter
    def show_correct_answers_last_attempt(self, value):
        """Setter for show_correct_answers_last_attempt property."""
        self.logger.warn("Setting values on show_correct_answers_last_attempt will NOT update the remote Canvas instance.")
        self._show_correct_answers_last_attempt = value

    @property
    def version_number(self):
        """Current version number of the quiz."""
        return self._version_number

    @version_number.setter
    def version_number(self, value):
        """Setter for version_number property."""
        self.logger.warn("Setting values on version_number will NOT update the remote Canvas instance.")
        self._version_number = value

    @property
    def unlock_at(self):
        """when to unlock the quiz."""
        return self._unlock_at

    @unlock_at.setter
    def unlock_at(self, value):
        """Setter for unlock_at property."""
        self.logger.warn("Setting values on unlock_at will NOT update the remote Canvas instance.")
        self._unlock_at = value

    @property
    def one_time_results(self):
        """prevent the students from seeing their results more than once (right after they submit the quiz)."""
        return self._one_time_results

    @one_time_results.setter
    def one_time_results(self, value):
        """Setter for one_time_results property."""
        self.logger.warn("Setting values on one_time_results will NOT update the remote Canvas instance.")
        self._one_time_results = value

    @property
    def due_at(self):
        """when the quiz is due."""
        return self._due_at

    @due_at.setter
    def due_at(self, value):
        """Setter for due_at property."""
        self.logger.warn("Setting values on due_at will NOT update the remote Canvas instance.")
        self._due_at = value

    @property
    def preview_url(self):
        """A url that can be visited in the browser with a POST request to preview a quiz as the teacher. Only present when the user may grade."""
        return self._preview_url

    @preview_url.setter
    def preview_url(self, value):
        """Setter for preview_url property."""
        self.logger.warn("Setting values on preview_url will NOT update the remote Canvas instance.")
        self._preview_url = value

    @property
    def lock_at(self):
        """when to lock the quiz."""
        return self._lock_at

    @lock_at.setter
    def lock_at(self, value):
        """Setter for lock_at property."""
        self.logger.warn("Setting values on lock_at will NOT update the remote Canvas instance.")
        self._lock_at = value

    @property
    def assignment_group_id(self):
        """the ID of the quiz's assignment group:."""
        return self._assignment_group_id

    @assignment_group_id.setter
    def assignment_group_id(self, value):
        """Setter for assignment_group_id property."""
        self.logger.warn("Setting values on assignment_group_id will NOT update the remote Canvas instance.")
        self._assignment_group_id = value

    @property
    def published(self):
        """whether the quiz has a published or unpublished draft state."""
        return self._published

    @published.setter
    def published(self, value):
        """Setter for published property."""
        self.logger.warn("Setting values on published will NOT update the remote Canvas instance.")
        self._published = value

    @property
    def access_code(self):
        """access code to restrict quiz access."""
        return self._access_code

    @access_code.setter
    def access_code(self, value):
        """Setter for access_code property."""
        self.logger.warn("Setting values on access_code will NOT update the remote Canvas instance.")
        self._access_code = value

    @property
    def unpublishable(self):
        """Whether the assignment's 'published' state can be changed to false. Will be false if there are student submissions for the quiz."""
        return self._unpublishable

    @unpublishable.setter
    def unpublishable(self, value):
        """Setter for unpublishable property."""
        self.logger.warn("Setting values on unpublishable will NOT update the remote Canvas instance.")
        self._unpublishable = value

