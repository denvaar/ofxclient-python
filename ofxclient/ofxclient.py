from urllib import request
from urllib.request import HTTPError
from urllib.parse import splittype, splithost
from http.client import HTTPSConnection
import uuid
import json
from datetime import datetime
import pkg_resources

from .ofxtemplates import OFXTemplate


class OFXClient(object):
    """Client for making requests to an OFX server"""

    def __init__(self, fi, userid, userpass, *args, **kwargs):
        
        resource_package = __name__
        resource_path = '/fi_data.json'
        fi_data_stream = pkg_resources.resource_stream(
            resource_package, resource_path).read().decode()

        self.fi_data = json.loads(fi_data_stream)
        self.ofx_templates = OFXTemplate()

        self.userid = userid
        self.userpass = userpass
        self.acctid = kwargs.pop('acctid', None)
        self.fi = fi
        self.server_url = self.fi_data[fi]['bootstrap_url']

    def _build_template(self, **kwargs):
        return (
            ''.join([
                self.ofx_templates.xml_header(),
                self.ofx_templates.ofx_header(),
                '<OFX>',
                self.ofx_templates.get_aggregate_request('SIGNONMSGSRQV1'),
                self.ofx_templates.get_aggregate_request('CREDITCARDMSGSRQV1'),
                '</OFX>'
            ]).format(
                dtclient=datetime.now().strftime('%Y%m%d%H%m%S'),
                userid=kwargs.get('userid', self.userid),
                userpass=kwargs.get('userpass', self.userpass),
                org=self.fi_data[self.fi]['fi_org'],
                fid=self.fi_data[self.fi]['fi_id'],
                appver=self.fi_data[self.fi]['app_ver'],
                appid=self.fi_data[self.fi]['app_id'],
                acctid=kwargs.get('acctid', self.acctid),
                trnuid=uuid.uuid4(),
                dtstart=kwargs.get('dtstart', None)
            )
        )

    def make_request(self, data):
        """Perform OFX request to server"""

        server_full_path = self.fi_data[self.fi]['bootstrap_url']
        server_fqdn = server_full_path.strip('/').split('//')[1]
        
        _, path = splittype(server_full_path)
        _, selector = splithost(path)
        
        h = HTTPSConnection(server_fqdn)
        h.putrequest('POST', selector, skip_host=True,
                     skip_accept_encoding=True)
        h.putheader('Content-Type', 'application/x-ofx')
        h.putheader('Host', server_fqdn)
        h.putheader('Content-Length', len(data))
        h.putheader('Connection', 'Keep-Alive')
        h.endheaders(data.encode()) 
        
        res = h.getresponse()
        return res.read().decode('ascii', 'ignore')

    def get_transactions(self, start_date, **kwargs):
        """Return list of credit card transactions"""

        kwargs = {
            'dtstart': start_date.strftime('%Y%m%d%H%m%S'),
        }
        return self.make_request(
            self._build_template(**kwargs)
        )

