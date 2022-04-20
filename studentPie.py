df = pd.read_csv('student.csv')
df.head()

df['lunch'].value_counts()

name = df['lunch'].value_counts().index.tolist()
name

numbers = df['lunch'].value_counts().tolist()
numbers

color_pal = ['#d8829d', '#6ab547']

fig = plt.figure(figsize=(8,8))
plt.pie(numbers, labels=name, 
        autopct='%1.1f%%',
        colors=color_pal)
plt.show()