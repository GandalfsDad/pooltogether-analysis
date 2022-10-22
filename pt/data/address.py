from .queryBuilder import Chain

ADDRESSES = {
            'POOL':
                {
                    Chain.Optimism:'0x395Ae52bB17aef68C2888d941736A71dC6d4e125',
                    Chain.Polygon:'0x25788a1a171ec66Da6502f9975a15B609fF54CF6',
                    Chain.Ethereum:'0x0cEC1A9154Ff802e7934Fc916Ed7Ca50bDE6844e',
                },
            'USDC':
                {
                    Chain.Optimism:'0x7F5c764cBc14f9669B88837ca1490cCa17c31607',
                    Chain.Polygon:'0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174',
                    Chain.Ethereum:'0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'
                },
            'PTUSDC':
                {
                    Chain.Optimism:'0x62BB4fc73094c83B5e952C2180B23fA7054954c4',
                    Chain.Polygon:'0x6a304dFdb9f808741244b6bfEe65ca7B3b3A6076',
                    Chain.Ethereum:'0xdd4d117723C257CEe402285D3aCF218E9A8236E1'
                }
            }