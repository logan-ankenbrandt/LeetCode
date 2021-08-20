import collections
from typing import List
import snoop as dog

@dog
def subdomainVisits(cpdomains: List[str]) -> List[str]:
    """
    1. Goal 
        - Return an array of the number of visits to
        each subdomain in an array.
    2. Examples
        - Example #1
            a. Input:
                i. ["9001 discuss.leetcode.com"]
            b. Output:
                i. [["9001", "discuss.leetcode.com", "9001"]]
        - Example #2
            a. Input:
                i. ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
            b. Output:
                i. [["9001", "google.mail.com", "9001"], ["50", "yahoo.com", "50"], ["1", "intel.mail.com", "1"], ["5", "wiki.org", "5"]]
    3. Implementation
        - Summary
        - Steps
            a. Initailize a counter variable to count 


    """
    
    ans = collections.Counter()
    for domain in cpdomains:
        count, domain = domain.split()
        count = int(count)
        fragments = domain.split('.')
        for i in range(len(fragments)):
            ans[".".join(fragments[i:])] += count

    l = []
    for dom, ct in ans.items():
        ans = "{} {}".format(ct, dom)
        l.append(ans)
    
    return l

print(subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))