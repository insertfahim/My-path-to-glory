class webpage:
    def __init__(self,link):
        self.prev=None
        self.next=None
        self.link=link

class BrowserHistory:

    def __init__(self, homepage: str):
        self.home=webpage(homepage)
        self.curr=self.home
        

    def visit(self, url: str) -> None:
        newpage = webpage(url)
        self.curr.next=newpage
        newpage.prev=self.curr
        self.curr=newpage

    def back(self, steps: int) -> str:
        curr=self.curr
        while curr.prev and steps>0:
            curr=curr.prev
            steps-=1
        self.curr=curr
        return curr.link
        

    def forward(self, steps: int) -> str:
        curr=self.curr
        while curr.next and steps>0:
            curr=curr.next
            steps-=1
        self.curr=curr
        return curr.link
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)