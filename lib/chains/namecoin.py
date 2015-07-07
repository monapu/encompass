"""Chain-specific Namecoin code."""

from cryptocur import CryptoCur, hash_encode, hash_decode, rev_hex, int_to_hex

class Namecoin(CryptoCur):
    PoW = False
    chain_index = 7
    coin_name = 'Namecoin'
    code = 'NMC'
    p2pkh_version = 52
    p2sh_version = 13
    wif_version = 180
    ext_pub_version = '0488b21e'
    ext_priv_version = '0488ade4'

    DUST_THRESHOLD = 5430
    MIN_RELAY_TX_FEE = 100000
    RECOMMENDED_FEE = 500000
    COINBASE_MATURITY = 100

    block_explorers = {
        'Namecoin.info': 'https://explorer.namecoin.info/tx/',
        'Namecha.in': 'https://namecha.in/tx/',
        'Coinplorer.com': 'https://coinplorer.com/NMC/Transactions/'
    }

    base_units = {
        'NMC': 8
    }

    DEFAULT_PORTS = {'t':'50001', 's':'50002', 'h':'8081', 'g':'8082'}

    DEFAULT_SERVERS = {
        'e-nmc.us-west-2.maza.club': DEFAULT_PORTS,
    }

Currency = Namecoin
