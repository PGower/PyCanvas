"""Conversations API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class ConversationsAPI(BaseCanvasAPI):
    """Conversations API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for ConversationsAPI."""
        super(ConversationsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.ConversationsAPI")

    def list_conversations(self, filter=None, filter_mode=None, include=None, include_all_conversation_ids=None, interleave_submissions=None, scope=None):
        """
        List conversations.

        Returns the list of conversations for the current user, most recent ones first.
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - scope
        """When set, only return conversations of the specified type. For example,
        set to "unread" to return only conversations that haven't been read.
        The default behavior is to return all non-archived conversations (i.e.
        read and unread)."""
        if scope is not None:
            self._validate_enum(scope, ["unread", "starred", "archived"])
            params["scope"] = scope
        # OPTIONAL - filter
        """When set, only return conversations for the specified courses, groups
        or users. The id should be prefixed with its type, e.g. "user_123" or
        "course_456". Can be an array (by setting "filter[]") or single value
        (by setting "filter")"""
        if filter is not None:
            params["filter"] = filter
        # OPTIONAL - filter_mode
        """When filter[] contains multiple filters, combine them with this mode,
        filtering conversations that at have at least all of the contexts ("and")
        or at least one of the contexts ("or")"""
        if filter_mode is not None:
            self._validate_enum(filter_mode, ["and", "or", "default or"])
            params["filter_mode"] = filter_mode
        # OPTIONAL - interleave_submissions
        """(Obsolete) Submissions are no
        longer linked to conversations. This parameter is ignored."""
        if interleave_submissions is not None:
            params["interleave_submissions"] = interleave_submissions
        # OPTIONAL - include_all_conversation_ids
        """Default is false. If true,
        the top-level element of the response will be an object rather than
        an array, and will have the keys "conversations" which will contain the
        paged conversation data, and "conversation_ids" which will contain the
        ids of all conversations under this scope/filter in the same order."""
        if include_all_conversation_ids is not None:
            params["include_all_conversation_ids"] = include_all_conversation_ids
        # OPTIONAL - include
        """"participant_avatars":: Optionally include an "avatar_url" key for each user participanting in the conversation"""
        if include is not None:
            self._validate_enum(include, ["participant_avatars"])
            params["include"] = include

        self.logger.debug("GET /api/v1/conversations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/conversations".format(**path), data=data, params=params, all_pages=True)

    def create_conversation(self, body, recipients, attachment_ids=None, context_code=None, filter=None, filter_mode=None, group_conversation=None, media_comment_id=None, media_comment_type=None, mode=None, scope=None, subject=None, user_note=None):
        """
        Create a conversation.

        Create a new conversation with one or more recipients. If there is already
        an existing private conversation with the given recipients, it will be
        reused.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - recipients
        """An array of recipient ids. These may be user ids or course/group ids
        prefixed with "course_" or "group_" respectively, e.g.
        recipients[]=1&recipients[]=2&recipients[]=course_3"""
        data["recipients"] = recipients
        # OPTIONAL - subject
        """The subject of the conversation. This is ignored when reusing a
        conversation. Maximum length is 255 characters."""
        if subject is not None:
            data["subject"] = subject
        # REQUIRED - body
        """The message to be sent"""
        data["body"] = body
        # OPTIONAL - group_conversation
        """Defaults to false. If true, this will be a group conversation (i.e. all
        recipients may see all messages and replies). If false, individual private
        conversations will be started with each recipient. Must be set false if the
        number of recipients is over the set maximum (default is 100)."""
        if group_conversation is not None:
            data["group_conversation"] = group_conversation
        # OPTIONAL - attachment_ids
        """An array of attachments ids. These must be files that have been previously
        uploaded to the sender's "conversation attachments" folder."""
        if attachment_ids is not None:
            data["attachment_ids"] = attachment_ids
        # OPTIONAL - media_comment_id
        """Media comment id of an audio of video file to be associated with this
        message."""
        if media_comment_id is not None:
            data["media_comment_id"] = media_comment_id
        # OPTIONAL - media_comment_type
        """Type of the associated media file"""
        if media_comment_type is not None:
            self._validate_enum(media_comment_type, ["audio", "video"])
            data["media_comment_type"] = media_comment_type
        # OPTIONAL - user_note
        """Will add a faculty journal entry for each recipient as long as the user
        making the api call has permission, the recipient is a student and
        faculty journals are enabled in the account."""
        if user_note is not None:
            data["user_note"] = user_note
        # OPTIONAL - mode
        """Determines whether the messages will be created/sent synchronously or
        asynchronously. Defaults to sync, and this option is ignored if this is a
        group conversation or there is just one recipient (i.e. it must be a bulk
        private message). When sent async, the response will be an empty array
        (batch status can be queried via the {api:ConversationsController#batches batches API})"""
        if mode is not None:
            self._validate_enum(mode, ["sync", "async"])
            data["mode"] = mode
        # OPTIONAL - scope
        """Used when generating "visible" in the API response. See the explanation
        under the {api:ConversationsController#index index API action}"""
        if scope is not None:
            self._validate_enum(scope, ["unread", "starred", "archived"])
            data["scope"] = scope
        # OPTIONAL - filter
        """Used when generating "visible" in the API response. See the explanation
        under the {api:ConversationsController#index index API action}"""
        if filter is not None:
            data["filter"] = filter
        # OPTIONAL - filter_mode
        """Used when generating "visible" in the API response. See the explanation
        under the {api:ConversationsController#index index API action}"""
        if filter_mode is not None:
            self._validate_enum(filter_mode, ["and", "or", "default or"])
            data["filter_mode"] = filter_mode
        # OPTIONAL - context_code
        """The course or group that is the context for this conversation. Same format
        as courses or groups in the recipients argument."""
        if context_code is not None:
            data["context_code"] = context_code

        self.logger.debug("POST /api/v1/conversations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/conversations".format(**path), data=data, params=params, no_data=True)

    def get_running_batches(self):
        """
        Get running batches.

        Returns any currently running conversation batches for the current user.
        Conversation batches are created when a bulk private message is sent
        asynchronously (see the mode argument to the {api:ConversationsController#create create API action}).
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("GET /api/v1/conversations/batches with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/conversations/batches".format(**path), data=data, params=params, no_data=True)

    def get_single_conversation(self, id, auto_mark_as_read=None, filter=None, filter_mode=None, interleave_submissions=None, scope=None):
        """
        Get a single conversation.

        Returns information for a single conversation for the current user. Response includes all
        fields that are present in the list/index action as well as messages
        and extended participant information.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id
        # OPTIONAL - interleave_submissions
        """(Obsolete) Submissions are no
        longer linked to conversations. This parameter is ignored."""
        if interleave_submissions is not None:
            params["interleave_submissions"] = interleave_submissions
        # OPTIONAL - scope
        """Used when generating "visible" in the API response. See the explanation
        under the {api:ConversationsController#index index API action}"""
        if scope is not None:
            self._validate_enum(scope, ["unread", "starred", "archived"])
            params["scope"] = scope
        # OPTIONAL - filter
        """Used when generating "visible" in the API response. See the explanation
        under the {api:ConversationsController#index index API action}"""
        if filter is not None:
            params["filter"] = filter
        # OPTIONAL - filter_mode
        """Used when generating "visible" in the API response. See the explanation
        under the {api:ConversationsController#index index API action}"""
        if filter_mode is not None:
            self._validate_enum(filter_mode, ["and", "or", "default or"])
            params["filter_mode"] = filter_mode
        # OPTIONAL - auto_mark_as_read
        """Default true. If true, unread
        conversations will be automatically marked as read. This will default
        to false in a future API release, so clients should explicitly send
        true if that is the desired behavior."""
        if auto_mark_as_read is not None:
            params["auto_mark_as_read"] = auto_mark_as_read

        self.logger.debug("GET /api/v1/conversations/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/conversations/{id}".format(**path), data=data, params=params, no_data=True)

    def edit_conversation(self, id, conversation_starred=None, conversation_subscribed=None, conversation_workflow_state=None, filter=None, filter_mode=None, scope=None):
        """
        Edit a conversation.

        Updates attributes for a single conversation.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id
        # OPTIONAL - conversation[workflow_state]
        """Change the state of this conversation"""
        if conversation_workflow_state is not None:
            self._validate_enum(conversation_workflow_state, ["read", "unread", "archived"])
            data["conversation[workflow_state]"] = conversation_workflow_state
        # OPTIONAL - conversation[subscribed]
        """Toggle the current user's subscription to the conversation (only valid for
        group conversations). If unsubscribed, the user will still have access to
        the latest messages, but the conversation won't be automatically flagged
        as unread, nor will it jump to the top of the inbox."""
        if conversation_subscribed is not None:
            data["conversation[subscribed]"] = conversation_subscribed
        # OPTIONAL - conversation[starred]
        """Toggle the starred state of the current user's view of the conversation."""
        if conversation_starred is not None:
            data["conversation[starred]"] = conversation_starred
        # OPTIONAL - scope
        """Used when generating "visible" in the API response. See the explanation
        under the {api:ConversationsController#index index API action}"""
        if scope is not None:
            self._validate_enum(scope, ["unread", "starred", "archived"])
            data["scope"] = scope
        # OPTIONAL - filter
        """Used when generating "visible" in the API response. See the explanation
        under the {api:ConversationsController#index index API action}"""
        if filter is not None:
            data["filter"] = filter
        # OPTIONAL - filter_mode
        """Used when generating "visible" in the API response. See the explanation
        under the {api:ConversationsController#index index API action}"""
        if filter_mode is not None:
            self._validate_enum(filter_mode, ["and", "or", "default or"])
            data["filter_mode"] = filter_mode

        self.logger.debug("PUT /api/v1/conversations/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/conversations/{id}".format(**path), data=data, params=params, no_data=True)

    def mark_all_as_read(self):
        """
        Mark all as read.

        Mark all conversations as read.
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("POST /api/v1/conversations/mark_all_as_read with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/conversations/mark_all_as_read".format(**path), data=data, params=params, no_data=True)

    def delete_conversation(self, id):
        """
        Delete a conversation.

        Delete this conversation and its messages. Note that this only deletes
        this user's view of the conversation.
        
        Response includes same fields as UPDATE action
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("DELETE /api/v1/conversations/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/conversations/{id}".format(**path), data=data, params=params, no_data=True)

    def add_recipients(self, id, recipients):
        """
        Add recipients.

        Add recipients to an existing group conversation. Response is similar to
        the GET/show action, except that only includes the
        latest message (e.g. "joe was added to the conversation by bob")
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id
        # REQUIRED - recipients
        """An array of recipient ids. These may be user ids or course/group ids
        prefixed with "course_" or "group_" respectively, e.g.
        recipients[]=1&recipients[]=2&recipients[]=course_3"""
        data["recipients"] = recipients

        self.logger.debug("POST /api/v1/conversations/{id}/add_recipients with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/conversations/{id}/add_recipients".format(**path), data=data, params=params, no_data=True)

    def add_message(self, id, body, attachment_ids=None, included_messages=None, media_comment_id=None, media_comment_type=None, recipients=None, user_note=None):
        """
        Add a message.

        Add a message to an existing conversation. Response is similar to the
        GET/show action, except that only includes the
        latest message (i.e. what we just sent)
        
        An array of user ids. Defaults to all of the current conversation
        recipients. To explicitly send a message to no other recipients,
        this array should consist of the logged-in user id.
        
        An array of message ids from this conversation to send to recipients
        of the new message. Recipients who already had a copy of included
        messages will not be affected.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id
        # REQUIRED - body
        """The message to be sent."""
        data["body"] = body
        # OPTIONAL - attachment_ids
        """An array of attachments ids. These must be files that have been previously
        uploaded to the sender's "conversation attachments" folder."""
        if attachment_ids is not None:
            data["attachment_ids"] = attachment_ids
        # OPTIONAL - media_comment_id
        """Media comment id of an audio of video file to be associated with this
        message."""
        if media_comment_id is not None:
            data["media_comment_id"] = media_comment_id
        # OPTIONAL - media_comment_type
        """Type of the associated media file."""
        if media_comment_type is not None:
            self._validate_enum(media_comment_type, ["audio", "video"])
            data["media_comment_type"] = media_comment_type
        # OPTIONAL - recipients
        """no description"""
        if recipients is not None:
            data["recipients"] = recipients
        # OPTIONAL - included_messages
        """no description"""
        if included_messages is not None:
            data["included_messages"] = included_messages
        # OPTIONAL - user_note
        """Will add a faculty journal entry for each recipient as long as the user
        making the api call has permission, the recipient is a student and
        faculty journals are enabled in the account."""
        if user_note is not None:
            data["user_note"] = user_note

        self.logger.debug("POST /api/v1/conversations/{id}/add_message with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/conversations/{id}/add_message".format(**path), data=data, params=params, no_data=True)

    def delete_message(self, id, remove):
        """
        Delete a message.

        Delete messages from this conversation. Note that this only affects this
        user's view of the conversation. If all messages are deleted, the
        conversation will be as well (equivalent to DELETE)
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id
        # REQUIRED - remove
        """Array of message ids to be deleted"""
        data["remove"] = remove

        self.logger.debug("POST /api/v1/conversations/{id}/remove_messages with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/conversations/{id}/remove_messages".format(**path), data=data, params=params, no_data=True)

    def batch_update_conversations(self, event, conversation_ids):
        """
        Batch update conversations.

        Perform a change on a set of conversations. Operates asynchronously; use the {api:ProgressController#show progress endpoint}
        to query the status of an operation.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - conversation_ids
        """List of conversations to update. Limited to 500 conversations."""
        data["conversation_ids"] = conversation_ids
        # REQUIRED - event
        """The action to take on each conversation."""
        self._validate_enum(event, ["mark_as_read", "mark_as_unread", "star", "unstar", "archive", "destroy"])
        data["event"] = event

        self.logger.debug("PUT /api/v1/conversations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/conversations".format(**path), data=data, params=params, single_item=True)

    def find_recipients(self):
        """
        Find recipients.

        Deprecated, see the {api:SearchController#recipients Find recipients endpoint} in the Search API
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("GET /api/v1/conversations/find_recipients with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/conversations/find_recipients".format(**path), data=data, params=params, no_data=True)

    def unread_count(self):
        """
        Unread count.

        Get the number of unread conversations for the current user
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("GET /api/v1/conversations/unread_count with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/conversations/unread_count".format(**path), data=data, params=params, no_data=True)


class Conversation(BaseModel):
    """Conversation Model."""

    def __init__(self, start_at=None, subscribed=None, workflow_state=None, last_message=None, visible=None, participants=None, private=None, properties=None, message_count=None, audience_contexts=None, audience=None, avatar_url=None, context_name=None, starred=None, id=None, subject=None):
        """Init method for Conversation class."""
        self._start_at = start_at
        self._subscribed = subscribed
        self._workflow_state = workflow_state
        self._last_message = last_message
        self._visible = visible
        self._participants = participants
        self._private = private
        self._properties = properties
        self._message_count = message_count
        self._audience_contexts = audience_contexts
        self._audience = audience
        self._avatar_url = avatar_url
        self._context_name = context_name
        self._starred = starred
        self._id = id
        self._subject = subject

        self.logger = logging.getLogger('pycanvas.Conversation')

    @property
    def start_at(self):
        """the date and time at which the last message was sent."""
        return self._start_at

    @start_at.setter
    def start_at(self, value):
        """Setter for start_at property."""
        self.logger.warn("Setting values on start_at will NOT update the remote Canvas instance.")
        self._start_at = value

    @property
    def subscribed(self):
        """whether the current user is subscribed to the conversation."""
        return self._subscribed

    @subscribed.setter
    def subscribed(self, value):
        """Setter for subscribed property."""
        self.logger.warn("Setting values on subscribed will NOT update the remote Canvas instance.")
        self._subscribed = value

    @property
    def workflow_state(self):
        """The current state of the conversation (read, unread or archived)."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def last_message(self):
        """A <=100 character preview from the most recent message."""
        return self._last_message

    @last_message.setter
    def last_message(self, value):
        """Setter for last_message property."""
        self.logger.warn("Setting values on last_message will NOT update the remote Canvas instance.")
        self._last_message = value

    @property
    def visible(self):
        """indicates whether the conversation is visible under the current scope and filter. This attribute is always true in the index API response, and is primarily useful in create/update responses so that you can know if the record should be displayed in the UI. The default scope is assumed, unless a scope or filter is passed to the create/update API call."""
        return self._visible

    @visible.setter
    def visible(self, value):
        """Setter for visible property."""
        self.logger.warn("Setting values on visible will NOT update the remote Canvas instance.")
        self._visible = value

    @property
    def participants(self):
        """Array of users (id, name) participating in the conversation. Includes current user."""
        return self._participants

    @participants.setter
    def participants(self, value):
        """Setter for participants property."""
        self.logger.warn("Setting values on participants will NOT update the remote Canvas instance.")
        self._participants = value

    @property
    def private(self):
        """whether the conversation is private."""
        return self._private

    @private.setter
    def private(self, value):
        """Setter for private property."""
        self.logger.warn("Setting values on private will NOT update the remote Canvas instance.")
        self._private = value

    @property
    def properties(self):
        """Additional conversation flags (last_author, attachments, media_objects). Each listed property means the flag is set to true (i.e. the current user is the most recent author, there are attachments, or there are media objects)."""
        return self._properties

    @properties.setter
    def properties(self, value):
        """Setter for properties property."""
        self.logger.warn("Setting values on properties will NOT update the remote Canvas instance.")
        self._properties = value

    @property
    def message_count(self):
        """the number of messages in the conversation."""
        return self._message_count

    @message_count.setter
    def message_count(self, value):
        """Setter for message_count property."""
        self.logger.warn("Setting values on message_count will NOT update the remote Canvas instance.")
        self._message_count = value

    @property
    def audience_contexts(self):
        """Most relevant shared contexts (courses and groups) between current user and other participants. If there is only one participant, it will also include that user's enrollment(s)/ membership type(s) in each course/group."""
        return self._audience_contexts

    @audience_contexts.setter
    def audience_contexts(self, value):
        """Setter for audience_contexts property."""
        self.logger.warn("Setting values on audience_contexts will NOT update the remote Canvas instance.")
        self._audience_contexts = value

    @property
    def audience(self):
        """Array of user ids who are involved in the conversation, ordered by participation level, then alphabetical. Excludes current user, unless this is a monologue."""
        return self._audience

    @audience.setter
    def audience(self, value):
        """Setter for audience property."""
        self.logger.warn("Setting values on audience will NOT update the remote Canvas instance.")
        self._audience = value

    @property
    def avatar_url(self):
        """URL to appropriate icon for this conversation (custom, individual or group avatar, depending on audience)."""
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, value):
        """Setter for avatar_url property."""
        self.logger.warn("Setting values on avatar_url will NOT update the remote Canvas instance.")
        self._avatar_url = value

    @property
    def context_name(self):
        """Name of the course or group in which the conversation is occurring."""
        return self._context_name

    @context_name.setter
    def context_name(self, value):
        """Setter for context_name property."""
        self.logger.warn("Setting values on context_name will NOT update the remote Canvas instance.")
        self._context_name = value

    @property
    def starred(self):
        """whether the conversation is starred."""
        return self._starred

    @starred.setter
    def starred(self, value):
        """Setter for starred property."""
        self.logger.warn("Setting values on starred will NOT update the remote Canvas instance.")
        self._starred = value

    @property
    def id(self):
        """the unique identifier for the conversation."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def subject(self):
        """the subject of the conversation."""
        return self._subject

    @subject.setter
    def subject(self, value):
        """Setter for subject property."""
        self.logger.warn("Setting values on subject will NOT update the remote Canvas instance.")
        self._subject = value

