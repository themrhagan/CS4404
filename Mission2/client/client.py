from ratelimit import limits, RateLimitException

import requests

FIFTEEN_MINUTES = 900

@limits(calls=3, period=FIFTEEN_MINUTES)
def call_api(url):
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception('API response: {}'.format(response.status_code))
    return response.text

for i in range(5):
        try:
                print call_api('http://bombast.com')
        except RateLimitException:
                print 'Rate Limited'
