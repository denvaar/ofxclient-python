from argparse import ArgumentParser
from datetime import datetime
from getpass import getpass
from pprint import pprint

from ofxclient import OFXClient
from ofxparser import OFXParser


# ofxclient-cli -u USERID -p USERPASS -a ACCTID --transactions
if __name__ == '__main__':
    
    parser = ArgumentParser(description='OFX Command-line Interface')
    
    parser.add_argument('-f', '--fi', action='store', dest='fi',
                        help='specify the fi, or financial institution',
                        required=True)
    parser.add_argument('-u', '--userid', action='store', dest='userid',
                        help='specify the userid', required=True)
    parser.add_argument('-a', '--acctid', action='store', dest='acctid',
                        help='specify the acctid, or account id', required=True)
    parser.add_argument('-t', '--transactions', action='store',
                        dest='transactions', help='list transactions')

    args = parser.parse_args()
    userpass = getpass()

    client = OFXClient(fi=args.fi, userid=args.userid, userpass=userpass,
                       acctid=args.acctid)

    if args.transactions:
        start_date = datetime.strptime(args.transactions, '%Y%m%d')
        data = client.get_transactions(start_date)
        pprint(OFXParser().as_json(data, pretty=True))

