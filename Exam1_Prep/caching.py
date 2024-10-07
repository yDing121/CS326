def LRU(pages, cache_size):
    cache = []
    page_faults = 0

    for page in pages:
        if page not in cache:
            # Page fault occurs
            page_faults += 1
            if len(cache) == cache_size:
                # Remove the least recently used page
                cache.pop(0)
        else:
            # Remove page from its current position
            cache.remove(page)
        # Add the current page at the end (most recently used)
        cache.append(page)

        print(f"Cache: {cache}")

    return page_faults


def furthest_in_future(pages, cache_size):
    cache = []
    page_faults = 0

    for i, page in enumerate(pages):
        if page not in cache:
            page_faults += 1
            if len(cache) == cache_size:
                # Find the page in the cache that will be used furthest in future
                future_indices = []
                for cached_page in cache:
                    if cached_page in pages[i + 1:]:
                        future_indices.append(pages[i + 1:].index(cached_page))
                    else:
                        future_indices.append(float('inf'))
                # Remove the page with the furthest usage in the future
                furthest_page_index = future_indices.index(max(future_indices))
                cache.pop(furthest_page_index)
        cache.append(page)

        print(f"Cache: {cache}")

    return page_faults


def fif_cache(capacity, future_requests):
    # Initialize an empty cache and a list to track the cache occupancy
    cache = []
    faults = 0

    # Iterate through future requests
    for request in future_requests:
        # Check if request is already in the cache
        if request in cache:
            continue  # If it is, no need to do anything
        faults += 1
        # If cache is not full, add the request
        if len(cache) < capacity:
            cache.append(request)
        else:
            # Cache is full, find the request to evict
            # Determine the request in cache that is farthest in the future
            farthest_request = -1
            farthest_index = -1

            for i in range(len(cache)):
                try:
                    # Find the index of the cached request in future_requests
                    index = future_requests.index(cache[i])
                    # Update if this request is further in future than current farthest
                    if index > farthest_index:
                        farthest_index = index
                        farthest_request = i
                except ValueError:
                    # If the request is not found in future_requests, it can be evicted
                    farthest_request = i
                    break

            # Evict the request that is farthest in the future
            cache[farthest_request] = request
    print(f"FIF2 faults:\t{faults}")
    return cache




if __name__ == '__main__':
    # Example usage:
    pages = [1, 2, 3, 4, 2, 5, 3, 1, 4]
    cache_size = 3

    print("LRU:")
    lru_faults = LRU(pages, cache_size)
    print(f"Total page faults (LRU): {lru_faults}")

    print("\nFurthest in Future:")
    fif_faults = furthest_in_future(pages, cache_size)
    print(f"Total page faults (Furthest in Future): {fif_faults}")

    print("_______")
    result_cache = fif_cache(cache_size, pages)
    print("Final cache content:", result_cache)
