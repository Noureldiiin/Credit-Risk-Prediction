import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

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

st.title("Cluster Statistics Summary")

# Create and display the plots
st.subheader('Checking Account Status Distribution by Cluster')
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for cluster in df['Cluster'].unique():
    ax = axes[cluster]
    subset = df[df['Cluster'] == cluster]
    subset['checking_status'].value_counts().plot(kind='bar', ax=ax)
    ax.set_title(f'Cluster {cluster}')
st.pyplot(fig)

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

# Streamlit app
st.write(display_string)

# Display Employment Distribution
st.subheader('Employment Duration Distribution by Cluster')
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for cluster in merged_df['Cluster'].unique():
    ax = axes[cluster]
    subset = merged_df[merged_df['Cluster'] == cluster]
    subset['employment'].value_counts().plot(kind='bar', ax=ax)
    ax.set_title(f'Cluster {cluster}')
st.pyplot(fig)

st.subheader("Employment Details")

# Display the explanation
st.write("""
Cluster 0: This cluster has five 'employment' status categories: '1<=X<4,' '4<=X<7,' '<1,' '>=7,' and 'unemployed.' The counts for each category within this cluster are 33, 14, 26, 22, and 5, respectively.

Cluster 1: Cluster 1 also contains the same five 'employment' status categories, with counts of 29, 25, 13, 19, and 14.

Cluster 2: Cluster 2 follows a similar pattern with the same five 'employment' status categories and counts of 29, 15, 10, 38, and 8.
""")


# Display Duration Distribution
st.subheader('Credit Duration Distribution by Cluster')
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for cluster in merged_df['Cluster'].unique():
    ax = axes[cluster]
    subset = merged_df[merged_df['Cluster'] == cluster]
    subset['duration'].plot(kind='hist', bins=20, ax=ax)
    ax.set_title(f'Cluster {cluster}')
st.pyplot(fig)




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
st.subheader('Credit History Distribution by Cluster')
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for cluster in merged_df['Cluster'].unique():
    ax = axes[cluster]
    subset = merged_df[merged_df['Cluster'] == cluster]
    subset['credit_history'].value_counts().plot(kind='bar', ax=ax)
    ax.set_title(f'Cluster {cluster}')
st.pyplot(fig)

st.subheader("Credit History by Cluster - Detailed Explanation")

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


# Purpose Distribution
st.subheader('Purpose Distribution by Cluster')
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for cluster in merged_df['Cluster'].unique():
    ax = axes[cluster]
    subset = merged_df[merged_df['Cluster'] == cluster]
    subset['purpose'].value_counts().plot(kind='bar', ax=ax)
    ax.set_title(f'Cluster {cluster}')
st.pyplot(fig)

st.subheader("Purpose of Credit by Cluster")

st.write("""
In this analysis, we have explored the distribution of credit purposes within three distinct clusters. The following summary provides insight into the distribution of 'purpose' categories for each cluster:

**Cluster 0**:
- **Business**: 2 cases in Cluster 0 indicate that applicants in this group are seeking credit for business-related purposes.
- **Domestic Appliance**: There are 2 instances where applicants are seeking credit for domestic appliance-related purchases.
- **Education**: 6 cases in Cluster 0 reflect credit requests for educational expenses.
- **Furniture/Equipment**: The majority of applicants in Cluster 0 (32 cases) are looking for credit to finance furniture or equipment purchases.
- **New Car**: 17 cases suggest that applicants in this cluster aim to finance a new car.
- **Radio/TV**: Radio or TV purchases are represented by 34 cases.
- **Repairs**: There is 1 case where applicants are seeking credit for repairs.
- **Used Car**: 6 cases indicate a desire to purchase a used car.

**Cluster 1**:
- **Business**: 19 cases in Cluster 1 suggest that applicants in this group are seeking credit for business-related purposes.
- **Domestic Appliance**: There is 1 instance where applicants are seeking credit for domestic appliance-related purchases.
- **Education**: 7 cases in Cluster 1 reflect credit requests for educational expenses.
- **Furniture/Equipment**: 10 cases in this cluster are related to financing furniture or equipment purchases.
- **New Car**: 24 cases indicate a desire to finance a new car.
- **Other**: 3 cases represent other unspecified credit purposes.
- **Radio/TV**: 14 cases reflect credit requests for radio or TV purchases.
- **Used Car**: 22 cases indicate a desire to purchase a used car.

**Cluster 2**:
- **Business**: Cluster 2 has 9 cases representing applicants seeking credit for business-related purposes.
- **Domestic Appliance**: There is 1 instance where applicants are seeking credit for domestic appliance-related purchases.
- **Education**: 5 cases in Cluster 2 reflect credit requests for educational expenses.
- **Furniture/Equipment**: 17 cases are related to financing furniture or equipment purchases.
- **New Car**: 30 cases suggest a desire to finance a new car.
- **Radio/TV**: 30 cases indicate credit requests for radio or TV purchases.
- **Repairs**: 4 cases represent credit requests for repairs.
- **Retraining**: There is 1 case indicating credit requests for retraining.
- **Used Car**: 3 cases reflect a desire to purchase a used car.

""")


