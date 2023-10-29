from main import BaseURLShort, RandomListURLShort
import pytest

def test_base():
    
    base_short = BaseURLShort(10)
    short_urls = []
    for i in range(10):
        hash = base_short.short(str(i))
        short_urls.append(hash)
        
    with pytest.raises(Exception):
        base_short.short("10")
    with pytest.raises(Exception):
        base_short.get("0")
    for short_url in short_urls:
        base_short.get(short_url)
        