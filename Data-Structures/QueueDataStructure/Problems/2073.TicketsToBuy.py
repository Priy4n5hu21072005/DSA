class sol:
    def BuyTickets(self,tickets,k):
        ans = 0
        for i in range(len(tickets)):
            if i <= k:
                ans += min(tickets[i],tickets[k])
            else:
                ans+=min(tickets[i],tickets[k]-1)
        return ans   