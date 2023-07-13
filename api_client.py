import urllib3

http_client = urllib3.PoolManager(
            retries=urllib3.Retry(
                connect=5,
                read=2,
                redirect=5,
                status_forcelist=[429, 500, 501, 502, 503, 504],
                backoff_factor=0.2,
            ),
            timeout=urllib3.Timeout(connect=5.0, read=120.0),
            num_pools=10,
        )

def summarize(text):
    _min = min(max(int(len(text)/100*8), 10), 200)
    _max = min(max(int(len(text)/100*12), 50), 400)
    if _min > _max:
        _min, _max = _max, _min
    fields= {
        'min_length': _min,
        'max_length': _max,
        'text': text
    }
    print(f"{_min} - {_max}")
    _request =  http_client.request(method='POST', url='http://localhost:8001/v1/summarize/', fields=fields)
    print(f"{text} summary generation {_request.status}  finished in {_request.headers.get('x-process-time')} seconds, summary:")
    return _request.data.decode("utf-8")

print(summarize('This is the text to summarize'))
