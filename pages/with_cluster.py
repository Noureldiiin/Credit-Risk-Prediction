import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.subplots as sp
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

df = pd.read_csv('credit_data.csv')

# Set Streamlit page config
st.set_page_config(page_title="With Clusters", page_icon="📈")

# Define the Streamlit app
st.title("With Clusters")

st.title("Cluster Statistics Summary")

# Create and display the plots for Checking Account Status Distribution
fig = sp.make_subplots(rows=1, cols=3, subplot_titles=("Cluster 0", "Cluster 1", "Cluster 2"))

for cluster in df['Cluster'].unique():
    subset = df[df['Cluster'] == cluster]
    data = subset['checking_status'].value_counts().reset_index()
    fig.add_trace(go.Bar(x=data['index'], y=data['checking_status'], name=f'Cluster {cluster}'), row=1, col=cluster)

fig.update_layout(title_text='Checking Account Status Distribution by Cluster')
fig.update_xaxes(title_text='Checking Status')
fig.update_yaxes(title_text='Count')

# Sample data for Cluster 0, 1, and 2
cluster0 = df[df['Cluster'] == 0].sample(n=100, replace=True)
cluster1 = df[df['Cluster'] == 1].sample(n=100, replace=True)
cluster2 = df[df['Cluster'] == 2].sample(n=100, replace=True)
merged_df = pd.concat([cluster0, cluster1, cluster2])
merged_df.reset_index(drop=True, inplace=True)

display_string = """
Cluster 0: This cluster has 4 categories of 'checking_status,' namely, '0<=X<200,' '<0,' '>=200,' and 'no checking.' The counts for each category within this cluster are 28, 30, 10, and 32, respectively.

Cluster 1: Within Cluster 1, you also have the same 4 categories of 'checking_status,' with counts of 44, 23, 1, and 32.

Cluster 2: Cluster 2 follows a similar pattern with the same 4 'checking_status' categories and counts of 18, 17, 7, and 58.
"""

# Streamlit app for Checking Account Status
st.write(display_string)
st.plotly_chart(fig)

# Display Employment Duration Distribution
fig = sp.make_subplots(rows=1, cols=3, subplot_titles=("Cluster 0", "Cluster 1", "Cluster 2"))

for cluster in merged_df['Cluster'].unique():
    subset = merged_df[merged_df['Cluster'] == cluster]
    data = subset['employment'].value_counts().reset_index()
    fig.add_trace(go.Bar(x=data['index'], y=data['employment'], name=f'Cluster {cluster}'), row=1, col=cluster)

fig.update_layout(title_text='Employment Duration Distribution by Cluster')
fig.update_xaxes(title_text='Employment Duration')
fig.update_yaxes(title_text='Count')

# Display the explanation for Employment Duration
st.write("""
Cluster 0: This cluster has five 'employment' status categories: '1<=X<4,' '4<=X<7,' '<1,' '>=7,' and 'unemployed.' The counts for each category within this cluster are 33, 14, 26, 22, and 5, respectively.

Cluster 1: Cluster 1 also contains the same five 'employment' status categories, with counts of 29, 25, 13, 19, and 14.

Cluster 2: Cluster 2 follows a similar pattern with the same five 'employment' status categories and counts of 29, 15, 10, 38, and 8.
""")
st.plotly_chart(fig)

# Credit Duration Distribution
fig = sp.make_subplots(rows=1, cols=3, subplot_titles=("Cluster 0", "Cluster 1", "Cluster 2"))

for cluster in merged_df['Cluster'].unique():
    subset = merged_df[merged_df['Cluster'] == cluster]
    fig.add_trace(go.Histogram(x=subset['duration'], nbinsx=20, name=f'Cluster {cluster}'), row=1, col=cluster)

fig.update_layout(title_text='Credit Duration Distribution by Cluster')
fig.update_xaxes(title_text='Credit Duration')
fig.update_yaxes(title_text='Count')

st.plotly_chart(fig)

