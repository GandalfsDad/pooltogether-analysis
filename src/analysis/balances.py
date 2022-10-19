from ..data.queryBuilder import QueryBuilder, CovalentQueryType
from ..data.querier import SequentialQuerier
from ..data.address import ADDRESSES

def getBalances(chain,token,API_KEY):
    qb = QueryBuilder(API_KEY,defaultPageSize=10000)
    query = qb.getQuery(CovalentQueryType.TokenHolders,chain,address = ADDRESSES[token][chain])
    sq = SequentialQuerier(query)

    holders = sq.queryAll()

    return  {x['address']:int(x['balance'])/(1*10**int(x['contract_decimals'])) for x in holders}
