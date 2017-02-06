"""DiscussionTopics API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class DiscussionTopicsAPI(BaseCanvasAPI):
    """DiscussionTopics API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for DiscussionTopicsAPI."""
        super(DiscussionTopicsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.DiscussionTopicsAPI")

    def list_discussion_topics_courses(self, course_id, exclude_context_module_locked_topics=None, include=None, only_announcements=None, order_by=None, scope=None, search_term=None):
        """
        List discussion topics.

        Returns the paginated list of discussion topics for this course or group.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # OPTIONAL - include
        """If "all_dates" is passed, all dates associated with graded discussions'
        assignments will be included."""
        if include is not None:
            self._validate_enum(include, ["all_dates"])
            params["include"] = include

        # OPTIONAL - order_by
        """Determines the order of the discussion topic list. Defaults to "position"."""
        if order_by is not None:
            self._validate_enum(order_by, ["position", "recent_activity"])
            params["order_by"] = order_by

        # OPTIONAL - scope
        """Only return discussion topics in the given state(s). Defaults to including
        all topics. Filtering is done after pagination, so pages
        may be smaller than requested if topics are filtered.
        Can pass multiple states as comma separated string."""
        if scope is not None:
            self._validate_enum(scope, ["locked", "unlocked", "pinned", "unpinned"])
            params["scope"] = scope

        # OPTIONAL - only_announcements
        """Return announcements instead of discussion topics. Defaults to false"""
        if only_announcements is not None:
            params["only_announcements"] = only_announcements

        # OPTIONAL - search_term
        """The partial title of the discussion topics to match and return."""
        if search_term is not None:
            params["search_term"] = search_term

        # OPTIONAL - exclude_context_module_locked_topics
        """For students, exclude topics that are locked by module progression.
        Defaults to false."""
        if exclude_context_module_locked_topics is not None:
            params["exclude_context_module_locked_topics"] = exclude_context_module_locked_topics

        self.logger.debug("GET /api/v1/courses/{course_id}/discussion_topics with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/discussion_topics".format(**path), data=data, params=params, all_pages=True)

    def list_discussion_topics_groups(self, group_id, exclude_context_module_locked_topics=None, include=None, only_announcements=None, order_by=None, scope=None, search_term=None):
        """
        List discussion topics.

        Returns the paginated list of discussion topics for this course or group.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # OPTIONAL - include
        """If "all_dates" is passed, all dates associated with graded discussions'
        assignments will be included."""
        if include is not None:
            self._validate_enum(include, ["all_dates"])
            params["include"] = include

        # OPTIONAL - order_by
        """Determines the order of the discussion topic list. Defaults to "position"."""
        if order_by is not None:
            self._validate_enum(order_by, ["position", "recent_activity"])
            params["order_by"] = order_by

        # OPTIONAL - scope
        """Only return discussion topics in the given state(s). Defaults to including
        all topics. Filtering is done after pagination, so pages
        may be smaller than requested if topics are filtered.
        Can pass multiple states as comma separated string."""
        if scope is not None:
            self._validate_enum(scope, ["locked", "unlocked", "pinned", "unpinned"])
            params["scope"] = scope

        # OPTIONAL - only_announcements
        """Return announcements instead of discussion topics. Defaults to false"""
        if only_announcements is not None:
            params["only_announcements"] = only_announcements

        # OPTIONAL - search_term
        """The partial title of the discussion topics to match and return."""
        if search_term is not None:
            params["search_term"] = search_term

        # OPTIONAL - exclude_context_module_locked_topics
        """For students, exclude topics that are locked by module progression.
        Defaults to false."""
        if exclude_context_module_locked_topics is not None:
            params["exclude_context_module_locked_topics"] = exclude_context_module_locked_topics

        self.logger.debug("GET /api/v1/groups/{group_id}/discussion_topics with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/discussion_topics".format(**path), data=data, params=params, all_pages=True)

    def create_new_discussion_topic_courses(self, course_id, allow_rating=None, assignment=None, attachment=None, delayed_post_at=None, discussion_type=None, group_category_id=None, is_announcement=None, lock_at=None, message=None, only_graders_can_rate=None, pinned=None, podcast_enabled=None, podcast_has_student_posts=None, position_after=None, published=None, require_initial_post=None, sort_by_rating=None, title=None):
        """
        Create a new discussion topic.

        Create an new discussion topic for the course or group.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # OPTIONAL - title
        """no description"""
        if title is not None:
            data["title"] = title

        # OPTIONAL - message
        """no description"""
        if message is not None:
            data["message"] = message

        # OPTIONAL - discussion_type
        """The type of discussion. Defaults to side_comment if not value is given. Accepted values are 'side_comment', for discussions that only allow one level of nested comments, and 'threaded' for fully threaded discussions."""
        if discussion_type is not None:
            self._validate_enum(discussion_type, ["side_comment", "threaded"])
            data["discussion_type"] = discussion_type

        # OPTIONAL - published
        """Whether this topic is published (true) or draft state (false). Only
        teachers and TAs have the ability to create draft state topics."""
        if published is not None:
            data["published"] = published

        # OPTIONAL - delayed_post_at
        """If a timestamp is given, the topic will not be published until that time."""
        if delayed_post_at is not None:
            data["delayed_post_at"] = delayed_post_at

        # OPTIONAL - lock_at
        """If a timestamp is given, the topic will be scheduled to lock at the
        provided timestamp. If the timestamp is in the past, the topic will be
        locked."""
        if lock_at is not None:
            data["lock_at"] = lock_at

        # OPTIONAL - podcast_enabled
        """If true, the topic will have an associated podcast feed."""
        if podcast_enabled is not None:
            data["podcast_enabled"] = podcast_enabled

        # OPTIONAL - podcast_has_student_posts
        """If true, the podcast will include posts from students as well. Implies
        podcast_enabled."""
        if podcast_has_student_posts is not None:
            data["podcast_has_student_posts"] = podcast_has_student_posts

        # OPTIONAL - require_initial_post
        """If true then a user may not respond to other replies until that user has
        made an initial reply. Defaults to false."""
        if require_initial_post is not None:
            data["require_initial_post"] = require_initial_post

        # OPTIONAL - assignment
        """To create an assignment discussion, pass the assignment parameters as a
        sub-object. See the {api:AssignmentsApiController#create Create an Assignment API}
        for the available parameters. The name parameter will be ignored, as it's
        taken from the discussion title. If you want to make a discussion that was
        an assignment NOT an assignment, pass set_assignment = false as part of
        the assignment object"""
        if assignment is not None:
            data["assignment"] = assignment

        # OPTIONAL - is_announcement
        """If true, this topic is an announcement. It will appear in the
        announcement's section rather than the discussions section. This requires
        announcment-posting permissions."""
        if is_announcement is not None:
            data["is_announcement"] = is_announcement

        # OPTIONAL - pinned
        """If true, this topic will be listed in the "Pinned Discussion" section"""
        if pinned is not None:
            data["pinned"] = pinned

        # OPTIONAL - position_after
        """By default, discussions are sorted chronologically by creation date, you
        can pass the id of another topic to have this one show up after the other
        when they are listed."""
        if position_after is not None:
            data["position_after"] = position_after

        # OPTIONAL - group_category_id
        """If present, the topic will become a group discussion assigned
        to the group."""
        if group_category_id is not None:
            data["group_category_id"] = group_category_id

        # OPTIONAL - allow_rating
        """If true, users will be allowed to rate entries."""
        if allow_rating is not None:
            data["allow_rating"] = allow_rating

        # OPTIONAL - only_graders_can_rate
        """If true, only graders will be allowed to rate entries."""
        if only_graders_can_rate is not None:
            data["only_graders_can_rate"] = only_graders_can_rate

        # OPTIONAL - sort_by_rating
        """If true, entries will be sorted by rating."""
        if sort_by_rating is not None:
            data["sort_by_rating"] = sort_by_rating

        # OPTIONAL - attachment
        """A multipart/form-data form-field-style attachment.
        Attachments larger than 1 kilobyte are subject to quota restrictions."""
        if attachment is not None:
            data["attachment"] = attachment

        self.logger.debug("POST /api/v1/courses/{course_id}/discussion_topics with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/discussion_topics".format(**path), data=data, params=params, no_data=True)

    def create_new_discussion_topic_groups(self, group_id, allow_rating=None, assignment=None, attachment=None, delayed_post_at=None, discussion_type=None, group_category_id=None, is_announcement=None, lock_at=None, message=None, only_graders_can_rate=None, pinned=None, podcast_enabled=None, podcast_has_student_posts=None, position_after=None, published=None, require_initial_post=None, sort_by_rating=None, title=None):
        """
        Create a new discussion topic.

        Create an new discussion topic for the course or group.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # OPTIONAL - title
        """no description"""
        if title is not None:
            data["title"] = title

        # OPTIONAL - message
        """no description"""
        if message is not None:
            data["message"] = message

        # OPTIONAL - discussion_type
        """The type of discussion. Defaults to side_comment if not value is given. Accepted values are 'side_comment', for discussions that only allow one level of nested comments, and 'threaded' for fully threaded discussions."""
        if discussion_type is not None:
            self._validate_enum(discussion_type, ["side_comment", "threaded"])
            data["discussion_type"] = discussion_type

        # OPTIONAL - published
        """Whether this topic is published (true) or draft state (false). Only
        teachers and TAs have the ability to create draft state topics."""
        if published is not None:
            data["published"] = published

        # OPTIONAL - delayed_post_at
        """If a timestamp is given, the topic will not be published until that time."""
        if delayed_post_at is not None:
            data["delayed_post_at"] = delayed_post_at

        # OPTIONAL - lock_at
        """If a timestamp is given, the topic will be scheduled to lock at the
        provided timestamp. If the timestamp is in the past, the topic will be
        locked."""
        if lock_at is not None:
            data["lock_at"] = lock_at

        # OPTIONAL - podcast_enabled
        """If true, the topic will have an associated podcast feed."""
        if podcast_enabled is not None:
            data["podcast_enabled"] = podcast_enabled

        # OPTIONAL - podcast_has_student_posts
        """If true, the podcast will include posts from students as well. Implies
        podcast_enabled."""
        if podcast_has_student_posts is not None:
            data["podcast_has_student_posts"] = podcast_has_student_posts

        # OPTIONAL - require_initial_post
        """If true then a user may not respond to other replies until that user has
        made an initial reply. Defaults to false."""
        if require_initial_post is not None:
            data["require_initial_post"] = require_initial_post

        # OPTIONAL - assignment
        """To create an assignment discussion, pass the assignment parameters as a
        sub-object. See the {api:AssignmentsApiController#create Create an Assignment API}
        for the available parameters. The name parameter will be ignored, as it's
        taken from the discussion title. If you want to make a discussion that was
        an assignment NOT an assignment, pass set_assignment = false as part of
        the assignment object"""
        if assignment is not None:
            data["assignment"] = assignment

        # OPTIONAL - is_announcement
        """If true, this topic is an announcement. It will appear in the
        announcement's section rather than the discussions section. This requires
        announcment-posting permissions."""
        if is_announcement is not None:
            data["is_announcement"] = is_announcement

        # OPTIONAL - pinned
        """If true, this topic will be listed in the "Pinned Discussion" section"""
        if pinned is not None:
            data["pinned"] = pinned

        # OPTIONAL - position_after
        """By default, discussions are sorted chronologically by creation date, you
        can pass the id of another topic to have this one show up after the other
        when they are listed."""
        if position_after is not None:
            data["position_after"] = position_after

        # OPTIONAL - group_category_id
        """If present, the topic will become a group discussion assigned
        to the group."""
        if group_category_id is not None:
            data["group_category_id"] = group_category_id

        # OPTIONAL - allow_rating
        """If true, users will be allowed to rate entries."""
        if allow_rating is not None:
            data["allow_rating"] = allow_rating

        # OPTIONAL - only_graders_can_rate
        """If true, only graders will be allowed to rate entries."""
        if only_graders_can_rate is not None:
            data["only_graders_can_rate"] = only_graders_can_rate

        # OPTIONAL - sort_by_rating
        """If true, entries will be sorted by rating."""
        if sort_by_rating is not None:
            data["sort_by_rating"] = sort_by_rating

        # OPTIONAL - attachment
        """A multipart/form-data form-field-style attachment.
        Attachments larger than 1 kilobyte are subject to quota restrictions."""
        if attachment is not None:
            data["attachment"] = attachment

        self.logger.debug("POST /api/v1/groups/{group_id}/discussion_topics with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/groups/{group_id}/discussion_topics".format(**path), data=data, params=params, no_data=True)

    def update_topic_courses(self, topic_id, course_id, allow_rating=None, assignment=None, delayed_post_at=None, discussion_type=None, group_category_id=None, is_announcement=None, lock_at=None, message=None, only_graders_can_rate=None, pinned=None, podcast_enabled=None, podcast_has_student_posts=None, position_after=None, published=None, require_initial_post=None, sort_by_rating=None, title=None):
        """
        Update a topic.

        Update an existing discussion topic for the course or group.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # OPTIONAL - title
        """no description"""
        if title is not None:
            data["title"] = title

        # OPTIONAL - message
        """no description"""
        if message is not None:
            data["message"] = message

        # OPTIONAL - discussion_type
        """The type of discussion. Defaults to side_comment if not value is given. Accepted values are 'side_comment', for discussions that only allow one level of nested comments, and 'threaded' for fully threaded discussions."""
        if discussion_type is not None:
            self._validate_enum(discussion_type, ["side_comment", "threaded"])
            data["discussion_type"] = discussion_type

        # OPTIONAL - published
        """Whether this topic is published (true) or draft state (false). Only
        teachers and TAs have the ability to create draft state topics."""
        if published is not None:
            data["published"] = published

        # OPTIONAL - delayed_post_at
        """If a timestamp is given, the topic will not be published until that time."""
        if delayed_post_at is not None:
            data["delayed_post_at"] = delayed_post_at

        # OPTIONAL - lock_at
        """If a timestamp is given, the topic will be scheduled to lock at the
        provided timestamp. If the timestamp is in the past, the topic will be
        locked."""
        if lock_at is not None:
            data["lock_at"] = lock_at

        # OPTIONAL - podcast_enabled
        """If true, the topic will have an associated podcast feed."""
        if podcast_enabled is not None:
            data["podcast_enabled"] = podcast_enabled

        # OPTIONAL - podcast_has_student_posts
        """If true, the podcast will include posts from students as well. Implies
        podcast_enabled."""
        if podcast_has_student_posts is not None:
            data["podcast_has_student_posts"] = podcast_has_student_posts

        # OPTIONAL - require_initial_post
        """If true then a user may not respond to other replies until that user has
        made an initial reply. Defaults to false."""
        if require_initial_post is not None:
            data["require_initial_post"] = require_initial_post

        # OPTIONAL - assignment
        """To create an assignment discussion, pass the assignment parameters as a
        sub-object. See the {api:AssignmentsApiController#create Create an Assignment API}
        for the available parameters. The name parameter will be ignored, as it's
        taken from the discussion title. If you want to make a discussion that was
        an assignment NOT an assignment, pass set_assignment = false as part of
        the assignment object"""
        if assignment is not None:
            data["assignment"] = assignment

        # OPTIONAL - is_announcement
        """If true, this topic is an announcement. It will appear in the
        announcement's section rather than the discussions section. This requires
        announcment-posting permissions."""
        if is_announcement is not None:
            data["is_announcement"] = is_announcement

        # OPTIONAL - pinned
        """If true, this topic will be listed in the "Pinned Discussion" section"""
        if pinned is not None:
            data["pinned"] = pinned

        # OPTIONAL - position_after
        """By default, discussions are sorted chronologically by creation date, you
        can pass the id of another topic to have this one show up after the other
        when they are listed."""
        if position_after is not None:
            data["position_after"] = position_after

        # OPTIONAL - group_category_id
        """If present, the topic will become a group discussion assigned
        to the group."""
        if group_category_id is not None:
            data["group_category_id"] = group_category_id

        # OPTIONAL - allow_rating
        """If true, users will be allowed to rate entries."""
        if allow_rating is not None:
            data["allow_rating"] = allow_rating

        # OPTIONAL - only_graders_can_rate
        """If true, only graders will be allowed to rate entries."""
        if only_graders_can_rate is not None:
            data["only_graders_can_rate"] = only_graders_can_rate

        # OPTIONAL - sort_by_rating
        """If true, entries will be sorted by rating."""
        if sort_by_rating is not None:
            data["sort_by_rating"] = sort_by_rating

        self.logger.debug("PUT /api/v1/courses/{course_id}/discussion_topics/{topic_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/discussion_topics/{topic_id}".format(**path), data=data, params=params, no_data=True)

    def update_topic_groups(self, group_id, topic_id, allow_rating=None, assignment=None, delayed_post_at=None, discussion_type=None, group_category_id=None, is_announcement=None, lock_at=None, message=None, only_graders_can_rate=None, pinned=None, podcast_enabled=None, podcast_has_student_posts=None, position_after=None, published=None, require_initial_post=None, sort_by_rating=None, title=None):
        """
        Update a topic.

        Update an existing discussion topic for the course or group.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # OPTIONAL - title
        """no description"""
        if title is not None:
            data["title"] = title

        # OPTIONAL - message
        """no description"""
        if message is not None:
            data["message"] = message

        # OPTIONAL - discussion_type
        """The type of discussion. Defaults to side_comment if not value is given. Accepted values are 'side_comment', for discussions that only allow one level of nested comments, and 'threaded' for fully threaded discussions."""
        if discussion_type is not None:
            self._validate_enum(discussion_type, ["side_comment", "threaded"])
            data["discussion_type"] = discussion_type

        # OPTIONAL - published
        """Whether this topic is published (true) or draft state (false). Only
        teachers and TAs have the ability to create draft state topics."""
        if published is not None:
            data["published"] = published

        # OPTIONAL - delayed_post_at
        """If a timestamp is given, the topic will not be published until that time."""
        if delayed_post_at is not None:
            data["delayed_post_at"] = delayed_post_at

        # OPTIONAL - lock_at
        """If a timestamp is given, the topic will be scheduled to lock at the
        provided timestamp. If the timestamp is in the past, the topic will be
        locked."""
        if lock_at is not None:
            data["lock_at"] = lock_at

        # OPTIONAL - podcast_enabled
        """If true, the topic will have an associated podcast feed."""
        if podcast_enabled is not None:
            data["podcast_enabled"] = podcast_enabled

        # OPTIONAL - podcast_has_student_posts
        """If true, the podcast will include posts from students as well. Implies
        podcast_enabled."""
        if podcast_has_student_posts is not None:
            data["podcast_has_student_posts"] = podcast_has_student_posts

        # OPTIONAL - require_initial_post
        """If true then a user may not respond to other replies until that user has
        made an initial reply. Defaults to false."""
        if require_initial_post is not None:
            data["require_initial_post"] = require_initial_post

        # OPTIONAL - assignment
        """To create an assignment discussion, pass the assignment parameters as a
        sub-object. See the {api:AssignmentsApiController#create Create an Assignment API}
        for the available parameters. The name parameter will be ignored, as it's
        taken from the discussion title. If you want to make a discussion that was
        an assignment NOT an assignment, pass set_assignment = false as part of
        the assignment object"""
        if assignment is not None:
            data["assignment"] = assignment

        # OPTIONAL - is_announcement
        """If true, this topic is an announcement. It will appear in the
        announcement's section rather than the discussions section. This requires
        announcment-posting permissions."""
        if is_announcement is not None:
            data["is_announcement"] = is_announcement

        # OPTIONAL - pinned
        """If true, this topic will be listed in the "Pinned Discussion" section"""
        if pinned is not None:
            data["pinned"] = pinned

        # OPTIONAL - position_after
        """By default, discussions are sorted chronologically by creation date, you
        can pass the id of another topic to have this one show up after the other
        when they are listed."""
        if position_after is not None:
            data["position_after"] = position_after

        # OPTIONAL - group_category_id
        """If present, the topic will become a group discussion assigned
        to the group."""
        if group_category_id is not None:
            data["group_category_id"] = group_category_id

        # OPTIONAL - allow_rating
        """If true, users will be allowed to rate entries."""
        if allow_rating is not None:
            data["allow_rating"] = allow_rating

        # OPTIONAL - only_graders_can_rate
        """If true, only graders will be allowed to rate entries."""
        if only_graders_can_rate is not None:
            data["only_graders_can_rate"] = only_graders_can_rate

        # OPTIONAL - sort_by_rating
        """If true, entries will be sorted by rating."""
        if sort_by_rating is not None:
            data["sort_by_rating"] = sort_by_rating

        self.logger.debug("PUT /api/v1/groups/{group_id}/discussion_topics/{topic_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/groups/{group_id}/discussion_topics/{topic_id}".format(**path), data=data, params=params, no_data=True)

    def delete_topic_courses(self, topic_id, course_id):
        """
        Delete a topic.

        Deletes the discussion topic. This will also delete the assignment, if it's
        an assignment discussion.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        self.logger.debug("DELETE /api/v1/courses/{course_id}/discussion_topics/{topic_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/discussion_topics/{topic_id}".format(**path), data=data, params=params, no_data=True)

    def delete_topic_groups(self, group_id, topic_id):
        """
        Delete a topic.

        Deletes the discussion topic. This will also delete the assignment, if it's
        an assignment discussion.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        self.logger.debug("DELETE /api/v1/groups/{group_id}/discussion_topics/{topic_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/groups/{group_id}/discussion_topics/{topic_id}".format(**path), data=data, params=params, no_data=True)

    def reorder_pinned_topics_courses(self, order, course_id):
        """
        Reorder pinned topics.

        Puts the pinned discussion topics in the specified order.
        All pinned topics should be included.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - order
        """The ids of the pinned discussion topics in the desired order.
        (For example, "order=104,102,103".)"""
        data["order"] = order

        self.logger.debug("POST /api/v1/courses/{course_id}/discussion_topics/reorder with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/discussion_topics/reorder".format(**path), data=data, params=params, no_data=True)

    def reorder_pinned_topics_groups(self, order, group_id):
        """
        Reorder pinned topics.

        Puts the pinned discussion topics in the specified order.
        All pinned topics should be included.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - order
        """The ids of the pinned discussion topics in the desired order.
        (For example, "order=104,102,103".)"""
        data["order"] = order

        self.logger.debug("POST /api/v1/groups/{group_id}/discussion_topics/reorder with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/groups/{group_id}/discussion_topics/reorder".format(**path), data=data, params=params, no_data=True)

    def update_entry_courses(self, id, topic_id, course_id, message=None):
        """
        Update an entry.

        Update an existing discussion entry.
        
        The entry must have been created by the current user, or the current user
        must have admin rights to the discussion. If the edit is not allowed, a 401 will be returned.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - message
        """The updated body of the entry."""
        if message is not None:
            data["message"] = message

        self.logger.debug("PUT /api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{id}".format(**path), data=data, params=params, no_data=True)

    def update_entry_groups(self, id, group_id, topic_id, message=None):
        """
        Update an entry.

        Update an existing discussion entry.
        
        The entry must have been created by the current user, or the current user
        must have admin rights to the discussion. If the edit is not allowed, a 401 will be returned.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - message
        """The updated body of the entry."""
        if message is not None:
            data["message"] = message

        self.logger.debug("PUT /api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{id}".format(**path), data=data, params=params, no_data=True)

    def delete_entry_courses(self, id, topic_id, course_id):
        """
        Delete an entry.

        Delete a discussion entry.
        
        The entry must have been created by the current user, or the current user
        must have admin rights to the discussion. If the delete is not allowed, a 401 will be returned.
        
        The discussion will be marked deleted, and the user_id and message will be cleared out.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("DELETE /api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{id}".format(**path), data=data, params=params, no_data=True)

    def delete_entry_groups(self, id, group_id, topic_id):
        """
        Delete an entry.

        Delete a discussion entry.
        
        The entry must have been created by the current user, or the current user
        must have admin rights to the discussion. If the delete is not allowed, a 401 will be returned.
        
        The discussion will be marked deleted, and the user_id and message will be cleared out.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("DELETE /api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{id}".format(**path), data=data, params=params, no_data=True)

    def get_single_topic_courses(self, topic_id, course_id):
        """
        Get a single topic.

        Returns data on an individual discussion topic. See the List action for the response formatting.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        self.logger.debug("GET /api/v1/courses/{course_id}/discussion_topics/{topic_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/discussion_topics/{topic_id}".format(**path), data=data, params=params, no_data=True)

    def get_single_topic_groups(self, group_id, topic_id):
        """
        Get a single topic.

        Returns data on an individual discussion topic. See the List action for the response formatting.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        self.logger.debug("GET /api/v1/groups/{group_id}/discussion_topics/{topic_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/discussion_topics/{topic_id}".format(**path), data=data, params=params, no_data=True)

    def get_full_topic_courses(self, topic_id, course_id):
        """
        Get the full topic.

        Return a cached structure of the discussion topic, containing all entries,
        their authors, and their message bodies.
        
        May require (depending on the topic) that the user has posted in the topic.
        If it is required, and the user has not posted, will respond with a 403
        Forbidden status and the body 'require_initial_post'.
        
        In some rare situations, this cached structure may not be available yet. In
        that case, the server will respond with a 503 error, and the caller should
        try again soon.
        
        The response is an object containing the following keys:
        * "participants": A list of summary information on users who have posted to
          the discussion. Each value is an object containing their id, display_name,
          and avatar_url.
        * "unread_entries": A list of entry ids that are unread by the current
          user. this implies that any entry not in this list is read.
        * "entry_ratings": A map of entry ids to ratings by the current user. Entries
          not in this list have no rating. Only populated if rating is enabled.
        * "forced_entries": A list of entry ids that have forced_read_state set to
          true. This flag is meant to indicate the entry's read_state has been
          manually set to 'unread' by the user, so the entry should not be
          automatically marked as read.
        * "view": A threaded view of all the entries in the discussion, containing
          the id, user_id, and message.
        * "new_entries": Because this view is eventually consistent, it's possible
          that newly created or updated entries won't yet be reflected in the view.
          If the application wants to also get a flat list of all entries not yet
          reflected in the view, pass include_new_entries=1 to the request and this
          array of entries will be returned. These entries are returned in a flat
          array, in ascending created_at order.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        self.logger.debug("GET /api/v1/courses/{course_id}/discussion_topics/{topic_id}/view with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/view".format(**path), data=data, params=params, no_data=True)

    def get_full_topic_groups(self, group_id, topic_id):
        """
        Get the full topic.

        Return a cached structure of the discussion topic, containing all entries,
        their authors, and their message bodies.
        
        May require (depending on the topic) that the user has posted in the topic.
        If it is required, and the user has not posted, will respond with a 403
        Forbidden status and the body 'require_initial_post'.
        
        In some rare situations, this cached structure may not be available yet. In
        that case, the server will respond with a 503 error, and the caller should
        try again soon.
        
        The response is an object containing the following keys:
        * "participants": A list of summary information on users who have posted to
          the discussion. Each value is an object containing their id, display_name,
          and avatar_url.
        * "unread_entries": A list of entry ids that are unread by the current
          user. this implies that any entry not in this list is read.
        * "entry_ratings": A map of entry ids to ratings by the current user. Entries
          not in this list have no rating. Only populated if rating is enabled.
        * "forced_entries": A list of entry ids that have forced_read_state set to
          true. This flag is meant to indicate the entry's read_state has been
          manually set to 'unread' by the user, so the entry should not be
          automatically marked as read.
        * "view": A threaded view of all the entries in the discussion, containing
          the id, user_id, and message.
        * "new_entries": Because this view is eventually consistent, it's possible
          that newly created or updated entries won't yet be reflected in the view.
          If the application wants to also get a flat list of all entries not yet
          reflected in the view, pass include_new_entries=1 to the request and this
          array of entries will be returned. These entries are returned in a flat
          array, in ascending created_at order.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        self.logger.debug("GET /api/v1/groups/{group_id}/discussion_topics/{topic_id}/view with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/discussion_topics/{topic_id}/view".format(**path), data=data, params=params, no_data=True)

    def post_entry_courses(self, topic_id, course_id, attachment=None, message=None):
        """
        Post an entry.

        Create a new entry in a discussion topic. Returns a json representation of
        the created entry (see documentation for 'entries' method) on success.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # OPTIONAL - message
        """The body of the entry."""
        if message is not None:
            data["message"] = message

        # OPTIONAL - attachment
        """a multipart/form-data form-field-style
        attachment. Attachments larger than 1 kilobyte are subject to quota
        restrictions."""
        if attachment is not None:
            data["attachment"] = attachment

        self.logger.debug("POST /api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries".format(**path), data=data, params=params, no_data=True)

    def post_entry_groups(self, group_id, topic_id, attachment=None, message=None):
        """
        Post an entry.

        Create a new entry in a discussion topic. Returns a json representation of
        the created entry (see documentation for 'entries' method) on success.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # OPTIONAL - message
        """The body of the entry."""
        if message is not None:
            data["message"] = message

        # OPTIONAL - attachment
        """a multipart/form-data form-field-style
        attachment. Attachments larger than 1 kilobyte are subject to quota
        restrictions."""
        if attachment is not None:
            data["attachment"] = attachment

        self.logger.debug("POST /api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries".format(**path), data=data, params=params, no_data=True)

    def list_topic_entries_courses(self, topic_id, course_id):
        """
        List topic entries.

        Retrieve the (paginated) top-level entries in a discussion topic.
        
        May require (depending on the topic) that the user has posted in the topic.
        If it is required, and the user has not posted, will respond with a 403
        Forbidden status and the body 'require_initial_post'.
        
        Will include the 10 most recent replies, if any, for each entry returned.
        
        If the topic is a root topic with children corresponding to groups of a
        group assignment, entries from those subtopics for which the user belongs
        to the corresponding group will be returned.
        
        Ordering of returned entries is newest-first by posting timestamp (reply
        activity is ignored).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        self.logger.debug("GET /api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries".format(**path), data=data, params=params, no_data=True)

    def list_topic_entries_groups(self, group_id, topic_id):
        """
        List topic entries.

        Retrieve the (paginated) top-level entries in a discussion topic.
        
        May require (depending on the topic) that the user has posted in the topic.
        If it is required, and the user has not posted, will respond with a 403
        Forbidden status and the body 'require_initial_post'.
        
        Will include the 10 most recent replies, if any, for each entry returned.
        
        If the topic is a root topic with children corresponding to groups of a
        group assignment, entries from those subtopics for which the user belongs
        to the corresponding group will be returned.
        
        Ordering of returned entries is newest-first by posting timestamp (reply
        activity is ignored).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        self.logger.debug("GET /api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries".format(**path), data=data, params=params, no_data=True)

    def post_reply_courses(self, topic_id, entry_id, course_id, attachment=None, message=None):
        """
        Post a reply.

        Add a reply to an entry in a discussion topic. Returns a json
        representation of the created reply (see documentation for 'replies'
        method) on success.
        
        May require (depending on the topic) that the user has posted in the topic.
        If it is required, and the user has not posted, will respond with a 403
        Forbidden status and the body 'require_initial_post'.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # REQUIRED - PATH - entry_id
        """ID"""
        path["entry_id"] = entry_id

        # OPTIONAL - message
        """The body of the entry."""
        if message is not None:
            data["message"] = message

        # OPTIONAL - attachment
        """a multipart/form-data form-field-style
        attachment. Attachments larger than 1 kilobyte are subject to quota
        restrictions."""
        if attachment is not None:
            data["attachment"] = attachment

        self.logger.debug("POST /api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies".format(**path), data=data, params=params, no_data=True)

    def post_reply_groups(self, group_id, topic_id, entry_id, attachment=None, message=None):
        """
        Post a reply.

        Add a reply to an entry in a discussion topic. Returns a json
        representation of the created reply (see documentation for 'replies'
        method) on success.
        
        May require (depending on the topic) that the user has posted in the topic.
        If it is required, and the user has not posted, will respond with a 403
        Forbidden status and the body 'require_initial_post'.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # REQUIRED - PATH - entry_id
        """ID"""
        path["entry_id"] = entry_id

        # OPTIONAL - message
        """The body of the entry."""
        if message is not None:
            data["message"] = message

        # OPTIONAL - attachment
        """a multipart/form-data form-field-style
        attachment. Attachments larger than 1 kilobyte are subject to quota
        restrictions."""
        if attachment is not None:
            data["attachment"] = attachment

        self.logger.debug("POST /api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies".format(**path), data=data, params=params, no_data=True)

    def list_entry_replies_courses(self, topic_id, entry_id, course_id):
        """
        List entry replies.

        Retrieve the (paginated) replies to a top-level entry in a discussion
        topic.
        
        May require (depending on the topic) that the user has posted in the topic.
        If it is required, and the user has not posted, will respond with a 403
        Forbidden status and the body 'require_initial_post'.
        
        Ordering of returned entries is newest-first by creation timestamp.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # REQUIRED - PATH - entry_id
        """ID"""
        path["entry_id"] = entry_id

        self.logger.debug("GET /api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies".format(**path), data=data, params=params, no_data=True)

    def list_entry_replies_groups(self, group_id, topic_id, entry_id):
        """
        List entry replies.

        Retrieve the (paginated) replies to a top-level entry in a discussion
        topic.
        
        May require (depending on the topic) that the user has posted in the topic.
        If it is required, and the user has not posted, will respond with a 403
        Forbidden status and the body 'require_initial_post'.
        
        Ordering of returned entries is newest-first by creation timestamp.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # REQUIRED - PATH - entry_id
        """ID"""
        path["entry_id"] = entry_id

        self.logger.debug("GET /api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies".format(**path), data=data, params=params, no_data=True)

    def list_entries_courses(self, topic_id, course_id, ids=None):
        """
        List entries.

        Retrieve a paginated list of discussion entries, given a list of ids.
        
        May require (depending on the topic) that the user has posted in the topic.
        If it is required, and the user has not posted, will respond with a 403
        Forbidden status and the body 'require_initial_post'.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # OPTIONAL - ids
        """A list of entry ids to retrieve. Entries will be returned in id order,
        smallest id first."""
        if ids is not None:
            params["ids"] = ids

        self.logger.debug("GET /api/v1/courses/{course_id}/discussion_topics/{topic_id}/entry_list with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/entry_list".format(**path), data=data, params=params, no_data=True)

    def list_entries_groups(self, group_id, topic_id, ids=None):
        """
        List entries.

        Retrieve a paginated list of discussion entries, given a list of ids.
        
        May require (depending on the topic) that the user has posted in the topic.
        If it is required, and the user has not posted, will respond with a 403
        Forbidden status and the body 'require_initial_post'.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # OPTIONAL - ids
        """A list of entry ids to retrieve. Entries will be returned in id order,
        smallest id first."""
        if ids is not None:
            params["ids"] = ids

        self.logger.debug("GET /api/v1/groups/{group_id}/discussion_topics/{topic_id}/entry_list with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/discussion_topics/{topic_id}/entry_list".format(**path), data=data, params=params, no_data=True)

    def mark_topic_as_read_courses(self, topic_id, course_id):
        """
        Mark topic as read.

        Mark the initial text of the discussion topic as read.
        
        No request fields are necessary.
        
        On success, the response will be 204 No Content with an empty body.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        self.logger.debug("PUT /api/v1/courses/{course_id}/discussion_topics/{topic_id}/read with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/read".format(**path), data=data, params=params, no_data=True)

    def mark_topic_as_read_groups(self, group_id, topic_id):
        """
        Mark topic as read.

        Mark the initial text of the discussion topic as read.
        
        No request fields are necessary.
        
        On success, the response will be 204 No Content with an empty body.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        self.logger.debug("PUT /api/v1/groups/{group_id}/discussion_topics/{topic_id}/read with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/groups/{group_id}/discussion_topics/{topic_id}/read".format(**path), data=data, params=params, no_data=True)

    def mark_topic_as_unread_courses(self, topic_id, course_id):
        """
        Mark topic as unread.

        Mark the initial text of the discussion topic as unread.
        
        No request fields are necessary.
        
        On success, the response will be 204 No Content with an empty body.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        self.logger.debug("DELETE /api/v1/courses/{course_id}/discussion_topics/{topic_id}/read with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/read".format(**path), data=data, params=params, no_data=True)

    def mark_topic_as_unread_groups(self, group_id, topic_id):
        """
        Mark topic as unread.

        Mark the initial text of the discussion topic as unread.
        
        No request fields are necessary.
        
        On success, the response will be 204 No Content with an empty body.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        self.logger.debug("DELETE /api/v1/groups/{group_id}/discussion_topics/{topic_id}/read with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/groups/{group_id}/discussion_topics/{topic_id}/read".format(**path), data=data, params=params, no_data=True)

    def mark_all_entries_as_read_courses(self, topic_id, course_id, forced_read_state=None):
        """
        Mark all entries as read.

        Mark the discussion topic and all its entries as read.
        
        No request fields are necessary.
        
        On success, the response will be 204 No Content with an empty body.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # OPTIONAL - forced_read_state
        """A boolean value to set all of the entries' forced_read_state. No change
        is made if this argument is not specified."""
        if forced_read_state is not None:
            data["forced_read_state"] = forced_read_state

        self.logger.debug("PUT /api/v1/courses/{course_id}/discussion_topics/{topic_id}/read_all with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/read_all".format(**path), data=data, params=params, no_data=True)

    def mark_all_entries_as_read_groups(self, group_id, topic_id, forced_read_state=None):
        """
        Mark all entries as read.

        Mark the discussion topic and all its entries as read.
        
        No request fields are necessary.
        
        On success, the response will be 204 No Content with an empty body.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # OPTIONAL - forced_read_state
        """A boolean value to set all of the entries' forced_read_state. No change
        is made if this argument is not specified."""
        if forced_read_state is not None:
            data["forced_read_state"] = forced_read_state

        self.logger.debug("PUT /api/v1/groups/{group_id}/discussion_topics/{topic_id}/read_all with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/groups/{group_id}/discussion_topics/{topic_id}/read_all".format(**path), data=data, params=params, no_data=True)

    def mark_all_entries_as_unread_courses(self, topic_id, course_id, forced_read_state=None):
        """
        Mark all entries as unread.

        Mark the discussion topic and all its entries as unread.
        
        No request fields are necessary.
        
        On success, the response will be 204 No Content with an empty body.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # OPTIONAL - forced_read_state
        """A boolean value to set all of the entries' forced_read_state. No change is
        made if this argument is not specified."""
        if forced_read_state is not None:
            params["forced_read_state"] = forced_read_state

        self.logger.debug("DELETE /api/v1/courses/{course_id}/discussion_topics/{topic_id}/read_all with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/read_all".format(**path), data=data, params=params, no_data=True)

    def mark_all_entries_as_unread_groups(self, group_id, topic_id, forced_read_state=None):
        """
        Mark all entries as unread.

        Mark the discussion topic and all its entries as unread.
        
        No request fields are necessary.
        
        On success, the response will be 204 No Content with an empty body.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # OPTIONAL - forced_read_state
        """A boolean value to set all of the entries' forced_read_state. No change is
        made if this argument is not specified."""
        if forced_read_state is not None:
            params["forced_read_state"] = forced_read_state

        self.logger.debug("DELETE /api/v1/groups/{group_id}/discussion_topics/{topic_id}/read_all with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/groups/{group_id}/discussion_topics/{topic_id}/read_all".format(**path), data=data, params=params, no_data=True)

    def mark_entry_as_read_courses(self, topic_id, entry_id, course_id, forced_read_state=None):
        """
        Mark entry as read.

        Mark a discussion entry as read.
        
        No request fields are necessary.
        
        On success, the response will be 204 No Content with an empty body.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # REQUIRED - PATH - entry_id
        """ID"""
        path["entry_id"] = entry_id

        # OPTIONAL - forced_read_state
        """A boolean value to set the entry's forced_read_state. No change is made if
        this argument is not specified."""
        if forced_read_state is not None:
            data["forced_read_state"] = forced_read_state

        self.logger.debug("PUT /api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/read with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/read".format(**path), data=data, params=params, no_data=True)

    def mark_entry_as_read_groups(self, group_id, topic_id, entry_id, forced_read_state=None):
        """
        Mark entry as read.

        Mark a discussion entry as read.
        
        No request fields are necessary.
        
        On success, the response will be 204 No Content with an empty body.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # REQUIRED - PATH - entry_id
        """ID"""
        path["entry_id"] = entry_id

        # OPTIONAL - forced_read_state
        """A boolean value to set the entry's forced_read_state. No change is made if
        this argument is not specified."""
        if forced_read_state is not None:
            data["forced_read_state"] = forced_read_state

        self.logger.debug("PUT /api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/read with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/read".format(**path), data=data, params=params, no_data=True)

    def mark_entry_as_unread_courses(self, topic_id, entry_id, course_id, forced_read_state=None):
        """
        Mark entry as unread.

        Mark a discussion entry as unread.
        
        No request fields are necessary.
        
        On success, the response will be 204 No Content with an empty body.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # REQUIRED - PATH - entry_id
        """ID"""
        path["entry_id"] = entry_id

        # OPTIONAL - forced_read_state
        """A boolean value to set the entry's forced_read_state. No change is made if
        this argument is not specified."""
        if forced_read_state is not None:
            params["forced_read_state"] = forced_read_state

        self.logger.debug("DELETE /api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/read with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/read".format(**path), data=data, params=params, no_data=True)

    def mark_entry_as_unread_groups(self, group_id, topic_id, entry_id, forced_read_state=None):
        """
        Mark entry as unread.

        Mark a discussion entry as unread.
        
        No request fields are necessary.
        
        On success, the response will be 204 No Content with an empty body.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # REQUIRED - PATH - entry_id
        """ID"""
        path["entry_id"] = entry_id

        # OPTIONAL - forced_read_state
        """A boolean value to set the entry's forced_read_state. No change is made if
        this argument is not specified."""
        if forced_read_state is not None:
            params["forced_read_state"] = forced_read_state

        self.logger.debug("DELETE /api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/read with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/read".format(**path), data=data, params=params, no_data=True)

    def rate_entry_courses(self, topic_id, entry_id, course_id, rating=None):
        """
        Rate entry.

        Rate a discussion entry.
        
        On success, the response will be 204 No Content with an empty body.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # REQUIRED - PATH - entry_id
        """ID"""
        path["entry_id"] = entry_id

        # OPTIONAL - rating
        """A rating to set on this entry. Only 0 and 1 are accepted."""
        if rating is not None:
            data["rating"] = rating

        self.logger.debug("POST /api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/rating with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/rating".format(**path), data=data, params=params, no_data=True)

    def rate_entry_groups(self, group_id, topic_id, entry_id, rating=None):
        """
        Rate entry.

        Rate a discussion entry.
        
        On success, the response will be 204 No Content with an empty body.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        # REQUIRED - PATH - entry_id
        """ID"""
        path["entry_id"] = entry_id

        # OPTIONAL - rating
        """A rating to set on this entry. Only 0 and 1 are accepted."""
        if rating is not None:
            data["rating"] = rating

        self.logger.debug("POST /api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/rating with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/rating".format(**path), data=data, params=params, no_data=True)

    def subscribe_to_topic_courses(self, topic_id, course_id):
        """
        Subscribe to a topic.

        Subscribe to a topic to receive notifications about new entries
        
        On success, the response will be 204 No Content with an empty body
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        self.logger.debug("PUT /api/v1/courses/{course_id}/discussion_topics/{topic_id}/subscribed with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/subscribed".format(**path), data=data, params=params, no_data=True)

    def subscribe_to_topic_groups(self, group_id, topic_id):
        """
        Subscribe to a topic.

        Subscribe to a topic to receive notifications about new entries
        
        On success, the response will be 204 No Content with an empty body
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        self.logger.debug("PUT /api/v1/groups/{group_id}/discussion_topics/{topic_id}/subscribed with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/groups/{group_id}/discussion_topics/{topic_id}/subscribed".format(**path), data=data, params=params, no_data=True)

    def unsubscribe_from_topic_courses(self, topic_id, course_id):
        """
        Unsubscribe from a topic.

        Unsubscribe from a topic to stop receiving notifications about new entries
        
        On success, the response will be 204 No Content with an empty body
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        self.logger.debug("DELETE /api/v1/courses/{course_id}/discussion_topics/{topic_id}/subscribed with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/subscribed".format(**path), data=data, params=params, no_data=True)

    def unsubscribe_from_topic_groups(self, group_id, topic_id):
        """
        Unsubscribe from a topic.

        Unsubscribe from a topic to stop receiving notifications about new entries
        
        On success, the response will be 204 No Content with an empty body
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - topic_id
        """ID"""
        path["topic_id"] = topic_id

        self.logger.debug("DELETE /api/v1/groups/{group_id}/discussion_topics/{topic_id}/subscribed with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/groups/{group_id}/discussion_topics/{topic_id}/subscribed".format(**path), data=data, params=params, no_data=True)


class Discussiontopic(BaseModel):
    """Discussiontopic Model.
    A discussion topic"""

    def __init__(self, lock_info=None, delayed_post_at=None, last_reply_at=None, only_graders_can_rate=None, subscription_hold=None, message=None, read_state=None, id=None, locked_for_user=None, subscribed=None, title=None, discussion_type=None, posted_at=None, require_initial_post=None, pinned=None, allow_rating=None, discussion_subentry_count=None, topic_children=None, user_name=None, sort_by_rating=None, root_topic_id=None, html_url=None, podcast_url=None, user_can_see_posts=None, permissions=None, locked=None, group_category_id=None, assignment_id=None, lock_at=None, attachments=None, unread_count=None, published=None, lock_explanation=None):
        """Init method for Discussiontopic class."""
        self._lock_info = lock_info
        self._delayed_post_at = delayed_post_at
        self._last_reply_at = last_reply_at
        self._only_graders_can_rate = only_graders_can_rate
        self._subscription_hold = subscription_hold
        self._message = message
        self._read_state = read_state
        self._id = id
        self._locked_for_user = locked_for_user
        self._subscribed = subscribed
        self._title = title
        self._discussion_type = discussion_type
        self._posted_at = posted_at
        self._require_initial_post = require_initial_post
        self._pinned = pinned
        self._allow_rating = allow_rating
        self._discussion_subentry_count = discussion_subentry_count
        self._topic_children = topic_children
        self._user_name = user_name
        self._sort_by_rating = sort_by_rating
        self._root_topic_id = root_topic_id
        self._html_url = html_url
        self._podcast_url = podcast_url
        self._user_can_see_posts = user_can_see_posts
        self._permissions = permissions
        self._locked = locked
        self._group_category_id = group_category_id
        self._assignment_id = assignment_id
        self._lock_at = lock_at
        self._attachments = attachments
        self._unread_count = unread_count
        self._published = published
        self._lock_explanation = lock_explanation

        self.logger = logging.getLogger('pycanvas.Discussiontopic')

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
    def delayed_post_at(self):
        """The datetime to publish the topic (if not right away)."""
        return self._delayed_post_at

    @delayed_post_at.setter
    def delayed_post_at(self, value):
        """Setter for delayed_post_at property."""
        self.logger.warn("Setting values on delayed_post_at will NOT update the remote Canvas instance.")
        self._delayed_post_at = value

    @property
    def last_reply_at(self):
        """The datetime for when the last reply was in the topic."""
        return self._last_reply_at

    @last_reply_at.setter
    def last_reply_at(self, value):
        """Setter for last_reply_at property."""
        self.logger.warn("Setting values on last_reply_at will NOT update the remote Canvas instance.")
        self._last_reply_at = value

    @property
    def only_graders_can_rate(self):
        """Whether or not grade permissions are required to rate entries."""
        return self._only_graders_can_rate

    @only_graders_can_rate.setter
    def only_graders_can_rate(self, value):
        """Setter for only_graders_can_rate property."""
        self.logger.warn("Setting values on only_graders_can_rate will NOT update the remote Canvas instance.")
        self._only_graders_can_rate = value

    @property
    def subscription_hold(self):
        """(Optional) Why the user cannot subscribe to this topic. Only one reason will be returned even if multiple apply. Can be one of: 'initial_post_required': The user must post a reply first; 'not_in_group_set': The user is not in the group set for this graded group discussion; 'not_in_group': The user is not in this topic's group; 'topic_is_announcement': This topic is an announcement."""
        return self._subscription_hold

    @subscription_hold.setter
    def subscription_hold(self, value):
        """Setter for subscription_hold property."""
        self.logger.warn("Setting values on subscription_hold will NOT update the remote Canvas instance.")
        self._subscription_hold = value

    @property
    def message(self):
        """The HTML content of the message body."""
        return self._message

    @message.setter
    def message(self, value):
        """Setter for message property."""
        self.logger.warn("Setting values on message will NOT update the remote Canvas instance.")
        self._message = value

    @property
    def read_state(self):
        """The read_state of the topic for the current user, 'read' or 'unread'."""
        return self._read_state

    @read_state.setter
    def read_state(self, value):
        """Setter for read_state property."""
        self.logger.warn("Setting values on read_state will NOT update the remote Canvas instance.")
        self._read_state = value

    @property
    def id(self):
        """The ID of this topic."""
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
    def subscribed(self):
        """Whether or not the current user is subscribed to this topic."""
        return self._subscribed

    @subscribed.setter
    def subscribed(self, value):
        """Setter for subscribed property."""
        self.logger.warn("Setting values on subscribed will NOT update the remote Canvas instance.")
        self._subscribed = value

    @property
    def title(self):
        """The topic title."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value

    @property
    def discussion_type(self):
        """The type of discussion. Values are 'side_comment', for discussions that only allow one level of nested comments, and 'threaded' for fully threaded discussions."""
        return self._discussion_type

    @discussion_type.setter
    def discussion_type(self, value):
        """Setter for discussion_type property."""
        self.logger.warn("Setting values on discussion_type will NOT update the remote Canvas instance.")
        self._discussion_type = value

    @property
    def posted_at(self):
        """The datetime the topic was posted. If it is null it hasn't been posted yet. (see delayed_post_at)."""
        return self._posted_at

    @posted_at.setter
    def posted_at(self, value):
        """Setter for posted_at property."""
        self.logger.warn("Setting values on posted_at will NOT update the remote Canvas instance.")
        self._posted_at = value

    @property
    def require_initial_post(self):
        """If true then a user may not respond to other replies until that user has made an initial reply. Defaults to false."""
        return self._require_initial_post

    @require_initial_post.setter
    def require_initial_post(self, value):
        """Setter for require_initial_post property."""
        self.logger.warn("Setting values on require_initial_post will NOT update the remote Canvas instance.")
        self._require_initial_post = value

    @property
    def pinned(self):
        """Whether or not the discussion has been 'pinned' by an instructor."""
        return self._pinned

    @pinned.setter
    def pinned(self, value):
        """Setter for pinned property."""
        self.logger.warn("Setting values on pinned will NOT update the remote Canvas instance.")
        self._pinned = value

    @property
    def allow_rating(self):
        """Whether or not users can rate entries in this topic."""
        return self._allow_rating

    @allow_rating.setter
    def allow_rating(self, value):
        """Setter for allow_rating property."""
        self.logger.warn("Setting values on allow_rating will NOT update the remote Canvas instance.")
        self._allow_rating = value

    @property
    def discussion_subentry_count(self):
        """The count of entries in the topic."""
        return self._discussion_subentry_count

    @discussion_subentry_count.setter
    def discussion_subentry_count(self, value):
        """Setter for discussion_subentry_count property."""
        self.logger.warn("Setting values on discussion_subentry_count will NOT update the remote Canvas instance.")
        self._discussion_subentry_count = value

    @property
    def topic_children(self):
        """An array of topic_ids for the group discussions the user is a part of."""
        return self._topic_children

    @topic_children.setter
    def topic_children(self, value):
        """Setter for topic_children property."""
        self.logger.warn("Setting values on topic_children will NOT update the remote Canvas instance.")
        self._topic_children = value

    @property
    def user_name(self):
        """The username of the topic creator."""
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        """Setter for user_name property."""
        self.logger.warn("Setting values on user_name will NOT update the remote Canvas instance.")
        self._user_name = value

    @property
    def sort_by_rating(self):
        """Whether or not entries should be sorted by rating."""
        return self._sort_by_rating

    @sort_by_rating.setter
    def sort_by_rating(self, value):
        """Setter for sort_by_rating property."""
        self.logger.warn("Setting values on sort_by_rating will NOT update the remote Canvas instance.")
        self._sort_by_rating = value

    @property
    def root_topic_id(self):
        """If the topic is for grading and a group assignment this will point to the original topic in the course."""
        return self._root_topic_id

    @root_topic_id.setter
    def root_topic_id(self, value):
        """Setter for root_topic_id property."""
        self.logger.warn("Setting values on root_topic_id will NOT update the remote Canvas instance.")
        self._root_topic_id = value

    @property
    def html_url(self):
        """The URL to the discussion topic in canvas."""
        return self._html_url

    @html_url.setter
    def html_url(self, value):
        """Setter for html_url property."""
        self.logger.warn("Setting values on html_url will NOT update the remote Canvas instance.")
        self._html_url = value

    @property
    def podcast_url(self):
        """If the topic is a podcast topic this is the feed url for the current user."""
        return self._podcast_url

    @podcast_url.setter
    def podcast_url(self, value):
        """Setter for podcast_url property."""
        self.logger.warn("Setting values on podcast_url will NOT update the remote Canvas instance.")
        self._podcast_url = value

    @property
    def user_can_see_posts(self):
        """Whether or not posts in this topic are visible to the user."""
        return self._user_can_see_posts

    @user_can_see_posts.setter
    def user_can_see_posts(self, value):
        """Setter for user_can_see_posts property."""
        self.logger.warn("Setting values on user_can_see_posts will NOT update the remote Canvas instance.")
        self._user_can_see_posts = value

    @property
    def permissions(self):
        """The current user's permissions on this topic."""
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """Setter for permissions property."""
        self.logger.warn("Setting values on permissions will NOT update the remote Canvas instance.")
        self._permissions = value

    @property
    def locked(self):
        """Whether or not the discussion is 'closed for comments'."""
        return self._locked

    @locked.setter
    def locked(self, value):
        """Setter for locked property."""
        self.logger.warn("Setting values on locked will NOT update the remote Canvas instance.")
        self._locked = value

    @property
    def group_category_id(self):
        """The unique identifier of the group category if the topic is a group discussion, otherwise null."""
        return self._group_category_id

    @group_category_id.setter
    def group_category_id(self, value):
        """Setter for group_category_id property."""
        self.logger.warn("Setting values on group_category_id will NOT update the remote Canvas instance.")
        self._group_category_id = value

    @property
    def assignment_id(self):
        """The unique identifier of the assignment if the topic is for grading, otherwise null."""
        return self._assignment_id

    @assignment_id.setter
    def assignment_id(self, value):
        """Setter for assignment_id property."""
        self.logger.warn("Setting values on assignment_id will NOT update the remote Canvas instance.")
        self._assignment_id = value

    @property
    def lock_at(self):
        """The datetime to lock the topic (if ever)."""
        return self._lock_at

    @lock_at.setter
    def lock_at(self, value):
        """Setter for lock_at property."""
        self.logger.warn("Setting values on lock_at will NOT update the remote Canvas instance.")
        self._lock_at = value

    @property
    def attachments(self):
        """Array of file attachments."""
        return self._attachments

    @attachments.setter
    def attachments(self, value):
        """Setter for attachments property."""
        self.logger.warn("Setting values on attachments will NOT update the remote Canvas instance.")
        self._attachments = value

    @property
    def unread_count(self):
        """The count of unread entries of this topic for the current user."""
        return self._unread_count

    @unread_count.setter
    def unread_count(self, value):
        """Setter for unread_count property."""
        self.logger.warn("Setting values on unread_count will NOT update the remote Canvas instance.")
        self._unread_count = value

    @property
    def published(self):
        """Whether this discussion topic is published (true) or draft state (false)."""
        return self._published

    @published.setter
    def published(self, value):
        """Setter for published property."""
        self.logger.warn("Setting values on published will NOT update the remote Canvas instance.")
        self._published = value

    @property
    def lock_explanation(self):
        """(Optional) An explanation of why this is locked for the user. Present when locked_for_user is true."""
        return self._lock_explanation

    @lock_explanation.setter
    def lock_explanation(self, value):
        """Setter for lock_explanation property."""
        self.logger.warn("Setting values on lock_explanation will NOT update the remote Canvas instance.")
        self._lock_explanation = value


class Fileattachment(BaseModel):
    """Fileattachment Model.
    A file attachment"""

    def __init__(self, url=None, display_name=None, content_type=None, filename=None):
        """Init method for Fileattachment class."""
        self._url = url
        self._display_name = display_name
        self._content_type = content_type
        self._filename = filename

        self.logger = logging.getLogger('pycanvas.Fileattachment')

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
    def filename(self):
        """filename."""
        return self._filename

    @filename.setter
    def filename(self, value):
        """Setter for filename property."""
        self.logger.warn("Setting values on filename will NOT update the remote Canvas instance.")
        self._filename = value

