from typing import List, Dict, Set
from collections import defaultdict
import heapq
import time


def total_time_per_user(logs: List[Dict]) -> Dict[str, float]:
    """Calculate total duration spent by each user."""
    
    user_totals = defaultdict(float)

    for log in logs:
        user = log["user"]
        duration = log["duration"]
        user_totals[user] += duration

    return dict(user_totals)


def most_active_users(logs: List[Dict], k: int) -> List[str]:
    """Return top k users with the highest total activity time."""
    
    totals = total_time_per_user(logs)

    top_users = heapq.nlargest(
        k,
        totals.items(),
        key=lambda item: item[1]
    )

    return [user for user, _ in top_users]


def unique_actions(logs: List[Dict]) -> Set[str]:
    """Return a set of unique actions performed."""
    
    return {log["action"] for log in logs}


if __name__ == "__main__":

    logs = [
        {"user": "user 1", "action": "YouTube", "duration": 30.5},
        {"user": "user 2", "action": "Instagram", "duration": 20},
        {"user": "user 3", "action": "Chrome", "duration": 40},
        {"user": "user 4", "action": "YouTube", "duration": 10},
        {"user": "user 5", "action": "WhatsApp", "duration": 25}
    ]

    start_time = time.perf_counter()

    totals = total_time_per_user(logs)
    print("Total time per user:")
    print(totals)

    print("\nMost active users:")
    print(most_active_users(logs, 2))

    print("\nUnique actions:")
    print(unique_actions(logs))

    end_time = time.perf_counter()

    execution_time = (end_time - start_time) * 1e6
    print(f"\nExecution Time: {execution_time:.2f} µs")