# Credit Amount Distribution
st.subheader('Credit Amount Distribution by Cluster')
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for cluster in merged_df['Cluster'].unique():
    ax = axes[cluster]
    subset = merged_df[merged_df['Cluster'] == cluster]
    subset['credit_amount'].plot(kind='hist', bins=20, ax=ax)
    ax.set_title(f'Cluster {cluster}')
st.pyplot(fig)

st.subheader("Conclusion: Cluster Statistics Summary")

st.write("""
In our analysis of three clusters, we've examined important characteristics for each cluster:

**Cluster 0**:
- **Minimum**: The lowest value within this cluster is 426.0.
- **25th Percentile**: 25% of the data falls below 1,489.0.
- **Median (50th Percentile)**: The middle value of the data is 2,321.0.
- **75th Percentile**: 75% of the data falls below 3,238.5.
- **Maximum**: The highest value in this cluster is 6,350.0.

**Cluster 1**:
- **Minimum**: The lowest value within this cluster is 3,535.0.
- **25th Percentile**: 25% of the data falls below 5,907.25.
- **Median (50th Percentile)**: The middle value of the data is 7,474.0.
- **75th Percentile**: 75% of the data falls below 10,240.75.
- **Maximum**: The highest value in this cluster is 18,424.0.

**Cluster 2**:
- **Minimum**: The lowest value within this cluster is 250.0.
- **25th Percentile**: 25% of the data falls below 1,261.75.
- **Median (50th Percentile)**: The middle value of the data is 1,568.5.
- **75th Percentile**: 75% of the data falls below 2,336.5.
- **Maximum**: The highest value in this cluster is 4,591.0.

""")


# ECDF of Credit Amount by Cluster
st.subheader('ECDF of Credit Amount by Cluster')
fig, ax = plt.subplots(figsize=(12, 6))
for cluster in merged_df['Cluster'].unique():
    subset = merged_df[merged_df['Cluster'] == cluster]
    sns.ecdfplot(data=subset, x='credit_amount', label=f'Cluster {cluster}', ax=ax)
ax.legend(title='Cluster')
st.pyplot(fig)

st.subheader("Conclusion: Cluster Statistics Summary")

st.write("""
In our analysis of three clusters, we've explored key characteristics for each cluster:

**Cluster 0**:
- **Minimum**: The lowest value within this cluster is 1.
- **25th Percentile**: 25% of the data falls below 2.
- **Median (50th Percentile)**: The middle value of the data is 4.
- **75th Percentile**: 75% of the data falls below 4.
- **Maximum**: The highest value in this cluster is 4.

**Cluster 1**:
- **Minimum**: The lowest value within this cluster is 1.
- **25th Percentile**: 25% of the data falls below 2.
- **Median (50th Percentile)**: The middle value of the data is 2.
- **75th Percentile**: 75% of the data falls below 4.
- **Maximum**: The highest value in this cluster is 4.

**Cluster 2**:
- **Minimum**: The lowest value within this cluster is 1.
- **25th Percentile**: 25% of the data falls below 2.
- **Median (50th Percentile)**: The middle value of the data is 3.
- **75th Percentile**: 75% of the data falls below 4.
- **Maximum**: The highest value in this cluster is 4.

""")


# Installment Commitment Distribution
st.subheader('Installment Commitment Distribution by Cluster')
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for cluster in merged_df['Cluster'].unique():
    ax = axes[cluster]
    subset = merged_df[merged_df['Cluster'] == cluster]
    subset['installment_commitment'].value_counts().plot(kind='bar', ax=ax)
    ax.set_title(f'Cluster {cluster}')
