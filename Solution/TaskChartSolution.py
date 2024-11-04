import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('dataset.csv')

platforms = ['PS4', 'XOne', 'PC', 'WiiU']
filtered_data = data[data['platform'].isin(platforms)]

colors = {
    "Action": "#ff9999",
    "Adventure": "#ffcc66",
    "Fighting": "#cccc66",
    "Misc": "#99cc66",
    "Platform": "#66cc99",
    "Puzzle": "#66cccc",
    "Racing": "#66ccff",
    "Role-Playing": "#6699cc",
    "Shooter": "#9966cc",
    "Simulation": "#cc66cc",
    "Sports": "#cc6699",
    "Strategy": "#cc9999"
}

game_counts = filtered_data.groupby(['platform', 'genre']).size().unstack().fillna(0)

game_counts = game_counts.sort_values("Action", ascending=False)

game_counts.plot(kind='bar', figsize=(12, 8), color=colors)

plt.xlabel('platform')
plt.xticks(rotation=0)
plt.ylabel('count')
plt.legend(title='genre',bbox_to_anchor=(1.00, 0.75), loc='upper left')
plt.tight_layout()
plt.show()
