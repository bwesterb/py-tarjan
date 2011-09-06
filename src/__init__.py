from collections import namedtuple

__all__ = ['tarjan',
           'tarjan_iter',
           'tarjan_recursive']

""" Context used to implement the algorithm without recursion in @tarjan
    and @tarjan_iter """
TarjanContext = namedtuple('TarjanContext',
                                ['g',           # the graph
                                 'S',           # The main stack of the alg.
                                 'S_set',       # == set(S) for performance
                                 'index',       # { v : <index of v> }
                                 'lowlink',     # { v : <lowlink of v> }
                                 'T',           # stack to replace recursion
                                 'ret'])        # return code

def _tarjan_head(ctx, v):
        """ Used by @tarjan and @tarjan_iter.  This is the head of the
            main iteration """
        ctx.index[v] = len(ctx.index)
        ctx.lowlink[v] = ctx.index[v]
        ctx.S.append(v)
        ctx.S_set.add(v)
        it = iter(ctx.g.get(v, ()))
        ctx.T.append((it,False,v,None))

def _tarjan_body(ctx, it, v):
        """ Used by @tarjan and @tarjan_iter.  This is the body of the
            main iteration """
        for w in it:
                if w not in ctx.index:
                        ctx.T.append((it,True,v,w))
                        _tarjan_head(ctx, w)
                        return
                if w in ctx.S_set:
                        ctx.lowlink[v] = min(ctx.lowlink[v], ctx.index[w])
        if ctx.lowlink[v] == ctx.index[v]:
                scc = []
                w = None
                while v != w:
                        w = ctx.S.pop()
                        scc.append(w)
                        ctx.S_set.remove(w)
                ctx.ret.append(scc)

def tarjan_iter(g):
        """ Returns the strongly connected components of the graph @g
            in a topological order.

                @g is the graph represented as a dictionary
                        { <vertex> : <successors of vertex> }.

            This function does not recurse.  It returns an iterator. """
        ctx = TarjanContext(
                g = g,
                S = [],
                S_set = set(),
                index = {},
                lowlink = {},
                T = [],
                ret = [])
        main_iter = iter(g)
        while True:
                try:
                        v = next(main_iter)
                except StopIteration:
                        return
                if v not in ctx.index:
                        _tarjan_head(ctx, v)
                while ctx.T:
                        it, inside, v, w = ctx.T.pop()
                        if inside:
                                ctx.lowlink[v] = min(ctx.lowlink[w],
                                                        ctx.lowlink[v])
                        _tarjan_body(ctx, it, v)
                        if ctx.ret:
                                assert len(ctx.ret) == 1
                                yield ctx.ret.pop()

def tarjan(g):
        """ Returns the strongly connected components of the graph @g
            in a topological order.

                @g is the graph represented as a dictionary
                        { <vertex> : <successors of vertex> }.
        
            This function does not recurse. """
        ctx = TarjanContext(
                g = g,
                S = [],
                S_set = set(),
                index = {},
                lowlink = {},
                T = [],
                ret = [])
        main_iter = iter(g)
        while True:
                try:
                        v = next(main_iter)
                except StopIteration:
                        return ctx.ret
                if v not in ctx.index:
                        _tarjan_head(ctx, v)
                while ctx.T:
                        it, inside, v, w = ctx.T.pop()
                        if inside:
                                ctx.lowlink[v] = min(ctx.lowlink[w],
                                                        ctx.lowlink[v])
                        _tarjan_body(ctx, it, v)

def tarjan_recursive(g):
        """ Returns the strongly connected components of the graph @g
            in a topological order.

                @g is the graph represented as a dictionary
                        { <vertex> : <successors of vertex> }.
                        
            This function recurses --- large graphs may cause a stack
            overflow. """
        S = []
        S_set = set()
        index = {}
        lowlink = {}
        ret = []

        def visit(v):
                index[v] = len(index)
                lowlink[v] = index[v]
                S.append(v)
                S_set.add(v)
                for w in g.get(v,()):
                        if w not in index:
                                visit(w)
                                lowlink[v] = min(lowlink[w], lowlink[v])
                        elif w in S_set:
                                lowlink[v] = min(lowlink[v], index[w])
                if lowlink[v] == index[v]:
                        scc = []
                        w = None
                        while v != w:
                                w = S.pop()
                                scc.append(w)
                                S_set.remove(w)
                        ret.append(scc)

        for v in g:
                if not v in index:
                        visit(v)
        return ret
