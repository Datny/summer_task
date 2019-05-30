def sort_by_single_mb_cost(memes_list):
    """Sorts original memes list, by new number
    that is created by dividing price/size"""
    memes_list.sort(key=lambda meme: meme[2] / meme[1], reverse=True)


def calculate(usb_size, memes):
    """Calculate optimal set of memes that will
    fit on pendrive of fixed size. """
    usb_size_mb = usb_size*1024
    sort_by_single_mb_cost(memes)
    set_of_memes = set()
    total_income = 0
    usb_used_space = 0
    for meme in memes:
        if (usb_used_space + meme[1] > usb_size_mb) \
                or ((meme[1] < 0) or (meme[2]) < 0):
            continue
        elif meme[0] not in set_of_memes:
            usb_used_space += meme[1]
            total_income += meme[2]
            set_of_memes.add(meme[0])
    return total_income, set_of_memes


