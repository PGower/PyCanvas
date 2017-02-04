import threading
from requests import Request, Session, AuthBase

HTTP_VERBS = ['GET', 'HEAD', 'OPTIONS', 'POST', 'PUT', 'PATCH', 'DELETE']


class CanvasAuth(AuthBase):
    def __init__(self, access_token):
        self.access_token = access_token

    def __call__(self, r):
        # modify and return the request
        r.headers['Authorization'] = 'Bearer {}'.format(self.access_token)
        return r


class BaseApi(object):
    """A base API subclass."""

    default_path_attributes = {}
    default_query_attributes = {}
    default_header_attributes = {}
    default_form_attributes = {}
    default_body_attributes = {}

    def __init__(self, access_token, host='https://canvas.instructure.com/api', verify_ssl=True, cert=None):
        """Return a BaseAPI instance."""
        # Base host for the Canvas instance
        self.host = host

        self.session = requests.Session()
        self.session.auth = CanvasAuth(access_token)
        self.session.verify = verify_ssl
        self.session.cert = cert

    def api_precall(self,
                    api_meta,
                    params,
                    returns='JSON',
                    callback=None):
        import pdb;pdb.set_trace()

        path_attributes = self.build_attrs('path', attributes, attribute_map)
        query_attributes = self.build_attrs('query', attributes, attribute_map)
        header_attributes = self.build_attrs('header', attributes, attribute_map)
        form_attributes = self.build_attrs('form', attributes, attribute_map)
        body_attributes = self.build_attrs('body', attributes, attribute_map)

        # resource_path = '/v1/accounts/{account_id}/sub_accounts'.replace('{format}', 'json')
        url = host + url
        url = url.format(**path_attributes)

        method = method.upper()

        if method not in HTTP_VERBS:
            raise UnknownHTTPVerbError(method)

        request_args = {}
        if method in ['GET', 'HEAD']:
            if query_attributes != {}:
                request_args['params'] = query_attributes
            if header_attributes != {}:
                request_args['headers'] = header_attributes
        elif method in ['POST', 'PUT', 'PATCH', :
            if form_attributes != {}:
                request_args['data'] = form_attributes
            if header_attributes != {}:
                request_args['headers'] = header_attributes
        else:
            # Its OPTIONS
            pass

        if callback is None:
            return self.api_call(url, method, request_args, callback)
        else:
            thread = threading.Thread(target='api_call',
                                      args=(url,
                                            method,
                                            request_args,
                                            callback))
            thread.start()
            return thread

    def api_call(self, 
                 url,
                 method,
                 request_args,
                 callback):
        r = self.session.Request(method, url, **request_args)
        if callback is not None:
            callback(r)
        else:
            return r

