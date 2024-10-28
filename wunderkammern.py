def activate():
    print("Activated")


class Wunderkammern:
    def topics(self):
        print("Learning, Life, Tech, Science, Productivity")


class CommonplaceBook(Wunderkammern):
    def insights(self):
        print("Don't eat with people you wouldn't starve with")
    def anime(self):
        return "Erwin Smith's Last Speech"


class Podcasts(Wunderkammern):
    def hosts(self):
        print("Andrew Huberman, Joe Rogan, Lex Fridman")