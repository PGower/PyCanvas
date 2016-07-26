from apis.configuration import Configuration

c = Configuration(host='https://stmonicas.instructure.com/api',
                  access_token='6523~GeT5Khqvbk8mlquAzlnQ6xLYGjddxmqbrappG5vWS3ihEsuupwxyWVfdC4UN0rX3',
                  debug=True)

from apis.users import UsersApi

u = UsersApi()

r = u.list_users_in_account(account_id=1, per_page=50, page=20)
print r['data']
print len(r['data'])
r = u.list_user_page_views(2)
print r['data']
import pdb;pdb.set_trace()
