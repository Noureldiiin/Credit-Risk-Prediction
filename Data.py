import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Credit Data Dashboard",
    page_icon="🏦",
)

df = pd.read_csv('credit_data.csv')

st.title('Credit Data Analysis')

# Create and display the plots
st.subheader('Checking Account Status Distribution')
fig, ax = plt.subplots()
df['checking_status'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Credit Duration Distribution')
fig, ax = plt.subplots()
df['duration'].plot(kind='hist', bins=20)
st.pyplot(fig)

st.subheader('Credit History Distribution')
fig, ax = plt.subplots()
df['credit_history'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Purpose of Credit Distribution')
fig, ax = plt.subplots()
df['purpose'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Credit Amount Distribution')
fig, ax = plt.subplots()
df['credit_amount'].plot(kind='hist', bins=20)
st.pyplot(fig)

st.subheader('Savings Status Distribution')
fig, ax = plt.subplots()
df['savings_status'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Employment Duration Distribution')
fig, ax = plt.subplots()
df['employment'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Installment Commitment Distribution')
fig, ax = plt.subplots()
df['installment_commitment'].plot(kind='hist', bins=10)
st.pyplot(fig)

st.subheader('Personal Status Distribution')
fig, ax = plt.subplots()
df['personal_status'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Other Parties Distribution')
fig, ax = plt.subplots()
df['other_parties'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Residence Since Distribution')
fig, ax = plt.subplots()
df['residence_since'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Property Magnitude Distribution')
fig, ax = plt.subplots()
df['property_magnitude'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Age Distribution')
fig, ax = plt.subplots()
df['age'].plot(kind='hist', bins=20)
st.pyplot(fig)

st.subheader('Other Payment Plans Distribution')
fig, ax = plt.subplots()
df['other_payment_plans'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Housing Distribution')
fig, ax = plt.subplots()
df['housing'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Existing Credits Distribution')
fig, ax = plt.subplots()
df['existing_credits'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Job Distribution')
fig, ax = plt.subplots()
df['job'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Number of Dependents Distribution')
fig, ax = plt.subplots()
df['num_dependents'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Own Telephone Distribution')
fig, ax = plt.subplots()
df['own_telephone'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Foreign Worker Distribution')
fig, ax = plt.subplots()
df['foreign_worker'].value_counts().plot(kind='bar')
st.pyplot(fig)

