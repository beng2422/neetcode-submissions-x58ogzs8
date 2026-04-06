class TimeMap:

    def __init__(self):
        self.dictionary = {}
        self.dictionary2 = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key+str(timestamp)] = value
        if not self.dictionary2.get(key):
            self.dictionary2[key]=[str(timestamp)]
            print(self.dictionary2[key])
        else:
            output = self.dictionary2[key]
            output.append(str(timestamp))
            print('output', output)
            self.dictionary2[key] = output
        

    def get(self, key: str, timestamp: int) -> str:
        print(self.dictionary2)
        if self.dictionary.get(key+str(timestamp), '') != '':
            return self.dictionary.get(key+str(timestamp))
        elif self.dictionary2.get(key):
            lengthOfDict = len(self.dictionary2.get(key))
            latestVal = self.dictionary2.get(key)[lengthOfDict-1]
            if int(latestVal)>timestamp:
                return ''
            print('end of get', self.dictionary2)
            return self.dictionary.get(key+str(latestVal))
        return ''
            
        
