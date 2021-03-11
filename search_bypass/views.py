from django.shortcuts import render
import subprocess
import os
import re
import sys

from urllib3 import connectionpool, poolmanager
from search.bypass import WAFBypass
from requests.exceptions import MissingSchema
from search.table_out import table_payload_zone, table_status_count_accuracy
# Create your views here.



def search_page(request):
    a='Testovaya stroka '
    context = {
        'test' :a,
    }
    return render(request, 'first_page.html',context)
def search_fun(request):
    query = request.GET.get('q','')
    #subprocess.run('/home/mentall/Документы/Django_main_page/main_page/search_bypass/main.py')
    count, accuracy = sr(query)
    passed = count[2]
    failed = count[1]
    error = count[0]
    passed_a = accuracy[0]
    failed_a = accuracy[1]
    error_a = accuracy[2]
    #[0, 1115, 264] [19.14, 80.86, 0.0]
    context = {
        'ac':accuracy,
        'passed':passed,
        'failed':failed,
        'error':error,

        'passed_a':passed_a,
        'failed_a':failed_a,
        'error_a':error_a,
        
        'query':query,
    }
    return render(request, 'second_page.html',context)




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
    
    count, accuracy = table_status_count_accuracy()
    print(count)
    print(accuracy)
    
    print("\n")
    return count,accuracy