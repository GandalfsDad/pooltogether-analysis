import requests

class SequentialQuerier:

    def __init__(self,queryString):
        self.__page = 0
        self._queryString = queryString

    def queryAll(self):
        all_res = []

        res, more = self.query()
        all_res = all_res+res

        while more:
            res, more = self.query()
            all_res = all_res + res
        
        return all_res


    def query(self):
        return self._next()

    def _next(self):
        url = self._queryString.format(page=self.__page)
        result = requests.get(url).json()
        data = result['data']

        self.__page +=1
        
        return data['items'], data['pagination']['has_more']
        
    def reset(self):
        self.__page = 0

