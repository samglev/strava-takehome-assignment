"""
Performs sorting and analysis of data and reports results

Author: Sam Lev
3/16/26
"""
from math import ceil

BYTES_TO_GB = 2 ** 30
SEPARATOR = "\n----------------------------------------------------"
MAX_GB_PER_SHARD = 30


def print_largest_indexes(data):
    data = sort_by_field(data, "size", True)

    print(SEPARATOR)
    print("Largest Indexes by Size:\n")
    for i in range(5):
        curr_index = data[i]
        print(f"{curr_index["name"]} -- {curr_index["size"]} GB")


def print_most_shards(data):
    data = sort_by_field(data, "shards", True)

    print(SEPARATOR)
    print("Largest Indexes by Shard Count:\n")
    for i in range(5):
        curr_index = data[i]
        print(f"{curr_index["name"]} -- {curr_index["shards"]} shards")


def print_least_balanced(data):
    data = sort_by_field(data, "shard ratio", True)

    print(SEPARATOR)
    print("Least Balanced Indexes:\n")
    for i in range(5):
        curr_index = data[i]
        curr_ratio = curr_index["shard ratio"]
        if curr_ratio <= 30:
            print("All remaining indexes have less than 30GB per shard!")
            break
        new_shard_count = ceil(curr_index["size"] / MAX_GB_PER_SHARD)

        print(f"Index: {curr_index["name"]}")
        print(f"Current shard count: {curr_index["shards"]} ({curr_ratio} GB per shard)")
        print(f"Recommended shard count: {new_shard_count}\n")


def pre_process(data):
    """
    Adds a field for size-to-shard ratio, converts size to GB, and converts all
    numerical data to numerical types. returns a new list
    """
    processed_data = []
    for item in data:
        size_in_gb = int(item["pri.store.size"]) / BYTES_TO_GB
        shards = int(item["pri"])
        shard_ratio = size_in_gb / shards
        processed_data.append({"name": item["index"], "size": size_in_gb,
                               "shards": shards, "shard ratio": shard_ratio})
    return processed_data


def sort_by_field(data, key, reverse=False):
    return sorted(data, key=lambda item : item[key], reverse=reverse)