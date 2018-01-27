import pandas as pd
import matplotlib.pyplot as plt

dateparse = lambda x: pd.datetime.strptime(x, '%m/%Y')
df = pd.read_csv('test.csv', sep='\t', parse_dates=['date'], date_parser=dateparse, thousands=',',
                 names=['date', 'assets'], index_col='date')
df['growth'] = (df['assets'] - df['assets'].shift())
df['growth_perc'] = (100 / df['assets'].shift() * df['growth'])
print(df)


def formatBarAxis(ax):
    ax.yaxis.grid()
    ax.set_axisbelow(True)
    ax.yaxis.grid(color='gray', linestyle='dashed', linewidth=1)
    # For formatting the date labels see: https://stackoverflow.com/questions/30133280/pandas-bar-plot-changes-date-format


plt.figure(figsize=(12, 7))

plt.subplot(2, 2, 1)
ax = df['growth'].plot.bar(color='red', title="Monthly savings")
formatBarAxis(ax)

plt.subplot(2, 2, 2)
df['assets'].plot.line(title="Asset growth")

plt.subplot(2, 2, 3)
ax = df['growth_perc'].plot.bar(color='red', title="Relative asset growth in %")
formatBarAxis(ax)

mng = plt.get_current_fig_manager()
plt.show()
