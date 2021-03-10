#!/usr/bin/env python3

import getopt
import os
import re
import sys
from urllib3 import connectionpool, poolmanager
from search.bypass import WAFBypass
from requests.exceptions import MissingSchema
from search.table_out import table_payload_zone, table_status_count_accuracy
# Create your views here.
def patch_http_connection_pool(**constructor_kwargs):
    """
    This allows to override the default parameters of the
    HTTPConnectionPool constructor.
    For example, to increase the poolsize to fix problems
    with "HttpConnectionPool is full, discarding connection"
    """
    class MyHTTPConnectionPool(connectionpool.HTTPConnectionPool):
        def __init__(self, *args, **kwargs):
            kwargs.update(constructor_kwargs)
            super(MyHTTPConnectionPool, self).__init__(*args, **kwargs)
    poolmanager.pool_classes_by_scheme['http'] = MyHTTPConnectionPool

def sr(host):
    # Increasing max pool size
    patch_http_connection_pool(maxsize=100)
#https://yandex.ru/
    
    proxy = ''

    # Processing args from cmd


    # check host
    if not host:
        print("ERROR: the host is not set. Syntax: main.py --host=example.com:80 --proxy='http://proxy.example.com:3128'")
        sys.exit()

    # create log. dir
    try:
        log_dir = '/tmp/waf-bypass-log/'
        os.mkdir(log_dir)
    except OSError:
        pass

    print('\n')
    print('##')
    print('# Target: ', host)
    print('# Proxy: ', proxy)
    print('##')
    print('\n')

    test = WAFBypass(host, proxy)

    try:
        test.start_test()
        table_status_count_accuracy()
        table_payload_zone()
    except KeyboardInterrupt:
        print('\nKeyboard Interrupt')

    except MissingSchema:
        print('The protocol is not set for TARGET or PROXY')
    print(type(test))
    print("\n")