st.pyplot(fig)

# Personal Status Distribution
st.subheader('Personal Status Distribution by Cluster')
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for cluster in merged_df['Cluster'].unique():
    ax = axes[cluster]
    subset = merged_df[merged_df['Cluster'] == cluster]
    subset['personal_status'].value_counts().plot(kind='bar', ax=ax)
    ax.set_title(f'Cluster {cluster}')
st.pyplot(fig)

st.subheader("Personal Status by Cluster")

st.write("""
In our analysis, we've examined the distribution of 'personal_status' within three distinct clusters. Here's a summary of the 'personal_status' categories for each cluster:

**Cluster 0**:
- **Female Div/Dep/Mar**: There are 36 cases in this cluster with the 'female div/dep/mar' personal status.
- **Male Div/Sep**: 5 cases in this cluster are associated with 'male div/sep' personal status.
- **Male Mar/Wid**: There are 7 instances in this cluster with 'male mar/wid' personal status.
- **Male Single**: The majority of cases in Cluster 0 (52 cases) are related to 'male single' personal status.

**Cluster 1**:
- **Female Div/Dep/Mar**: Cluster 1 includes 28 cases with 'female div/dep/mar' personal status.
- **Male Div/Sep**: There are 2 cases in this cluster with 'male div/sep' personal status.
- **Male Mar/Wid**: Cluster 1 has 6 instances with 'male mar/wid' personal status.
- **Male Single**: The majority of cases in Cluster 1 (64 cases) are related to 'male single' personal status.

**Cluster 2**:
- **Female Div/Dep/Mar**: There are 35 cases in Cluster 2 with the 'female div/dep/mar' personal status.
- **Male Div/Sep**: Cluster 2 includes 6 cases with 'male div/sep' personal status.
- **Male Mar/Wid**: There are 5 instances in this cluster with 'male mar/wid' personal status.
- **Male Single**: The majority of cases in Cluster 2 (54 cases) are associated with 'male single' personal status.

""")

# Residence Since Distribution
st.subheader('Residence Since Distribution by Cluster')
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for cluster in merged_df['Cluster'].unique():
    ax = axes[cluster]
    subset = merged_df[merged_df['Cluster'] == cluster]
    subset['residence_since'].value_counts().plot(kind='bar', ax=ax)
    ax.set_title(f'Cluster {cluster}')
st.pyplot(fig)

st.subheader("Residence Duration by Cluster")

st.write("""
In our analysis, we've examined the distribution of 'residence_since' within three distinct clusters. Here's a summary of the 'residence_since' categories for each cluster:

**Cluster 0**:
- **1 Year**: There are 12 cases in this cluster with a residence duration of 1 year.
- **2 Years**: 34 cases in this cluster have a residence duration of 2 years.
- **3 Years**: There are 14 instances in this cluster with a residence duration of 3 years.
- **4 Years**: The majority of cases in Cluster 0 (40 cases) have a residence duration of 4 years.

**Cluster 1**:
- **1 Year**: Cluster 1 includes 8 cases with a residence duration of 1 year.
- **2 Years**: There are 29 cases in this cluster with a residence duration of 2 years.
- **3 Years**: Cluster 1 has 13 instances with a residence duration of 3 years.
- **4 Years**: The majority of cases in Cluster 1 (50 cases) have a residence duration of 4 years.

**Cluster 2**:
- **1 Year**: There are 9 cases in Cluster 2 with a residence duration of 1 year.
- **2 Years**: Cluster 2 includes 24 cases with a residence duration of 2 years.
- **3 Years**: There are 22 instances in this cluster with a residence duration of 3 years.
- **4 Years**: The majority of cases in Cluster 2 (45 cases) have a residence duration of 4 years.

""")


# Property Magnitude Distribution
st.subheader('Property Magnitude Distribution by Cluster')
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for cluster in merged_df['Cluster'].unique():
    ax = axes[cluster]
    subset = merged_df[merged_df['Cluster'] == cluster]
    subset['property_magnitude'].value_counts().plot(kind='bar', ax=ax)
    ax.set_title(f'Cluster {cluster}')
st.pyplot(fig)

