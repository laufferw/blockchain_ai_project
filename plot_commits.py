import matplotlib.pyplot as plt
import pandas as pd

# Load commit data
data = []
with open('commit_counts.txt', 'r') as f:
    for line in f:
        parts = line.strip().split()
        count = int(parts[0])
        date = parts[1]
        data.append((date, count))

# Create a DataFrame
df = pd.DataFrame(data, columns=['Date', 'Commits'])
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# Plot the data
plt.figure(figsize=(10, 6))
df.plot(kind='bar')
plt.title('Commits in the Last 30 Days')
plt.xlabel('Date')
plt.ylabel('Number of Commits')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('commit_timeseries.png')
plt.show()
