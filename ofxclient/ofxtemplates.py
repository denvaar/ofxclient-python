import re


class OFXTemplate(object):
    """Methods to help form reusable and composable OFX requests"""

    def xml_header(self):
        return """<?xml version="1.0" encoding="UTF-8"?>"""

    def ofx_header(self, *args, **kwargs):
        header_kwargs = {
            'ofxheader': '200',
            'version': '200',
            'security': 'NONE',
            'oldfileuid': 'NONE',
            'newfileuid': 'NONE',
        }
        header_kwargs.update(**kwargs)
        return self.split_and_replace(
            """
            <?OFX OFXHEADER="{ofxheader}"
                  VERSION="{version}"
                  SECURITY="{security}"
                  OLDFILEUID="{oldfileuid}"
                  NEWFILEUID="{newfileuid}" ?>
            """
        ).format(**header_kwargs)

    def split_and_replace(self, string):
        """Remove extra spaces and new line characters from given string"""
        return re.sub(r'\> *<',
            '><',
            ' '.join(string.split()).replace('\n', '').replace('\r', '')
        )

    def get_aggregate_request(self, aggregate_name, **kwargs):
        """Return an OFX Aggregate based on provided aggregate name"""
        try:
            return self.split_and_replace(
                self.aggregates[aggregate_name.upper()]
            )
        except KeyError:
            raise KeyError(
                '{} aggregate does not exist. Must be one of {}'.format(
                    aggregate_name,
                    ', '.join(self.aggregates.keys())
                )
            )
    
    aggregates = {
        'SIGNONMSGSRQV1': """
            <SIGNONMSGSRQV1>
                <SONRQ>
                    <DTCLIENT>{dtclient}</DTCLIENT>
                    <USERID>{userid}</USERID>
                    <USERPASS>{userpass}</USERPASS>
                    <LANGUAGE>ENG</LANGUAGE>
                    <FI>
                        <ORG>{org}</ORG>
                        <FID>{fid}</FID>
                    </FI>
                    <APPID>{appid}</APPID>
                    <APPVER>{appver}</APPVER>
                </SONRQ>
            </SIGNONMSGSRQV1>
            """,
        'CREDITCARDMSGSRQV1': """
            <CREDITCARDMSGSRQV1>
                <CCSTMTTRNRQ>
                    <TRNUID>{trnuid}</TRNUID>
                    <CLTCOOKIE>4</CLTCOOKIE>
                    <CCSTMTRQ>
                        <CCACCTFROM>
                            <ACCTID>{acctid}</ACCTID>
                        </CCACCTFROM>
                        <INCTRAN>
                            <DTSTART>{dtstart}</DTSTART>
                            <INCLUDE>Y</INCLUDE>
                        </INCTRAN>
                    </CCSTMTRQ>
                </CCSTMTTRNRQ>
            </CREDITCARDMSGSRQV1>
            """
    }

