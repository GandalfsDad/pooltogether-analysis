from ..data.queryBuilder import QueryBuilder, CovalentQueryType
from ..data.querier import SequentialQuerier
from ..data.address import ADDRESSES

from tqdm import tqdm

import pandas as pd

def getUSDCTransfers(address, chain, API_KEY, defaultPagesize):
    qb = QueryBuilder(API_KEY,defaultPageSize=defaultPagesize)
    query = qb.getQuery(CovalentQueryType.Transfers,chain,address = address,contractAddress = ADDRESSES['USDC'][chain])
    sq = SequentialQuerier(query)

    transfersRaw = sq.queryAll()

    transfers = [
                {'To':tfer['transfers'][0]['to_address'],
                'From':tfer['transfers'][0]['from_address'],
                'Value':int(tfer['transfers'][0]['delta'])/(1*10**int(tfer['transfers'][0]['contract_decimals'])),
                'Time':pd.to_datetime(tfer['transfers'][0]['block_signed_at'])} for tfer in transfersRaw]

    return pd.DataFrame(transfers)
    
def getAllUSDCTransfers(users, chain, API_KEY, defaultPagesize):
    res = []
    for address in tqdm(list(users)):
        res.append(getUSDCTransfers(address, chain, API_KEY, defaultPagesize))
    
    combined =  pd.concat(res)

    return combined.dropna()
    