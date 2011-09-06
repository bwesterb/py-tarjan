from tarjan import tarjan

def tc(g):
        """ Given a graph @g, returns the transitive closure of @g """
        ret = {}
        for scc in tarjan(g):
                ws = set()
                ews = set()
                for v in scc:
                        ws.update(g[v])
                for w in ws:
                        assert w in ret or w in scc
                        ews.add(w)
                        ews.update(ret.get(w,()))
                if len(scc) > 1:
                        ews.update(scc)
                ews = tuple(ews)
                for v in scc:
                        ret[v] = ews
        return ret
