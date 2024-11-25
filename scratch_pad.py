def outer():
    coin = "Head"
    def inner():
        nonlocal coin
        coin = "Tail"
        print(f'Inner: {coin}')
    inner()
    print(f'Outer: {coin}')


outer()