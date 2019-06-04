def calculate(usb_size, memes):
    W = usb_size * 1024
    memes = set(memes)
    n = len(memes)
    val = []
    wt = []
    memes_names = []
    choosen_memes = set()

    for meme in memes:
        val.append(meme[2])
        wt.append(meme[1])
        memes_names.append(meme[0])

    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0

            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    res = K[n][W]

    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:
            choosen_memes.add(memes_names[i-1])
            res = res - val[i - 1]
            w = w - wt[i - 1]

    return (K[n][W], choosen_memes)

