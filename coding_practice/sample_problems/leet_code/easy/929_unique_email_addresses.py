from typing import List


"""
Summary: Iterate over emails, split on @ and process the left part. Remove
dots and ignore anything after +.
_______________________________________________________________________________

https://leetcode.com/problems/unique-email-addresses/

Every valid email consists of a local name and a domain name, separated by 
the '@' sign. Besides lowercase letters, the email may contain one or more 
'.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and 
"leetcode.com" is the domain name.

If you add periods '.' between some characters in the local name part of an 
email address, mail sent there will be forwarded to the same address without 
dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the 
same email address.

If you add a plus '+' in the local name, everything after the first plus sign 
will be ignored. This allows certain emails to be filtered. Note that this rule 
does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], 
return the number of different addresses that actually receive mails.

Example 1:
Input: emails = [
    "test.email+alex@leetcode.com",
    "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com"
]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

Example 2:
Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3
"""


class Solution:

    # T: O(N2); S: O(N)
    def numUniqueEmails(self, emails: List[str]) -> int:

        def _process_email(email: str) -> str:
            if not email:
                return ""

            local_name, domain_name = email.split("@")

            local_name_processed = []
            for char in local_name:  # O(N)
                if char == ".":
                    continue
                elif char == "+":
                    break
                local_name_processed.append(char)
            return f'{"".join(local_name_processed)}@{domain_name}'

        unique_emails = set()
        for email in emails:  # O(N)
            processed_email = _process_email(email)
            print(f"{email} -> {processed_email}")
            unique_emails.add(processed_email)

        return len(unique_emails)


def main():
    print(Solution().numUniqueEmails(
        # emails=[
        #     "test.email+alex@leetcode.com",
        #     "test.e.mail+bob.cathy@leetcode.com",
        #     "testemail+david@lee.tcode.com"
        # ]
        emails=["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
    ))


if __name__ == '__main__':
    main()
