#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 履歴情報:
# Ver.0.1   試作
"""TCP server.

>>> import tcp_server
"""

__prog__ = 'tcp_server.py'
__description__ = 'TCP窓口'
__epilog__ = 'Python 3.7 以上で動作します。'
__version__ = '0.1'

import sys
import argparse
import doctest
import socket as sock
import threading

TARGET_HOST = '0.0.0.0'
TARGET_PORT = 9999
SEND_DATA = 'ACK!'
DAT_SIZ = 1024


def tcp_server(host, port, data=SEND_DATA.encode('utf-8'), vbs=False):
    """處理實行.

    Args:
        host(str):      處番地
        port(int):      港番
        data(bytes):    送信資料
        vbs(bool):      詳細情報表示旌旗
    Returns:
        bytes:          應答
    Raises:
        TypeError:      引數の型の不具合
        ValueError:     引數の値の不具合
        AssertionError: 不具合
    Tests:
        >>> tcp_server(7, 90)
        Traceback (most recent call last):
            ...
        TypeError: [!!] <host> must be a string.
        >>> tcp_server('host', 'two', 1)
        Traceback (most recent call last):
            ...
        TypeError: [!!] <port> must be an integer.
        >>> tcp_server('host', -5, 1)
        Traceback (most recent call last):
            ...
        ValueError: [!!] <port> must be positive.
        >>> tcp_server('host', 90, 'data', True)
        Traceback (most recent call last):
            ...
        TypeError: [!!] <data> must be bytes.
        >>> tcp_server('host', 90, b'data', 1)
        Traceback (most recent call last):
            ...
        AssertionError: [!!] <vbs> must be a boolean.
    """
    if not isinstance(host, str):
        raise TypeError('[!!] <host> must be a string.')
    if not isinstance(port, int):
        raise TypeError('[!!] <port> must be an integer.')
    if port <= 0:
        raise ValueError('[!!] <port> must be positive.')
    if not isinstance(data, bytes):
        raise TypeError('[!!] <data> must be bytes.')
    assert isinstance(vbs, bool), '[!!] <vbs> must be a boolean.'

    if vbs:
        print('[*] tcp_server()')
        print(f'  data: {data.decode("utf-8")}')

    svr = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
    svr.bind((host, port))
    svr.listen(5)
    print(f'[*] Listening on {host:s}:{port:d}')

    def handle_client(client_socket):
        req = client_socket.recv(DAT_SIZ)
        # 顧客が送信して來た資料を表示
        print(f'[*] Received: {req.decode("utf-8")}')

        # 電包の返送
        client_socket.send(data)
    # End of def handle_client(client_socket):

    while True:
        cli, addr = svr.accept()

        print(f'[*] Accepted connection from: {host:s}:{port:d}')

        # 受信資料を處理する動作斷片の起動
        handler = threading.Thread(target=handle_client, args=(cli,))
        handler.start()
# End of def tcp_server(host, port, data=SEND_DATA.encode('utf-8'), ...):


def main():
    """Do main function.

    >>> import tcp_server
    """
    parser = argparse.ArgumentParser(
        prog=__prog__,
        # usage='usage',
        description=__description__,
        epilog=__epilog__,
        add_help=True,
        )
    parser.add_argument('-v', '--verbose',
                        help='詳細情報表示',
                        action='store_true')
    parser.add_argument('-t', '--test',
                        help='内部試驗',
                        action='store_true')
    parser.add_argument('-V', '--version',
                        help='履歴情報表示',
                        action='store_true')
    parser.add_argument('-H', '--host',
                        default=TARGET_HOST,
                        help='處番地')
    parser.add_argument('-p', '--port',
                        default=TARGET_PORT,
                        type=int,
                        help='港番')
    parser.add_argument('-d', '--data',
                        default=SEND_DATA,
                        help='處番地')
    args = parser.parse_args()
    args = parser.parse_args()
    if args.test:
        doctest.testmod(verbose=args.verbose)
        sys.exit()

    if args.version:
        print('Ver: {}'.format(__version__))
        sys.exit()

    if args.verbose:
        print(f'Program: {__prog__}')
        print(f'   Host: {args.host:s}')
        print(f'   Port: {args.port:d}')
        print(f'   Bytes: {args.data}')

    res = tcp_server(args.host, args.port,
                     args.data.encode('utf-8'), args.verbose)
    print(res)
# End of def main():


if __name__ == '__main__':
    main()