st.write("""
**Cluster 0:**
The average value in this cluster is approximately 20.92.
The data points have a spread of around 10.05.
The smallest value in this cluster is 4.0.
About 25% of the data falls below 12.0.
The middle value of the data is 18.0.
About 75% of the data falls below 24.0.
The largest value in this cluster is 48.0.

**Cluster 1:**
The average value in this cluster is approximately 36.15.
The data points have a spread of around 13.38.
The smallest value in this cluster is 6.0.
About 25% of the data falls below 24.0.
The middle value of the data is 36.0.
About 75% of the data falls below 48.0.
The largest value in this cluster is 60.0.

**Cluster 2:**
The average value in this cluster is approximately 15.14.
The data points have a spread of around 6.96.
The smallest value in this cluster is 4.0.
About 25% of the data falls below 11.0.
The middle value of the data is 12.0.
About 75% of the data falls below 21.0.
The largest value in this cluster is 36.0.
""")

# Credit History Distribution
fig = sp.make_subplots(rows=1, cols=3, subplot_titles=("Cluster 0", "Cluster 1", "Cluster 2"))

for cluster in merged_df['Cluster'].unique():
    subset = merged_df[merged_df['Cluster'] == cluster]
    data = subset['credit_history'].value_counts().reset_index()
    fig.add_trace(go.Bar(x=data['index'], y=data['credit_history'], name=f'Cluster {cluster}'), row=1, col=cluster)

fig.update_layout(title_text='Credit History Distribution by Cluster')
fig.update_xaxes(title_text='Credit History')
fig.update_yaxes(title_text='Count')

st.plotly_chart(fig)

st.write("""
In this analysis, we have explored the distribution of 'credit_history' within three distinct clusters. Let's break down what each cluster's 'credit_history' distribution means:

**Cluster 0**:
- **'all paid'**: In Cluster 0, there are 8 cases with a credit history of 'all paid.' This indicates that there are 8 instances where applicants have a history of repaying their credit completely.
- **'critical/other existing credit'**: Cluster 0 has 5 cases falling into this category. It suggests that 5 applicants have a credit history described as 'critical/other existing credit.'
- **'delayed previously'**: There are 7 cases where applicants in Cluster 0 have a history of 'delayed previously,' suggesting a history of late payments or delays.
- **'existing paid'**: The majority of applicants in Cluster 0 (76 cases) have an 'existing paid' credit history, indicating a record of successfully repaid credit.
- **'no credits/all paid'**: There are 4 instances where applicants in Cluster 0 either have no previous credit history or have a history of 'all paid.'

**Cluster 1**:
- **'all paid'**: Cluster 1 contains 12 cases with a credit history of 'all paid,' indicating successful credit repayment.
- **'critical/other existing credit'**: This cluster includes 24 applicants with a history categorized as 'critical/other existing credit.'
- **'delayed previously'**: In Cluster 1, 17 cases have a history of 'delayed previously,' suggesting past late payments.
- **'existing paid'**: The majority of applicants in Cluster 1 (33 cases) have an 'existing paid' credit history, indicating successful repayment.
- **'no credits/all paid'**: There are 14 instances in Cluster 1 where applicants either have no prior credit history or have a history of 'all paid.'

**Cluster 2**:
- **'all paid'**: Cluster 2 has only 1 case with a 'all paid' credit history.
- **'critical/other existing credit'**: The majority of applicants in Cluster 2 (71 cases) have a history categorized as 'critical/other existing credit,' indicating a substantial presence of this credit history type.
- **'delayed previously'**: There are 9 cases in Cluster 2 with a history of 'delayed previously.'
- **'existing paid'**: 16 cases in Cluster 2 have an 'existing paid' credit history, suggesting successful credit repayment.
- **'no credits/all paid'**: There are 3 instances in Cluster 2 where applicants either have no prior credit history or have a history of 'all paid.'
""")

# Purpose Distribution by Cluster
fig = px.bar(merged_df, x='Cluster', color='purpose', barmode='group',
             title='Purpose Distribution by Cluster')
fig.update_layout(xaxis_title="Cluster", yaxis_title="Count")
st.plotly_chart(fig)

# Purpose of Credit by Cluster
st.subheader("Purpose of Credit by Cluster")
st.write("""
In this analysis, we have explored the distribution of credit purposes within three distinct clusters. 
The following summary provides insight into the distribution of 'purpose' categories for each cluster:
""")

# Credit Amount Distribution by Cluster
fig = px.histogram(merged_df, x='credit_amount', color='Cluster', nbins=20,
                   title='Credit Amount Distribution by Cluster')
fig.update_layout(xaxis_title="Credit Amount", yaxis_title="Count")
st.plotly_chart(fig)

