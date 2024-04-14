# import streamlit as st
# import gspread
# from google.oauth2 import service_account
# import pandas as pd
# import plotly.express as px
# import calendar

# # Set up Google Sheets credentials
# scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# creds = service_account.Credentials.from_service_account_file('./centered-oasis-416512-58461cae0d1d.json', scopes=scope)
# client = gspread.authorize(creds)

# # Open the Google Sheet and specific worksheets
# sheet_url = 'https://docs.google.com/spreadsheets/d/1XENlmMrDjW5GUhdFjVSheVPtEfHauyOPjtLa8rNH46g/edit#gid=871780544'
# workbook = client.open_by_url(sheet_url)
# sheet1 = workbook.worksheet('Exit Analysis - Reason for exit')  # Replace with your actual sheet name
# sheet2 = workbook.worksheet('Employee Connects')

# # Retrieve data from the first sheet
# data1 = sheet1.get_all_records()
# df1 = pd.DataFrame(data1)

# # Retrieve data from the second sheet
# data2 = sheet2.get_all_values()
# headers = data2[1]  # This should be the actual header row with 'Department', 'Red', 'Amber', 'Green'
# data_rows = data2[2:]  # This should start with the actual data rows
# df2 = pd.DataFrame(data_rows, columns=headers)

# # Clean up headers in df2 if they have leading/trailing spaces
# df2.columns = [col.strip() for col in df2.columns]

# # Plotly charts
# st.title('Company Department Data Analysis')

# st.header('Interactive Chart of Department Data')
# fig1 = px.bar(df1, x='Department', y=['Career Growth/ Better Opp.', 'Performance issues', 'Health reasons', 'Higher studies'],
#               title='Reasons for Department Change',
#               labels={'value': 'Number of Responses', 'variable': 'Categories'},
#               barmode='group')
# st.plotly_chart(fig1)

# # Open the 'Employee Connects' worksheet
# employee_connects_sheet = workbook.worksheet('Employee Connects')

# # Retrieve data from the 'Employee Connects' sheet, starting from the second row
# employee_connects_data = employee_connects_sheet.get_all_values()[1:]  # Skip the first row

# # The headers are assumed to be in the second row, now the first row of our list
# headers_employee_connects = employee_connects_data[0]
# data_rows_employee_connects = employee_connects_data[1:]  # The rest is data

# # Create the DataFrame
# df_employee_connects = pd.DataFrame(data_rows_employee_connects, columns=headers_employee_connects)

# # Convert the numeric columns to integers
# for col in ['Red', 'Amber', 'Green']:
#     df_employee_connects[col] = df_employee_connects[col].astype(int)

# # Create a Plotly bar chart for the 'Employee Connects' data
# st.header('Employee Connect Status by Department')
# fig_employee_connects = px.bar(df_employee_connects, x='Department', y=['Red', 'Amber', 'Green'],
#                                title='Employee Connects - RAG Status by Department',
#                                labels={'value': 'Number of Cases', 'variable': 'Status'},
#                                barmode='group')
# st.plotly_chart(fig_employee_connects)



# # Define the correct order of months
# month_order = {month: index for index, month in enumerate(calendar.month_abbr)}

# # Open the new tab/worksheet by name
# sheet3 = workbook.worksheet('HR Helpdesk')  # Replace with the actual name of your new tab

# # Retrieve data from the new sheet
# data3 = sheet3.get_all_values()[1:]  # Skip the first row
# headers3 = data3[0]  # This should be ['Queries / request received', 'Jan', 'Feb', 'Mar', ...]
# data_rows3 = data3[1:]  # The rest is data

# # Create the DataFrame
# df3 = pd.DataFrame(data_rows3, columns=headers3)

# # Melt the DataFrame to have one row per month per 'Queries / request received'
# df3_melted = df3.melt(id_vars=[headers3[0]], value_vars=headers3[1:],
#                       var_name='Month', value_name='Queries/Requests')

# # Convert the 'Queries/Requests' column to numeric, as they will be strings initially
# df3_melted['Queries/Requests'] = pd.to_numeric(df3_melted['Queries/Requests'])

# # Convert 'Month' to categorical and order it correctly
# df3_melted['Month'] = pd.Categorical(df3_melted['Month'], categories=month_order.keys(), ordered=True)

# # Sort by 'Month' to ensure the line chart follows the chronological order
# df3_melted = df3_melted.sort_values(by='Month')

# # Plotly chart for the new data
# st.header('Queries/Request Received Over Months')
# fig3 = px.line(df3_melted, x='Month', y='Queries/Requests',
#                title='Monthly Queries/Requests',
#                labels={'Month': 'Month', 'Queries/Requests': 'Number of Queries/Requests'})

