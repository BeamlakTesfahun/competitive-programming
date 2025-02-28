class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = collections.defaultdict(int)
        res = []

        for i in cpdomains:
            count, domain = i.split()

            count = int(count)
            frag = domain.split(".")
            

            for i in range(len(frag)):
                counts['.'.join(frag[i:])] += count


        for domain, count in counts.items():
            val = str(count) + " " + domain
            res.append(val)
        return res
        