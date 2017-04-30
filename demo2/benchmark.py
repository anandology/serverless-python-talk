"""Script to load test a URL.
"""
import requests
import argparse
import logging
import time
from multiprocessing.pool import ThreadPool

logger = logging.getLogger(__name__)

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("-c", "--concurrency",
        help="Number of concurrent connections",
        type=int,
        default=4)
    p.add_argument("-n",
        help="Number requests to perform",
        type=int,
        default=100)
    p.add_argument("url", help="URL to fetch")
    return p.parse_args()

def fetch(args):
    n, url = args
    t1 = time.time()
    result = requests.get(url).text
    t2 = time.time()
    t = t2-t1
    logger.info("%d - fetched the URL in %.1f seconds", n, t)
    return result

def setup_logger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def main():
    setup_logger()
    args = parse_args()
    logger.info("BEGIN")

    pool = ThreadPool(args.concurrency)
    urls = [args.url] * args.n
    t1 = time.time()
    pool.map(fetch, enumerate(urls))
    t2 = time.time()
    t = t2-t1
    req_sec = args.n / t
    logger.info("Fetched %s times using %s threads", args.n, args.concurrency)
    logger.info("Total time: %s", t)
    logger.info("Requests/sec: %s", req_sec)

if __name__ == '__main__':
    main()
