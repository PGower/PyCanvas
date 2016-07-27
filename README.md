#PyCanvas
A python library for accessing the Instructure Canvas REST Api. Mostly generated with swagger-codegen-cli from the published swagger api specs.

Quickstart:

`from pycanvas.configuration import Configuration`  
`c = Configuration(host='https://yourname.instructure.com/api', access_token='generated_oauth_token')`  
`from pycanvas.users import UserApi`  
`u = UserApi`  
`data, status, headers, paging = u.list_users_in_account(account_id=1)`  
`data, status, headers, paging = u.list_users_in_account(account_id=1, per_page=50, page=3)`  