"""
Configures access to BingAds API and where to store results
"""


def data_dir() -> str:
    """The directory where result data is written to"""
    return '/tmp/bingads/'


def data_file() -> str:
    """The name of the file the result is written to"""
    return 'ad_performance.csv.gz'


def first_date() -> str:
    """The first day from which on data will be downloaded"""
    return '2015-01-01'

def developer_token() -> str:
    """The developer token that is used to access the BingAds API"""
    return '012345679ABCDEF'


def environment() -> str:
    """The deployment environment"""
    return 'production'


def oauth2_client_id() -> str:
    """The Oauth client id obtained from the BingAds developer center"""
    return 'abc1234-1234-1234-abc-abcd1234'


def oauth2_client_secret() -> str:
    """The Oauth client secret obtained from the BingAds developer center"""
    return 'ABCDefgh!1234567890'


def oauth2_refresh_token() -> str:
    """The Oauth refresh token returned from the adwords-downloader-refresh-oauth2-token script"""
    return 'ABCDefgh!1234567890ABCDefgh!1234567890ABCDefgh!1234567890ABCDefgh!1234567890ABCDefgh!1234567890ABCDefgh!1234567890ABCDefgh!1234567890'


def timeout() -> int:
    """The maximum amount of time (in milliseconds) that you want to wait for the report download"""
    return 3600000
