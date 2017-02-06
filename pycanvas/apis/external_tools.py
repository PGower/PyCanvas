"""ExternalTools API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI



class ExternalToolsAPI(BaseCanvasAPI):
    """ExternalTools API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for ExternalToolsAPI."""
        super(ExternalToolsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.ExternalToolsAPI")

    def list_external_tools_courses(self, course_id, include_parents=None, search_term=None, selectable=None):
        """
        List external tools.

        Returns the paginated list of external tools for the current context.
        See the get request docs for a single tool for a list of properties on an external tool.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # OPTIONAL - search_term
        """The partial name of the tools to match and return."""
        if search_term is not None:
            params["search_term"] = search_term

        # OPTIONAL - selectable
        """If true, then only tools that are meant to be selectable are returned"""
        if selectable is not None:
            params["selectable"] = selectable

        # OPTIONAL - include_parents
        """If true, then include tools installed in all accounts above the current context"""
        if include_parents is not None:
            params["include_parents"] = include_parents

        self.logger.debug("GET /api/v1/courses/{course_id}/external_tools with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/external_tools".format(**path), data=data, params=params, no_data=True)

    def list_external_tools_accounts(self, account_id, include_parents=None, search_term=None, selectable=None):
        """
        List external tools.

        Returns the paginated list of external tools for the current context.
        See the get request docs for a single tool for a list of properties on an external tool.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # OPTIONAL - search_term
        """The partial name of the tools to match and return."""
        if search_term is not None:
            params["search_term"] = search_term

        # OPTIONAL - selectable
        """If true, then only tools that are meant to be selectable are returned"""
        if selectable is not None:
            params["selectable"] = selectable

        # OPTIONAL - include_parents
        """If true, then include tools installed in all accounts above the current context"""
        if include_parents is not None:
            params["include_parents"] = include_parents

        self.logger.debug("GET /api/v1/accounts/{account_id}/external_tools with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/external_tools".format(**path), data=data, params=params, no_data=True)

    def list_external_tools_groups(self, group_id, include_parents=None, search_term=None, selectable=None):
        """
        List external tools.

        Returns the paginated list of external tools for the current context.
        See the get request docs for a single tool for a list of properties on an external tool.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # OPTIONAL - search_term
        """The partial name of the tools to match and return."""
        if search_term is not None:
            params["search_term"] = search_term

        # OPTIONAL - selectable
        """If true, then only tools that are meant to be selectable are returned"""
        if selectable is not None:
            params["selectable"] = selectable

        # OPTIONAL - include_parents
        """If true, then include tools installed in all accounts above the current context"""
        if include_parents is not None:
            params["include_parents"] = include_parents

        self.logger.debug("GET /api/v1/groups/{group_id}/external_tools with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/external_tools".format(**path), data=data, params=params, no_data=True)

    def get_sessionless_launch_url_for_external_tool_courses(self, course_id, assignment_id=None, id=None, launch_type=None, module_item_id=None, url=None):
        """
        Get a sessionless launch url for an external tool.

        Returns a sessionless launch url for an external tool.
        
        NOTE: Either the id or url must be provided unless launch_type is assessment or module_item.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # OPTIONAL - id
        """The external id of the tool to launch."""
        if id is not None:
            params["id"] = id

        # OPTIONAL - url
        """The LTI launch url for the external tool."""
        if url is not None:
            params["url"] = url

        # OPTIONAL - assignment_id
        """The assignment id for an assignment launch. Required if launch_type is set to "assessment"."""
        if assignment_id is not None:
            params["assignment_id"] = assignment_id

        # OPTIONAL - module_item_id
        """The assignment id for a module item launch. Required if launch_type is set to "module_item"."""
        if module_item_id is not None:
            params["module_item_id"] = module_item_id

        # OPTIONAL - launch_type
        """The type of launch to perform on the external tool. Placement names (eg. "course_navigation")
        can also be specified to use the custom launch url for that placement; if done, the tool id
        must be provided."""
        if launch_type is not None:
            self._validate_enum(launch_type, ["assessment", "module_item"])
            params["launch_type"] = launch_type

        self.logger.debug("GET /api/v1/courses/{course_id}/external_tools/sessionless_launch with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/external_tools/sessionless_launch".format(**path), data=data, params=params, no_data=True)

    def get_sessionless_launch_url_for_external_tool_accounts(self, account_id, assignment_id=None, id=None, launch_type=None, module_item_id=None, url=None):
        """
        Get a sessionless launch url for an external tool.

        Returns a sessionless launch url for an external tool.
        
        NOTE: Either the id or url must be provided unless launch_type is assessment or module_item.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # OPTIONAL - id
        """The external id of the tool to launch."""
        if id is not None:
            params["id"] = id

        # OPTIONAL - url
        """The LTI launch url for the external tool."""
        if url is not None:
            params["url"] = url

        # OPTIONAL - assignment_id
        """The assignment id for an assignment launch. Required if launch_type is set to "assessment"."""
        if assignment_id is not None:
            params["assignment_id"] = assignment_id

        # OPTIONAL - module_item_id
        """The assignment id for a module item launch. Required if launch_type is set to "module_item"."""
        if module_item_id is not None:
            params["module_item_id"] = module_item_id

        # OPTIONAL - launch_type
        """The type of launch to perform on the external tool. Placement names (eg. "course_navigation")
        can also be specified to use the custom launch url for that placement; if done, the tool id
        must be provided."""
        if launch_type is not None:
            self._validate_enum(launch_type, ["assessment", "module_item"])
            params["launch_type"] = launch_type

        self.logger.debug("GET /api/v1/accounts/{account_id}/external_tools/sessionless_launch with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/external_tools/sessionless_launch".format(**path), data=data, params=params, no_data=True)

    def get_single_external_tool_courses(self, course_id, external_tool_id):
        """
        Get a single external tool.

        Returns the specified external tool.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - external_tool_id
        """ID"""
        path["external_tool_id"] = external_tool_id

        self.logger.debug("GET /api/v1/courses/{course_id}/external_tools/{external_tool_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/external_tools/{external_tool_id}".format(**path), data=data, params=params, no_data=True)

    def get_single_external_tool_accounts(self, account_id, external_tool_id):
        """
        Get a single external tool.

        Returns the specified external tool.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - PATH - external_tool_id
        """ID"""
        path["external_tool_id"] = external_tool_id

        self.logger.debug("GET /api/v1/accounts/{account_id}/external_tools/{external_tool_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/external_tools/{external_tool_id}".format(**path), data=data, params=params, no_data=True)

    def create_external_tool_courses(self, name, course_id, consumer_key, privacy_level, shared_secret, account_navigation_enabled=None, account_navigation_selection_height=None, account_navigation_selection_width=None, account_navigation_text=None, account_navigation_url=None, config_type=None, config_url=None, config_xml=None, course_home_sub_navigation_enabled=None, course_home_sub_navigation_icon_url=None, course_home_sub_navigation_text=None, course_home_sub_navigation_url=None, course_navigation_default=None, course_navigation_enabled=None, course_navigation_text=None, course_navigation_visibility=None, course_navigation_windowTarget=None, custom_fields_field_name=None, description=None, domain=None, editor_button_enabled=None, editor_button_icon_url=None, editor_button_message_type=None, editor_button_selection_height=None, editor_button_selection_width=None, editor_button_url=None, homework_submission_enabled=None, homework_submission_message_type=None, homework_submission_text=None, homework_submission_url=None, icon_url=None, link_selection_enabled=None, link_selection_message_type=None, link_selection_text=None, link_selection_url=None, migration_selection_enabled=None, migration_selection_message_type=None, migration_selection_url=None, not_selectable=None, oauth_compliant=None, resource_selection_enabled=None, resource_selection_icon_url=None, resource_selection_selection_height=None, resource_selection_selection_width=None, resource_selection_url=None, text=None, tool_configuration_enabled=None, tool_configuration_message_type=None, tool_configuration_url=None, url=None, user_navigation_enabled=None, user_navigation_text=None, user_navigation_url=None):
        """
        Create an external tool.

        Create an external tool in the specified course/account.
        The created tool will be returned, see the "show" endpoint for an example.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - name
        """The name of the tool"""
        data["name"] = name

        # REQUIRED - privacy_level
        """What information to send to the external tool."""
        self._validate_enum(privacy_level, ["anonymous", "name_only", "public"])
        data["privacy_level"] = privacy_level

        # REQUIRED - consumer_key
        """The consumer key for the external tool"""
        data["consumer_key"] = consumer_key

        # REQUIRED - shared_secret
        """The shared secret with the external tool"""
        data["shared_secret"] = shared_secret

        # OPTIONAL - description
        """A description of the tool"""
        if description is not None:
            data["description"] = description

        # OPTIONAL - url
        """The url to match links against. Either "url" or "domain" should be set,
        not both."""
        if url is not None:
            data["url"] = url

        # OPTIONAL - domain
        """The domain to match links against. Either "url" or "domain" should be
        set, not both."""
        if domain is not None:
            data["domain"] = domain

        # OPTIONAL - icon_url
        """The url of the icon to show for this tool"""
        if icon_url is not None:
            data["icon_url"] = icon_url

        # OPTIONAL - text
        """The default text to show for this tool"""
        if text is not None:
            data["text"] = text

        # OPTIONAL - custom_fields[field_name]
        """Custom fields that will be sent to the tool consumer; can be used
        multiple times"""
        if custom_fields_field_name is not None:
            data["custom_fields[field_name]"] = custom_fields_field_name

        # OPTIONAL - account_navigation[url]
        """The url of the external tool for account navigation"""
        if account_navigation_url is not None:
            data["account_navigation[url]"] = account_navigation_url

        # OPTIONAL - account_navigation[enabled]
        """Set this to enable this feature"""
        if account_navigation_enabled is not None:
            data["account_navigation[enabled]"] = account_navigation_enabled

        # OPTIONAL - account_navigation[text]
        """The text that will show on the left-tab in the account navigation"""
        if account_navigation_text is not None:
            data["account_navigation[text]"] = account_navigation_text

        # OPTIONAL - account_navigation[selection_width]
        """The width of the dialog the tool is launched in"""
        if account_navigation_selection_width is not None:
            data["account_navigation[selection_width]"] = account_navigation_selection_width

        # OPTIONAL - account_navigation[selection_height]
        """The height of the dialog the tool is launched in"""
        if account_navigation_selection_height is not None:
            data["account_navigation[selection_height]"] = account_navigation_selection_height

        # OPTIONAL - user_navigation[url]
        """The url of the external tool for user navigation"""
        if user_navigation_url is not None:
            data["user_navigation[url]"] = user_navigation_url

        # OPTIONAL - user_navigation[enabled]
        """Set this to enable this feature"""
        if user_navigation_enabled is not None:
            data["user_navigation[enabled]"] = user_navigation_enabled

        # OPTIONAL - user_navigation[text]
        """The text that will show on the left-tab in the user navigation"""
        if user_navigation_text is not None:
            data["user_navigation[text]"] = user_navigation_text

        # OPTIONAL - course_home_sub_navigation[url]
        """The url of the external tool for right-side course home navigation menu"""
        if course_home_sub_navigation_url is not None:
            data["course_home_sub_navigation[url]"] = course_home_sub_navigation_url

        # OPTIONAL - course_home_sub_navigation[enabled]
        """Set this to enable this feature"""
        if course_home_sub_navigation_enabled is not None:
            data["course_home_sub_navigation[enabled]"] = course_home_sub_navigation_enabled

        # OPTIONAL - course_home_sub_navigation[text]
        """The text that will show on the right-side course home navigation menu"""
        if course_home_sub_navigation_text is not None:
            data["course_home_sub_navigation[text]"] = course_home_sub_navigation_text

        # OPTIONAL - course_home_sub_navigation[icon_url]
        """The url of the icon to show in the right-side course home navigation menu"""
        if course_home_sub_navigation_icon_url is not None:
            data["course_home_sub_navigation[icon_url]"] = course_home_sub_navigation_icon_url

        # OPTIONAL - course_navigation[enabled]
        """Set this to enable this feature"""
        if course_navigation_enabled is not None:
            data["course_navigation[enabled]"] = course_navigation_enabled

        # OPTIONAL - course_navigation[text]
        """The text that will show on the left-tab in the course navigation"""
        if course_navigation_text is not None:
            data["course_navigation[text]"] = course_navigation_text

        # OPTIONAL - course_navigation[visibility]
        """Who will see the navigation tab. "admins" for course admins, "members" for
        students, null for everyone"""
        if course_navigation_visibility is not None:
            self._validate_enum(course_navigation_visibility, ["admins", "members"])
            data["course_navigation[visibility]"] = course_navigation_visibility

        # OPTIONAL - course_navigation[windowTarget]
        """Determines how the navigation tab will be opened.
        "_blank"	Launches the external tool in a new window or tab.
        "_self"	(Default) Launches the external tool in an iframe inside of Canvas."""
        if course_navigation_windowTarget is not None:
            self._validate_enum(course_navigation_windowTarget, ["_blank", "_self"])
            data["course_navigation[windowTarget]"] = course_navigation_windowTarget

        # OPTIONAL - course_navigation[default]
        """Whether the navigation option will show in the course by default or
        whether the teacher will have to explicitly enable it"""
        if course_navigation_default is not None:
            data["course_navigation[default]"] = course_navigation_default

        # OPTIONAL - editor_button[url]
        """The url of the external tool"""
        if editor_button_url is not None:
            data["editor_button[url]"] = editor_button_url

        # OPTIONAL - editor_button[enabled]
        """Set this to enable this feature"""
        if editor_button_enabled is not None:
            data["editor_button[enabled]"] = editor_button_enabled

        # OPTIONAL - editor_button[icon_url]
        """The url of the icon to show in the WYSIWYG editor"""
        if editor_button_icon_url is not None:
            data["editor_button[icon_url]"] = editor_button_icon_url

        # OPTIONAL - editor_button[selection_width]
        """The width of the dialog the tool is launched in"""
        if editor_button_selection_width is not None:
            data["editor_button[selection_width]"] = editor_button_selection_width

        # OPTIONAL - editor_button[selection_height]
        """The height of the dialog the tool is launched in"""
        if editor_button_selection_height is not None:
            data["editor_button[selection_height]"] = editor_button_selection_height

        # OPTIONAL - editor_button[message_type]
        """Set this to ContentItemSelectionRequest to tell the tool to use
        content-item; otherwise, omit"""
        if editor_button_message_type is not None:
            data["editor_button[message_type]"] = editor_button_message_type

        # OPTIONAL - homework_submission[url]
        """The url of the external tool"""
        if homework_submission_url is not None:
            data["homework_submission[url]"] = homework_submission_url

        # OPTIONAL - homework_submission[enabled]
        """Set this to enable this feature"""
        if homework_submission_enabled is not None:
            data["homework_submission[enabled]"] = homework_submission_enabled

        # OPTIONAL - homework_submission[text]
        """The text that will show on the homework submission tab"""
        if homework_submission_text is not None:
            data["homework_submission[text]"] = homework_submission_text

        # OPTIONAL - homework_submission[message_type]
        """Set this to ContentItemSelectionRequest to tell the tool to use
        content-item; otherwise, omit"""
        if homework_submission_message_type is not None:
            data["homework_submission[message_type]"] = homework_submission_message_type

        # OPTIONAL - link_selection[url]
        """The url of the external tool"""
        if link_selection_url is not None:
            data["link_selection[url]"] = link_selection_url

        # OPTIONAL - link_selection[enabled]
        """Set this to enable this feature"""
        if link_selection_enabled is not None:
            data["link_selection[enabled]"] = link_selection_enabled

        # OPTIONAL - link_selection[text]
        """The text that will show for the link selection text"""
        if link_selection_text is not None:
            data["link_selection[text]"] = link_selection_text

        # OPTIONAL - link_selection[message_type]
        """Set this to ContentItemSelectionRequest to tell the tool to use
        content-item; otherwise, omit"""
        if link_selection_message_type is not None:
            data["link_selection[message_type]"] = link_selection_message_type

        # OPTIONAL - migration_selection[url]
        """The url of the external tool"""
        if migration_selection_url is not None:
            data["migration_selection[url]"] = migration_selection_url

        # OPTIONAL - migration_selection[enabled]
        """Set this to enable this feature"""
        if migration_selection_enabled is not None:
            data["migration_selection[enabled]"] = migration_selection_enabled

        # OPTIONAL - migration_selection[message_type]
        """Set this to ContentItemSelectionRequest to tell the tool to use
        content-item; otherwise, omit"""
        if migration_selection_message_type is not None:
            data["migration_selection[message_type]"] = migration_selection_message_type

        # OPTIONAL - tool_configuration[url]
        """The url of the external tool"""
        if tool_configuration_url is not None:
            data["tool_configuration[url]"] = tool_configuration_url

        # OPTIONAL - tool_configuration[enabled]
        """Set this to enable this feature"""
        if tool_configuration_enabled is not None:
            data["tool_configuration[enabled]"] = tool_configuration_enabled

        # OPTIONAL - tool_configuration[message_type]
        """Set this to ContentItemSelectionRequest to tell the tool to use
        content-item; otherwise, omit"""
        if tool_configuration_message_type is not None:
            data["tool_configuration[message_type]"] = tool_configuration_message_type

        # OPTIONAL - resource_selection[url]
        """The url of the external tool"""
        if resource_selection_url is not None:
            data["resource_selection[url]"] = resource_selection_url

        # OPTIONAL - resource_selection[enabled]
        """Set this to enable this feature"""
        if resource_selection_enabled is not None:
            data["resource_selection[enabled]"] = resource_selection_enabled

        # OPTIONAL - resource_selection[icon_url]
        """The url of the icon to show in the module external tool list"""
        if resource_selection_icon_url is not None:
            data["resource_selection[icon_url]"] = resource_selection_icon_url

        # OPTIONAL - resource_selection[selection_width]
        """The width of the dialog the tool is launched in"""
        if resource_selection_selection_width is not None:
            data["resource_selection[selection_width]"] = resource_selection_selection_width

        # OPTIONAL - resource_selection[selection_height]
        """The height of the dialog the tool is launched in"""
        if resource_selection_selection_height is not None:
            data["resource_selection[selection_height]"] = resource_selection_selection_height

        # OPTIONAL - config_type
        """Configuration can be passed in as CC xml instead of using query
        parameters. If this value is "by_url" or "by_xml" then an xml
        configuration will be expected in either the "config_xml" or "config_url"
        parameter. Note that the name parameter overrides the tool name provided
        in the xml"""
        if config_type is not None:
            data["config_type"] = config_type

        # OPTIONAL - config_xml
        """XML tool configuration, as specified in the CC xml specification. This is
        required if "config_type" is set to "by_xml""""
        if config_xml is not None:
            data["config_xml"] = config_xml

        # OPTIONAL - config_url
        """URL where the server can retrieve an XML tool configuration, as specified
        in the CC xml specification. This is required if "config_type" is set to
        "by_url""""
        if config_url is not None:
            data["config_url"] = config_url

        # OPTIONAL - not_selectable
        """Default: false, if set to true the tool won't show up in the external tool
        selection UI in modules and assignments"""
        if not_selectable is not None:
            data["not_selectable"] = not_selectable

        # OPTIONAL - oauth_compliant
        """Default: false, if set to true LTI query params will not be copied to the
        post body."""
        if oauth_compliant is not None:
            data["oauth_compliant"] = oauth_compliant

        self.logger.debug("POST /api/v1/courses/{course_id}/external_tools with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/external_tools".format(**path), data=data, params=params, no_data=True)

    def create_external_tool_accounts(self, name, account_id, consumer_key, privacy_level, shared_secret, account_navigation_enabled=None, account_navigation_selection_height=None, account_navigation_selection_width=None, account_navigation_text=None, account_navigation_url=None, config_type=None, config_url=None, config_xml=None, course_home_sub_navigation_enabled=None, course_home_sub_navigation_icon_url=None, course_home_sub_navigation_text=None, course_home_sub_navigation_url=None, course_navigation_default=None, course_navigation_enabled=None, course_navigation_text=None, course_navigation_visibility=None, course_navigation_windowTarget=None, custom_fields_field_name=None, description=None, domain=None, editor_button_enabled=None, editor_button_icon_url=None, editor_button_message_type=None, editor_button_selection_height=None, editor_button_selection_width=None, editor_button_url=None, homework_submission_enabled=None, homework_submission_message_type=None, homework_submission_text=None, homework_submission_url=None, icon_url=None, link_selection_enabled=None, link_selection_message_type=None, link_selection_text=None, link_selection_url=None, migration_selection_enabled=None, migration_selection_message_type=None, migration_selection_url=None, not_selectable=None, oauth_compliant=None, resource_selection_enabled=None, resource_selection_icon_url=None, resource_selection_selection_height=None, resource_selection_selection_width=None, resource_selection_url=None, text=None, tool_configuration_enabled=None, tool_configuration_message_type=None, tool_configuration_url=None, url=None, user_navigation_enabled=None, user_navigation_text=None, user_navigation_url=None):
        """
        Create an external tool.

        Create an external tool in the specified course/account.
        The created tool will be returned, see the "show" endpoint for an example.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - name
        """The name of the tool"""
        data["name"] = name

        # REQUIRED - privacy_level
        """What information to send to the external tool."""
        self._validate_enum(privacy_level, ["anonymous", "name_only", "public"])
        data["privacy_level"] = privacy_level

        # REQUIRED - consumer_key
        """The consumer key for the external tool"""
        data["consumer_key"] = consumer_key

        # REQUIRED - shared_secret
        """The shared secret with the external tool"""
        data["shared_secret"] = shared_secret

        # OPTIONAL - description
        """A description of the tool"""
        if description is not None:
            data["description"] = description

        # OPTIONAL - url
        """The url to match links against. Either "url" or "domain" should be set,
        not both."""
        if url is not None:
            data["url"] = url

        # OPTIONAL - domain
        """The domain to match links against. Either "url" or "domain" should be
        set, not both."""
        if domain is not None:
            data["domain"] = domain

        # OPTIONAL - icon_url
        """The url of the icon to show for this tool"""
        if icon_url is not None:
            data["icon_url"] = icon_url

        # OPTIONAL - text
        """The default text to show for this tool"""
        if text is not None:
            data["text"] = text

        # OPTIONAL - custom_fields[field_name]
        """Custom fields that will be sent to the tool consumer; can be used
        multiple times"""
        if custom_fields_field_name is not None:
            data["custom_fields[field_name]"] = custom_fields_field_name

        # OPTIONAL - account_navigation[url]
        """The url of the external tool for account navigation"""
        if account_navigation_url is not None:
            data["account_navigation[url]"] = account_navigation_url

        # OPTIONAL - account_navigation[enabled]
        """Set this to enable this feature"""
        if account_navigation_enabled is not None:
            data["account_navigation[enabled]"] = account_navigation_enabled

        # OPTIONAL - account_navigation[text]
        """The text that will show on the left-tab in the account navigation"""
        if account_navigation_text is not None:
            data["account_navigation[text]"] = account_navigation_text

        # OPTIONAL - account_navigation[selection_width]
        """The width of the dialog the tool is launched in"""
        if account_navigation_selection_width is not None:
            data["account_navigation[selection_width]"] = account_navigation_selection_width

        # OPTIONAL - account_navigation[selection_height]
        """The height of the dialog the tool is launched in"""
        if account_navigation_selection_height is not None:
            data["account_navigation[selection_height]"] = account_navigation_selection_height

        # OPTIONAL - user_navigation[url]
        """The url of the external tool for user navigation"""
        if user_navigation_url is not None:
            data["user_navigation[url]"] = user_navigation_url

        # OPTIONAL - user_navigation[enabled]
        """Set this to enable this feature"""
        if user_navigation_enabled is not None:
            data["user_navigation[enabled]"] = user_navigation_enabled

        # OPTIONAL - user_navigation[text]
        """The text that will show on the left-tab in the user navigation"""
        if user_navigation_text is not None:
            data["user_navigation[text]"] = user_navigation_text

        # OPTIONAL - course_home_sub_navigation[url]
        """The url of the external tool for right-side course home navigation menu"""
        if course_home_sub_navigation_url is not None:
            data["course_home_sub_navigation[url]"] = course_home_sub_navigation_url

        # OPTIONAL - course_home_sub_navigation[enabled]
        """Set this to enable this feature"""
        if course_home_sub_navigation_enabled is not None:
            data["course_home_sub_navigation[enabled]"] = course_home_sub_navigation_enabled

        # OPTIONAL - course_home_sub_navigation[text]
        """The text that will show on the right-side course home navigation menu"""
        if course_home_sub_navigation_text is not None:
            data["course_home_sub_navigation[text]"] = course_home_sub_navigation_text

        # OPTIONAL - course_home_sub_navigation[icon_url]
        """The url of the icon to show in the right-side course home navigation menu"""
        if course_home_sub_navigation_icon_url is not None:
            data["course_home_sub_navigation[icon_url]"] = course_home_sub_navigation_icon_url

        # OPTIONAL - course_navigation[enabled]
        """Set this to enable this feature"""
        if course_navigation_enabled is not None:
            data["course_navigation[enabled]"] = course_navigation_enabled

        # OPTIONAL - course_navigation[text]
        """The text that will show on the left-tab in the course navigation"""
        if course_navigation_text is not None:
            data["course_navigation[text]"] = course_navigation_text

        # OPTIONAL - course_navigation[visibility]
        """Who will see the navigation tab. "admins" for course admins, "members" for
        students, null for everyone"""
        if course_navigation_visibility is not None:
            self._validate_enum(course_navigation_visibility, ["admins", "members"])
            data["course_navigation[visibility]"] = course_navigation_visibility

        # OPTIONAL - course_navigation[windowTarget]
        """Determines how the navigation tab will be opened.
        "_blank"	Launches the external tool in a new window or tab.
        "_self"	(Default) Launches the external tool in an iframe inside of Canvas."""
        if course_navigation_windowTarget is not None:
            self._validate_enum(course_navigation_windowTarget, ["_blank", "_self"])
            data["course_navigation[windowTarget]"] = course_navigation_windowTarget

        # OPTIONAL - course_navigation[default]
        """Whether the navigation option will show in the course by default or
        whether the teacher will have to explicitly enable it"""
        if course_navigation_default is not None:
            data["course_navigation[default]"] = course_navigation_default

        # OPTIONAL - editor_button[url]
        """The url of the external tool"""
        if editor_button_url is not None:
            data["editor_button[url]"] = editor_button_url

        # OPTIONAL - editor_button[enabled]
        """Set this to enable this feature"""
        if editor_button_enabled is not None:
            data["editor_button[enabled]"] = editor_button_enabled

        # OPTIONAL - editor_button[icon_url]
        """The url of the icon to show in the WYSIWYG editor"""
        if editor_button_icon_url is not None:
            data["editor_button[icon_url]"] = editor_button_icon_url

        # OPTIONAL - editor_button[selection_width]
        """The width of the dialog the tool is launched in"""
        if editor_button_selection_width is not None:
            data["editor_button[selection_width]"] = editor_button_selection_width

        # OPTIONAL - editor_button[selection_height]
        """The height of the dialog the tool is launched in"""
        if editor_button_selection_height is not None:
            data["editor_button[selection_height]"] = editor_button_selection_height

        # OPTIONAL - editor_button[message_type]
        """Set this to ContentItemSelectionRequest to tell the tool to use
        content-item; otherwise, omit"""
        if editor_button_message_type is not None:
            data["editor_button[message_type]"] = editor_button_message_type

        # OPTIONAL - homework_submission[url]
        """The url of the external tool"""
        if homework_submission_url is not None:
            data["homework_submission[url]"] = homework_submission_url

        # OPTIONAL - homework_submission[enabled]
        """Set this to enable this feature"""
        if homework_submission_enabled is not None:
            data["homework_submission[enabled]"] = homework_submission_enabled

        # OPTIONAL - homework_submission[text]
        """The text that will show on the homework submission tab"""
        if homework_submission_text is not None:
            data["homework_submission[text]"] = homework_submission_text

        # OPTIONAL - homework_submission[message_type]
        """Set this to ContentItemSelectionRequest to tell the tool to use
        content-item; otherwise, omit"""
        if homework_submission_message_type is not None:
            data["homework_submission[message_type]"] = homework_submission_message_type

        # OPTIONAL - link_selection[url]
        """The url of the external tool"""
        if link_selection_url is not None:
            data["link_selection[url]"] = link_selection_url

        # OPTIONAL - link_selection[enabled]
        """Set this to enable this feature"""
        if link_selection_enabled is not None:
            data["link_selection[enabled]"] = link_selection_enabled

        # OPTIONAL - link_selection[text]
        """The text that will show for the link selection text"""
        if link_selection_text is not None:
            data["link_selection[text]"] = link_selection_text

        # OPTIONAL - link_selection[message_type]
        """Set this to ContentItemSelectionRequest to tell the tool to use
        content-item; otherwise, omit"""
        if link_selection_message_type is not None:
            data["link_selection[message_type]"] = link_selection_message_type

        # OPTIONAL - migration_selection[url]
        """The url of the external tool"""
        if migration_selection_url is not None:
            data["migration_selection[url]"] = migration_selection_url

        # OPTIONAL - migration_selection[enabled]
        """Set this to enable this feature"""
        if migration_selection_enabled is not None:
            data["migration_selection[enabled]"] = migration_selection_enabled

        # OPTIONAL - migration_selection[message_type]
        """Set this to ContentItemSelectionRequest to tell the tool to use
        content-item; otherwise, omit"""
        if migration_selection_message_type is not None:
            data["migration_selection[message_type]"] = migration_selection_message_type

        # OPTIONAL - tool_configuration[url]
        """The url of the external tool"""
        if tool_configuration_url is not None:
            data["tool_configuration[url]"] = tool_configuration_url

        # OPTIONAL - tool_configuration[enabled]
        """Set this to enable this feature"""
        if tool_configuration_enabled is not None:
            data["tool_configuration[enabled]"] = tool_configuration_enabled

        # OPTIONAL - tool_configuration[message_type]
        """Set this to ContentItemSelectionRequest to tell the tool to use
        content-item; otherwise, omit"""
        if tool_configuration_message_type is not None:
            data["tool_configuration[message_type]"] = tool_configuration_message_type

        # OPTIONAL - resource_selection[url]
        """The url of the external tool"""
        if resource_selection_url is not None:
            data["resource_selection[url]"] = resource_selection_url

        # OPTIONAL - resource_selection[enabled]
        """Set this to enable this feature"""
        if resource_selection_enabled is not None:
            data["resource_selection[enabled]"] = resource_selection_enabled

        # OPTIONAL - resource_selection[icon_url]
        """The url of the icon to show in the module external tool list"""
        if resource_selection_icon_url is not None:
            data["resource_selection[icon_url]"] = resource_selection_icon_url

        # OPTIONAL - resource_selection[selection_width]
        """The width of the dialog the tool is launched in"""
        if resource_selection_selection_width is not None:
            data["resource_selection[selection_width]"] = resource_selection_selection_width

        # OPTIONAL - resource_selection[selection_height]
        """The height of the dialog the tool is launched in"""
        if resource_selection_selection_height is not None:
            data["resource_selection[selection_height]"] = resource_selection_selection_height

        # OPTIONAL - config_type
        """Configuration can be passed in as CC xml instead of using query
        parameters. If this value is "by_url" or "by_xml" then an xml
        configuration will be expected in either the "config_xml" or "config_url"
        parameter. Note that the name parameter overrides the tool name provided
        in the xml"""
        if config_type is not None:
            data["config_type"] = config_type

        # OPTIONAL - config_xml
        """XML tool configuration, as specified in the CC xml specification. This is
        required if "config_type" is set to "by_xml""""
        if config_xml is not None:
            data["config_xml"] = config_xml

        # OPTIONAL - config_url
        """URL where the server can retrieve an XML tool configuration, as specified
        in the CC xml specification. This is required if "config_type" is set to
        "by_url""""
        if config_url is not None:
            data["config_url"] = config_url

        # OPTIONAL - not_selectable
        """Default: false, if set to true the tool won't show up in the external tool
        selection UI in modules and assignments"""
        if not_selectable is not None:
            data["not_selectable"] = not_selectable

        # OPTIONAL - oauth_compliant
        """Default: false, if set to true LTI query params will not be copied to the
        post body."""
        if oauth_compliant is not None:
            data["oauth_compliant"] = oauth_compliant

        self.logger.debug("POST /api/v1/accounts/{account_id}/external_tools with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/external_tools".format(**path), data=data, params=params, no_data=True)

    def edit_external_tool_courses(self, course_id, external_tool_id):
        """
        Edit an external tool.

        Update the specified external tool. Uses same parameters as create
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - external_tool_id
        """ID"""
        path["external_tool_id"] = external_tool_id

        self.logger.debug("PUT /api/v1/courses/{course_id}/external_tools/{external_tool_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/external_tools/{external_tool_id}".format(**path), data=data, params=params, no_data=True)

    def edit_external_tool_accounts(self, account_id, external_tool_id):
        """
        Edit an external tool.

        Update the specified external tool. Uses same parameters as create
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - PATH - external_tool_id
        """ID"""
        path["external_tool_id"] = external_tool_id

        self.logger.debug("PUT /api/v1/accounts/{account_id}/external_tools/{external_tool_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{account_id}/external_tools/{external_tool_id}".format(**path), data=data, params=params, no_data=True)

    def delete_external_tool_courses(self, course_id, external_tool_id):
        """
        Delete an external tool.

        Remove the specified external tool
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - external_tool_id
        """ID"""
        path["external_tool_id"] = external_tool_id

        self.logger.debug("DELETE /api/v1/courses/{course_id}/external_tools/{external_tool_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/external_tools/{external_tool_id}".format(**path), data=data, params=params, no_data=True)

    def delete_external_tool_accounts(self, account_id, external_tool_id):
        """
        Delete an external tool.

        Remove the specified external tool
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - PATH - external_tool_id
        """ID"""
        path["external_tool_id"] = external_tool_id

        self.logger.debug("DELETE /api/v1/accounts/{account_id}/external_tools/{external_tool_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/accounts/{account_id}/external_tools/{external_tool_id}".format(**path), data=data, params=params, no_data=True)

