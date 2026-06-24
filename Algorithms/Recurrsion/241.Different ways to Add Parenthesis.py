from pasta.base.annotate import expression

from Algorithms.DFS.p111 import Solution


class solution:
    def AddParanthesis(self,expression):
        def solve(exp):
            ans = []
            for i in range(len(exp)):
                if exp[i]=='+' or exp[i]=='-' or exp[i]=='*':
                    lp=exp[:i]
                    rp=exp[i+1:]
                    la=solve(lp)
                    ra=solve(rp)
                    for l in la:
                        for r in ra:
                            if exp[i]=='+':
                                ans.append(l+r)
                            elif exp[i]=='-':
                                ans.append(l-r)
                            else:
                                ans.append(l*r)
            if len(ans)==0:
                ans.append(int(exp))
            return ans
        return solve(expression)