# Conclusion: Cluster Statistics Summary for Credit Amount
st.subheader("Conclusion: Cluster Statistics Summary")
st.write("""
In our analysis of three clusters, we've examined key characteristics related to credit amount:

**Cluster 0**:
- Minimum: The lowest value within this cluster is 426.0.
- 25th Percentile: 25% of the data falls below 1,489.0.
- Median (50th Percentile): The middle value of the data is 2,321.0.
- 75th Percentile: 75% of the data falls below 3,238.5.
- Maximum: The highest value in this cluster is 6,350.0.

**Cluster 1**:
- Minimum: The lowest value within this cluster is 3,535.0.
- 25th Percentile: 25% of the data falls below 5,907.25.
- Median (50th Percentile): The middle value of the data is 7,474.0.
- 75th Percentile: 75% of the data falls below 10,240.75.
- Maximum: The highest value in this cluster is 18,424.0.

**Cluster 2**:
- Minimum: The lowest value within this cluster is 250.0.
- 25th Percentile: 25% of the data falls below 1,261.75.
- Median (50th Percentile): The middle value of the data is 1,568.5.
- 75th Percentile: 75% of the data falls below 2,336.5.
- Maximum: The highest value in this cluster is 4,591.0.
""")

# ECDF of Credit Amount by Cluster
st.subheader('ECDF of Credit Amount by Cluster')
fig = px.ecdf(merged_df, x='credit_amount', color='Cluster',
              title='ECDF of Credit Amount by Cluster')
fig.update_layout(xaxis_title="Credit Amount", yaxis_title="ECDF")
st.plotly_chart(fig)

# Conclusion: Cluster Statistics Summary for ECDF of Credit Amount
st.subheader("Conclusion: Cluster Statistics Summary")
st.write("""
In our analysis of three clusters, we've explored key characteristics using the ECDF of credit amount:

**Cluster 0**:
- Minimum: The lowest value within this cluster is 1.
- 25th Percentile: 25% of the data falls below 2.
- Median (50th Percentile): The middle value of the data is 4.
- 75th Percentile: 75% of the data falls below 4.
- Maximum: The highest value in this cluster is 4.

**Cluster 1**:
- Minimum: The lowest value within this cluster is 1.
- 25th Percentile: 25% of the data falls below 2.
- Median (50th Percentile): The middle value of the data is 2.
- 75th Percentile: 75% of the data falls below 4.
- Maximum: The highest value in this cluster is 4.

**Cluster 2**:
- Minimum: The lowest value within this cluster is 1.
- 25th Percentile: 25% of the data falls below 2.
- Median (50th Percentile): The middle value of the data is 3.
- 75th Percentile: 75% of the data falls below 4.
- Maximum: The highest value in this cluster is 4.
""")

# Installment Commitment Distribution by Cluster
fig = px.bar(merged_df, x='Cluster', color='installment_commitment', barmode='group',
             title='Installment Commitment Distribution by Cluster')
fig.update_layout(xaxis_title="Cluster", yaxis_title="Count")
st.plotly_chart(fig)

# Personal Status Distribution by Cluster
fig = px.bar(merged_df, x='Cluster', color='personal_status', barmode='group',
             title='Personal Status Distribution by Cluster')
fig.update_layout(xaxis_title="Cluster", yaxis_title="Count")
st.plotly_chart(fig)

# Personal Status by Cluster
st.subheader("Personal Status by Cluster")
st.write("""
In our analysis, we've examined the distribution of 'personal_status' within three distinct clusters. Here's a summary of the 'personal_status' categories for each cluster:
""")

# Residence Since Distribution by Cluster
fig = px.bar(merged_df, x='Cluster', color='residence_since', barmode='group',
             title='Residence Since Distribution by Cluster')
fig.update_layout(xaxis_title="Cluster", yaxis_title="Count")
st.plotly_chart(fig)

# Conclusion: Residence Duration by Cluster
st.subheader("Conclusion: Residence Duration by Cluster")
st.write("""
In our analysis, we've examined the distribution of 'residence_since' within three distinct clusters. Here's a summary of the 'residence_since' categories for each cluster:
""")

# Property Magnitude Distribution by Cluster
fig = px.bar(merged_df, x='Cluster', color='property_magnitude', barmode='group',
             title='Property Magnitude Distribution by Cluster')
