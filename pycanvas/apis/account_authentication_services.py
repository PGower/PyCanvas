"""AccountAuthenticationServices API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class AccountAuthenticationServicesAPI(BaseCanvasAPI):
    """AccountAuthenticationServices API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for AccountAuthenticationServicesAPI."""
        super(AccountAuthenticationServicesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.AccountAuthenticationServicesAPI")

    def list_authorization_configs(self, account_id):
        """
        List Authorization Configs.

        Returns the list of authorization configs
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id

        self.logger.debug("GET /api/v1/accounts/{account_id}/account_authorization_configs with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/account_authorization_configs".format(**path), data=data, params=params, all_pages=True)

    def create_authorization_config(self, account_id):
        """
        Create Authorization Config.

        Add external account authentication service(s) for the account.
        Services may be CAS, SAML, or LDAP.
        
        Each authentication service is specified as a set of parameters as
        described below. A service specification must include an 'auth_type'
        parameter with a value of 'cas', 'saml', or 'ldap'. The other recognized
        parameters depend on this auth_type; unrecognized parameters are discarded.
        Service specifications not specifying a valid auth_type are ignored.
        
        Any service specification may include an optional 'login_handle_name'
        parameter. This parameter specifies the label used for unique login
        identifiers; for example: 'Login', 'Username', 'Student ID', etc. The
        default is 'Email'.
        
        You can set the 'position' for any configuration. The config in the 1st position
        is considered the default.
        
        For CAS authentication services, the additional recognized parameters are:
        
        - auth_base
        
          The CAS server's URL.
        
        - log_in_url [Optional]
        
          An alternate SSO URL for logging into CAS. You probably should not set
          this.
        
        - unknown_user_url [Optional]
        
          A url to redirect to when a user is authorized through CAS but is not
          found in Canvas.
        
        For SAML authentication services, the additional recognized parameters are:
        
        - idp_entity_id
        
          The SAML IdP's entity ID - This is used to look up the correct SAML IdP if
          multiple are configured
        
        - log_in_url
        
          The SAML service's SSO target URL
        
        - log_out_url
        
          The SAML service's SLO target URL
        
        - certificate_fingerprint
        
          The SAML service's certificate fingerprint.
        
        - change_password_url [Optional]
        
          Forgot Password URL. Leave blank for default Canvas behavior.
        
        - unknown_user_url [Optional]
        
          A url to redirect to when a user is authorized through SAML but is not
          found in Canvas.
        
        - identifier_format
        
          The SAML service's identifier format. Must be one of:
        
          - urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress
          - urn:oasis:names:tc:SAML:2.0:nameid-format:entity
          - urn:oasis:names:tc:SAML:2.0:nameid-format:kerberos
          - urn:oasis:names:tc:SAML:2.0:nameid-format:persistent
          - urn:oasis:names:tc:SAML:2.0:nameid-format:transient
          - urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified
          - urn:oasis:names:tc:SAML:1.1:nameid-format:WindowsDomainQualifiedName
          - urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName
        
        - requested_authn_context
        
          The SAML AuthnContext
        
        For LDAP authentication services, the additional recognized parameters are:
        
        - auth_host
        
          The LDAP server's URL.
        
        - auth_port [Optional, Integer]
        
          The LDAP server's TCP port. (default: 389)
        
        - auth_over_tls [Optional]
        
          Whether to use TLS. Can be '', 'simple_tls', or 'start_tls'. For backwards
          compatibility, booleans are also accepted, with true meaning simple_tls.
          If not provided, it will default to start_tls.
        
        - auth_base [Optional]
        
          A default treebase parameter for searches performed against the LDAP
          server.
        
        - auth_filter
        
          LDAP search filter. Use !{{login}} as a placeholder for the username
          supplied by the user. For example: "(sAMAccountName=!{{login}})".
        
        - identifier_format [Optional]
        
          The LDAP attribute to use to look up the Canvas login. Omit to use
          the username supplied by the user.
        
        - auth_username
        
          Username
        
        - auth_password
        
          Password
        
        - change_password_url [Optional]
        
          Forgot Password URL. Leave blank for default Canvas behavior.
        
        - account_authorization_config[n] (deprecated)
          The nth service specification as described above. For instance, the
          auth_type of the first service is given by the
          account_authorization_config[0][auth_type] parameter. There must be
          either a single CAS or SAML specification, or one or more LDAP
          specifications. Additional services after an initial CAS or SAML service
          are ignored; additional non-LDAP services after an initial LDAP service
          are ignored.
        
        _Deprecated_ Examples:
        
        This endpoint still supports a deprecated version of setting the authorization configs.
        If you send data in this format it is considered a snapshot of how the configs
        should be setup and will clear any configs not sent.
        
        Simple CAS server integration.
        
          account_authorization_config[0][auth_type]=cas&
          account_authorization_config[0][auth_base]=cas.mydomain.edu
        
        Single SAML server integration.
        
          account_authorization_config[0][idp_entity_id]=http://idp.myschool.com/sso/saml2
          account_authorization_config[0][log_in_url]=saml-sso.mydomain.com&
          account_authorization_config[0][log_out_url]=saml-slo.mydomain.com&
          account_authorization_config[0][certificate_fingerprint]=1234567890ABCDEF&
          account_authorization_config[0][identifier_format]=urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress
        
        Two SAML server integration with discovery url.
        
          discovery_url=http://www.myschool.com/sso/identity_provider_selection
          account_authorization_config[0][idp_entity_id]=http://idp.myschool.com/sso/saml2&
          account_authorization_config[0][log_in_url]=saml-sso.mydomain.com&
          account_authorization_config[0][log_out_url]=saml-slo.mydomain.com&
          account_authorization_config[0][certificate_fingerprint]=1234567890ABCDEF&
          account_authorization_config[0][identifier_format]=urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress&
          account_authorization_config[1][idp_entity_id]=http://idp.otherschool.com/sso/saml2&
          account_authorization_config[1][log_in_url]=saml-sso.otherdomain.com&
          account_authorization_config[1][log_out_url]=saml-slo.otherdomain.com&
          account_authorization_config[1][certificate_fingerprint]=ABCDEFG12345678789&
          account_authorization_config[1][identifier_format]=urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress
        
        Single LDAP server integration.
        
          account_authorization_config[0][auth_type]=ldap&
          account_authorization_config[0][auth_host]=ldap.mydomain.edu&
          account_authorization_config[0][auth_filter]=(sAMAccountName={{login}})&
          account_authorization_config[0][auth_username]=username&
          account_authorization_config[0][auth_password]=password
        
        Multiple LDAP server integration.
        
          account_authorization_config[0][auth_type]=ldap&
          account_authorization_config[0][auth_host]=faculty-ldap.mydomain.edu&
          account_authorization_config[0][auth_filter]=(sAMAccountName={{login}})&
          account_authorization_config[0][auth_username]=username&
          account_authorization_config[0][auth_password]=password&
          account_authorization_config[1][auth_type]=ldap&
          account_authorization_config[1][auth_host]=student-ldap.mydomain.edu&
          account_authorization_config[1][auth_filter]=(sAMAccountName={{login}})&
          account_authorization_config[1][auth_username]=username&
          account_authorization_config[1][auth_password]=password
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id

        self.logger.debug("POST /api/v1/accounts/{account_id}/account_authorization_configs with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/account_authorization_configs".format(**path), data=data, params=params, single_item=True)

    def update_authorization_config(self, id, account_id):
        """
        Update Authorization Config.

        Update an authorization config using the same options as the create endpoint.
        You can not update an existing configuration to a new authentication type.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("PUT /api/v1/accounts/{account_id}/account_authorization_configs/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{account_id}/account_authorization_configs/{id}".format(**path), data=data, params=params, single_item=True)

    def get_authorization_config(self, id, account_id):
        """
        Get Authorization Config.

        Get the specified authorization config
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("GET /api/v1/accounts/{account_id}/account_authorization_configs/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/account_authorization_configs/{id}".format(**path), data=data, params=params, single_item=True)

    def delete_authorization_config(self, id, account_id):
        """
        Delete Authorization Config.

        Delete the config
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("DELETE /api/v1/accounts/{account_id}/account_authorization_configs/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/accounts/{account_id}/account_authorization_configs/{id}".format(**path), data=data, params=params, no_data=True)

    def get_discovery_url(self, account_id):
        """
        GET discovery url.

        Get the discovery url
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id

        self.logger.debug("GET /api/v1/accounts/{account_id}/account_authorization_configs/discovery_url with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/account_authorization_configs/discovery_url".format(**path), data=data, params=params, single_item=True)

    def set_discovery_url(self, account_id):
        """
        Set discovery url.

        If you have multiple IdPs configured, you can set a `discovery_url`.
        If that is set, canvas will forward all users to that URL when they need to
        be authenticated. That page will need to then help the user figure out where
        they need to go to log in.
        
        If no discovery url is configured, the 1st auth config will be used to
        attempt to authenticate the user.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id

        self.logger.debug("PUT /api/v1/accounts/{account_id}/account_authorization_configs/discovery_url with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{account_id}/account_authorization_configs/discovery_url".format(**path), data=data, params=params, single_item=True)

    def delete_discovery_url(self, account_id):
        """
        Delete discovery url.

        Clear discovery url
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id

        self.logger.debug("DELETE /api/v1/accounts/{account_id}/account_authorization_configs/discovery_url with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/accounts/{account_id}/account_authorization_configs/discovery_url".format(**path), data=data, params=params, no_data=True)


class Accountauthorizationconfig(BaseModel):
    """Accountauthorizationconfig Model."""

    def __init__(self, auth_type=None, auth_base=None, log_in_url=None, auth_over_tls=None, requested_authn_context=None, identifier_format=None, auth_port=None, idp_entity_id=None, log_out_url=None, certificate_fingerprint=None, auth_filter=None, login_attribute=None, auth_host=None, position=None, change_password_url=None, unknown_user_url=None, login_handle_name=None, auth_username=None, id=None):
        """Init method for Accountauthorizationconfig class."""
        self._auth_type = auth_type
        self._auth_base = auth_base
        self._log_in_url = log_in_url
        self._auth_over_tls = auth_over_tls
        self._requested_authn_context = requested_authn_context
        self._identifier_format = identifier_format
        self._auth_port = auth_port
        self._idp_entity_id = idp_entity_id
        self._log_out_url = log_out_url
        self._certificate_fingerprint = certificate_fingerprint
        self._auth_filter = auth_filter
        self._login_attribute = login_attribute
        self._auth_host = auth_host
        self._position = position
        self._change_password_url = change_password_url
        self._unknown_user_url = unknown_user_url
        self._login_handle_name = login_handle_name
        self._auth_username = auth_username
        self._id = id

        self.logger = logging.getLogger('pycanvas.Accountauthorizationconfig')

    @property
    def auth_type(self):
        """Valid for SAML, LDAP and CAS authorization."""
        return self._auth_type

    @auth_type.setter
    def auth_type(self, value):
        """Setter for auth_type property."""
        self.logger.warn("Setting values on auth_type will NOT update the remote Canvas instance.")
        self._auth_type = value

    @property
    def auth_base(self):
        """Valid for LDAP and CAS authorization."""
        return self._auth_base

    @auth_base.setter
    def auth_base(self, value):
        """Setter for auth_base property."""
        self.logger.warn("Setting values on auth_base will NOT update the remote Canvas instance.")
        self._auth_base = value

    @property
    def log_in_url(self):
        """Valid for SAML and CAS authorization."""
        return self._log_in_url

    @log_in_url.setter
    def log_in_url(self, value):
        """Setter for log_in_url property."""
        self.logger.warn("Setting values on log_in_url will NOT update the remote Canvas instance.")
        self._log_in_url = value

    @property
    def auth_over_tls(self):
        """Valid for LDAP authorization."""
        return self._auth_over_tls

    @auth_over_tls.setter
    def auth_over_tls(self, value):
        """Setter for auth_over_tls property."""
        self.logger.warn("Setting values on auth_over_tls will NOT update the remote Canvas instance.")
        self._auth_over_tls = value

    @property
    def requested_authn_context(self):
        """Valid for SAML authorization."""
        return self._requested_authn_context

    @requested_authn_context.setter
    def requested_authn_context(self, value):
        """Setter for requested_authn_context property."""
        self.logger.warn("Setting values on requested_authn_context will NOT update the remote Canvas instance.")
        self._requested_authn_context = value

    @property
    def identifier_format(self):
        """Valid for SAML authorization."""
        return self._identifier_format

    @identifier_format.setter
    def identifier_format(self, value):
        """Setter for identifier_format property."""
        self.logger.warn("Setting values on identifier_format will NOT update the remote Canvas instance.")
        self._identifier_format = value

    @property
    def auth_port(self):
        """Valid for LDAP authorization."""
        return self._auth_port

    @auth_port.setter
    def auth_port(self, value):
        """Setter for auth_port property."""
        self.logger.warn("Setting values on auth_port will NOT update the remote Canvas instance.")
        self._auth_port = value

    @property
    def idp_entity_id(self):
        """Valid for SAML authorization."""
        return self._idp_entity_id

    @idp_entity_id.setter
    def idp_entity_id(self, value):
        """Setter for idp_entity_id property."""
        self.logger.warn("Setting values on idp_entity_id will NOT update the remote Canvas instance.")
        self._idp_entity_id = value

    @property
    def log_out_url(self):
        """Valid for SAML authorization."""
        return self._log_out_url

    @log_out_url.setter
    def log_out_url(self, value):
        """Setter for log_out_url property."""
        self.logger.warn("Setting values on log_out_url will NOT update the remote Canvas instance.")
        self._log_out_url = value

    @property
    def certificate_fingerprint(self):
        """Valid for SAML authorization."""
        return self._certificate_fingerprint

    @certificate_fingerprint.setter
    def certificate_fingerprint(self, value):
        """Setter for certificate_fingerprint property."""
        self.logger.warn("Setting values on certificate_fingerprint will NOT update the remote Canvas instance.")
        self._certificate_fingerprint = value

    @property
    def auth_filter(self):
        """Valid for LDAP authorization."""
        return self._auth_filter

    @auth_filter.setter
    def auth_filter(self, value):
        """Setter for auth_filter property."""
        self.logger.warn("Setting values on auth_filter will NOT update the remote Canvas instance.")
        self._auth_filter = value

    @property
    def login_attribute(self):
        """Valid for SAML authorization."""
        return self._login_attribute

    @login_attribute.setter
    def login_attribute(self, value):
        """Setter for login_attribute property."""
        self.logger.warn("Setting values on login_attribute will NOT update the remote Canvas instance.")
        self._login_attribute = value

    @property
    def auth_host(self):
        """Valid for LDAP authorization."""
        return self._auth_host

    @auth_host.setter
    def auth_host(self, value):
        """Setter for auth_host property."""
        self.logger.warn("Setting values on auth_host will NOT update the remote Canvas instance.")
        self._auth_host = value

    @property
    def position(self):
        """Valid for SAML, LDAP and CAS authorization."""
        return self._position

    @position.setter
    def position(self, value):
        """Setter for position property."""
        self.logger.warn("Setting values on position will NOT update the remote Canvas instance.")
        self._position = value

    @property
    def change_password_url(self):
        """Valid for SAML authorization."""
        return self._change_password_url

    @change_password_url.setter
    def change_password_url(self, value):
        """Setter for change_password_url property."""
        self.logger.warn("Setting values on change_password_url will NOT update the remote Canvas instance.")
        self._change_password_url = value

    @property
    def unknown_user_url(self):
        """Valid for SAML and CAS authorization."""
        return self._unknown_user_url

    @unknown_user_url.setter
    def unknown_user_url(self, value):
        """Setter for unknown_user_url property."""
        self.logger.warn("Setting values on unknown_user_url will NOT update the remote Canvas instance.")
        self._unknown_user_url = value

    @property
    def login_handle_name(self):
        """Valid for SAML and CAS authorization."""
        return self._login_handle_name

    @login_handle_name.setter
    def login_handle_name(self, value):
        """Setter for login_handle_name property."""
        self.logger.warn("Setting values on login_handle_name will NOT update the remote Canvas instance.")
        self._login_handle_name = value

    @property
    def auth_username(self):
        """Valid for LDAP authorization."""
        return self._auth_username

    @auth_username.setter
    def auth_username(self, value):
        """Setter for auth_username property."""
        self.logger.warn("Setting values on auth_username will NOT update the remote Canvas instance.")
        self._auth_username = value

    @property
    def id(self):
        """Valid for SAML, LDAP and CAS authorization."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value


class Discoveryurl(BaseModel):
    """Discoveryurl Model."""

    def __init__(self, discovery_url=None):
        """Init method for Discoveryurl class."""
        self._discovery_url = discovery_url

        self.logger = logging.getLogger('pycanvas.Discoveryurl')

    @property
    def discovery_url(self):
        """discovery_url."""
        return self._discovery_url

    @discovery_url.setter
    def discovery_url(self, value):
        """Setter for discovery_url property."""
        self.logger.warn("Setting values on discovery_url will NOT update the remote Canvas instance.")
        self._discovery_url = value

