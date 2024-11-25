import pandas as pd

df = pd.read_csv('tarantino.csv')

# число проклятий, летальных исходов и их соотношение по фильмам 
event_counts = df.groupby(['movie', 'type']).size().unstack(fill_value=0)
event_counts['death_to_word_ratio'] = event_counts['death'] / event_counts['word']
print(event_counts)

# частота употребления конкретных проклятий 
word_counts = df[df['type'] == 'word'].groupby(['word']).size().reset_index(name='word_count')
word_counts_sorted = word_counts.sort_values(by='word_count', ascending=False)
print(word_counts_sorted)

# распределение времени между проклятиями 
words = df[df['type'] == 'word']
words_sorted = words.sort_values(by=['movie', 'minutes_in'])
words_sorted['time_diff'] = words_sorted.groupby('movie')['minutes_in'].diff()
print(words_sorted[['movie', 'minutes_in', 'time_diff']])
