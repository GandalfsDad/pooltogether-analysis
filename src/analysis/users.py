from ..data.queryBuilder import QueryBuilder, CovalentQueryType
from ..data.querier import SequentialQuerier
from ..data.address import ADDRESSES

def getPTUsers(chain, API_KEY):
    qb = QueryBuilder(API_KEY,defaultPageSize=10000)
    query = qb.getQuery(CovalentQueryType.TokenHolders,chain,address = ADDRESSES['PTUSDC'][chain])
    sq = SequentialQuerier(query)

    OPHolders = sq.queryAll()

    return  {x['address']:int(x['balance'])/(1*10**int(x['contract_decimals'])) for x in OPHolders}
