from pushould import Pushould
import httpretty
from sure import expect
import nose
import os
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class TestPushould(object):
    def __init__(self):
        self.pushould = Pushould(url=os.environ['URL'],
                                 server_token=os.environ['SERVER_TOKEN'],
                                 email=os.environ['EMAIL'],
                                 password=os.environ['PASSWORD'])

    def test_version(self):
        version = Pushould.version()
        expect(version).to.equal('0.0.2')

    @httpretty.activate
    def test_pushould(self):

        def request_callback(request, uri, headers):
            return (200, headers, 'OK'.format(request.method, uri))

        httpretty.register_uri(httpretty.GET,
                               os.environ['URL'],
                               body=request_callback)

        response = self.pushould.trigger(room='foo', event='bar', data={'msg': 'baz'})
        expect(response.text).to.equal('OK')


if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])
