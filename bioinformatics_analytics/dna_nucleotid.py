#####################
# import libraries
#####################

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

#####################
# page title
#####################

image = Image.open('dna-logo.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

***
""")

#####################
# Input Text Box
#####################

st.header('Enter the DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # skips the sequence name first name 
sequence = ''.join(sequence) # concatenates list to string

st.write("""
***
""")

# prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

# DNA nucleotide count 
st.header('OUTPUT (DNA Nucleotide Count)')

# print dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),
    ])
    return d 

x = DNA_nucleotide_count(sequence)

# x_label = list(x)
# x_values = list(x.values())

x

# 2. print text

st.subheader('2. Print text')
st.write('There are ' + str(x['A']) + ' adenine (A)')
st.write('There are ' + str(x['T']) + ' thymine (T)')
st.write('There are ' + str(x['G']) + ' guanine (G)')
st.write('There are ' + str(x['C']) + ' cytosine (C)')

# 3. Display dataframe
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(x, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
st.write(df)

# ## 4. display bar chart using Altair 
st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x = 'nucleotide',
    y = 'count'
)
p = p.properties(
    width=alt.Step(80) # controls width of bar 
)

st.write(p)




