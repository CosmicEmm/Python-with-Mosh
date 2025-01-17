class Emm:
    def __hash__(self):
        return 1

emm = Emm()
print(hash(emm))
css = Emm()
print(hash(emm))
