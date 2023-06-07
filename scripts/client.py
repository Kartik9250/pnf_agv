#!/usr/bin/env python3

import socket


class Client:
    def __init__(self):
        self.ip = "192.168.2.2"
        self.port = "50020"
        self.req_data = 0
        self.checksum_data = 0
        self.redhead_output = 0
        self.s = 0
        self.conn()

    # def getip(self, ip1, port1):
    #     self.ip = ip1
    #     self.port = int(port1)
    #     self.conn()


    def conn(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.ip, int(self.port)))

    def output(self):
        self.req_data = bytes.fromhex('D0')
        self.checksum_data = bytes.fromhex('2F')
        self.s.send(self.req_data)
        self.s.send(self.checksum_data)
        self.redhead_output = self.s.recv(61).hex()
        return self.redhead_output
