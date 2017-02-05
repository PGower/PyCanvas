#PyCanvas
A python library for accessing the Canvas LMS API. Generated from the Canvas API specs using a template.
All requests currently return json data.

Not all of the API's have been checked, if you fix an issue in one of the generated files please submit a pul request and I will integrate your changes.


Quickstart:

from pycanvas.apis import AccountsAPI

`client = AccountsAPI(instance_address="https://mycanvas.instance.com", access_token="my access token")
`client.list_accounts()