import requests

resp = requests.get('http://www.google.com/pic')
#if resp.status_code != 200:
    # This means something went wrong.
    #raise ApiError('GET /tasks/ {}'.format(resp.status_code))
# for todo_item in resp.json():
#     print('{} {}'.format(todo_item['id'], todo_item['summary']))
assert resp.status_code==200, 'not 200';

print "done"