fig.update_layout(xaxis_title="Cluster", yaxis_title="Count")
st.plotly_chart(fig)

# Conclusion: Property Magnitude by Cluster
st.subheader("Conclusion: Property Magnitude by Cluster")
st.write("""
In our analysis, we've examined the distribution of 'property_magnitude' within three distinct clusters. Here's a summary of the 'property_magnitude' categories for each cluster:
""")

# Age Distribution by Cluster
fig = px.histogram(merged_df, x='age', color='Cluster', nbins=20,
                   title='Age Distribution by Cluster')
fig.update_layout(xaxis_title="Age", yaxis_title="Count")
st.plotly_chart(fig)

# Conclusion: Cluster Statistics Summary for Age
st.subheader("Conclusion: Cluster Statistics Summary")
st.write("""
**Cluster 0**:
- Minimum: The lowest value within this cluster is 20.0.
- 25th Percentile: 25% of the data falls below 26.0.
- Median (50th Percentile): The middle value of the data is 35.0.
- 75th Percentile: 75% of the data falls below 46.0.
- Maximum: The highest value in this cluster is 74.0.

**Cluster 1**:
- Minimum: The lowest value within this cluster is 23.0.
- 25th Percentile: 25% of the data falls below 26.0.
- Median (50th Percentile): The middle value of the data is 30.0.
- 75th Percentile: 75% of the data falls below 35.0.
- Maximum: The highest value in this cluster is 45.0.

**Cluster 2**:
- Minimum: The lowest value within this cluster is 19.0.
- 25th Percentile: 25% of the data falls below 29.0.
- Median (50th Percentile): The middle value of the data is 36.0.
- 75th Percentile: 75% of the data falls below 42.0.
- Maximum: The highest value in this cluster is 75.0.
""")

# Number of Existing Credits at this Bank Distribution by Cluster
fig = px.bar(merged_df, x='Cluster', color='num_existing_credits', barmode='group',
             title='Number of Existing Credits Distribution by Cluster')
fig.update_layout(xaxis_title="Cluster", yaxis_title="Count")
st.plotly_chart(fig)

# Conclusion: Number of Existing Credits at this Bank by Cluster
st.subheader("Conclusion: Number of Existing Credits at this Bank by Cluster")
st.write("""
In our analysis, we've examined the distribution of 'num_existing_credits' within three distinct clusters. Here's a summary of the 'num_existing_credits' categories for each cluster:
""")

# Job Distribution by Cluster
fig = px.bar(merged_df, x='Cluster', color='job', barmode='group',
             title='Job Distribution by Cluster')
fig.update_layout(xaxis_title="Cluster", yaxis_title="Count")
st.plotly_chart(fig)

# Conclusion: Job by Cluster
st.subheader("Conclusion: Job by Cluster")
st.write("""
In our analysis, we've examined the distribution of 'job' within three distinct clusters. Here's a summary of the 'job' categories for each cluster:
""")

# Number of Dependents Distribution by Cluster
fig = px.bar(merged_df, x='Cluster', color='num_dependents', barmode='group',
             title='Number of Dependents Distribution by Cluster')
fig.update_layout(xaxis_title="Cluster", yaxis_title="Count")
st.plotly_chart(fig)

# Conclusion: Number of Dependents by Cluster
st.subheader("Conclusion: Number of Dependents by Cluster")
st.write("""
In our analysis, we've examined the distribution of 'num_dependents' within three distinct clusters. Here's a summary of the 'num_dependents' categories for each cluster:
""")

# Create a table of the original features and their statistics by cluster
st.subheader("Original Features Summary by Cluster")
st.write(merged_df.groupby('Cluster').agg({
    'duration': ['mean', 'std'],
    'credit_amount': ['mean', 'std'],
    'installment_commitment': ['mean', 'std'],
    'residence_since': ['mean', 'std'],
    'age': ['mean', 'std'],
    'num_existing_credits': ['mean', 'std'],
    'num_dependents': ['mean', 'std']
}))

# Create a correlation matrix heatmap for the original features
correlation_matrix = merged_df.corr()
fig = go.Figure(data=go.Heatmap(
    z=correlation_matrix.values,
    x=correlation_matrix.index,
    y=correlation_matrix.columns,
    colorscale='Viridis'))
fig.update_layout(title="Correlation Matrix Heatmap")
st.plotly_chart(fig)
