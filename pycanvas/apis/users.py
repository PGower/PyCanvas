"""Users API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class UsersAPI(BaseCanvasAPI):
    """Users API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for UsersAPI."""
        super(UsersAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.UsersAPI")

    def list_users_in_account(self, account_id, search_term=None):
        """
        List users in account.

        Retrieve the list of users associated with this account.
        
         @example_request
           curl https://<canvas>/api/v1/accounts/self/users?search_term=<sis_user_id> \
              -X GET \
              -H 'Authorization: Bearer <token>'
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # OPTIONAL - search_term - The partial name or full ID of the users to match and return in the results list. Must be at least 3 characters.
        if search_term is not None:
            params["search_term"] = search_term

        self.logger.debug("GET /api/v1/accounts/{account_id}/users with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/users".format(**path), data=data, params=params, all_pages=True)

    def list_activity_stream_self(self):
        """
        List the activity stream.

        Returns the current user's global activity stream, paginated.
        
        There are many types of objects that can be returned in the activity
        stream. All object types have the same basic set of shared attributes:
          !!!javascript
          {
            'created_at': '2011-07-13T09:12:00Z',
            'updated_at': '2011-07-25T08:52:41Z',
            'id': 1234,
            'title': 'Stream Item Subject',
            'message': 'This is the body text of the activity stream item. It is plain-text, and can be multiple paragraphs.',
            'type': 'DiscussionTopic|Conversation|Message|Submission|Conference|Collaboration|AssessmentRequest...',
            'read_state': false,
            'context_type': 'course', // course|group
            'course_id': 1,
            'group_id': null,
            'html_url': "http://..." // URL to the Canvas web UI for this stream item
          }
        
        In addition, each item type has its own set of attributes available.
        
        DiscussionTopic:
        
          !!!javascript
          {
            'type': 'DiscussionTopic',
            'discussion_topic_id': 1234,
            'total_root_discussion_entries': 5,
            'require_initial_post': true,
            'user_has_posted': true,
            'root_discussion_entries': {
              ...
            }
          }
        
        For DiscussionTopic, the message is truncated at 4kb.
        
        Announcement:
        
          !!!javascript
          {
            'type': 'Announcement',
            'announcement_id': 1234,
            'total_root_discussion_entries': 5,
            'require_initial_post': true,
            'user_has_posted': null,
            'root_discussion_entries': {
              ...
            }
          }
        
        For Announcement, the message is truncated at 4kb.
        
        Conversation:
        
          !!!javascript
          {
            'type': 'Conversation',
            'conversation_id': 1234,
            'private': false,
            'participant_count': 3,
          }
        
        Message:
        
          !!!javascript
          {
            'type': 'Message',
            'message_id': 1234,
            'notification_category': 'Assignment Graded'
          }
        
        Submission:
        
        Returns an {api:Submissions:Submission Submission} with its Course and Assignment data.
        
        Conference:
        
          !!!javascript
          {
            'type': 'Conference',
            'web_conference_id': 1234
          }
        
        Collaboration:
        
          !!!javascript
          {
            'type': 'Collaboration',
            'collaboration_id': 1234
          }
        
        AssessmentRequest:
        
          !!!javascript
          {
            'type': 'AssessmentRequest',
            'assessment_request_id': 1234
          }
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("GET /api/v1/users/self/activity_stream with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/self/activity_stream".format(**path), data=data, params=params, no_data=True)

    def list_activity_stream_activity_stream(self):
        """
        List the activity stream.

        Returns the current user's global activity stream, paginated.
        
        There are many types of objects that can be returned in the activity
        stream. All object types have the same basic set of shared attributes:
          !!!javascript
          {
            'created_at': '2011-07-13T09:12:00Z',
            'updated_at': '2011-07-25T08:52:41Z',
            'id': 1234,
            'title': 'Stream Item Subject',
            'message': 'This is the body text of the activity stream item. It is plain-text, and can be multiple paragraphs.',
            'type': 'DiscussionTopic|Conversation|Message|Submission|Conference|Collaboration|AssessmentRequest...',
            'read_state': false,
            'context_type': 'course', // course|group
            'course_id': 1,
            'group_id': null,
            'html_url': "http://..." // URL to the Canvas web UI for this stream item
          }
        
        In addition, each item type has its own set of attributes available.
        
        DiscussionTopic:
        
          !!!javascript
          {
            'type': 'DiscussionTopic',
            'discussion_topic_id': 1234,
            'total_root_discussion_entries': 5,
            'require_initial_post': true,
            'user_has_posted': true,
            'root_discussion_entries': {
              ...
            }
          }
        
        For DiscussionTopic, the message is truncated at 4kb.
        
        Announcement:
        
          !!!javascript
          {
            'type': 'Announcement',
            'announcement_id': 1234,
            'total_root_discussion_entries': 5,
            'require_initial_post': true,
            'user_has_posted': null,
            'root_discussion_entries': {
              ...
            }
          }
        
        For Announcement, the message is truncated at 4kb.
        
        Conversation:
        
          !!!javascript
          {
            'type': 'Conversation',
            'conversation_id': 1234,
            'private': false,
            'participant_count': 3,
          }
        
        Message:
        
          !!!javascript
          {
            'type': 'Message',
            'message_id': 1234,
            'notification_category': 'Assignment Graded'
          }
        
        Submission:
        
        Returns an {api:Submissions:Submission Submission} with its Course and Assignment data.
        
        Conference:
        
          !!!javascript
          {
            'type': 'Conference',
            'web_conference_id': 1234
          }
        
        Collaboration:
        
          !!!javascript
          {
            'type': 'Collaboration',
            'collaboration_id': 1234
          }
        
        AssessmentRequest:
        
          !!!javascript
          {
            'type': 'AssessmentRequest',
            'assessment_request_id': 1234
          }
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("GET /api/v1/users/activity_stream with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/activity_stream".format(**path), data=data, params=params, no_data=True)

    def activity_stream_summary(self):
        """
        Activity stream summary.

        Returns a summary of the current user's global activity stream.
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("GET /api/v1/users/self/activity_stream/summary with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/self/activity_stream/summary".format(**path), data=data, params=params, no_data=True)

    def list_todo_items(self):
        """
        List the TODO items.

        Returns the current user's list of todo items, as seen on the user dashboard.
        
        There is a limit to the number of items returned.
        
        The `ignore` and `ignore_permanently` URLs can be used to update the user's
        preferences on what items will be displayed.
        Performing a DELETE request against the `ignore` URL will hide that item
        from future todo item requests, until the item changes.
        Performing a DELETE request against the `ignore_permanently` URL will hide
        that item forever.
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("GET /api/v1/users/self/todo with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/self/todo".format(**path), data=data, params=params, no_data=True)

    def list_upcoming_assignments_calendar_events(self):
        """
        List upcoming assignments, calendar events.

        Returns the current user's upcoming events, i.e. the same things shown
        in the dashboard 'Coming Up' sidebar.
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("GET /api/v1/users/self/upcoming_events with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/self/upcoming_events".format(**path), data=data, params=params, no_data=True)

    def hide_stream_item(self, id):
        """
        Hide a stream item.

        Hide the given stream item.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("DELETE /api/v1/users/self/activity_stream/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/users/self/activity_stream/{id}".format(**path), data=data, params=params, no_data=True)

    def hide_all_stream_items(self):
        """
        Hide all stream items.

        Hide all stream items for the user
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("DELETE /api/v1/users/self/activity_stream with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/users/self/activity_stream".format(**path), data=data, params=params, no_data=True)

    def upload_file(self, user_id):
        """
        Upload a file.

        Upload a file to the user's personal files section.
        
        This API endpoint is the first step in uploading a file to a user's files.
        See the {file:file_uploads.html File Upload Documentation} for details on
        the file upload workflow.
        
        Note that typically users will only be able to upload files to their
        own files section. Passing a user_id of +self+ is an easy shortcut
        to specify the current user.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id - ID
        path["user_id"] = user_id

        self.logger.debug("POST /api/v1/users/{user_id}/files with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/users/{user_id}/files".format(**path), data=data, params=params, no_data=True)

    def show_user_details(self, id):
        """
        Show user details.

        Shows details for user.
        
        Also includes an attribute "permissions", a non-comprehensive list of permissions for the user.
        Example:
          !!!javascript
          "permissions": {
           "can_update_name": true, // Whether the user can update their name.
           "can_update_avatar": false // Whether the user can update their avatar.
          }
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("GET /api/v1/users/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{id}".format(**path), data=data, params=params, single_item=True)

    def create_user(self, account_id, pseudonym_unique_id, communication_channel_address=None, communication_channel_confirmation_url=None, communication_channel_skip_confirmation=None, communication_channel_type=None, force_validations=None, pseudonym_password=None, pseudonym_send_confirmation=None, pseudonym_sis_user_id=None, user_birthdate=None, user_locale=None, user_name=None, user_short_name=None, user_sortable_name=None, user_terms_of_use=None, user_time_zone=None):
        """
        Create a user.

        Create and return a new user and pseudonym for an account.
        
        If you don't have the "Modify login details for users" permission, but
        self-registration is enabled on the account, you can still use this
        endpoint to register new users. Certain fields will be required, and
        others will be ignored (see below).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # OPTIONAL - user[name] - The full name of the user. This name will be used by teacher for grading. Required if this is a self-registration.
        if user_name is not None:
            data["user[name]"] = user_name
        # OPTIONAL - user[short_name] - User's name as it will be displayed in discussions, messages, and comments.
        if user_short_name is not None:
            data["user[short_name]"] = user_short_name
        # OPTIONAL - user[sortable_name] - User's name as used to sort alphabetically in lists.
        if user_sortable_name is not None:
            data["user[sortable_name]"] = user_sortable_name
        # OPTIONAL - user[time_zone] - The time zone for the user. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}.
        if user_time_zone is not None:
            data["user[time_zone]"] = user_time_zone
        # OPTIONAL - user[locale] - The user's preferred language as a two-letter ISO 639-1 code.
        if user_locale is not None:
            data["user[locale]"] = user_locale
        # OPTIONAL - user[birthdate] - The user's birth date.
        if user_birthdate is not None:
            data["user[birthdate]"] = user_birthdate
        # OPTIONAL - user[terms_of_use] - Whether the user accepts the terms of use. Required if this is a self-registration and this canvas instance requires users to accept the terms (on by default).
        if user_terms_of_use is not None:
            data["user[terms_of_use]"] = user_terms_of_use
        # REQUIRED - pseudonym[unique_id] - User's login ID. If this is a self-registration, it must be a valid email address.
        data["pseudonym[unique_id]"] = pseudonym_unique_id
        # OPTIONAL - pseudonym[password] - User's password. Cannot be set during self-registration.
        if pseudonym_password is not None:
            data["pseudonym[password]"] = pseudonym_password
        # OPTIONAL - pseudonym[sis_user_id] - SIS ID for the user's account. To set this parameter, the caller must be able to manage SIS permissions.
        if pseudonym_sis_user_id is not None:
            data["pseudonym[sis_user_id]"] = pseudonym_sis_user_id
        # OPTIONAL - pseudonym[send_confirmation] - Send user notification of account creation if true. Automatically set to true during self-registration.
        if pseudonym_send_confirmation is not None:
            data["pseudonym[send_confirmation]"] = pseudonym_send_confirmation
        # OPTIONAL - communication_channel[type] - The communication channel type, e.g. 'email' or 'sms'.
        if communication_channel_type is not None:
            data["communication_channel[type]"] = communication_channel_type
        # OPTIONAL - communication_channel[address] - The communication channel address, e.g. the user's email address.
        if communication_channel_address is not None:
            data["communication_channel[address]"] = communication_channel_address
        # OPTIONAL - communication_channel[confirmation_url] - Only valid for account admins. If true, returns the new user account confirmation URL in the response.
        if communication_channel_confirmation_url is not None:
            data["communication_channel[confirmation_url]"] = communication_channel_confirmation_url
        # OPTIONAL - communication_channel[skip_confirmation] - Only valid for site admins and account admins making requests; If true, the channel is automatically validated and no confirmation email or SMS is sent. Otherwise, the user must respond to a confirmation message to confirm the channel.
        if communication_channel_skip_confirmation is not None:
            data["communication_channel[skip_confirmation]"] = communication_channel_skip_confirmation
        # OPTIONAL - force_validations - If true, validations are performed on the newly created user (and their associated pseudonym) even if the request is made by a privileged user like an admin. When set to false, or not included in the request parameters, any newly created users are subject to validations unless the request is made by a user with a 'manage_user_logins' right. In which case, certain validations such as 'require_acceptance_of_terms' and 'require_presence_of_name' are not enforced. Use this parameter to return helpful json errors while building users with an admin request.
        if force_validations is not None:
            data["force_validations"] = force_validations

        self.logger.debug("POST /api/v1/accounts/{account_id}/users with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/users".format(**path), data=data, params=params, single_item=True)

    def update_user_settings(self, id, manual_mark_as_read=None):
        """
        Update user settings.

        Update an existing user's settings.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id - ID
        path["id"] = id
        # OPTIONAL - manual_mark_as_read - If true, require user to manually mark discussion posts as read (don't auto-mark as read).
        if manual_mark_as_read is not None:
            params["manual_mark_as_read"] = manual_mark_as_read

        self.logger.debug("GET /api/v1/users/{id}/settings with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{id}/settings".format(**path), data=data, params=params, no_data=True)

    def edit_user(self, id, user_avatar_token=None, user_avatar_url=None, user_locale=None, user_name=None, user_short_name=None, user_sortable_name=None, user_time_zone=None):
        """
        Edit a user.

        Modify an existing user. To modify a user's login, see the documentation for logins.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id - ID
        path["id"] = id
        # OPTIONAL - user[name] - The full name of the user. This name will be used by teacher for grading.
        if user_name is not None:
            data["user[name]"] = user_name
        # OPTIONAL - user[short_name] - User's name as it will be displayed in discussions, messages, and comments.
        if user_short_name is not None:
            data["user[short_name]"] = user_short_name
        # OPTIONAL - user[sortable_name] - User's name as used to sort alphabetically in lists.
        if user_sortable_name is not None:
            data["user[sortable_name]"] = user_sortable_name
        # OPTIONAL - user[time_zone] - The time zone for the user. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}.
        if user_time_zone is not None:
            data["user[time_zone]"] = user_time_zone
        # OPTIONAL - user[locale] - The user's preferred language as a two-letter ISO 639-1 code.
        if user_locale is not None:
            data["user[locale]"] = user_locale
        # OPTIONAL - user[avatar][token] - A unique representation of the avatar record to assign as the user's current avatar. This token can be obtained from the user avatars endpoint. This supersedes the user [avatar] [url] argument, and if both are included the url will be ignored. Note: this is an internal representation and is subject to change without notice. It should be consumed with this api endpoint and used in the user update endpoint, and should not be constructed by the client.
        if user_avatar_token is not None:
            data["user[avatar][token]"] = user_avatar_token
        # OPTIONAL - user[avatar][url] - To set the user's avatar to point to an external url, do not include a token and instead pass the url here. Warning: For maximum compatibility, please use 128 px square images.
        if user_avatar_url is not None:
            data["user[avatar][url]"] = user_avatar_url

        self.logger.debug("PUT /api/v1/users/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/users/{id}".format(**path), data=data, params=params, single_item=True)

    def merge_user_into_another_user_destination_user_id(self, id, destination_user_id):
        """
        Merge user into another user.

        Merge a user into another user.
        To merge users, the caller must have permissions to manage both users.
        
        When finding users by SIS ids in different accounts the
        destination_account_id is required.
        
        The account can also be identified by passing the domain in destination_account_id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id - ID
        path["id"] = id
        # REQUIRED - PATH - destination_user_id - ID
        path["destination_user_id"] = destination_user_id

        self.logger.debug("PUT /api/v1/users/{id}/merge_into/{destination_user_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/users/{id}/merge_into/{destination_user_id}".format(**path), data=data, params=params, single_item=True)

    def merge_user_into_another_user_accounts(self, id, destination_user_id, destination_account_id):
        """
        Merge user into another user.

        Merge a user into another user.
        To merge users, the caller must have permissions to manage both users.
        
        When finding users by SIS ids in different accounts the
        destination_account_id is required.
        
        The account can also be identified by passing the domain in destination_account_id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id - ID
        path["id"] = id
        # REQUIRED - PATH - destination_account_id - ID
        path["destination_account_id"] = destination_account_id
        # REQUIRED - PATH - destination_user_id - ID
        path["destination_user_id"] = destination_user_id

        self.logger.debug("PUT /api/v1/users/{id}/merge_into/accounts/{destination_account_id}/users/{destination_user_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/users/{id}/merge_into/accounts/{destination_account_id}/users/{destination_user_id}".format(**path), data=data, params=params, single_item=True)

    def get_user_profile(self, user_id):
        """
        Get user profile.

        Returns user profile data, including user id, name, and profile pic.
        
        When requesting the profile for the user accessing the API, the user's
        calendar feed URL will be returned as well.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id - ID
        path["user_id"] = user_id

        self.logger.debug("GET /api/v1/users/{user_id}/profile with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/profile".format(**path), data=data, params=params, single_item=True)

    def list_avatar_options(self, user_id):
        """
        List avatar options.

        Retrieve the possible user avatar options that can be set with the user update endpoint. The response will be an array of avatar records. If the 'type' field is 'attachment', the record will include all the normal attachment json fields; otherwise it will include only the 'url' and 'display_name' fields. Additionally, all records will include a 'type' field and a 'token' field. The following explains each field in more detail
        type:: ["gravatar"|"attachment"|"no_pic"] The type of avatar record, for categorization purposes.
        url:: The url of the avatar
        token:: A unique representation of the avatar record which can be used to set the avatar with the user update endpoint. Note: this is an internal representation and is subject to change without notice. It should be consumed with this api endpoint and used in the user update endpoint, and should not be constructed by the client.
        display_name:: A textual description of the avatar record
        id:: ['attachment' type only] the internal id of the attachment
        content-type:: ['attachment' type only] the content-type of the attachment
        filename:: ['attachment' type only] the filename of the attachment
        size:: ['attachment' type only] the size of the attachment
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id - ID
        path["user_id"] = user_id

        self.logger.debug("GET /api/v1/users/{user_id}/avatars with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/avatars".format(**path), data=data, params=params, all_pages=True)

    def list_user_page_views(self, user_id, end_time=None, start_time=None):
        """
        List user page views.

        Return the user's page view history in json format, similar to the
        available CSV download. Pagination is used as described in API basics
        section. Page views are returned in descending order, newest to oldest.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id - ID
        path["user_id"] = user_id
        # OPTIONAL - start_time - The beginning of the time range from which you want page views.
        if start_time is not None:
            if issubclass(start_time.__class__, date) or issubclass(start_time.__class__, datetime):
                start_time = start_time.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            elif issubclass(start_time.__class__, basestring):
                start_time = self._validate_iso8601_string(start_time)
            params["start_time"] = start_time
        # OPTIONAL - end_time - The end of the time range from which you want page views.
        if end_time is not None:
            if issubclass(end_time.__class__, date) or issubclass(end_time.__class__, datetime):
                end_time = end_time.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            elif issubclass(end_time.__class__, basestring):
                end_time = self._validate_iso8601_string(end_time)
            params["end_time"] = end_time

        self.logger.debug("GET /api/v1/users/{user_id}/page_views with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/page_views".format(**path), data=data, params=params, all_pages=True)

    def store_custom_data(self, ns, data, user_id):
        """
        Store custom data.

        Store arbitrary user data as JSON.
        
        Arbitrary JSON data can be stored for a User.
        A typical scenario would be an external site/service that registers users in Canvas
        and wants to capture additional info about them.  The part of the URL that follows
        +/custom_data/+ defines the scope of the request, and it reflects the structure of
        the JSON data to be stored or retrieved.
        
        A namespace parameter, +ns+, is used to prevent custom_data collisions between
        different apps.  This parameter is required for all custom_data requests.
        
        A request with Content-Type multipart/form-data or Content-Type
        application/x-www-form-urlencoded can only be used to store strings.
        
        Example PUT with multipart/form-data data:
          curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/telephone' \
            -X PUT \
            -F 'ns=com.my-organization.canvas-app' \
            -F 'data=555-1234' \
            -H 'Authorization: Bearer <token>'
        
        Response:
          !!!javascript
          {
            "data": "555-1234"
          }
        
        Subscopes (or, generated scopes) can also be specified by passing values to
        data[<subscope>].
        
        Example PUT specifying subscopes:
          curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/body/measurements' \
            -X PUT \
            -F 'ns=com.my-organization.canvas-app' \
            -F 'data[waist]=32in' \
            -F 'data[inseam]=34in' \
            -F 'data[chest]=40in' \
            -H 'Authorization: Bearer <token>'
        
        Response:
          !!!javascript
          {
            "data": {
              "chest": "40in",
              "waist": "32in",
              "inseam": "34in"
            }
          }
        
        Following such a request, subsets of the stored data to be retrieved directly from a subscope.
        
        Example {api:UsersController#get_custom_data GET} from a generated scope
          curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/body/measurements/chest' \
            -X GET \
            -F 'ns=com.my-organization.canvas-app' \
            -H 'Authorization: Bearer <token>'
        
        Response:
          !!!javascript
          {
            "data": "40in"
          }
        
        If you want to store more than just strings (i.e. numbers, arrays, hashes, true, false,
        and/or null), you must make a request with Content-Type application/json as in the following
        example.
        
        Example PUT with JSON data:
          curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
            -H 'Content-Type: application/json' \
            -X PUT \
            -d '{
                  "ns": "com.my-organization.canvas-app",
                  "data": {
                    "a-number": 6.02e23,
                    "a-bool": true,
                    "a-string": "true",
                    "a-hash": {"a": {"b": "ohai"}},
                    "an-array": [1, "two", null, false]
                  }
                }' \
            -H 'Authorization: Bearer <token>'
        
        Response:
          !!!javascript
          {
            "data": {
              "a-number": 6.02e+23,
              "a-bool": true,
              "a-string": "true",
              "a-hash": {
                "a": {
                  "b": "ohai"
                }
              },
              "an-array": [1, "two", null, false]
            }
          }
        
        If the data is an Object (as it is in the above example), then subsets of the data can
        be accessed by including the object's (possibly nested) keys in the scope of a GET request.
        
        Example {api:UsersController#get_custom_data GET} with a generated scope:
          curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/a-hash/a/b' \
            -X GET \
            -F 'ns=com.my-organization.canvas-app' \
            -H 'Authorization: Bearer <token>'
        
        Response:
          !!!javascript
          {
            "data": "ohai"
          }
        
        
        On success, this endpoint returns an object containing the data that was stored.
        
        Responds with status code 200 if the scope already contained data, and it was overwritten
        by the data specified in the request.
        
        Responds with status code 201 if the scope was previously empty, and the data specified
        in the request was successfully stored there.
        
        Responds with status code 400 if the namespace parameter, +ns+, is missing or invalid, or if
        the +data+ parameter is missing.
        
        Responds with status code 409 if the requested scope caused a conflict and data was not stored.
        This happens when storing data at the requested scope would cause data at an outer scope
        to be lost.  e.g., if +/custom_data+ was +{"fashion_app": {"hair": "blonde"}}+, but
        you tried to +`PUT /custom_data/fashion_app/hair/style -F data=buzz`+, then for the request
        to succeed,the value of +/custom_data/fashion_app/hair+ would have to become a hash, and its
        old string value would be lost.  In this situation, an error object is returned with the
        following format:
        
          !!!javascript
          {
            "message": "write conflict for custom_data hash",
            "conflict_scope": "fashion_app/hair",
            "type_at_conflict": "String",
            "value_at_conflict": "blonde"
          }
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id - ID
        path["user_id"] = user_id
        # REQUIRED - ns - The namespace under which to store the data. This should be something other Canvas API apps aren't likely to use, such as a reverse DNS for your organization.
        data["ns"] = ns
        # REQUIRED - data - The data you want to store for the user, at the specified scope. If the data is composed of (possibly nested) JSON objects, scopes will be generated for the (nested) keys (see examples).
        data["data"] = data

        self.logger.debug("PUT /api/v1/users/{user_id}/custom_data with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/users/{user_id}/custom_data".format(**path), data=data, params=params, no_data=True)

    def load_custom_data(self, ns, user_id):
        """
        Load custom data.

        Load custom user data.
        
        Arbitrary JSON data can be stored for a User.  This API call
        retrieves that data for a (optional) given scope.
        See {api:UsersController#set_custom_data Store Custom Data} for details and
        examples.
        
        On success, this endpoint returns an object containing the data that was requested.
        
        Responds with status code 400 if the namespace parameter, +ns+, is missing or invalid,
        or if the specified scope does not contain any data.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id - ID
        path["user_id"] = user_id
        # REQUIRED - ns - The namespace from which to retrieve the data. This should be something other Canvas API apps aren't likely to use, such as a reverse DNS for your organization.
        params["ns"] = ns

        self.logger.debug("GET /api/v1/users/{user_id}/custom_data with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/custom_data".format(**path), data=data, params=params, no_data=True)

    def delete_custom_data(self, ns, user_id):
        """
        Delete custom data.

        Delete custom user data.
        
        Arbitrary JSON data can be stored for a User.  This API call
        deletes that data for a given scope.  Without a scope, all custom_data is deleted.
        See {api:UsersController#set_custom_data Store Custom Data} for details and
        examples of storage and retrieval.
        
        As an example, we'll store some data, then delete a subset of it.
        
        Example {api:UsersController#set_custom_data PUT} with valid JSON data:
          curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
            -X PUT \
            -F 'ns=com.my-organization.canvas-app' \
            -F 'data[fruit][apple]=so tasty' \
            -F 'data[fruit][kiwi]=a bit sour' \
            -F 'data[veggies][root][onion]=tear-jerking' \
            -H 'Authorization: Bearer <token>'
        
        Response:
          !!!javascript
          {
            "data": {
              "fruit": {
                "apple": "so tasty",
                "kiwi": "a bit sour"
              },
              "veggies": {
                "root": {
                  "onion": "tear-jerking"
                }
              }
            }
          }
        
        Example DELETE:
          curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/fruit/kiwi' \
            -X DELETE \
            -F 'ns=com.my-organization.canvas-app' \
            -H 'Authorization: Bearer <token>'
        
        Response:
          !!!javascript
          {
            "data": "a bit sour"
          }
        
        Example {api:UsersController#get_custom_data GET} following the above DELETE:
          curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
            -X GET \
            -F 'ns=com.my-organization.canvas-app' \
            -H 'Authorization: Bearer <token>'
        
        Response:
          !!!javascript
          {
            "data": {
              "fruit": {
                "apple": "so tasty"
              },
              "veggies": {
                "root": {
                  "onion": "tear-jerking"
                }
              }
            }
          }
        
        Note that hashes left empty after a DELETE will get removed from the custom_data store.
        For example, following the previous commands, if we delete /custom_data/veggies/root/onion,
        then the entire /custom_data/veggies scope will be removed.
        
        Example DELETE that empties a parent scope:
          curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/veggies/root/onion' \
            -X DELETE \
            -F 'ns=com.my-organization.canvas-app' \
            -H 'Authorization: Bearer <token>'
        
        Response:
          !!!javascript
          {
            "data": "tear-jerking"
          }
        
        Example {api:UsersController#get_custom_data GET} following the above DELETE:
          curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
            -X GET \
            -F 'ns=com.my-organization.canvas-app' \
            -H 'Authorization: Bearer <token>'
        
        Response:
          !!!javascript
          {
            "data": {
              "fruit": {
                "apple": "so tasty"
              }
            }
          }
        
        On success, this endpoint returns an object containing the data that was deleted.
        
        Responds with status code 400 if the namespace parameter, +ns+, is missing or invalid,
        or if the specified scope does not contain any data.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id - ID
        path["user_id"] = user_id
        # REQUIRED - ns - The namespace from which to delete the data. This should be something other Canvas API apps aren't likely to use, such as a reverse DNS for your organization.
        params["ns"] = ns

        self.logger.debug("DELETE /api/v1/users/{user_id}/custom_data with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/users/{user_id}/custom_data".format(**path), data=data, params=params, no_data=True)


class Profile(BaseModel):
    """Profile Model.
    Profile details for a Canvas user."""

    def __init__(self, bio=None, login_id=None, sortable_name=None, name=None, short_name=None, title=None, locale=None, sis_user_id=None, time_zone=None, avatar_url=None, primary_email=None, calendar=None, sis_login_id=None, id=None):
        """Init method for Profile class."""
        self._bio = bio
        self._login_id = login_id
        self._sortable_name = sortable_name
        self._name = name
        self._short_name = short_name
        self._title = title
        self._locale = locale
        self._sis_user_id = sis_user_id
        self._time_zone = time_zone
        self._avatar_url = avatar_url
        self._primary_email = primary_email
        self._calendar = calendar
        self._sis_login_id = sis_login_id
        self._id = id

        self.logger = logging.getLogger('pycanvas.Profile')

    @property
    def bio(self):
        """bio."""
        return self._bio

    @bio.setter
    def bio(self, value):
        """Setter for bio property."""
        self.logger.warn("Setting values on bio will NOT update the remote Canvas instance.")
        self._bio = value

    @property
    def login_id(self):
        """sample_user@example.com."""
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        """Setter for login_id property."""
        self.logger.warn("Setting values on login_id will NOT update the remote Canvas instance.")
        self._login_id = value

    @property
    def sortable_name(self):
        """user, sample."""
        return self._sortable_name

    @sortable_name.setter
    def sortable_name(self, value):
        """Setter for sortable_name property."""
        self.logger.warn("Setting values on sortable_name will NOT update the remote Canvas instance.")
        self._sortable_name = value

    @property
    def name(self):
        """Sample User."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def short_name(self):
        """Sample User."""
        return self._short_name

    @short_name.setter
    def short_name(self, value):
        """Setter for short_name property."""
        self.logger.warn("Setting values on short_name will NOT update the remote Canvas instance.")
        self._short_name = value

    @property
    def title(self):
        """title."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value

    @property
    def locale(self):
        """The users locale."""
        return self._locale

    @locale.setter
    def locale(self, value):
        """Setter for locale property."""
        self.logger.warn("Setting values on locale will NOT update the remote Canvas instance.")
        self._locale = value

    @property
    def sis_user_id(self):
        """sis1."""
        return self._sis_user_id

    @sis_user_id.setter
    def sis_user_id(self, value):
        """Setter for sis_user_id property."""
        self.logger.warn("Setting values on sis_user_id will NOT update the remote Canvas instance.")
        self._sis_user_id = value

    @property
    def time_zone(self):
        """Optional: This field is only returned in certain API calls, and will return the IANA time zone name of the user's preferred timezone."""
        return self._time_zone

    @time_zone.setter
    def time_zone(self, value):
        """Setter for time_zone property."""
        self.logger.warn("Setting values on time_zone will NOT update the remote Canvas instance.")
        self._time_zone = value

    @property
    def avatar_url(self):
        """The avatar_url can change over time, so we recommend not caching it for more than a few hours."""
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, value):
        """Setter for avatar_url property."""
        self.logger.warn("Setting values on avatar_url will NOT update the remote Canvas instance.")
        self._avatar_url = value

    @property
    def primary_email(self):
        """sample_user@example.com."""
        return self._primary_email

    @primary_email.setter
    def primary_email(self, value):
        """Setter for primary_email property."""
        self.logger.warn("Setting values on primary_email will NOT update the remote Canvas instance.")
        self._primary_email = value

    @property
    def calendar(self):
        """calendar."""
        return self._calendar

    @calendar.setter
    def calendar(self, value):
        """Setter for calendar property."""
        self.logger.warn("Setting values on calendar will NOT update the remote Canvas instance.")
        self._calendar = value

    @property
    def sis_login_id(self):
        """sis1-login."""
        return self._sis_login_id

    @sis_login_id.setter
    def sis_login_id(self, value):
        """Setter for sis_login_id property."""
        self.logger.warn("Setting values on sis_login_id will NOT update the remote Canvas instance.")
        self._sis_login_id = value

    @property
    def id(self):
        """The ID of the user."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value


class Pageviewlinks(BaseModel):
    """Pageviewlinks Model.
    The links of a page view access in Canvas"""

    def __init__(self, account=None, real_user=None, user=None, context=None, asset=None):
        """Init method for Pageviewlinks class."""
        self._account = account
        self._real_user = real_user
        self._user = user
        self._context = context
        self._asset = asset

        self.logger = logging.getLogger('pycanvas.Pageviewlinks')

    @property
    def account(self):
        """The ID of the account context for this page view."""
        return self._account

    @account.setter
    def account(self, value):
        """Setter for account property."""
        self.logger.warn("Setting values on account will NOT update the remote Canvas instance.")
        self._account = value

    @property
    def real_user(self):
        """The ID of the actual user who made this request, if the request was made by a user who was masquerading."""
        return self._real_user

    @real_user.setter
    def real_user(self, value):
        """Setter for real_user property."""
        self.logger.warn("Setting values on real_user will NOT update the remote Canvas instance.")
        self._real_user = value

    @property
    def user(self):
        """The ID of the user for this page view."""
        return self._user

    @user.setter
    def user(self, value):
        """Setter for user property."""
        self.logger.warn("Setting values on user will NOT update the remote Canvas instance.")
        self._user = value

    @property
    def context(self):
        """The ID of the context for the request (course id if context_type is Course, etc)."""
        return self._context

    @context.setter
    def context(self, value):
        """Setter for context property."""
        self.logger.warn("Setting values on context will NOT update the remote Canvas instance.")
        self._context = value

    @property
    def asset(self):
        """The ID of the asset for the request, if any."""
        return self._asset

    @asset.setter
    def asset(self, value):
        """Setter for asset property."""
        self.logger.warn("Setting values on asset will NOT update the remote Canvas instance.")
        self._asset = value


class Pageview(BaseModel):
    """Pageview Model.
    The record of a user page view access in Canvas"""

    def __init__(self, id, links=None, url=None, created_at=None, contributed=None, interaction_seconds=None, asset_type=None, context_type=None, controller=None, user_request=None, http_method=None, user_agent=None, action=None, remote_ip=None, participated=None, render_time=None):
        """Init method for Pageview class."""
        self._links = links
        self._url = url
        self._created_at = created_at
        self._contributed = contributed
        self._interaction_seconds = interaction_seconds
        self._asset_type = asset_type
        self._context_type = context_type
        self._controller = controller
        self._user_request = user_request
        self._http_method = http_method
        self._user_agent = user_agent
        self._action = action
        self._remote_ip = remote_ip
        self._participated = participated
        self._id = id
        self._render_time = render_time

        self.logger = logging.getLogger('pycanvas.Pageview')

    @property
    def links(self):
        """The page view links to define the relationships."""
        return self._links

    @links.setter
    def links(self, value):
        """Setter for links property."""
        self.logger.warn("Setting values on links will NOT update the remote Canvas instance.")
        self._links = value

    @property
    def url(self):
        """The URL requested."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def created_at(self):
        """When the request was made."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def contributed(self):
        """This field is deprecated, and will always be false."""
        return self._contributed

    @contributed.setter
    def contributed(self, value):
        """Setter for contributed property."""
        self.logger.warn("Setting values on contributed will NOT update the remote Canvas instance.")
        self._contributed = value

    @property
    def interaction_seconds(self):
        """An approximation of how long the user spent on the page, in seconds."""
        return self._interaction_seconds

    @interaction_seconds.setter
    def interaction_seconds(self, value):
        """Setter for interaction_seconds property."""
        self.logger.warn("Setting values on interaction_seconds will NOT update the remote Canvas instance.")
        self._interaction_seconds = value

    @property
    def asset_type(self):
        """The type of asset in the context for the request, if any."""
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        """Setter for asset_type property."""
        self.logger.warn("Setting values on asset_type will NOT update the remote Canvas instance.")
        self._asset_type = value

    @property
    def context_type(self):
        """The type of context for the request."""
        return self._context_type

    @context_type.setter
    def context_type(self, value):
        """Setter for context_type property."""
        self.logger.warn("Setting values on context_type will NOT update the remote Canvas instance.")
        self._context_type = value

    @property
    def controller(self):
        """The rails controller that handled the request."""
        return self._controller

    @controller.setter
    def controller(self, value):
        """Setter for controller property."""
        self.logger.warn("Setting values on controller will NOT update the remote Canvas instance.")
        self._controller = value

    @property
    def user_request(self):
        """A flag indicating whether the request was user-initiated, or automatic (such as an AJAX call)."""
        return self._user_request

    @user_request.setter
    def user_request(self, value):
        """Setter for user_request property."""
        self.logger.warn("Setting values on user_request will NOT update the remote Canvas instance.")
        self._user_request = value

    @property
    def http_method(self):
        """The HTTP method such as GET or POST."""
        return self._http_method

    @http_method.setter
    def http_method(self, value):
        """Setter for http_method property."""
        self.logger.warn("Setting values on http_method will NOT update the remote Canvas instance.")
        self._http_method = value

    @property
    def user_agent(self):
        """The user-agent of the browser or program that made the request."""
        return self._user_agent

    @user_agent.setter
    def user_agent(self, value):
        """Setter for user_agent property."""
        self.logger.warn("Setting values on user_agent will NOT update the remote Canvas instance.")
        self._user_agent = value

    @property
    def action(self):
        """The rails action that handled the request."""
        return self._action

    @action.setter
    def action(self, value):
        """Setter for action property."""
        self.logger.warn("Setting values on action will NOT update the remote Canvas instance.")
        self._action = value

    @property
    def remote_ip(self):
        """The origin IP address of the request."""
        return self._remote_ip

    @remote_ip.setter
    def remote_ip(self, value):
        """Setter for remote_ip property."""
        self.logger.warn("Setting values on remote_ip will NOT update the remote Canvas instance.")
        self._remote_ip = value

    @property
    def participated(self):
        """True if the request counted as participating, such as submitting homework."""
        return self._participated

    @participated.setter
    def participated(self, value):
        """Setter for participated property."""
        self.logger.warn("Setting values on participated will NOT update the remote Canvas instance.")
        self._participated = value

    @property
    def id(self):
        """A UUID representing the page view.  This is also the unique request id."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def render_time(self):
        """How long the response took to render, in seconds."""
        return self._render_time

    @render_time.setter
    def render_time(self, value):
        """Setter for render_time property."""
        self.logger.warn("Setting values on render_time will NOT update the remote Canvas instance.")
        self._render_time = value


class User(BaseModel):
    """User Model.
    A Canvas user, e.g. a student, teacher, administrator, observer, etc."""

    def __init__(self, id, login_id=None, sortable_name=None, name=None, short_name=None, bio=None, locale=None, sis_user_id=None, time_zone=None, email=None, sis_import_id=None, avatar_url=None, last_login=None, enrollments=None, sis_login_id=None):
        """Init method for User class."""
        self._login_id = login_id
        self._sortable_name = sortable_name
        self._name = name
        self._short_name = short_name
        self._bio = bio
        self._locale = locale
        self._sis_user_id = sis_user_id
        self._time_zone = time_zone
        self._email = email
        self._sis_import_id = sis_import_id
        self._avatar_url = avatar_url
        self._last_login = last_login
        self._enrollments = enrollments
        self._sis_login_id = sis_login_id
        self._id = id

        self.logger = logging.getLogger('pycanvas.User')

    @property
    def login_id(self):
        """The unique login id for the user.  This is what the user uses to log in to Canvas."""
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        """Setter for login_id property."""
        self.logger.warn("Setting values on login_id will NOT update the remote Canvas instance.")
        self._login_id = value

    @property
    def sortable_name(self):
        """The name of the user that is should be used for sorting groups of users, such as in the gradebook."""
        return self._sortable_name

    @sortable_name.setter
    def sortable_name(self, value):
        """Setter for sortable_name property."""
        self.logger.warn("Setting values on sortable_name will NOT update the remote Canvas instance.")
        self._sortable_name = value

    @property
    def name(self):
        """The name of the user."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def short_name(self):
        """A short name the user has selected, for use in conversations or other less formal places through the site."""
        return self._short_name

    @short_name.setter
    def short_name(self, value):
        """Setter for short_name property."""
        self.logger.warn("Setting values on short_name will NOT update the remote Canvas instance.")
        self._short_name = value

    @property
    def bio(self):
        """Optional: The user's bio."""
        return self._bio

    @bio.setter
    def bio(self, value):
        """Setter for bio property."""
        self.logger.warn("Setting values on bio will NOT update the remote Canvas instance.")
        self._bio = value

    @property
    def locale(self):
        """Optional: This field can be requested with certain API calls, and will return the users locale."""
        return self._locale

    @locale.setter
    def locale(self, value):
        """Setter for locale property."""
        self.logger.warn("Setting values on locale will NOT update the remote Canvas instance.")
        self._locale = value

    @property
    def sis_user_id(self):
        """The SIS ID associated with the user.  This field is only included if the user came from a SIS import and has permissions to view SIS information."""
        return self._sis_user_id

    @sis_user_id.setter
    def sis_user_id(self, value):
        """Setter for sis_user_id property."""
        self.logger.warn("Setting values on sis_user_id will NOT update the remote Canvas instance.")
        self._sis_user_id = value

    @property
    def time_zone(self):
        """Optional: This field is only returned in certain API calls, and will return the IANA time zone name of the user's preferred timezone."""
        return self._time_zone

    @time_zone.setter
    def time_zone(self, value):
        """Setter for time_zone property."""
        self.logger.warn("Setting values on time_zone will NOT update the remote Canvas instance.")
        self._time_zone = value

    @property
    def email(self):
        """Optional: This field can be requested with certain API calls, and will return the users primary email address."""
        return self._email

    @email.setter
    def email(self, value):
        """Setter for email property."""
        self.logger.warn("Setting values on email will NOT update the remote Canvas instance.")
        self._email = value

    @property
    def sis_import_id(self):
        """The id of the SIS import.  This field is only included if the user came from a SIS import and has permissions to manage SIS information."""
        return self._sis_import_id

    @sis_import_id.setter
    def sis_import_id(self, value):
        """Setter for sis_import_id property."""
        self.logger.warn("Setting values on sis_import_id will NOT update the remote Canvas instance.")
        self._sis_import_id = value

    @property
    def avatar_url(self):
        """If avatars are enabled, this field will be included and contain a url to retrieve the user's avatar."""
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, value):
        """Setter for avatar_url property."""
        self.logger.warn("Setting values on avatar_url will NOT update the remote Canvas instance.")
        self._avatar_url = value

    @property
    def last_login(self):
        """Optional: This field is only returned in certain API calls, and will return a timestamp representing the last time the user logged in to canvas."""
        return self._last_login

    @last_login.setter
    def last_login(self, value):
        """Setter for last_login property."""
        self.logger.warn("Setting values on last_login will NOT update the remote Canvas instance.")
        self._last_login = value

    @property
    def enrollments(self):
        """Optional: This field can be requested with certain API calls, and will return a list of the users active enrollments. See the List enrollments API for more details about the format of these records."""
        return self._enrollments

    @enrollments.setter
    def enrollments(self, value):
        """Setter for enrollments property."""
        self.logger.warn("Setting values on enrollments will NOT update the remote Canvas instance.")
        self._enrollments = value

    @property
    def sis_login_id(self):
        """DEPRECATED: The SIS login ID associated with the user. Please use the sis_user_id or login_id. This field will be removed in a future version of the API."""
        return self._sis_login_id

    @sis_login_id.setter
    def sis_login_id(self, value):
        """Setter for sis_login_id property."""
        self.logger.warn("Setting values on sis_login_id will NOT update the remote Canvas instance.")
        self._sis_login_id = value

    @property
    def id(self):
        """The ID of the user."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value


class Avatar(BaseModel):
    """Avatar Model.
    Possible avatar for a user."""

    def __init__(self, type, url, token, display_name, content_type=None, filename=None, id=None, size=None):
        """Init method for Avatar class."""
        self._display_name = display_name
        self._url = url
        self._content_type = content_type
        self._filename = filename
        self._token = token
        self._type = type
        self._id = id
        self._size = size

        self.logger = logging.getLogger('pycanvas.Avatar')

    @property
    def display_name(self):
        """A textual description of the avatar record."""
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        """Setter for display_name property."""
        self.logger.warn("Setting values on display_name will NOT update the remote Canvas instance.")
        self._display_name = value

    @property
    def url(self):
        """The url of the avatar."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def content_type(self):
        """['attachment' type only] the content-type of the attachment."""
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        """Setter for content_type property."""
        self.logger.warn("Setting values on content_type will NOT update the remote Canvas instance.")
        self._content_type = value

    @property
    def filename(self):
        """['attachment' type only] the filename of the attachment."""
        return self._filename

    @filename.setter
    def filename(self, value):
        """Setter for filename property."""
        self.logger.warn("Setting values on filename will NOT update the remote Canvas instance.")
        self._filename = value

    @property
    def token(self):
        """A unique representation of the avatar record which can be used to set the avatar with the user update endpoint. Note: this is an internal representation and is subject to change without notice. It should be consumed with this api endpoint and used in the user update endpoint, and should not be constructed by the client."""
        return self._token

    @token.setter
    def token(self, value):
        """Setter for token property."""
        self.logger.warn("Setting values on token will NOT update the remote Canvas instance.")
        self._token = value

    @property
    def type(self):
        """['gravatar'|'attachment'|'no_pic'] The type of avatar record, for categorization purposes."""
        return self._type

    @type.setter
    def type(self, value):
        """Setter for type property."""
        self.logger.warn("Setting values on type will NOT update the remote Canvas instance.")
        self._type = value

    @property
    def id(self):
        """['attachment' type only] the internal id of the attachment."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def size(self):
        """['attachment' type only] the size of the attachment."""
        return self._size

    @size.setter
    def size(self, value):
        """Setter for size property."""
        self.logger.warn("Setting values on size will NOT update the remote Canvas instance.")
        self._size = value

