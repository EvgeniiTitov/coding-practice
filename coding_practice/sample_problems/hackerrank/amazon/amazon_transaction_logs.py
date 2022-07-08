# !/bin/python3

import math
import os
import random
import re
import sys


"""
#!/bin/python3

import math
import os
import random
import re
import sys



#

"""


#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER threshold
#


def processLogs(logs, threshold):
    # Write your code here
    # logs: List[str],
    # threshold: int

    if not len(logs):
        return []

    from collections import defaultdict

    transactions_per_user = defaultdict(int)

    for transaction in logs:
        sender, recipient, amount = transaction.split(" ")
        if sender == recipient:
            transactions_per_user[sender] += 1
        else:
            transactions_per_user[sender] += 1
            transactions_per_user[recipient] += 1

    out = []
    for user, transactions in transactions_per_user.items():
        if transactions >= threshold:
            out.append(user)

    return sorted(out, key=lambda e: int(e))


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    threshold = int(input().strip())

    result = processLogs(logs, threshold)

    fptr.write("\n".join(result))
    fptr.write("\n")

    fptr.close()
