"""
Design an algorithm that determines a researcher's h-index
Pg: 1
"""


def h_index(citations):
    citations.sort()
    total = len(citations)
    h_number = None
    for idx, val in enumerate(citations):
        least_papers = total - idx
        if val <= least_papers:
            h_number = val
    return h_number


if __name__ == "__main__":
    print(h_index([1, 4, 1, 4, 2, 1, 3, 5, 6]))
    print(h_index([1, 1, 1, 2, 3, 4, 4, 5, 6]))