st.subheader("Property Magnitude by Cluster")

st.write("""
In our analysis, we've examined the distribution of 'property_magnitude' within three distinct clusters. Here's a summary of the 'property_magnitude' categories for each cluster:

**Cluster 0**:
- **Car**: There are 47 cases in this cluster where applicants have 'car' as their property magnitude.
- **Life Insurance**: 17 cases in this cluster have 'life insurance' as their property magnitude.
- **No Known Property**: There are 9 instances in this cluster where applicants have 'no known property' as their property magnitude.
- **Real Estate**: The majority of cases in Cluster 0 (27 cases) have 'real estate' as their property magnitude.

**Cluster 1**:
- **Car**: Cluster 1 includes 35 cases where applicants have 'car' as their property magnitude.
- **Life Insurance**: There are 19 cases in this cluster with 'life insurance' as their property magnitude.
- **No Known Property**: Cluster 1 has 36 instances where applicants have 'no known property' as their property magnitude.
- **Real Estate**: There are 10 cases in Cluster 1 with 'real estate' as their property magnitude.

**Cluster 2**:
- **Car**: There are 31 cases in Cluster 2 where applicants have 'car' as their property magnitude.
- **Life Insurance**: Cluster 2 includes 22 cases with 'life insurance' as their property magnitude.
- **No Known Property**: There are 10 instances in this cluster where applicants have 'no known property' as their property magnitude.
- **Real Estate**: The majority of cases in Cluster 2 (37 cases) have 'real estate' as their property magnitude.

""")


# Age Distribution
st.subheader('Age Distribution by Cluster')
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for cluster in merged_df['Cluster'].unique():
    ax = axes[cluster]
    subset = merged_df[merged_df['Cluster'] == cluster]
    subset['age'].plot(kind='hist', bins=20, ax=ax)
    ax.set_title(f'Cluster {cluster}')
st.pyplot(fig)

st.subheader("Conclusion: Cluster Statistics Summary")

st.write("""
**Cluster 0**:
- **Minimum**: The lowest value within this cluster is 20.0.
- **25th Percentile**: 25% of the data falls below 25.0.
- **Median (50th Percentile)**: The middle value of the data is 29.0.
- **75th Percentile**: 75% of the data falls below 36.25.
- **Maximum**: The highest value in this cluster is 49.0.

**Cluster 1**:
- **Minimum**: The lowest value within this cluster is 20.0.
- **25th Percentile**: 25% of the data falls below 27.0.
- **Median (50th Percentile)**: The middle value of the data is 33.5.
- **75th Percentile**: 75% of the data falls below 42.0.
- **Maximum**: The highest value in this cluster is 70.0.

**Cluster 2**:
- **Minimum**: The lowest value within this cluster is 24.0.
- **25th Percentile**: 25% of the data falls below 34.0.
- **Median (50th Percentile)**: The middle value of the data is 41.0.
- **75th Percentile**: 75% of the data falls below 54.0.
- **Maximum**: The highest value in this cluster is 74.0.

""")


# Other Payment Plans Distribution
st.subheader('Other Payment Plans Distribution by Cluster')
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for cluster in merged_df['Cluster'].unique():
    ax = axes[cluster]
    subset = merged_df[merged_df['Cluster'] == cluster]
    subset['other_payment_plans'].value_counts().plot(kind='bar', ax=ax)
    ax.set_title(f'Cluster {cluster}')
st.pyplot(fig)

st.subheader("Other Payment Plans by Cluster")

st.write("""
In our analysis, we've examined the distribution of 'other_payment_plans' within three distinct clusters. Here's a summary of the 'other_payment_plans' categories for each cluster:

**Cluster 0**:
- **Bank**: There are 11 cases in this cluster with 'bank' as the chosen payment plan.
- **None**: The majority of cases in Cluster 0 (84 cases) have 'none' as their payment plan.
- **Stores**: There are 5 instances in this cluster with 'stores' as the payment plan.

**Cluster 1**:
- **Bank**: Cluster 1 includes 17 cases with 'bank' as the selected payment plan.
- **None**: The majority of cases in Cluster 1 (76 cases) have 'none' as their payment plan.
- **Stores**: There are 7 cases in this cluster with 'stores' as the payment plan.

**Cluster 2**:
- **Bank**: There are 12 cases in Cluster 2 with 'bank' as the chosen payment plan.
- **None**: The majority of cases in Cluster 2 (85 cases) have 'none' as their payment plan.
- **Stores**: There are 3 instances in this cluster with 'stores' as the payment plan.

""")


