"""Load balancer class and dependencies"""
import random


class LoadBalencer:
    def __init__(self, limit):
        self.servers = []
        self.limit = limit

    def register(self, server):
        if len(self.servers) == self.limit:
            raise Exception("Load balancer limit has been reached!")
        if server.name in [s.name for s in self.servers]:
            raise Exception("Server is already registered!")
        self.servers.append(server)
        return True

    def get(self):
        return random.choice(self.servers)
