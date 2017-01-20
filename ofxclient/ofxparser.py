from xml.etree import ElementTree
import json
from datetime import datetime


class OFXParser(object):
    """Format and display OFX data"""

    def load_from_string(self, string):
        return ElementTree.fromstring(string)
    
    def load_from_file(self, path):
        with open(path, 'rt') as f:
            return ElementTree.parse(f)    

    def as_json(self, data, pretty=False, **filters):
        """
        Return JSON-formatted data
        
        `data`: the OFX data to parse as a string, or file path
        `pretty`: True to display JSON data in a more readable way,
                  otherwise preserve OFX names and value formatting.
        `filters`: dictionary of functions, mapped to keys to filter the data.
        """

        data = self.load_from_string(data)

        transaction_data = []
        for node in data.findall('.//STMTTRN'):
            transaction = {}
            for child in node.iter():
                key = (child.tag if not pretty else
                    self.pretty_mapping[child.tag])
                if child.tag == 'DTPOSTED' and pretty:
                    child.text = self.format_date(child.text)
                if child.tag != 'STMTTRN':
                    transaction[key] = child.text
            if self.apply_filters(transaction, **filters):
                transaction_data.append(transaction)
        return json.dumps(transaction_data)

    def apply_filters(self, mapping, **filters):
        for key, filter_condition in filters.items():
            try:
                if not filter_condition(mapping[key]):
                    return False
            except (KeyError, IndexError,):
                pass
        return True

    def format_date(self, date):
        return datetime.strptime(date.split('.')[0], '%Y%m%d%H%M%S').strftime(
            '%Y-%m-%d %H:%M')

    pretty_mapping = {
        'NAME': 'name',
        'TRNTYPE': 'transactionType',
        'FITID': 'id',
        'TRNAMT': 'transactionAmount',
        'DTPOSTED': 'datePosted',
        'STMTTRN': None,
    }
