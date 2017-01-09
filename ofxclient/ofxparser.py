from xml.etree import ElementTree


class OFXParser(object):

    def __init__(self, *args, **kwargs):
        path = kwargs.pop('path', None)
        string = kwargs.pop('string', None)
    
        if path:
            self.load_from_file(path)
        elif string:
            self.load_from_string(string)

    def load_from_string(self, string):
        self.data = ElementTree.fromstring(string)
    
    def load_from_file(self, path):
        with open(path, 'rt') as f:
            self.data = ElementTree.parse(f)    

    @property
    def transactions(self):
        transaction_data = []
        for node in self.data.findall('.//STMTTRN'):
            transaction = {}
            for child in node.iter():
                transaction[child.tag] = child.text.strip()
            transaction_data.append(transaction)
        return transaction_data
