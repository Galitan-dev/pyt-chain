class ChainLink:
    def __init__(self, next, content) {
        self.next = next
        self.content = content
    }

    def isEmpty(self):
        return self.content == None

    def length(self):
        if (self.isEmpty())