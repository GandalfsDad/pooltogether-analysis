from enum import Enum

class CovalentQueryType(Enum):
    Balances = 0
    Portfolio = 1
    Transfers = 2
    TokenHolders = 3
    TokenHolderChanges = 4
    Transactions = 5
    EventsAddress = 6
    EventsTopic = 7

class Chain(Enum):
    Ethereum = 1
    Optimism = 10
    Polygon = 137


class QueryBuilder:

    BASE_URL = 'https://api.covalenthq.com/v1'

    def __init__(self, key, defaultPageSize = 100):
        self.__key = key
        self.__pageSize = defaultPageSize

    def getQuery(self, queryType, chain, **kwargs):
        
        if queryType == CovalentQueryType.Balances:
            return self._getQuery_Balances(chain, **kwargs)

        elif queryType == CovalentQueryType.Portfolio:
            return self._getQuery_Portfolio(chain, **kwargs)

        elif queryType == CovalentQueryType.Transfers:
            return self._getQuery_Transfers(chain, **kwargs)

        elif queryType == CovalentQueryType.TokenHolders:
            return self._getQuery_TokenHolders(chain, **kwargs)

        elif queryType == CovalentQueryType.TokenHolderChanges:
            return self._getQuery_TokenHolderChanges(chain, **kwargs)

        elif queryType == CovalentQueryType.Transactions:
            return self._getQuery_Transactions(chain, **kwargs)

        elif queryType == CovalentQueryType.EventsAddress:
            return self._getQuery_EventsAddress(chain, **kwargs)

        elif queryType == CovalentQueryType.EventsTopic:
            return self._getQuery_EventsTopic(chain, **kwargs)

        else:
            raise NotImplemented(f"Covalent Query Type {queryType} not supported.")
    
    def _getQuery_Balances(self, chain, address, page=None, pageSize= None):
        return self.__conditionals(self.BASE_URL+f'/{chain.value}/address/{address}/balances_v2',page=page,pageSize=pageSize)

    def _getQuery_Portfolio(self, chain, address, page=None, pageSize= None):
        return self.__conditionals(self.BASE_URL+f'/{chain.value}/address/{address}/portfolio_v2',page=page,pageSize=pageSize)

    def _getQuery_Transfers(self, chain, address, contractAddress, page=None, pageSize= None):
        return self.__conditionals(self.BASE_URL+f'/{chain.value}/address/{address}/transfers_v2',page=page,pageSize=pageSize, extras = {'contract-address':contractAddress})

    def _getQuery_TokenHolders(self, chain, address, page=None, pageSize= None, blockHeight = None):
        extras = {}
        if blockHeight is not None:
            extras['block-height'] = blockHeight

        return self.__conditionals(self.BASE_URL+f'/{chain.value}/tokens/{address}/token_holders',page=page,pageSize=pageSize, extras= extras)
    
    def _getQuery_TokenHolderChanges(self, chain, address, page=None, pageSize= None, startBlock = None, endBlock = None):
        extras = {'starting-block':startBlock, 'ending-block':endBlock}

        return self.__conditionals(self.BASE_URL+f'/{chain.value}/tokens/{address}/token_holders_changes',page=page,pageSize=pageSize, extras= extras)
    
    def _getQuery_Transactions(self, chain, address, page=None, pageSize= None):
        return self.__conditionals(self.BASE_URL+f'/{chain.value}/tokens/{address}/transactions_v2',page=page,pageSize=pageSize)

    def _getQuery_EventsAddress(self, chain, address, page=None, pageSize= None, startBlock = None, endBlock = None):
        extras = {'starting-block':startBlock, 'ending-block':endBlock}

        return self.__conditionals(self.BASE_URL+f'/{chain.value}/events/address/{address}',page=page,pageSize=pageSize, extras= extras)

    def _getQuery_EventsTopic(self, chain, address, page=None, pageSize= None, startBlock = None, endBlock = None, topic = []):
        extras = {'starting-block':startBlock, 'ending-block':endBlock, 'sender-address':address}

        #Need Type Check
        if len(topic)==0:
            raise ValueError("NEed at least One Topic")
        elif len(topic)==1:
            topicStr = topic[0]
        else:
            topicStr = ",".join(topic)
        
        return self.__conditionals(self.BASE_URL+f'/{chain.value}/events/topics/{topicStr}',page=page,pageSize=pageSize, extras= extras)
    
    


    def __conditionals(self, str,page, pageSize, extras = {}):
        if pageSize is None:
            pageSizeStr = self.__pageSize
        else:
            pageSizeStr = pageSize
        
        pageStr = '{page}' if page is None else page

        qStr = f'{str}/?key={self.__key}&page-number={pageStr}&page-size={pageSizeStr}'
        for k, V in extras.items():
            qStr+=f'&{k}={V}'
        
        return qStr