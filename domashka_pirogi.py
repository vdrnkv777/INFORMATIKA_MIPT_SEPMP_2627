import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris_data.csv')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

kinds_counts = df['Species'].value_counts()

ax1.pie(
    kinds_counts, 
    labels=kinds_counts.index,
    autopct='%1.1f%%',            
    startangle=90,               
    colors=['#ff9999', '#66b3ff', '#99ff99'], 
    textprops={'fontsize': 12}   
)
ax1.set_title('Распределение по видам ирисов', fontsize=16, fontweight='bold')

bins = [0, 1.2, 1.5, float('inf')] 
labels = ['<= 1.2 см', '1.2 - 1.5 см', '> 1.5 см']

df['Petal_Category'] = pd.cut(df['PetalLengthCm'], bins=bins, labels=labels)

petals_counts = df['Petal_Category'].value_counts().sort_index()

ax2.pie(
    petals_counts, 
    labels=petals_counts.index, 
    autopct='%1.1f%%', 
    startangle=90,
    colors=['#c2c2f0', '#ffb3e6', '#c2f0c2'],
    textprops={'fontsize': 12}
)
ax2.set_title('Распределение по длине лепестка', fontsize=16, fontweight='bold')

plt.tight_layout() 
plt.show()