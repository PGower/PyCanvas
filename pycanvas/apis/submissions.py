"""Submissions API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class SubmissionsAPI(BaseCanvasAPI):
    """Submissions API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for SubmissionsAPI."""
        super(SubmissionsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.SubmissionsAPI")

    def submit_assignment_courses(self, course_id, assignment_id, submission_submission_type, comment_text_comment=None, submission_body=None, submission_file_ids=None, submission_media_comment_id=None, submission_media_comment_type=None, submission_url=None):
        """
        Submit an assignment.

        Make a submission for an assignment. You must be enrolled as a student in
        the course/section to do this.
        
        All online turn-in submission types are supported in this API. However,
        there are a few things that are not yet supported:
        
        * Files can be submitted based on a file ID of a user or group file. However, there is no API yet for listing the user and group files, or uploading new files via the API. A file upload API is coming soon.
        * Media comments can be submitted, however, there is no API yet for creating a media comment to submit.
        * Integration with Google Docs is not yet supported.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - assignment_id
        """ID"""
        path["assignment_id"] = assignment_id

        # OPTIONAL - comment[text_comment]
        """Include a textual comment with the submission."""
        if comment_text_comment is not None:
            data["comment[text_comment]"] = comment_text_comment

        # REQUIRED - submission[submission_type]
        """The type of submission being made. The assignment submission_types must
        include this submission type as an allowed option, or the submission will be rejected with a 400 error.
        
        The submission_type given determines which of the following parameters is
        used. For instance, to submit a URL, submission [submission_type] must be
        set to "online_url", otherwise the submission [url] parameter will be
        ignored."""
        self._validate_enum(submission_submission_type, ["online_text_entry", "online_url", "online_upload", "media_recording", "basic_lti_launch"])
        data["submission[submission_type]"] = submission_submission_type

        # OPTIONAL - submission[body]
        """Submit the assignment as an HTML document snippet. Note this HTML snippet
        will be sanitized using the same ruleset as a submission made from the
        Canvas web UI. The sanitized HTML will be returned in the response as the
        submission body. Requires a submission_type of "online_text_entry"."""
        if submission_body is not None:
            data["submission[body]"] = submission_body

        # OPTIONAL - submission[url]
        """Submit the assignment as a URL. The URL scheme must be "http" or "https",
        no "ftp" or other URL schemes are allowed. If no scheme is given (e.g.
        "www.example.com") then "http" will be assumed. Requires a submission_type
        of "online_url" or "basic_lti_launch"."""
        if submission_url is not None:
            data["submission[url]"] = submission_url

        # OPTIONAL - submission[file_ids]
        """Submit the assignment as a set of one or more previously uploaded files
        residing in the submitting user's files section (or the group's files
        section, for group assignments).
        
        To upload a new file to submit, see the submissions {api:SubmissionsApiController#create_file Upload a file API}.
        
        Requires a submission_type of "online_upload"."""
        if submission_file_ids is not None:
            data["submission[file_ids]"] = submission_file_ids

        # OPTIONAL - submission[media_comment_id]
        """The media comment id to submit. Media comment ids can be submitted via
        this API, however, note that there is not yet an API to generate or list
        existing media comments, so this functionality is currently of limited use.
        
        Requires a submission_type of "media_recording"."""
        if submission_media_comment_id is not None:
            data["submission[media_comment_id]"] = submission_media_comment_id

        # OPTIONAL - submission[media_comment_type]
        """The type of media comment being submitted."""
        if submission_media_comment_type is not None:
            self._validate_enum(submission_media_comment_type, ["audio", "video"])
            data["submission[media_comment_type]"] = submission_media_comment_type

        self.logger.debug("POST /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions".format(**path), data=data, params=params, no_data=True)

    def submit_assignment_sections(self, section_id, assignment_id, submission_submission_type, comment_text_comment=None, submission_body=None, submission_file_ids=None, submission_media_comment_id=None, submission_media_comment_type=None, submission_url=None):
        """
        Submit an assignment.

        Make a submission for an assignment. You must be enrolled as a student in
        the course/section to do this.
        
        All online turn-in submission types are supported in this API. However,
        there are a few things that are not yet supported:
        
        * Files can be submitted based on a file ID of a user or group file. However, there is no API yet for listing the user and group files, or uploading new files via the API. A file upload API is coming soon.
        * Media comments can be submitted, however, there is no API yet for creating a media comment to submit.
        * Integration with Google Docs is not yet supported.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - section_id
        """ID"""
        path["section_id"] = section_id

        # REQUIRED - PATH - assignment_id
        """ID"""
        path["assignment_id"] = assignment_id

        # OPTIONAL - comment[text_comment]
        """Include a textual comment with the submission."""
        if comment_text_comment is not None:
            data["comment[text_comment]"] = comment_text_comment

        # REQUIRED - submission[submission_type]
        """The type of submission being made. The assignment submission_types must
        include this submission type as an allowed option, or the submission will be rejected with a 400 error.
        
        The submission_type given determines which of the following parameters is
        used. For instance, to submit a URL, submission [submission_type] must be
        set to "online_url", otherwise the submission [url] parameter will be
        ignored."""
        self._validate_enum(submission_submission_type, ["online_text_entry", "online_url", "online_upload", "media_recording", "basic_lti_launch"])
        data["submission[submission_type]"] = submission_submission_type

        # OPTIONAL - submission[body]
        """Submit the assignment as an HTML document snippet. Note this HTML snippet
        will be sanitized using the same ruleset as a submission made from the
        Canvas web UI. The sanitized HTML will be returned in the response as the
        submission body. Requires a submission_type of "online_text_entry"."""
        if submission_body is not None:
            data["submission[body]"] = submission_body

        # OPTIONAL - submission[url]
        """Submit the assignment as a URL. The URL scheme must be "http" or "https",
        no "ftp" or other URL schemes are allowed. If no scheme is given (e.g.
        "www.example.com") then "http" will be assumed. Requires a submission_type
        of "online_url" or "basic_lti_launch"."""
        if submission_url is not None:
            data["submission[url]"] = submission_url

        # OPTIONAL - submission[file_ids]
        """Submit the assignment as a set of one or more previously uploaded files
        residing in the submitting user's files section (or the group's files
        section, for group assignments).
        
        To upload a new file to submit, see the submissions {api:SubmissionsApiController#create_file Upload a file API}.
        
        Requires a submission_type of "online_upload"."""
        if submission_file_ids is not None:
            data["submission[file_ids]"] = submission_file_ids

        # OPTIONAL - submission[media_comment_id]
        """The media comment id to submit. Media comment ids can be submitted via
        this API, however, note that there is not yet an API to generate or list
        existing media comments, so this functionality is currently of limited use.
        
        Requires a submission_type of "media_recording"."""
        if submission_media_comment_id is not None:
            data["submission[media_comment_id]"] = submission_media_comment_id

        # OPTIONAL - submission[media_comment_type]
        """The type of media comment being submitted."""
        if submission_media_comment_type is not None:
            self._validate_enum(submission_media_comment_type, ["audio", "video"])
            data["submission[media_comment_type]"] = submission_media_comment_type

        self.logger.debug("POST /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions".format(**path), data=data, params=params, no_data=True)

    def list_assignment_submissions_courses(self, course_id, assignment_id, grouped=None, include=None):
        """
        List assignment submissions.

        Get all existing submissions for an assignment.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - assignment_id
        """ID"""
        path["assignment_id"] = assignment_id

        # OPTIONAL - include
        """Associations to include with the group.  "group" will add group_id and group_name."""
        if include is not None:
            self._validate_enum(include, ["submission_history", "submission_comments", "rubric_assessment", "assignment", "visibility", "course", "user", "group"])
            params["include"] = include

        # OPTIONAL - grouped
        """If this argument is true, the response will be grouped by student groups."""
        if grouped is not None:
            params["grouped"] = grouped

        self.logger.debug("GET /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions".format(**path), data=data, params=params, all_pages=True)

    def list_assignment_submissions_sections(self, section_id, assignment_id, grouped=None, include=None):
        """
        List assignment submissions.

        Get all existing submissions for an assignment.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - section_id
        """ID"""
        path["section_id"] = section_id

        # REQUIRED - PATH - assignment_id
        """ID"""
        path["assignment_id"] = assignment_id

        # OPTIONAL - include
        """Associations to include with the group.  "group" will add group_id and group_name."""
        if include is not None:
            self._validate_enum(include, ["submission_history", "submission_comments", "rubric_assessment", "assignment", "visibility", "course", "user", "group"])
            params["include"] = include

        # OPTIONAL - grouped
        """If this argument is true, the response will be grouped by student groups."""
        if grouped is not None:
            params["grouped"] = grouped

        self.logger.debug("GET /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions".format(**path), data=data, params=params, all_pages=True)

    def list_submissions_for_multiple_assignments_courses(self, course_id, assignment_ids=None, grading_period_id=None, grouped=None, include=None, order=None, order_direction=None, student_ids=None):
        """
        List submissions for multiple assignments.

        Get all existing submissions for a given set of students and assignments.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # OPTIONAL - student_ids
        """List of student ids to return submissions for. If this argument is
        omitted, return submissions for the calling user. Students may only list
        their own submissions. Observers may only list those of associated
        students. The special id "all" will return submissions for all students
        in the course/section as appropriate."""
        if student_ids is not None:
            params["student_ids"] = student_ids

        # OPTIONAL - assignment_ids
        """List of assignments to return submissions for. If none are given,
        submissions for all assignments are returned."""
        if assignment_ids is not None:
            params["assignment_ids"] = assignment_ids

        # OPTIONAL - grouped
        """If this argument is present, the response will be grouped by student,
        rather than a flat array of submissions."""
        if grouped is not None:
            params["grouped"] = grouped

        # OPTIONAL - grading_period_id
        """The id of the grading period in which submissions are being requested
        (Requires the Multiple Grading Periods account feature turned on)"""
        if grading_period_id is not None:
            params["grading_period_id"] = grading_period_id

        # OPTIONAL - order
        """The order submissions will be returned in.  Defaults to "id".  Doesn't
        affect results for "grouped" mode."""
        if order is not None:
            self._validate_enum(order, ["id", "graded_at"])
            params["order"] = order

        # OPTIONAL - order_direction
        """Determines whether ordered results are retured in ascending or descending
        order.  Defaults to "ascending".  Doesn't affect results for "grouped" mode."""
        if order_direction is not None:
            self._validate_enum(order_direction, ["ascending", "descending"])
            params["order_direction"] = order_direction

        # OPTIONAL - include
        """Associations to include with the group. `total_scores` requires the
        `grouped` argument."""
        if include is not None:
            self._validate_enum(include, ["submission_history", "submission_comments", "rubric_assessment", "assignment", "total_scores", "visibility", "course", "user"])
            params["include"] = include

        self.logger.debug("GET /api/v1/courses/{course_id}/students/submissions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/students/submissions".format(**path), data=data, params=params, no_data=True)

    def list_submissions_for_multiple_assignments_sections(self, section_id, assignment_ids=None, grading_period_id=None, grouped=None, include=None, order=None, order_direction=None, student_ids=None):
        """
        List submissions for multiple assignments.

        Get all existing submissions for a given set of students and assignments.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - section_id
        """ID"""
        path["section_id"] = section_id

        # OPTIONAL - student_ids
        """List of student ids to return submissions for. If this argument is
        omitted, return submissions for the calling user. Students may only list
        their own submissions. Observers may only list those of associated
        students. The special id "all" will return submissions for all students
        in the course/section as appropriate."""
        if student_ids is not None:
            params["student_ids"] = student_ids

        # OPTIONAL - assignment_ids
        """List of assignments to return submissions for. If none are given,
        submissions for all assignments are returned."""
        if assignment_ids is not None:
            params["assignment_ids"] = assignment_ids

        # OPTIONAL - grouped
        """If this argument is present, the response will be grouped by student,
        rather than a flat array of submissions."""
        if grouped is not None:
            params["grouped"] = grouped

        # OPTIONAL - grading_period_id
        """The id of the grading period in which submissions are being requested
        (Requires the Multiple Grading Periods account feature turned on)"""
        if grading_period_id is not None:
            params["grading_period_id"] = grading_period_id

        # OPTIONAL - order
        """The order submissions will be returned in.  Defaults to "id".  Doesn't
        affect results for "grouped" mode."""
        if order is not None:
            self._validate_enum(order, ["id", "graded_at"])
            params["order"] = order

        # OPTIONAL - order_direction
        """Determines whether ordered results are retured in ascending or descending
        order.  Defaults to "ascending".  Doesn't affect results for "grouped" mode."""
        if order_direction is not None:
            self._validate_enum(order_direction, ["ascending", "descending"])
            params["order_direction"] = order_direction

        # OPTIONAL - include
        """Associations to include with the group. `total_scores` requires the
        `grouped` argument."""
        if include is not None:
            self._validate_enum(include, ["submission_history", "submission_comments", "rubric_assessment", "assignment", "total_scores", "visibility", "course", "user"])
            params["include"] = include

        self.logger.debug("GET /api/v1/sections/{section_id}/students/submissions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/sections/{section_id}/students/submissions".format(**path), data=data, params=params, no_data=True)

    def get_single_submission_courses(self, user_id, course_id, assignment_id, include=None):
        """
        Get a single submission.

        Get a single submission, based on user id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - assignment_id
        """ID"""
        path["assignment_id"] = assignment_id

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        # OPTIONAL - include
        """Associations to include with the group."""
        if include is not None:
            self._validate_enum(include, ["submission_history", "submission_comments", "rubric_assessment", "visibility", "course", "user"])
            params["include"] = include

        self.logger.debug("GET /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}".format(**path), data=data, params=params, no_data=True)

    def get_single_submission_sections(self, user_id, section_id, assignment_id, include=None):
        """
        Get a single submission.

        Get a single submission, based on user id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - section_id
        """ID"""
        path["section_id"] = section_id

        # REQUIRED - PATH - assignment_id
        """ID"""
        path["assignment_id"] = assignment_id

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        # OPTIONAL - include
        """Associations to include with the group."""
        if include is not None:
            self._validate_enum(include, ["submission_history", "submission_comments", "rubric_assessment", "visibility", "course", "user"])
            params["include"] = include

        self.logger.debug("GET /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}".format(**path), data=data, params=params, no_data=True)

    def upload_file_courses(self, user_id, course_id, assignment_id):
        """
        Upload a file.

        Upload a file to a submission.
        
        This API endpoint is the first step in uploading a file to a submission as a student.
        See the {file:file_uploads.html File Upload Documentation} for details on the file upload workflow.
        
        The final step of the file upload workflow will return the attachment data,
        including the new file id. The caller can then POST to submit the
        +online_upload+ assignment with these file ids.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - assignment_id
        """ID"""
        path["assignment_id"] = assignment_id

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        self.logger.debug("POST /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/files with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/files".format(**path), data=data, params=params, no_data=True)

    def upload_file_sections(self, user_id, section_id, assignment_id):
        """
        Upload a file.

        Upload a file to a submission.
        
        This API endpoint is the first step in uploading a file to a submission as a student.
        See the {file:file_uploads.html File Upload Documentation} for details on the file upload workflow.
        
        The final step of the file upload workflow will return the attachment data,
        including the new file id. The caller can then POST to submit the
        +online_upload+ assignment with these file ids.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - section_id
        """ID"""
        path["section_id"] = section_id

        # REQUIRED - PATH - assignment_id
        """ID"""
        path["assignment_id"] = assignment_id

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        self.logger.debug("POST /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/files with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/files".format(**path), data=data, params=params, no_data=True)

    def grade_or_comment_on_submission_courses(self, user_id, course_id, assignment_id, comment_file_ids=None, comment_group_comment=None, comment_media_comment_id=None, comment_media_comment_type=None, comment_text_comment=None, include_visibility=None, rubric_assessment=None, submission_excuse=None, submission_posted_grade=None):
        """
        Grade or comment on a submission.

        Comment on and/or update the grading for a student's assignment submission.
        If any submission or rubric_assessment arguments are provided, the user
        must have permission to manage grades in the appropriate context (course or
        section).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - assignment_id
        """ID"""
        path["assignment_id"] = assignment_id

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        # OPTIONAL - comment[text_comment]
        """Add a textual comment to the submission."""
        if comment_text_comment is not None:
            data["comment[text_comment]"] = comment_text_comment

        # OPTIONAL - comment[group_comment]
        """Whether or not this comment should be sent to the entire group (defaults
        to false). Ignored if this is not a group assignment or if no text_comment
        is provided."""
        if comment_group_comment is not None:
            data["comment[group_comment]"] = comment_group_comment

        # OPTIONAL - comment[media_comment_id]
        """Add an audio/video comment to the submission. Media comments can be added
        via this API, however, note that there is not yet an API to generate or
        list existing media comments, so this functionality is currently of
        limited use."""
        if comment_media_comment_id is not None:
            data["comment[media_comment_id]"] = comment_media_comment_id

        # OPTIONAL - comment[media_comment_type]
        """The type of media comment being added."""
        if comment_media_comment_type is not None:
            self._validate_enum(comment_media_comment_type, ["audio", "video"])
            data["comment[media_comment_type]"] = comment_media_comment_type

        # OPTIONAL - comment[file_ids]
        """Attach files to this comment that were previously uploaded using the
        Submission Comment API's files action"""
        if comment_file_ids is not None:
            data["comment[file_ids]"] = comment_file_ids

        # OPTIONAL - include[visibility]
        """Whether this assignment is visible to the owner of the submission"""
        if include_visibility is not None:
            data["include[visibility]"] = include_visibility

        # OPTIONAL - submission[posted_grade]
        """Assign a score to the submission, updating both the "score" and "grade"
        fields on the submission record. This parameter can be passed in a few
        different formats:
        
        points:: A floating point or integral value, such as "13.5". The grade
          will be interpreted directly as the score of the assignment.
          Values above assignment.points_possible are allowed, for awarding
          extra credit.
        percentage:: A floating point value appended with a percent sign, such as
           "40%". The grade will be interpreted as a percentage score on the
           assignment, where 100% == assignment.points_possible. Values above 100%
           are allowed, for awarding extra credit.
        letter grade:: A letter grade, following the assignment's defined letter
           grading scheme. For example, "A-". The resulting score will be the high
           end of the defined range for the letter grade. For instance, if "B" is
           defined as 86% to 84%, a letter grade of "B" will be worth 86%. The
           letter grade will be rejected if the assignment does not have a defined
           letter grading scheme. For more fine-grained control of scores, pass in
           points or percentage rather than the letter grade.
        "pass/complete/fail/incomplete":: A string value of "pass" or "complete"
           will give a score of 100%. "fail" or "incomplete" will give a score of
           0.
        
        Note that assignments with grading_type of "pass_fail" can only be
        assigned a score of 0 or assignment.points_possible, nothing inbetween. If
        a posted_grade in the "points" or "percentage" format is sent, the grade
        will only be accepted if the grade equals one of those two values."""
        if submission_posted_grade is not None:
            data["submission[posted_grade]"] = submission_posted_grade

        # OPTIONAL - submission[excuse]
        """Sets the "excused" status of an assignment."""
        if submission_excuse is not None:
            data["submission[excuse]"] = submission_excuse

        # OPTIONAL - rubric_assessment
        """Assign a rubric assessment to this assignment submission. The
        sub-parameters here depend on the rubric for the assignment. The general
        format is, for each row in the rubric:
        
        The points awarded for this row.
          rubric_assessment[criterion_id][points]
        
        Comments to add for this row.
          rubric_assessment[criterion_id][comments]
        
        For example, if the assignment rubric is (in JSON format):
          !!!javascript
          [
            {
              'id': 'crit1',
              'points': 10,
              'description': 'Criterion 1',
              'ratings':
              [
                { 'description': 'Good', 'points': 10 },
                { 'description': 'Poor', 'points': 3 }
              ]
            },
            {
              'id': 'crit2',
              'points': 5,
              'description': 'Criterion 2',
              'ratings':
              [
                { 'description': 'Complete', 'points': 5 },
                { 'description': 'Incomplete', 'points': 0 }
              ]
            }
          ]
        
        Then a possible set of values for rubric_assessment would be:
            rubric_assessment[crit1][points]=3&rubric_assessment[crit2][points]=5&rubric_assessment[crit2][comments]=Well%20Done."""
        if rubric_assessment is not None:
            data["rubric_assessment"] = rubric_assessment

        self.logger.debug("PUT /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}".format(**path), data=data, params=params, no_data=True)

    def grade_or_comment_on_submission_sections(self, user_id, section_id, assignment_id, comment_file_ids=None, comment_group_comment=None, comment_media_comment_id=None, comment_media_comment_type=None, comment_text_comment=None, include_visibility=None, rubric_assessment=None, submission_excuse=None, submission_posted_grade=None):
        """
        Grade or comment on a submission.

        Comment on and/or update the grading for a student's assignment submission.
        If any submission or rubric_assessment arguments are provided, the user
        must have permission to manage grades in the appropriate context (course or
        section).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - section_id
        """ID"""
        path["section_id"] = section_id

        # REQUIRED - PATH - assignment_id
        """ID"""
        path["assignment_id"] = assignment_id

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        # OPTIONAL - comment[text_comment]
        """Add a textual comment to the submission."""
        if comment_text_comment is not None:
            data["comment[text_comment]"] = comment_text_comment

        # OPTIONAL - comment[group_comment]
        """Whether or not this comment should be sent to the entire group (defaults
        to false). Ignored if this is not a group assignment or if no text_comment
        is provided."""
        if comment_group_comment is not None:
            data["comment[group_comment]"] = comment_group_comment

        # OPTIONAL - comment[media_comment_id]
        """Add an audio/video comment to the submission. Media comments can be added
        via this API, however, note that there is not yet an API to generate or
        list existing media comments, so this functionality is currently of
        limited use."""
        if comment_media_comment_id is not None:
            data["comment[media_comment_id]"] = comment_media_comment_id

        # OPTIONAL - comment[media_comment_type]
        """The type of media comment being added."""
        if comment_media_comment_type is not None:
            self._validate_enum(comment_media_comment_type, ["audio", "video"])
            data["comment[media_comment_type]"] = comment_media_comment_type

        # OPTIONAL - comment[file_ids]
        """Attach files to this comment that were previously uploaded using the
        Submission Comment API's files action"""
        if comment_file_ids is not None:
            data["comment[file_ids]"] = comment_file_ids

        # OPTIONAL - include[visibility]
        """Whether this assignment is visible to the owner of the submission"""
        if include_visibility is not None:
            data["include[visibility]"] = include_visibility

        # OPTIONAL - submission[posted_grade]
        """Assign a score to the submission, updating both the "score" and "grade"
        fields on the submission record. This parameter can be passed in a few
        different formats:
        
        points:: A floating point or integral value, such as "13.5". The grade
          will be interpreted directly as the score of the assignment.
          Values above assignment.points_possible are allowed, for awarding
          extra credit.
        percentage:: A floating point value appended with a percent sign, such as
           "40%". The grade will be interpreted as a percentage score on the
           assignment, where 100% == assignment.points_possible. Values above 100%
           are allowed, for awarding extra credit.
        letter grade:: A letter grade, following the assignment's defined letter
           grading scheme. For example, "A-". The resulting score will be the high
           end of the defined range for the letter grade. For instance, if "B" is
           defined as 86% to 84%, a letter grade of "B" will be worth 86%. The
           letter grade will be rejected if the assignment does not have a defined
           letter grading scheme. For more fine-grained control of scores, pass in
           points or percentage rather than the letter grade.
        "pass/complete/fail/incomplete":: A string value of "pass" or "complete"
           will give a score of 100%. "fail" or "incomplete" will give a score of
           0.
        
        Note that assignments with grading_type of "pass_fail" can only be
        assigned a score of 0 or assignment.points_possible, nothing inbetween. If
        a posted_grade in the "points" or "percentage" format is sent, the grade
        will only be accepted if the grade equals one of those two values."""
        if submission_posted_grade is not None:
            data["submission[posted_grade]"] = submission_posted_grade

        # OPTIONAL - submission[excuse]
        """Sets the "excused" status of an assignment."""
        if submission_excuse is not None:
            data["submission[excuse]"] = submission_excuse

        # OPTIONAL - rubric_assessment
        """Assign a rubric assessment to this assignment submission. The
        sub-parameters here depend on the rubric for the assignment. The general
        format is, for each row in the rubric:
        
        The points awarded for this row.
          rubric_assessment[criterion_id][points]
        
        Comments to add for this row.
          rubric_assessment[criterion_id][comments]
        
        For example, if the assignment rubric is (in JSON format):
          !!!javascript
          [
            {
              'id': 'crit1',
              'points': 10,
              'description': 'Criterion 1',
              'ratings':
              [
                { 'description': 'Good', 'points': 10 },
                { 'description': 'Poor', 'points': 3 }
              ]
            },
            {
              'id': 'crit2',
              'points': 5,
              'description': 'Criterion 2',
              'ratings':
              [
                { 'description': 'Complete', 'points': 5 },
                { 'description': 'Incomplete', 'points': 0 }
              ]
            }
          ]
        
        Then a possible set of values for rubric_assessment would be:
            rubric_assessment[crit1][points]=3&rubric_assessment[crit2][points]=5&rubric_assessment[crit2][comments]=Well%20Done."""
        if rubric_assessment is not None:
            data["rubric_assessment"] = rubric_assessment

        self.logger.debug("PUT /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}".format(**path), data=data, params=params, no_data=True)

    def list_gradeable_students(self, course_id, assignment_id):
        """
        List gradeable students.

        List students eligible to submit the assignment. The caller must have permission to view grades.
        
        Section-limited instructors will only see students in their own sections.
        
        returns [UserDisplay]
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - assignment_id
        """ID"""
        path["assignment_id"] = assignment_id

        self.logger.debug("GET /api/v1/courses/{course_id}/assignments/{assignment_id}/gradeable_students with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignments/{assignment_id}/gradeable_students".format(**path), data=data, params=params, no_data=True)

    def grade_or_comment_on_multiple_submissions_courses_submissions(self, course_id, grade_data_<student_id>_excuse=None, grade_data_<student_id>_file_ids=None, grade_data_<student_id>_group_comment=None, grade_data_<student_id>_media_comment_id=None, grade_data_<student_id>_media_comment_type=None, grade_data_<student_id>_posted_grade=None, grade_data_<student_id>_rubric_assessment=None, grade_data_<student_id>_text_comment=None):
        """
        Grade or comment on multiple submissions.

        Update the grading and comments on multiple student's assignment
        submissions in an asynchronous job.
        
        The user must have permission to manage grades in the appropriate context
        (course or section).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # OPTIONAL - grade_data[<student_id>][posted_grade]
        """See documentation for the posted_grade argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation"""
        if grade_data_<student_id>_posted_grade is not None:
            data["grade_data[<student_id>][posted_grade]"] = grade_data_<student_id>_posted_grade

        # OPTIONAL - grade_data[<student_id>][excuse]
        """See documentation for the excuse argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation"""
        if grade_data_<student_id>_excuse is not None:
            data["grade_data[<student_id>][excuse]"] = grade_data_<student_id>_excuse

        # OPTIONAL - grade_data[<student_id>][rubric_assessment]
        """See documentation for the rubric_assessment argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation"""
        if grade_data_<student_id>_rubric_assessment is not None:
            data["grade_data[<student_id>][rubric_assessment]"] = grade_data_<student_id>_rubric_assessment

        # OPTIONAL - grade_data[<student_id>][text_comment]
        """no description"""
        if grade_data_<student_id>_text_comment is not None:
            data["grade_data[<student_id>][text_comment]"] = grade_data_<student_id>_text_comment

        # OPTIONAL - grade_data[<student_id>][group_comment]
        """no description"""
        if grade_data_<student_id>_group_comment is not None:
            data["grade_data[<student_id>][group_comment]"] = grade_data_<student_id>_group_comment

        # OPTIONAL - grade_data[<student_id>][media_comment_id]
        """no description"""
        if grade_data_<student_id>_media_comment_id is not None:
            data["grade_data[<student_id>][media_comment_id]"] = grade_data_<student_id>_media_comment_id

        # OPTIONAL - grade_data[<student_id>][media_comment_type]
        """no description"""
        if grade_data_<student_id>_media_comment_type is not None:
            self._validate_enum(grade_data_<student_id>_media_comment_type, ["audio", "video"])
            data["grade_data[<student_id>][media_comment_type]"] = grade_data_<student_id>_media_comment_type

        # OPTIONAL - grade_data[<student_id>][file_ids]
        """See documentation for the comment[] arguments in the
        {api:SubmissionsApiController#update Submissions Update} documentation"""
        if grade_data_<student_id>_file_ids is not None:
            data["grade_data[<student_id>][file_ids]"] = grade_data_<student_id>_file_ids

        self.logger.debug("POST /api/v1/courses/{course_id}/submissions/update_grades with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/submissions/update_grades".format(**path), data=data, params=params, single_item=True)

    def grade_or_comment_on_multiple_submissions_courses_assignments(self, course_id, assignment_id, grade_data_<student_id>_excuse=None, grade_data_<student_id>_file_ids=None, grade_data_<student_id>_group_comment=None, grade_data_<student_id>_media_comment_id=None, grade_data_<student_id>_media_comment_type=None, grade_data_<student_id>_posted_grade=None, grade_data_<student_id>_rubric_assessment=None, grade_data_<student_id>_text_comment=None):
        """
        Grade or comment on multiple submissions.

        Update the grading and comments on multiple student's assignment
        submissions in an asynchronous job.
        
        The user must have permission to manage grades in the appropriate context
        (course or section).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - assignment_id
        """ID"""
        path["assignment_id"] = assignment_id

        # OPTIONAL - grade_data[<student_id>][posted_grade]
        """See documentation for the posted_grade argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation"""
        if grade_data_<student_id>_posted_grade is not None:
            data["grade_data[<student_id>][posted_grade]"] = grade_data_<student_id>_posted_grade

        # OPTIONAL - grade_data[<student_id>][excuse]
        """See documentation for the excuse argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation"""
        if grade_data_<student_id>_excuse is not None:
            data["grade_data[<student_id>][excuse]"] = grade_data_<student_id>_excuse

        # OPTIONAL - grade_data[<student_id>][rubric_assessment]
        """See documentation for the rubric_assessment argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation"""
        if grade_data_<student_id>_rubric_assessment is not None:
            data["grade_data[<student_id>][rubric_assessment]"] = grade_data_<student_id>_rubric_assessment

        # OPTIONAL - grade_data[<student_id>][text_comment]
        """no description"""
        if grade_data_<student_id>_text_comment is not None:
            data["grade_data[<student_id>][text_comment]"] = grade_data_<student_id>_text_comment

        # OPTIONAL - grade_data[<student_id>][group_comment]
        """no description"""
        if grade_data_<student_id>_group_comment is not None:
            data["grade_data[<student_id>][group_comment]"] = grade_data_<student_id>_group_comment

        # OPTIONAL - grade_data[<student_id>][media_comment_id]
        """no description"""
        if grade_data_<student_id>_media_comment_id is not None:
            data["grade_data[<student_id>][media_comment_id]"] = grade_data_<student_id>_media_comment_id

        # OPTIONAL - grade_data[<student_id>][media_comment_type]
        """no description"""
        if grade_data_<student_id>_media_comment_type is not None:
            self._validate_enum(grade_data_<student_id>_media_comment_type, ["audio", "video"])
            data["grade_data[<student_id>][media_comment_type]"] = grade_data_<student_id>_media_comment_type

        # OPTIONAL - grade_data[<student_id>][file_ids]
        """See documentation for the comment[] arguments in the
        {api:SubmissionsApiController#update Submissions Update} documentation"""
        if grade_data_<student_id>_file_ids is not None:
            data["grade_data[<student_id>][file_ids]"] = grade_data_<student_id>_file_ids

        self.logger.debug("POST /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/update_grades with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/update_grades".format(**path), data=data, params=params, single_item=True)

    def grade_or_comment_on_multiple_submissions_sections_submissions(self, section_id, grade_data_<student_id>_excuse=None, grade_data_<student_id>_file_ids=None, grade_data_<student_id>_group_comment=None, grade_data_<student_id>_media_comment_id=None, grade_data_<student_id>_media_comment_type=None, grade_data_<student_id>_posted_grade=None, grade_data_<student_id>_rubric_assessment=None, grade_data_<student_id>_text_comment=None):
        """
        Grade or comment on multiple submissions.

        Update the grading and comments on multiple student's assignment
        submissions in an asynchronous job.
        
        The user must have permission to manage grades in the appropriate context
        (course or section).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - section_id
        """ID"""
        path["section_id"] = section_id

        # OPTIONAL - grade_data[<student_id>][posted_grade]
        """See documentation for the posted_grade argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation"""
        if grade_data_<student_id>_posted_grade is not None:
            data["grade_data[<student_id>][posted_grade]"] = grade_data_<student_id>_posted_grade

        # OPTIONAL - grade_data[<student_id>][excuse]
        """See documentation for the excuse argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation"""
        if grade_data_<student_id>_excuse is not None:
            data["grade_data[<student_id>][excuse]"] = grade_data_<student_id>_excuse

        # OPTIONAL - grade_data[<student_id>][rubric_assessment]
        """See documentation for the rubric_assessment argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation"""
        if grade_data_<student_id>_rubric_assessment is not None:
            data["grade_data[<student_id>][rubric_assessment]"] = grade_data_<student_id>_rubric_assessment

        # OPTIONAL - grade_data[<student_id>][text_comment]
        """no description"""
        if grade_data_<student_id>_text_comment is not None:
            data["grade_data[<student_id>][text_comment]"] = grade_data_<student_id>_text_comment

        # OPTIONAL - grade_data[<student_id>][group_comment]
        """no description"""
        if grade_data_<student_id>_group_comment is not None:
            data["grade_data[<student_id>][group_comment]"] = grade_data_<student_id>_group_comment

        # OPTIONAL - grade_data[<student_id>][media_comment_id]
        """no description"""
        if grade_data_<student_id>_media_comment_id is not None:
            data["grade_data[<student_id>][media_comment_id]"] = grade_data_<student_id>_media_comment_id

        # OPTIONAL - grade_data[<student_id>][media_comment_type]
        """no description"""
        if grade_data_<student_id>_media_comment_type is not None:
            self._validate_enum(grade_data_<student_id>_media_comment_type, ["audio", "video"])
            data["grade_data[<student_id>][media_comment_type]"] = grade_data_<student_id>_media_comment_type

        # OPTIONAL - grade_data[<student_id>][file_ids]
        """See documentation for the comment[] arguments in the
        {api:SubmissionsApiController#update Submissions Update} documentation"""
        if grade_data_<student_id>_file_ids is not None:
            data["grade_data[<student_id>][file_ids]"] = grade_data_<student_id>_file_ids

        self.logger.debug("POST /api/v1/sections/{section_id}/submissions/update_grades with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/sections/{section_id}/submissions/update_grades".format(**path), data=data, params=params, single_item=True)

    def grade_or_comment_on_multiple_submissions_sections_assignments(self, section_id, assignment_id, grade_data_<student_id>_excuse=None, grade_data_<student_id>_file_ids=None, grade_data_<student_id>_group_comment=None, grade_data_<student_id>_media_comment_id=None, grade_data_<student_id>_media_comment_type=None, grade_data_<student_id>_posted_grade=None, grade_data_<student_id>_rubric_assessment=None, grade_data_<student_id>_text_comment=None):
        """
        Grade or comment on multiple submissions.

        Update the grading and comments on multiple student's assignment
        submissions in an asynchronous job.
        
        The user must have permission to manage grades in the appropriate context
        (course or section).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - section_id
        """ID"""
        path["section_id"] = section_id

        # REQUIRED - PATH - assignment_id
        """ID"""
        path["assignment_id"] = assignment_id

        # OPTIONAL - grade_data[<student_id>][posted_grade]
        """See documentation for the posted_grade argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation"""
        if grade_data_<student_id>_posted_grade is not None:
            data["grade_data[<student_id>][posted_grade]"] = grade_data_<student_id>_posted_grade

        # OPTIONAL - grade_data[<student_id>][excuse]
        """See documentation for the excuse argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation"""
        if grade_data_<student_id>_excuse is not None:
            data["grade_data[<student_id>][excuse]"] = grade_data_<student_id>_excuse

        # OPTIONAL - grade_data[<student_id>][rubric_assessment]
        """See documentation for the rubric_assessment argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation"""
        if grade_data_<student_id>_rubric_assessment is not None:
            data["grade_data[<student_id>][rubric_assessment]"] = grade_data_<student_id>_rubric_assessment

        # OPTIONAL - grade_data[<student_id>][text_comment]
        """no description"""
        if grade_data_<student_id>_text_comment is not None:
            data["grade_data[<student_id>][text_comment]"] = grade_data_<student_id>_text_comment

        # OPTIONAL - grade_data[<student_id>][group_comment]
        """no description"""
        if grade_data_<student_id>_group_comment is not None:
            data["grade_data[<student_id>][group_comment]"] = grade_data_<student_id>_group_comment

        # OPTIONAL - grade_data[<student_id>][media_comment_id]
        """no description"""
        if grade_data_<student_id>_media_comment_id is not None:
            data["grade_data[<student_id>][media_comment_id]"] = grade_data_<student_id>_media_comment_id

        # OPTIONAL - grade_data[<student_id>][media_comment_type]
        """no description"""
        if grade_data_<student_id>_media_comment_type is not None:
            self._validate_enum(grade_data_<student_id>_media_comment_type, ["audio", "video"])
            data["grade_data[<student_id>][media_comment_type]"] = grade_data_<student_id>_media_comment_type

        # OPTIONAL - grade_data[<student_id>][file_ids]
        """See documentation for the comment[] arguments in the
        {api:SubmissionsApiController#update Submissions Update} documentation"""
        if grade_data_<student_id>_file_ids is not None:
            data["grade_data[<student_id>][file_ids]"] = grade_data_<student_id>_file_ids

        self.logger.debug("POST /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/update_grades with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/update_grades".format(**path), data=data, params=params, single_item=True)

    def mark_submission_as_read_courses(self, user_id, course_id, assignment_id):
        """
        Mark submission as read.

        No request fields are necessary.
        
        On success, the response will be 204 No Content with an empty body.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - assignment_id
        """ID"""
        path["assignment_id"] = assignment_id

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        self.logger.debug("PUT /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/read with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/read".format(**path), data=data, params=params, no_data=True)

    def mark_submission_as_read_sections(self, user_id, section_id, assignment_id):
        """
        Mark submission as read.

        No request fields are necessary.
        
        On success, the response will be 204 No Content with an empty body.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - section_id
        """ID"""
        path["section_id"] = section_id

        # REQUIRED - PATH - assignment_id
        """ID"""
        path["assignment_id"] = assignment_id

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        self.logger.debug("PUT /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/read with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/read".format(**path), data=data, params=params, no_data=True)

    def mark_submission_as_unread_courses(self, user_id, course_id, assignment_id):
        """
        Mark submission as unread.

        No request fields are necessary.
        
        On success, the response will be 204 No Content with an empty body.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - assignment_id
        """ID"""
        path["assignment_id"] = assignment_id

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        self.logger.debug("DELETE /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/read with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/read".format(**path), data=data, params=params, no_data=True)

    def mark_submission_as_unread_sections(self, user_id, section_id, assignment_id):
        """
        Mark submission as unread.

        No request fields are necessary.
        
        On success, the response will be 204 No Content with an empty body.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - section_id
        """ID"""
        path["section_id"] = section_id

        # REQUIRED - PATH - assignment_id
        """ID"""
        path["assignment_id"] = assignment_id

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        self.logger.debug("DELETE /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/read with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/read".format(**path), data=data, params=params, no_data=True)


class Submissioncomment(BaseModel):
    """Submissioncomment Model."""

    def __init__(self, comment=None, author=None, created_at=None, media_comment=None, author_name=None, author_id=None, id=None):
        """Init method for Submissioncomment class."""
        self._comment = comment
        self._author = author
        self._created_at = created_at
        self._media_comment = media_comment
        self._author_name = author_name
        self._author_id = author_id
        self._id = id

        self.logger = logging.getLogger('pycanvas.Submissioncomment')

    @property
    def comment(self):
        """comment."""
        return self._comment

    @comment.setter
    def comment(self, value):
        """Setter for comment property."""
        self.logger.warn("Setting values on comment will NOT update the remote Canvas instance.")
        self._comment = value

    @property
    def author(self):
        """Abbreviated user object UserDisplay (see users API)."""
        return self._author

    @author.setter
    def author(self, value):
        """Setter for author property."""
        self.logger.warn("Setting values on author will NOT update the remote Canvas instance.")
        self._author = value

    @property
    def created_at(self):
        """created_at."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def media_comment(self):
        """media_comment."""
        return self._media_comment

    @media_comment.setter
    def media_comment(self, value):
        """Setter for media_comment property."""
        self.logger.warn("Setting values on media_comment will NOT update the remote Canvas instance.")
        self._media_comment = value

    @property
    def author_name(self):
        """author_name."""
        return self._author_name

    @author_name.setter
    def author_name(self, value):
        """Setter for author_name property."""
        self.logger.warn("Setting values on author_name will NOT update the remote Canvas instance.")
        self._author_name = value

    @property
    def author_id(self):
        """author_id."""
        return self._author_id

    @author_id.setter
    def author_id(self, value):
        """Setter for author_id property."""
        self.logger.warn("Setting values on author_id will NOT update the remote Canvas instance.")
        self._author_id = value

    @property
    def id(self):
        """id."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value


class Submission(BaseModel):
    """Submission Model."""

    def __init__(self, body=None, attempt=None, submitted_at=None, excused=None, course=None, assignment_id=None, assignment=None, workflow_state=None, html_url=None, preview_url=None, late=None, grade=None, submission_comments=None, score=None, grade_matches_current_submission=None, url=None, grader_id=None, user_id=None, submission_type=None, assignment_visible=None, user=None):
        """Init method for Submission class."""
        self._body = body
        self._attempt = attempt
        self._submitted_at = submitted_at
        self._excused = excused
        self._course = course
        self._assignment_id = assignment_id
        self._assignment = assignment
        self._workflow_state = workflow_state
        self._html_url = html_url
        self._preview_url = preview_url
        self._late = late
        self._grade = grade
        self._submission_comments = submission_comments
        self._score = score
        self._grade_matches_current_submission = grade_matches_current_submission
        self._url = url
        self._grader_id = grader_id
        self._user_id = user_id
        self._submission_type = submission_type
        self._assignment_visible = assignment_visible
        self._user = user

        self.logger = logging.getLogger('pycanvas.Submission')

    @property
    def body(self):
        """The content of the submission, if it was submitted directly in a text field."""
        return self._body

    @body.setter
    def body(self, value):
        """Setter for body property."""
        self.logger.warn("Setting values on body will NOT update the remote Canvas instance.")
        self._body = value

    @property
    def attempt(self):
        """This is the submission attempt number."""
        return self._attempt

    @attempt.setter
    def attempt(self, value):
        """Setter for attempt property."""
        self.logger.warn("Setting values on attempt will NOT update the remote Canvas instance.")
        self._attempt = value

    @property
    def submitted_at(self):
        """The timestamp when the assignment was submitted."""
        return self._submitted_at

    @submitted_at.setter
    def submitted_at(self, value):
        """Setter for submitted_at property."""
        self.logger.warn("Setting values on submitted_at will NOT update the remote Canvas instance.")
        self._submitted_at = value

    @property
    def excused(self):
        """Whether the assignment is excused.  Excused assignments have no impact on a user's grade."""
        return self._excused

    @excused.setter
    def excused(self, value):
        """Setter for excused property."""
        self.logger.warn("Setting values on excused will NOT update the remote Canvas instance.")
        self._excused = value

    @property
    def course(self):
        """The submission's course (see the course API) (optional)."""
        return self._course

    @course.setter
    def course(self, value):
        """Setter for course property."""
        self.logger.warn("Setting values on course will NOT update the remote Canvas instance.")
        self._course = value

    @property
    def assignment_id(self):
        """The submission's assignment id."""
        return self._assignment_id

    @assignment_id.setter
    def assignment_id(self, value):
        """Setter for assignment_id property."""
        self.logger.warn("Setting values on assignment_id will NOT update the remote Canvas instance.")
        self._assignment_id = value

    @property
    def assignment(self):
        """The submission's assignment (see the assignments API) (optional)."""
        return self._assignment

    @assignment.setter
    def assignment(self, value):
        """Setter for assignment property."""
        self.logger.warn("Setting values on assignment will NOT update the remote Canvas instance.")
        self._assignment = value

    @property
    def workflow_state(self):
        """The current state of the submission."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def html_url(self):
        """URL to the submission. This will require the user to log in."""
        return self._html_url

    @html_url.setter
    def html_url(self, value):
        """Setter for html_url property."""
        self.logger.warn("Setting values on html_url will NOT update the remote Canvas instance.")
        self._html_url = value

    @property
    def preview_url(self):
        """URL to the submission preview. This will require the user to log in."""
        return self._preview_url

    @preview_url.setter
    def preview_url(self, value):
        """Setter for preview_url property."""
        self.logger.warn("Setting values on preview_url will NOT update the remote Canvas instance.")
        self._preview_url = value

    @property
    def late(self):
        """Whether the submission was made after the applicable due date."""
        return self._late

    @late.setter
    def late(self, value):
        """Setter for late property."""
        self.logger.warn("Setting values on late will NOT update the remote Canvas instance.")
        self._late = value

    @property
    def grade(self):
        """The grade for the submission, translated into the assignment grading scheme (so a letter grade, for example)."""
        return self._grade

    @grade.setter
    def grade(self, value):
        """Setter for grade property."""
        self.logger.warn("Setting values on grade will NOT update the remote Canvas instance.")
        self._grade = value

    @property
    def submission_comments(self):
        """Associated comments for a submission (optional)."""
        return self._submission_comments

    @submission_comments.setter
    def submission_comments(self, value):
        """Setter for submission_comments property."""
        self.logger.warn("Setting values on submission_comments will NOT update the remote Canvas instance.")
        self._submission_comments = value

    @property
    def score(self):
        """The raw score."""
        return self._score

    @score.setter
    def score(self, value):
        """Setter for score property."""
        self.logger.warn("Setting values on score will NOT update the remote Canvas instance.")
        self._score = value

    @property
    def grade_matches_current_submission(self):
        """A boolean flag which is false if the student has re-submitted since the submission was last graded."""
        return self._grade_matches_current_submission

    @grade_matches_current_submission.setter
    def grade_matches_current_submission(self, value):
        """Setter for grade_matches_current_submission property."""
        self.logger.warn("Setting values on grade_matches_current_submission will NOT update the remote Canvas instance.")
        self._grade_matches_current_submission = value

    @property
    def url(self):
        """The URL of the submission (for 'online_url' submissions)."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def grader_id(self):
        """The id of the user who graded the submission."""
        return self._grader_id

    @grader_id.setter
    def grader_id(self, value):
        """Setter for grader_id property."""
        self.logger.warn("Setting values on grader_id will NOT update the remote Canvas instance.")
        self._grader_id = value

    @property
    def user_id(self):
        """The id of the user who created the submission."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn("Setting values on user_id will NOT update the remote Canvas instance.")
        self._user_id = value

    @property
    def submission_type(self):
        """The types of submission ex: ('online_text_entry'|'online_url'|'online_upload'|'media_recording')."""
        return self._submission_type

    @submission_type.setter
    def submission_type(self, value):
        """Setter for submission_type property."""
        self.logger.warn("Setting values on submission_type will NOT update the remote Canvas instance.")
        self._submission_type = value

    @property
    def assignment_visible(self):
        """Whether the assignment is visible to the user who submitted the assignment. Submissions where `assignment_visible` is false no longer count towards the student's grade and the assignment can no longer be accessed by the student. `assignment_visible` becomes false for submissions that do not have a grade and whose assignment is no longer assigned to the student's section."""
        return self._assignment_visible

    @assignment_visible.setter
    def assignment_visible(self, value):
        """Setter for assignment_visible property."""
        self.logger.warn("Setting values on assignment_visible will NOT update the remote Canvas instance.")
        self._assignment_visible = value

    @property
    def user(self):
        """The submissions user (see user API) (optional)."""
        return self._user

    @user.setter
    def user(self, value):
        """Setter for user property."""
        self.logger.warn("Setting values on user will NOT update the remote Canvas instance.")
        self._user = value


class Mediacomment(BaseModel):
    """Mediacomment Model."""

    def __init__(self, media_id=None, display_name=None, content_type=None, url=None, media_type=None):
        """Init method for Mediacomment class."""
        self._media_id = media_id
        self._display_name = display_name
        self._content_type = content_type
        self._url = url
        self._media_type = media_type

        self.logger = logging.getLogger('pycanvas.Mediacomment')

    @property
    def media_id(self):
        """media_id."""
        return self._media_id

    @media_id.setter
    def media_id(self, value):
        """Setter for media_id property."""
        self.logger.warn("Setting values on media_id will NOT update the remote Canvas instance.")
        self._media_id = value

    @property
    def display_name(self):
        """display_name."""
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        """Setter for display_name property."""
        self.logger.warn("Setting values on display_name will NOT update the remote Canvas instance.")
        self._display_name = value

    @property
    def content_type(self):
        """content_type."""
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        """Setter for content_type property."""
        self.logger.warn("Setting values on content_type will NOT update the remote Canvas instance.")
        self._content_type = value

    @property
    def url(self):
        """url."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def media_type(self):
        """media_type."""
        return self._media_type

    @media_type.setter
    def media_type(self, value):
        """Setter for media_type property."""
        self.logger.warn("Setting values on media_type will NOT update the remote Canvas instance.")
        self._media_type = value

