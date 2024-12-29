class StringProcessor(object):
    def __init__(self, st):
        self._st = st
    def lowercase(self):
        print('invoked lowercase')
        self._st = self._st.lower()
        return self
    def uppercase(self):
        print ('invoked uppercase')
        self._st = self._st.upper()
        return self
    def capitalize(self):
        print('invoked capitalize')
        self._st = self._st.capitalize()
        return self
    def delspace(self):
        print('invoked delspace')
        self._st = self._st.replace(' ', '')
        return self



def process_string(s):
    print('Input String:', s)
    sp = StringProcessor(s)
    output = sp.uppercase().lowercase().capitalize()
    print('After change:', output)


def main():
    process_string('SENTENCE for Test')

main()