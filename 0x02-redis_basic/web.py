#!/usr/bin/env python3

import requests
import redis
import time

def get_page(url: str) -> str:
    cache_expiration = 10  # Cache expiration time in seconds
    cache_key = f"count:{url}"

    # Connect to Redis
    redis_client = redis.Redis()

    # Check if the URL is already cached
    cached_page = redis_client.get(url)
    if cached_page:
        # If cached, increase the access count and return the cached page
        redis_client.incr(cache_key)
        return cached_page.decode("utf-8")

    # If not cached, fetch the page content from the URL
    response = requests.get(url)

    # Cache the page content with the given URL as the key
    redis_client.setex(url, cache_expiration, response.text)

    # Increase the access count for the URL
    redis_client.incr(cache_key)

    return response.text

# Test the function
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/https://www.example.com"
    for _ in range(5):
        page_content = get_page(url)
        print(page_content)
        time.sleep(2)  # Sleep to demonstrate caching

    # Display access count
    redis_client = redis.Redis()
    access_count = redis_client.get(f"count:{url}")
    print(f"Access count for {url}: {int(access_count) if access_count else 0}")