# st.plotly_chart(fig3)


# # Open the 'Attrition data - Month & Department wise' worksheet
# attrition_data_sheet = workbook.worksheet('Attrititon data - Month & Department wise')

# # Retrieve data from the 'Attrition data - Month & Department wise' sheet
# attrition_data = attrition_data_sheet.get_all_records()

# # Convert the data to a Pandas DataFrame
# df_attrition = pd.DataFrame(attrition_data)

# # Melt the DataFrame to have one row per month per department for attrition data
# df_attrition_melted = df_attrition.melt(id_vars=['Department'], value_vars=['Jan', 'Feb', 'Mar'],
#                                         var_name='Month', value_name='Attrition Count')

# # Create a Plotly bar chart for the 'Attrition data - Month & Department wise' data
# st.header('Attrition Data - Month & Department Wise')
# fig_attrition = px.bar(df_attrition_melted, x='Month', y='Attrition Count', color='Department',
#                        title='Monthly Attrition Count by Department')
# st.plotly_chart(fig_attrition)





# # Open the 'Gender diversity' worksheet
# gender_diversity_sheet = workbook.worksheet('Gender diversity')

# # Retrieve data from the 'Gender diversity' sheet, including the headers
# gender_diversity_data = gender_diversity_sheet.get_all_values()

# # Manually define the headers if they are not present in the sheet
# headers_gender_diversity = ['Gender', 'Count']

# # Create the DataFrame without the first row if it does not contain headers
# df_gender_diversity = pd.DataFrame(gender_diversity_data, columns=headers_gender_diversity)

# # Convert the 'Count' column to numeric as it will be read as a string
# df_gender_diversity['Count'] = pd.to_numeric(df_gender_diversity['Count'])

# # Create a Plotly bar chart for the 'Gender diversity' data
# st.header('Gender Diversity')
# fig_gender = px.bar(df_gender_diversity, x='Gender', y='Count', title='Gender Diversity Count')
# st.plotly_chart(fig_gender)


import streamlit as st
import gspread
from google.oauth2 import service_account
import pandas as pd
import plotly.express as px
import calendar
import plotly.graph_objects as go

# Set up Google Sheets credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = service_account.Credentials.from_service_account_file('./centered-oasis-416512-58461cae0d1d.json', scopes=scope)
client = gspread.authorize(creds)

# Open the Google Sheet and specific worksheets
sheet_url = 'https://docs.google.com/spreadsheets/d/1XENlmMrDjW5GUhdFjVSheVPtEfHauyOPjtLa8rNH46g/edit#gid=871780544'
workbook = client.open_by_url(sheet_url)
sheet1 = workbook.worksheet('Exit Analysis - Reason for exit')
sheet2 = workbook.worksheet('Employee Connects')

# Retrieve data from the first sheet
data1 = sheet1.get_all_records()
df1 = pd.DataFrame(data1)

# Retrieve data from the second sheet
data2 = sheet2.get_all_values()
headers = data2[1]
data_rows = data2[2:]
df2 = pd.DataFrame(data_rows, columns=headers)

# Clean up headers in df2 if they have leading/trailing spaces
df2.columns = [col.strip() for col in df2.columns]

# Set page title and layout
st.set_page_config(page_title='HR Dashboard', layout='wide')

# Add a title and introduction
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🚀 Human Resources Dashboard 📊</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center; color: #ff7f50;'>This dashboard provides an overview of key HR metrics and insights.</p>", unsafe_allow_html=True)

# Create two columns for the first row of charts
col1, col2 = st.columns(2)

# First chart: Reasons for Department Change
with col1:
    st.markdown("<h3 style='text-align: center; color: #00b0ff;'>🔍 Reasons for Department Change</h3>", unsafe_allow_html=True)
    fig1 = px.bar(df1, x='Department', y=['Career Growth/ Better Opp.', 'Performance issues', 'Health reasons', 'Higher studies'],
                  title='Reasons for Department Change',
                  labels={'value': 'Number of Responses', 'variable': 'Categories'},
                  barmode='group')
    fig1.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig1)

# Second chart: Employee Connect Status by Department
employee_connects_sheet = workbook.worksheet('Employee Connects')

# Retrieve data from the 'Employee Connects' sheet, starting from the second row
employee_connects_data = employee_connects_sheet.get_all_values()[1:]  # Skip the first row

# The headers are assumed to be in the second row, now the first row of our list
headers_employee_connects = employee_connects_data[0]
data_rows_employee_connects = employee_connects_data[1:]  # The rest is data

