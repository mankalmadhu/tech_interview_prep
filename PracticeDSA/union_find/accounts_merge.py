# https://leetcode.com/problems/accounts-merge/
"""
Accounts Merge

accounts[i] = [name, email1, email2, ...]. The same person can appear
as multiple separate account entries, identified by sharing at least
one email in common (name alone does NOT imply same person). Merge
all accounts belonging to the same person and return each merged
account as [name, sorted list of all unique emails].

Approach: treat each email as a Union-Find element. For every
account, union its first email with each of its other emails - this
transitively merges accounts across the whole input (two accounts
that each independently share an email with a third account end up
in the same group, with no explicit pairwise account comparison
needed). After all unions, bucket every email under its root via one
pass over the full email list, then build the final [name, sorted
emails] entries from the buckets.

Note: an email -> name dict is used purely to recover the name for
a given root during the final build step; it is never iterated by
value (which could silently drop entries when two different
accounts share an email key) - it's only ever read by key, and by
construction email_to_name[root] is guaranteed to map to a name
that's correct for every email in that root's group (since all
emails sharing a root belong to the same merged person).

Complexity Analysis:
--------------------
Time:  O(E log E), where E = total number of emails across all
       accounts.
       - Building unique_emails, UnionFind init, the union loop, and
         email_to_name are each O(E) (union-find ops are amortized
         ~O(a(E)), effectively O(1)).
       - Bucketing every email under its root is O(E) finds.
       - The only place sorting happens is the final per-group
         sorted(emails) call; summed across all groups this is
         O(E log E) in the worst case (one group holding all E
         emails).
       So the single final sort dominates: O(E log E) overall.
Space: O(E) - unique_emails, the UnionFind's internal dict,
       email_to_name, and the groups dict are each O(E).
"""

import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(__file__))
from union_find import UnionFind  # noqa: E402


def solve(accounts):
    unique_emails = list({email for account in accounts for email in account[1:]})

    uf = UnionFind(unique_emails)

    for account in accounts:
        email_1 = account[1]
        for email in account[2:]:
            uf.union(email_1, email)

    email_to_name = {email: account[0] for account in accounts for email in account[1:]}

    groups = defaultdict(list)
    for email in unique_emails:
        root = uf.find(email)
        groups[root].append(email)

    result = []
    for root, emails in groups.items():
        name = email_to_name[root]
        result.append([name] + sorted(emails))

    return result


if __name__ == "__main__":
    accounts1 = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    expected1 = [
        ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    result1 = solve(accounts1)
    assert sorted(result1) == sorted(expected1)
    print("Example test passed!")

    # ---- stress test vs independent brute force ----
    import random
    import string

    def brute_force(accounts):
        """Independent reference: builds its own email-adjacency
        graph (not reusing UnionFind at all) and merges groups via
        plain BFS."""
        adj = {}
        name_of = {}
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                name_of[email] = name
                adj.setdefault(email, set())
            first = emails[0]
            for email in emails[1:]:
                adj[first].add(email)
                adj[email].add(first)

        seen = set()
        merged = []
        for email in adj:
            if email in seen:
                continue
            group = []
            queue = [email]
            seen.add(email)
            while queue:
                node = queue.pop()
                group.append(node)
                for nxt in adj[node]:
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append(nxt)
            merged.append([name_of[email]] + sorted(group))
        return merged

    def random_accounts(num_people, max_accounts_per_person=3, max_emails=4):
        """Generates accounts for num_people distinct people. Each
        person gets a disjoint pool of emails; some of those emails
        get reused across that person's multiple account entries
        (simulating real duplicate-account merges), while different
        people never share emails (so expected groups are known)."""
        accounts = []
        email_counter = 0
        for person in range(num_people):
            name = random.choice(string.ascii_uppercase[:5])
            pool_size = random.randint(1, max_emails)
            pool = [f"e{email_counter + i}@mail.com" for i in range(pool_size)]
            email_counter += pool_size

            num_accounts = random.randint(1, max_accounts_per_person)
            for _ in range(num_accounts):
                k = random.randint(1, len(pool))
                emails = random.sample(pool, k)
                accounts.append([name] + emails)
        random.shuffle(accounts)
        return accounts

    def normalize(merged):
        return sorted([acc[0]] + sorted(acc[1:]) for acc in merged)

    random.seed(42)
    trials = 300
    for t in range(trials):
        num_people = random.randint(1, 8)
        accounts = random_accounts(num_people)

        expected = normalize(brute_force(accounts))
        actual = normalize(solve(accounts))

        assert expected == actual, (
            f"mismatch on trial {t}: accounts={accounts}\n"
            f"expected={expected}\nactual={actual}"
        )

    print(f"Stress test passed: {trials} trials.")
