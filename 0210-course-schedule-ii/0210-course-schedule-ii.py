class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)

        for u, v in prerequisites:
            g[u].append(v)

        seen = set()
        path = set()
        op = []

        def dfs(node):
            if node in path:
                return True

            if node in seen:
                return False

            seen.add(node)
            path.add(node)

            for i in g[node]:
                if dfs(i):
                    return True

            path.remove(node)
            op.append(node)

            return False

        for i in range(numCourses):
            if dfs(i):
                return []

        return op