# Create the DataFrame
df_employee_connects = pd.DataFrame(data_rows_employee_connects, columns=headers_employee_connects)

# Convert the numeric columns to integers
for col in ['Red', 'Amber', 'Green']:
    df_employee_connects[col] = df_employee_connects[col].astype(int)
with col2:
    st.markdown("<h3 style='text-align: center; color: #00b0ff;'>🤝 Employee Connect Status by Department</h3>", unsafe_allow_html=True)
    fig_employee_connects = px.bar(df_employee_connects, x='Department', y=['Red', 'Amber', 'Green'],
                                title='Employee Connects - RAG Status by Department',
                                labels={'value': 'Number of Cases', 'variable': 'Status'},
                                barmode='group')
    st.plotly_chart(fig_employee_connects)

# Create two columns for the second row of charts
col3, col4 = st.columns(2)

# Retrieve data for the 'Queries/Request Received Over Months' chart
data_queries = {
    'Month': ['Jan', 'Feb', 'Mar'],
    'Queries/Requests': [10, 12, 14]
}
df_queries = pd.DataFrame(data_queries)

# Third chart: Queries/Request Received Over Months
with col3:
    st.markdown("<h3 style='text-align: center; color: #00b0ff;'>📈 Queries/Request Received Over Months</h3>", unsafe_allow_html=True)
    fig_queries = px.bar(df_queries, x='Month', y='Queries/Requests',
                         title='Queries/Request Received Over Months',
                         labels={'Month': 'Month', 'Queries/Requests': 'Number of Queries/Requests'})
    fig_queries.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_queries)

# Retrieve data from the 'Attrition data - Month & Department wise' sheet
attrition_data_sheet = workbook.worksheet('Attrititon data - Month & Department wise')
attrition_data = attrition_data_sheet.get_all_records()
df_attrition = pd.DataFrame(attrition_data)

# Retrieve data from the 'Attrition data - Month & Department wise' sheet
attrition_data_sheet = workbook.worksheet('Attrititon data - Month & Department wise')
attrition_data = attrition_data_sheet.get_all_records()
df_attrition = pd.DataFrame(attrition_data)

# Calculate the total attrition count by department
df_attrition['Total Attrition'] = df_attrition['Jan'] + df_attrition['Feb'] + df_attrition['Mar']

# Fourth chart: Attrition by Department
with col4:
    st.markdown("<h3 style='text-align: center; color: #00b0ff;'>📉 Attrition by Department</h3>", unsafe_allow_html=True)
    fig_attrition = px.bar(df_attrition, y='Department', x='Total Attrition',
                           orientation='h',
                           title='Attrition by Department')
    fig_attrition.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_attrition)


# Create two columns for the third row of charts
col5, col6 = st.columns(2)

# Retrieve data from the 'Gender diversity' sheet
gender_diversity_sheet = workbook.worksheet('Gender diversity')
gender_diversity_data = gender_diversity_sheet.get_all_values()
headers_gender_diversity = ['Gender', 'Count']
df_gender_diversity = pd.DataFrame(gender_diversity_data, columns=headers_gender_diversity)
df_gender_diversity['Count'] = pd.to_numeric(df_gender_diversity['Count'])

# Fifth chart: Gender Diversity
with col5:
    st.markdown("<h3 style='text-align: center; color: #ff4b4b;'>👥 Gender Diversity</h3>", unsafe_allow_html=True)
    labels = df_gender_diversity['Gender']
    values = df_gender_diversity['Count']

    fig_gender = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.5)])
    fig_gender.update_layout(
        title='Gender Diversity',
        annotations=[dict(text='', x=0.5, y=0.5, font_size=20, showarrow=False)],
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
    )
    st.plotly_chart(fig_gender)


# Retrieve data from the 'Engagement details - Month wise' sheet
engagement_details_sheet = workbook.worksheet('Engagement details - Month wise')
engagement_details_data = engagement_details_sheet.get_all_values()
headers_engagement_details = engagement_details_data[0]
data_rows_engagement_details = engagement_details_data[1:]
df_engagement_details = pd.DataFrame(data_rows_engagement_details, columns=headers_engagement_details)

# Sixth visual: Engagement Events by Month


transposed_df = df_engagement_details.transpose()

transposed_df.columns = transposed_df.iloc[0]
transposed_df = transposed_df[1:]

with col6:

# Display the transposed table
    st.markdown("<h3 style='text-align: center; color: #ff4b4b;'>🎉 Engagement Events by Month</h3>", unsafe_allow_html=True)
    st.table(transposed_df)


