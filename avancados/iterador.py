
def foreach(iteravel):
    iterador = iter(iteravel)
    while True:
        try:
            print(next(iterador))
        except StopIteration:
            break
