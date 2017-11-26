
from copy import deepcopy


class DependencyHelper:
    def __init__(self):
        self._graph = {}

    def add(self, a, b):
        self._graph.setdefault(b, set())
        self._graph.setdefault(a, set())
        self._graph[b].add(a)

    def __add__(self, pair):
        self.add(*pair)
        return self

    def remove(self, a, b):
        self._graph[b].remove(a)

    def __sub__(self, pair):
        self.remove(*pair)
        return self

    def copy(self):
        d = DependencyHelper()
        d._graph = deepcopy(self._graph)

        return d

    def get_dependent(self, key):
        return tuple(self._graph[key])

    def has_dependencies(self):
        if not self._graph:
            return True

        flags = dict((key, 0) for key in self._graph.keys())

        for key in self._graph.keys():
            if flags[key] == 0:
                stack = [key]

                while stack:
                    v = stack[-1]

                    if flags[v] == 0:
                        flags[v] = 1

                        for sv in self._graph[v]:
                            if flags[sv] == 1:
                                return False
                            stack.append(sv)
                    else:
                        flags[v] = 2
                        stack.pop()

        return True

    def __bool__(self):
        return self.has_dependencies()


class PriorityHelper(DependencyHelper):
    def enumerate_priorities(self):
        flags = {key: False for key in self._graph.keys()}
        answer = {key: 0 for key in self._graph.keys()}
        parents = {}

        for key in self._graph.keys():
            if not flags[key]:
                stack = [key]

                while stack:
                    v = stack[-1]

                    if flags[v] == 0:
                        flags[v] = 1

                        for sv in self._graph[v]:
                            if flags[sv] == 2 and answer[v] >= answer[sv]:
                                answer[v] = answer[sv] - 1

                        for sv in self._graph[v]:
                            if flags[sv] == 1 and answer[v] > answer[sv]:
                                parents[sv] = v

                                s, p = sv, v
                                while p != sv:
                                    answer[p] = answer[s]
                                    s, p = p, parents[p]

                        for sv in self._graph[v]:
                            if flags[sv] == 0:
                                parents[sv] = v

                                answer[sv] = answer[v] + 1
                                stack.append(sv)
                    else:
                        flags[v] = 2
                        stack.pop()

                        for sv in self._graph[v]:
                            if answer[v] > answer[sv]:
                                answer[v] = answer[sv]

        return answer
