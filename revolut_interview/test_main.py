from main import BaseURLShort, RandomListURLShort
import pytest


def test_base():
    base_short = BaseURLShort(limit=10)
    short_urls = []
    long_urls = [str(i) for i in range(10)]
    for i in long_urls:
        hash = base_short.short(str(i))
        short_urls.append(hash)

    with pytest.raises(Exception) as e:
        base_short.short("10")
        assert "Hash List is empty!" in str(e)
    with pytest.raises(Exception) as e:
        base_short.get("0")
        assert "Limit reached" in str(e)

    retrieved_list_url = []
    for short_url in short_urls:
        retrieved_list_url.append(base_short.get(short_url))

    assert retrieved_list_url == long_urls


def test_random():
    random_short = RandomListURLShort(limit=10)
    short_urls = []
    long_urls = [str(i) for i in range(10)]
    hash_list = random_short._hash_list.copy()
    for i in long_urls:
        hash = random_short.short(str(i))
        short_urls.append(hash)

    with pytest.raises(Exception) as e:
        random_short.short("10")
        assert "Hash List is empty!" in str(e)
    with pytest.raises(Exception) as e:
        random_short.get("0")
        assert "Limit reached" in str(e)
        
    assert sorted(hash_list) == sorted(short_urls)
        
    
