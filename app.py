import pandas as pd
import streamlit as st

# Load the data
data = pd.read_csv('New_clean_data.csv')
st.set_page_config(layout='wide', page_title='App Store Analysis')


# Set up the main title and image
st.title('App Store Analysis')
st.image('playstore_blk.png')  # Make sure you have an appropriate image file in your working directory
st.write('## This is how the Data looks like !!')
st.write(data.head(5))

# Sidebar for choosing the analysis
st.sidebar.header('Choose your analysis')

analysis_type = st.sidebar.selectbox('Analysis Type',
                                     ['Overall Analysis', 'Category-wise Analysis', 'Free and Paid Analysis',
                                      'Developer Analysis'])

if analysis_type != 'Select an option':
    if st.sidebar.button('Show Analysis'):
        if analysis_type == 'Overall Analysis':
            st.header('Overall Analysis')

            #1. Top 5 Apps by Installations
            st.subheader('Top 5 Apps with Highest Installations')
            top_5_installs = data[['App Name', 'Maximum Installs']].sort_values(by='Maximum Installs',
                                                                                ascending=False).head()
            st.table(top_5_installs)

            #2. Top 5 Apps by Ratings
            st.subheader('Top 5 Apps with Highest Ratings')
            top_5_rating_ = data[data['Rating'] == 5][['App Name', 'Rating', 'Rating Count']].sort_values(
                by='Rating Count', ascending=False).head()
            st.table(top_5_rating_)

            #3 AD Supported Percentage
            st.subheader('Percentage of Apps with Ad Support')
            ads = data['Ad Supported'].value_counts(normalize=True) * 100
            st.table(ads)

            #4. Significance of Ads in getting Editor's Choice Badge
            st.subheader('Significance of Ads in getting Editors Choice Badge')
            significance = pd.crosstab(index=data['Ad Supported'], columns=data['Editors Choice'])
            st.table(significance)

            #5. Category wise App Distribution
            st.subheader('Category-wise Percentage Distribution of Apps')
            distribution = data['Category'].value_counts(normalize=True) * 100
            st.table(distribution)



        elif analysis_type == 'Category-wise Analysis':
            st.header('Category-wise Analysis')

            category = st.sidebar.selectbox('Select Category', data['Category'].unique())
            category_data = data[data['Category'] == category]

            #1. Top 5 Apps with Maximum Installations
            st.subheader(f'Top 5 Apps in {category} with Highest Maximum Installs')
            top_5_category_installs = category_data[['App Name', 'Maximum Installs']].sort_values(by='Maximum Installs',
                                                                                                  ascending=False).head()
            st.table(top_5_category_installs)

            #2. Top 5 Apps with Highest Ratings
            st.subheader(f'Top 5 Apps in {category} with Highest Rating')
            top_5_category_ratings = category_data[category_data['Rating'] == 5][
                ['App Name', 'Rating', 'Rating Count']].sort_values(by='Rating Count', ascending=False).head()
            st.table(top_5_category_ratings)

            #3. Average Rating
            st.subheader(f'Average Rating in {category}')
            avg_rating = category_data['Rating'].mean()
            st.write(f'The average rating for apps in {category} is {avg_rating:.2f}')



        elif analysis_type == 'Free and Paid Analysis':
            st.header('Free and Paid Apps Analysis')

            free_data = data[data['Free'] == True]
            paid_data = data[data['Free'] == False]

            #1. Distribution of Free and Paid Apps
            st.write('### Distribution of Free and Paid Apps')
            dist = data['Free'].value_counts(normalize=True) * 100
            st.table(dist)

            #2. Average Rating
            st.write('### Average Rating')
            avg_free_rating = free_data['Rating'].mean()
            avg_paid_rating = paid_data['Rating'].mean()
            st.write(f'Average Rating for Free Apps: {avg_free_rating:.2f}')
            st.write(f'Average Rating for Paid Apps: {avg_paid_rating:.2f}')

            #3. Average Installs
            st.write('### Average Installs')
            avg_free_installs = free_data['Maximum Installs'].mean()
            avg_paid_installs = paid_data['Maximum Installs'].mean()
            st.write(f'Average Installs for Free Apps: {avg_free_installs:.2f}')
            st.write(f'Average Installs for Paid Apps: {avg_paid_installs:.2f}')

            #4. Ad Support in Free and Paid Apps:
            st.write('### Ads in Free vs Paid Apps')
            ad_sup = pd.crosstab(index=data['Free'], columns=data['Ad Supported'])
            st.table(ad_sup)

            #5. Distribution of Editor's Choice in Free vs Paid Apps

            st.write('### Distribution of Editors Choice in Free vs Paid Apps')
            Editor_choice = pd.crosstab(index=data['Free'], columns=data['Editors Choice'])
            st.table(Editor_choice)

        elif analysis_type == 'Developer Analysis':
            st.header('Developer Analysis')

            # 1. Top 5 Developers with Maximum Number of Apps
            st.subheader('Top 5 Developers by Number of Apps')
            top_5_developers = data['Developer Id'].value_counts().head(5)
            st.table(top_5_developers)

            #2. Top 5 Developers by Average Rating
            st.subheader('Top 5 Developers by Average Rating')
            top_5_developers_ratings = data.groupby('Developer Id')[['Rating', 'Rating Count']].mean().sort_values(
                by='Rating Count', ascending=False).head().sort_values(by='Rating', ascending=False)
            st.table(top_5_developers_ratings)

            #3. Top 5 Developers by Maximum Installations
            st.subheader('Top 5 Developers by Maximum Average Installations')
            top_5_developers_Installs = data.groupby('Developer Id')['Maximum Installs'].mean().sort_values(
                ascending=False).head()
            st.table(top_5_developers_Installs)

            #4. Top 5 Developers with Highest Editors Choice Badges

            st.subheader('Top 5 Developers by Number of Editors Choice Badges')
            top_5_developers_Editors_Choice = data[data['Editors Choice'] == True].groupby('Developer Id')[
                'Editors Choice'].count().sort_values(ascending=False).head()
            st.table(top_5_developers_Editors_Choice)