# Housing Distribution
st.subheader('Housing Distribution by Cluster')
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for cluster in merged_df['Cluster'].unique():
    ax = axes[cluster]
    subset = merged_df[merged_df['Cluster'] == cluster]
    subset['housing'].value_counts().plot(kind='bar', ax=ax)
    ax.set_title(f'Cluster {cluster}')
st.pyplot(fig)

st.subheader("Housing by Cluster")

st.write("""
In our analysis, we've examined the distribution of 'housing' categories within three distinct clusters. Here's a summary of the 'housing' categories for each cluster:

**Cluster 0**:
- **For Free**: There are 7 cases in this cluster where applicants have 'for free' housing.
- **Own**: The majority of cases in Cluster 0 (70 cases) have 'own' housing.
- **Rent**: There are 23 instances in this cluster with 'rent' housing.

**Cluster 1**:
- **For Free**: Cluster 1 includes 28 cases with 'for free' housing.
- **Own**: There are 55 cases in this cluster with 'own' housing.
- **Rent**: There are 17 cases in this cluster with 'rent' housing.

**Cluster 2**:
- **For Free**: There are 9 cases in Cluster 2 where applicants have 'for free' housing.
- **Own**: The majority of cases in Cluster 2 (83 cases) have 'own' housing.
- **Rent**: There are 8 instances in this cluster with 'rent' housing.

""")


# Existing Credits Distribution
st.subheader('Existing Credits Distribution by Cluster')
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for cluster in merged_df['Cluster'].unique():
    ax = axes[cluster]
    subset = merged_df[merged_df['Cluster'] == cluster]
    subset['existing_credits'].value_counts().plot(kind='bar', ax=ax)
    ax.set_title(f'Cluster {cluster}')
st.pyplot(fig)

st.subheader("Existing Credits by Cluster")

st.write("""
In our analysis, we've examined the distribution of 'existing_credits' within three distinct clusters. Here's a summary of the 'existing_credits' categories for each cluster:

**Cluster 0**:
- **1 Existing Credit**: There are 90 cases in this cluster with one existing credit.
- **2 Existing Credits**: 10 cases in this cluster have two existing credits.

**Cluster 1**:
- **1 Existing Credit**: Cluster 1 includes 50 cases with one existing credit.
- **2 Existing Credits**: There are 47 cases in this cluster with two existing credits.
- **3 Existing Credits**: 2 instances in this cluster have three existing credits.
- **4 Existing Credits**: There is 1 case in this cluster with four existing credits.

**Cluster 2**:
- **1 Existing Credit**: There are 28 cases in Cluster 2 with one existing credit.
- **2 Existing Credits**: 61 cases in this cluster have two existing credits.
- **3 Existing Credits**: 10 instances in this cluster have three existing credits.
- **4 Existing Credits**: There is 1 case in this cluster with four existing credits.

""")


# Job Distribution
st.subheader('Job Distribution by Cluster')
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for cluster in merged_df['Cluster'].unique():
    ax = axes[cluster]
    subset = merged_df[merged_df['Cluster'] == cluster]
    subset['job'].value_counts().plot(kind='bar', ax=ax)
    ax.set_title(f'Cluster {cluster}')
st.pyplot(fig)

st.subheader("Job Types by Cluster")

st.write("""
**Cluster 0**:  This cluster has the largest number of individuals with a "skilled" job,
            followed by "unskilled resident," "high qualif/self emp/mgmt," and "unemp/unskilled non-res" job categories.
            It appears that within this cluster, skilled jobs are the most prevalent.
            
**Cluster 1**:  In this cluster, "skilled" and "high qualif/self emp/mgmt" jobs have the highest representation,
            with "unskilled resident" and "unemp/unskilled non-res" jobs being less common.
            This suggests that skilled and self-employed or management roles dominate within this cluster.
            
**Cluster 2**:  Cluster 2 is characterized by a significant presence of "skilled" jobs, followed by "unskilled resident," "high qualif/self emp/mgmt," and "unemp/unskilled non-res" job categories.
            Skilled jobs are prominent within this cluster.
""")


