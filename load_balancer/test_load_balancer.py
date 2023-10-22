import random
import pytest
import mock

from load_balancer import LoadBalencer
from server import Server


def test_load_balancer_basic():
    lb = LoadBalencer(limit=10)
    s1 = Server("server_1")
    assert lb.register(s1)


def test_load_balancer_register():
    lb = LoadBalencer(limit=10)
    s1 = Server("server_1")
    assert lb.register(s1)
    with pytest.raises(Exception) as e:
        lb.register(s1)

    assert "Server is already registered!" in str(e.value)


def test_load_balancer_limit():
    lb = LoadBalencer(limit=10)
    for i in range(10):
        assert lb.register(Server(str(i)))

    with pytest.raises(Exception) as e:
        lb.register(Server("10"))

    assert "Load balancer limit has been reached!" in str(e.value)


def same_server(l):
    return Server("5")


def test_load_balancer_get_version_1():
    lb = LoadBalencer(limit=10)
    for i in range(10):
        assert lb.register(Server(str(i)))

    with mock.patch("random.choice", same_server):
        server = lb.get()
        assert server.name == "5"

        server = lb.get()
        assert server.name == "5"


def test_load_balancer_get_version_2():
    lb = LoadBalencer(limit=10)
    for i in range(10):
        assert lb.register(Server(str(i)))

    random.seed(0)
    s1 = lb.get()
    random.seed(0)
    s2 = lb.get()
    random.seed(0)
    s3 = lb.get()

    assert s1.name == s2.name == s3.name
