"""
return plot of item frequency in video
json file as input
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def graph(json):

    ITEMS_APPEARED = []

    for i in json:
        for key, value in i.items():
            if key not in ITEMS_APPEARED:
                ITEMS_APPEARED.append(key)

    list = [[i] for i in json]
    dict = {}
    for i,j in enumerate(list):
        dict[i] = j

    df = pd.DataFrame(columns = [i for i in ITEMS_APPEARED], index = [i for i in range(len(dict))])
    df.index.name = 'Seconds'

    for item in ITEMS_APPEARED:
        for i, j in dict.items():
            try:
                j = j[0]
                for k in j:
                    if k == item:
                        df[item].iloc[i] = j[item]
                    else:
                        pass
            except KeyError:
                pass

    df.fillna(value=0, inplace=True)

    fontP = FontProperties()
    fontP.set_size('small')
    fig, ax = plt.subplots()
    for i in ITEMS_APPEARED:
        ax.plot(df.index, df[i], label = i)
    plt.title('{} Second Video Log: {} items found'.format(len(df.index), len(ITEMS_APPEARED)),
              fontname = 'Ubuntu', fontstyle = 'italic')
    plt.xlim((-2, len(df.index) + 2))
    plt.ylabel('Item Frequency/Second')
    plt.xlabel('Video Length (s)')
    ax.legend(loc = 'right top',
              prop = fontP,
              fancybox = True)
    plt.tight_layout()

    plt.savefig('output/item-frequency.png')
    df.to_csv('output/video_log.csv')
