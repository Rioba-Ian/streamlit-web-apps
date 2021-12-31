import pandas as pd

clean_df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/streamlit_freecodecamp/main/app_8_classification_penguins/penguins_cleaned.csv')

df = clean_df.copy()
target = 'species'
encode = ['sex', 'island']

for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df,dummy], axis=1)
    del df[col]

target_mapper = {'Adelie':0, 'Chinstrap': 1, 'Gentoo': 2}
def target_encode(val):
    return target_mapper[val]

df['species'] = df['species'].apply(target_encode)

# separating x and y 
X = df.drop('species', axis=1)
Y = df['species']

# build random forest
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(X, Y)

import pickle
pickle.dump(clf, open('penguins_clf.pkl', 'wb'))
