""" set of utilities to turn data objects into neatly formatted telegram message packets """


def build_watchlist_str(entry):
    """takes a watchlist entry and returns a neatly formatted string"""
    strn = ""
    for i in entry["watchList"]:
        strn = strn + "\n\n" + i["market"]
        for j in i["aggs"]:
            strn = strn + "\n\t" + str(j)
    return strn


def dict_to_msg(dict_):
    """takes a top-level dict and returns a neat string"""
    str_ = ""
    for entry in sorted(list(dict_.keys())):
        str_ = str_ + "\n" + entry + " : " + str(dict_[entry])
    return str_
