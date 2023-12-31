import os

bind = 'unix:/tmp/gunicorn.sock'

workers = os.getenv('WORKERS', 1)
threads = os.getenv('THREADS', 1)
# backlog - The number of pending connections.
backlog = 64
# Workers silent for more than this many seconds are killed and restarted.
timeout = 300
# Timeout for graceful workers restart.
graceful_timeout = 300
# The maximum number of requests a worker will process before restarting.
max_requests = 0
max_requests_jitter = 0
worker_class = 'uvicorn.workers.UvicornWorker'
worker_tmp_dir = '/dev/shm'
# The number of seconds to wait for requests on a Keep-Alive connection.
keepalive = 120