# Number of Dependents Distribution
st.subheader('Number of Dependents Distribution by Cluster')
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for cluster in merged_df['Cluster'].unique():
    ax = axes[cluster]
    subset = merged_df[merged_df['Cluster'] == cluster]
    subset['num_dependents'].value_counts().plot(kind='bar', ax=ax)
    ax.set_title(f'Cluster {cluster}')
st.pyplot(fig)


st.write("""
**Cluster 0**:
This cluster has the largest number of individuals with a "skilled" job, followed by "unskilled resident," "high qualif/self emp/mgmt," and "unemp/unskilled non-res" job categories.
It appears that within this cluster, skilled jobs are the most prevalent.

**Cluster 1**:
In this cluster, "skilled" and "high qualif/self emp/mgmt" jobs have the highest representation, with "unskilled resident" and "unemp/unskilled non-res" jobs being less common.
This suggests that skilled and self-employed or management roles dominate within this cluster.

**Cluster 2**:
Cluster 2 is characterized by a significant presence of "skilled" jobs, followed by "unskilled resident," "high qualif/self emp/mgmt," and "unemp/unskilled non-res" job categories.
Skilled jobs are prominent within this cluster.
""")

# Own Telephone Distribution
st.subheader('Own Telephone Distribution by Cluster')
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for cluster in merged_df['Cluster'].unique():
    ax = axes[cluster]
    subset = merged_df[merged_df['Cluster'] == cluster]
    subset['own_telephone'].value_counts().plot(kind='bar', ax=ax)
    ax.set_title(f'Cluster {cluster}')
st.pyplot(fig)

st.subheader("Own Telephone Distribution by Cluster")

st.write("""
**Cluster 0**:
In this cluster, the majority of individuals have "none" for owning a telephone, followed by "yes." The cluster predominantly comprises individuals without telephones.

**Cluster 1**:
Cluster 1 exhibits a mix of telephone ownership, with "yes" and "none" being relatively balanced. Both categories are well-represented in this cluster.

**Cluster 2**:
Similar to Cluster 0, Cluster 2 also consists primarily of individuals with "none" for telephone ownership, but it has a notable presence of "yes" as well.
Individuals without telephones are more prevalent in this cluster.
""")


# Foreign Worker Distribution
st.subheader('Foreign Worker Distribution by Cluster')
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for cluster in merged_df['Cluster'].unique():
    ax = axes[cluster]
    subset = merged_df[merged_df['Cluster'] == cluster]
    subset['foreign_worker'].value_counts().plot(kind='bar', ax=ax)
    ax.set_title(f'Cluster {cluster}')
st.pyplot(fig)

st.subheader("Foreign Worker Distribution by Cluster")

st.write("""
**Cluster 0**:
In this cluster, the majority of individuals are "foreign workers" (yes), with a small number indicating "no." This cluster is primarily composed of foreign workers.

**Cluster 1**:
Cluster 1 is characterized by a dominant presence of "foreign workers" (yes), with very few individuals marked as "no." This cluster primarily consists of foreign workers.

**Cluster 2**:
Similar to Cluster 0, Cluster 2 is primarily composed of "foreign workers" (yes), although it has a slightly larger number of individuals marked as "no" compared to Cluster 0. Nevertheless, foreign workers are the majority in this cluster.
""")

st.title('Summary')
st.write("Cluster 0 encompasses individuals with predominantly 'skilled' jobs, 'no' telephone ownership, and a mix of 'foreign workers' status. They exhibit moderate duration and credit amounts, primarily seeking credit for 'real estate' or 'furniture/equipment' purposes. Housing is most commonly 'own,' with limited existing credits.")

st.write("Cluster 1 comprises individuals with varied 'skilled' and 'high qualif/self emp/mgmt' jobs. They have a balanced mix of 'yes' and 'no' telephone ownership, mostly being 'foreign workers.' This cluster features higher credit durations and amounts and is inclined towards 'new car' and 'radio/TV' credit purposes. Housing mainly falls under 'own,' and existing credits range from one to four.")

st.write("Cluster 2 showcases a majority of 'skilled' job holders, again with a mix of 'foreign workers.' They have relatively short credit durations and lower credit amounts, often seeking credit for 'car' and 'real estate' purposes. Housing is mainly 'own,' and existing credits range from one to three.")

