import numpy as np
import pandas as pd
import plotly.express as px


def load_data(path):
    return pd.read_csv(path)

def viz_employee_attrition(df, graph='bar'):
    df_attribution = df['Attrition'].value_counts()
    df_attribution.index = df_attribution.index.map({'Yes':'Left Company', 'No':'Stayed'})
    if graph == 'bar':
        fig = px.bar(x=df_attribution.index, y=df_attribution.values, labels={'x':'Attrition', 'y':'Number of Employee'}, title='Employee Attrition')
    elif graph == 'pie':
        fig = px.pie(names=df_attribution.index, values=df_attribution.values, title='Employee Attrition', hole=.7)     
        fig.add_annotation(text='Employees<br>'+str(df.shape[0]), x=0.5, y=0.5, font_size=20, showarrow=False, )

    return fig

# visualize the distribution of employees by department
def viz_department(df, graph='bar'):
    df_department = df['Department'].value_counts()
    if graph == 'bar':
        fig = px.bar(x=df_department.index, y=df_department.values, labels={'x':'Department', 'y':'Number of Employee'}, title='Employee Distribution by Department')
    elif graph == 'pie':
        fig = px.pie(names=df_department.index, values=df_department.values, title='Employee Distribution by Department', hole=.7)
        fig.add_annotation(text='Employees<br>'+str(df.shape[0]), x=0.5, y=0.5, font_size=20, showarrow=False, )
    elif graph == 'funnel':
        fig = px.funnel_area(names=df_department.index, values=df_department.values, title='Employee Distribution by Department')
    return fig

# travel
def viz_travel(df, graph='bar'):
    df_travel = df['BusinessTravel'].value_counts()
    if graph == 'area':
        fig = px.area(x=df_travel.index, y=df_travel.values, labels={'x':'Travel Frequency', 'y':'Number of Employee'}, title='Employee Travel Frequency')
    elif graph == 'pie':
        fig = px.pie(names=df_travel.index, values=df_travel.values, title='Employee Travel Frequency', hole=.7)
        fig.add_annotation(text='Employees<br>'+str(df.shape[0]), x=0.5, y=0.5, font_size=20, showarrow=False, )
    return fig

# visualize the distribution of employees by education field
def viz_education_field(df, graph='violin'):
    # violin, box, strip
    if graph == 'violin':
        fig = px.violin(df, x='EducationField', y='MonthlyIncome', box=True, title='Employee Monthly Income by Education Field')
    elif graph == 'box':
        fig = px.box(df, x='EducationField', y='MonthlyIncome', points="all", title='Employee Monthly Income by Education Field')
    elif graph == 'strip':
        fig = px.strip(df, x='EducationField', y='MonthlyIncome', title='Employee Monthly Income by Education Field')
    return fig

# visualize the distribution of employees by job role
def viz_job_role(df, graph='strip', color='Gender'):
    if graph == 'strip':
        fig = px.strip(df, x='JobRole', y='MonthlyIncome', title='Employee Monthly Income by Job Role', color=color)
    elif graph == 'box':
        fig = px.box(df, x='JobRole', y='MonthlyIncome', title='Employee Monthly Income by Job Role', color=color)
    elif graph == 'violin':
        fig = px.violin(df, x='JobRole', y='MonthlyIncome', title='Employee Monthly Income by Job Role', color=color)
    return fig

# visualize the distribution of employees by job satisfaction
def viz_job_satisfaction(df, graph='bar'):
    df_job_satisfaction = df['JobSatisfaction'].value_counts()
    # labels
    df_job_satisfaction.index = df_job_satisfaction.index.map({1:'Low', 2:'Medium', 3:'High', 4:'Very High'})
    if graph == 'bar':
        fig = px.bar(x=df_job_satisfaction.index, y=df_job_satisfaction.values, labels={'x':'Job Satisfaction', 'y':'Number of Employee'}, title='Employee Job Satisfaction', text=df_job_satisfaction.values)
        # increase text size
        fig.update_traces(texttemplate='%{text:.2s}', textposition='auto', textfont_size=50)
    elif graph == 'pie':
        fig = px.pie(names=df_job_satisfaction.index, values=df_job_satisfaction.values, title='Employee Job Satisfaction', hole=.7)
        fig.add_annotation(text='Employees<br>'+str(df.shape[0]), x=0.5, y=0.5, font_size=20, showarrow=False, )
    return fig

# visualize the distribution of employees by job level
def viz_job_level(df, graph='bar'):
    df_job_level = df['JobLevel'].value_counts()
    if graph == 'bar':
        fig = px.bar(x=df_job_level.index, y=df_job_level.values, labels={'x':'Job Level', 'y':'Number of Employee'}, title='Employee Job Level', text=df_job_level.values)
        # increase text size
        fig.update_traces(texttemplate='%{text:.2s}', textposition='auto', textfont_size=50)
    elif graph == 'pie':
        fig = px.pie(names=df_job_level.index, values=df_job_level.values, title='Employee Job Level', hole=.7)
        fig.add_annotation(text='Employees<br>'+str(df.shape[0]), x=0.5, y=0.5, font_size=20, showarrow=False, )
    return fig

# visualize the distribution of employees by job involvement
def viz_job_involvement(df, graph='bar'):
    df_job_involvement = df['JobInvolvement'].value_counts()
    # labels
    df_job_involvement.index = df_job_involvement.index.map({1:'Low', 2:'Medium', 3:'High', 4:'Very High'})
    if graph == 'bar':
        fig = px.bar(x=df_job_involvement.index, y=df_job_involvement.values, labels={'x':'Job Involvement', 'y':'Number of Employee'}, title='Employee Job Involvement', text=df_job_involvement.values)
        # increase text size
        fig.update_traces(texttemplate='%{text:.2s}', textposition='auto', textfont_size=50)
    elif graph == 'pie':
        fig = px.pie(names=df_job_involvement.index, values=df_job_involvement.values, title='Employee Job Involvement', hole=.7)
        fig.add_annotation(text='Employees<br>'+str(df.shape[0]), x=0.5, y=0.5, font_size=20, showarrow=False, )
    return fig

# visualize the distribution of employees by performance rating
def viz_performance_rating(df, graph='bar'):
    df_performance_rating = df['PerformanceRating'].value_counts()
    # labels
    df_performance_rating.index = df_performance_rating.index.map({1:'Low', 2:'Good', 3:'Excellent', 4:'Outstanding'})
    if graph == 'bar':
        fig = px.bar(x=df_performance_rating.index, y=df_performance_rating.values, labels={'x':'Performance Rating', 'y':'Number of Employee'}, title='Employee Performance Rating', text=df_performance_rating.values)
        # increase text size
        fig.update_traces(texttemplate='%{text:.2s}', textposition='auto', textfont_size=50)
    elif graph == 'pie':
        fig = px.pie(names=df_performance_rating.index, values=df_performance_rating.values, title='Employee Performance Rating', hole=.7)
        fig.add_annotation(text='Employees<br>'+str(df.shape[0]), x=0.5, y=0.5, font_size=20, showarrow=False, )
    return fig

# visualize the distribution of employees by relationship satisfaction
def viz_relationship_satisfaction(df, graph='bar'):
    df_relationship_satisfaction = df['RelationshipSatisfaction'].value_counts()
    # labels
    df_relationship_satisfaction.index = df_relationship_satisfaction.index.map({1:'Low', 2:'Medium', 3:'High', 4:'Very High'})
    if graph == 'bar':
        fig = px.bar(x=df_relationship_satisfaction.index, y=df_relationship_satisfaction.values, labels={'x':'Relationship Satisfaction', 'y':'Number of Employee'}, title='Employee Relationship Satisfaction', text=df_relationship_satisfaction.values)
        # increase text size
        fig.update_traces(texttemplate='%{text:.2s}', textposition='auto', textfont_size=50)
    elif graph == 'pie':
        fig = px.pie(names=df_relationship_satisfaction.index, values=df_relationship_satisfaction.values, title='Employee Relationship Satisfaction', hole=.7)
        fig.add_annotation(text='Employees<br>'+str(df.shape[0]), x=0.5, y=0.5, font_size=20, showarrow=False, )
    return fig


# visualize the distribution of employees by work life balance
def viz_work_life_balance(df, graph='bar'):
    df_work_life_balance = df['WorkLifeBalance'].value_counts()
    # labels
    df_work_life_balance.index = df_work_life_balance.index.map({1:'Bad', 2:'Good', 3:'Better', 4:'Best'})
    if graph == 'bar':
        fig = px.bar(x=df_work_life_balance.index, y=df_work_life_balance.values, labels={'x':'Work Life Balance', 'y':'Number of Employee'}, title='Employee Work Life Balance', text=df_work_life_balance.values)
        # increase text size
        fig.update_traces(texttemplate='%{text:.2s}', textposition='auto', textfont_size=50)
    elif graph == 'pie':
        fig = px.pie(names=df_work_life_balance.index, values=df_work_life_balance.values, title='Employee Work Life Balance', hole=.7)
        fig.add_annotation(text='Employees<br>'+str(df.shape[0]), x=0.5, y=0.5, font_size=20, showarrow=False, )
    return fig

# visualize the distribution of employees by environment satisfaction
def viz_environment_satisfaction(df, graph='bar'):
    df_environment_satisfaction = df['EnvironmentSatisfaction'].value_counts()
    # labels
    df_environment_satisfaction.index = df_environment_satisfaction.index.map({1:'Low', 2:'Medium', 3:'High', 4:'Very High'})
    if graph == 'bar':
        fig = px.bar(x=df_environment_satisfaction.index, y=df_environment_satisfaction.values, labels={'x':'Environment Satisfaction', 'y':'Number of Employee'}, title='Employee Environment Satisfaction', text=df_environment_satisfaction.values)
        # increase text size
        fig.update_traces(texttemplate='%{text:.2s}', textposition='auto', textfont_size=50)
    elif graph == 'pie':
        fig = px.pie(names=df_environment_satisfaction.index, values=df_environment_satisfaction.values, title='Employee Environment Satisfaction', hole=.7)
        fig.add_annotation(text='Employees<br>'+str(df.shape[0]), x=0.5, y=0.5, font_size=20, showarrow=False, )
    return fig

# visualize the distribution of employees
def viz_employee_distribution(df, graph='hist', group='Gender'):
    if graph == 'hist':
        fig = px.histogram(df, x='Age', title='Employee Age Distribution', nbins=50, marginal='box', opacity=0.7, color=group)
    elif graph == 'box':
        fig = px.box(df, x='Age', title='Employee Age Distribution', color=group)
    return fig

# employee income
def viz_employee_income(df, graph='hist'):
    if graph == 'hist':
        fig = px.histogram(df, x='MonthlyIncome', title='Employee Monthly Income Distribution', nbins=50, marginal='box', opacity=0.7)
    elif graph == 'box':
        fig = px.box(df, x='MonthlyIncome', title='Employee Monthly Income Distribution')
    elif graph == 'violin':
        fig = px.violin(df, y='MonthlyIncome', title='Employee Monthly Income Distribution')

    return fig

# employee income gender distribution by department
def viz_income(df, graph='box'):
    if graph == 'box':
        fig = px.box(df, x='Department', y='MonthlyIncome', title='Employee Monthly Income by Department', color='Gender')
    elif graph == 'strip':
        fig = px.strip(df, x='Department', y='MonthlyIncome', title='Employee Monthly Income by Department', color='Gender')
    return fig

# sunburst chart
def viz_sunburst(df, path=['Department', 'JobRole'], values='MonthlyIncome'):
    fig = px.sunburst(df, path=path, values=values, title='Employee Monthly Income by Department and Job Role')
    return fig

# scatter plots
def viz_employee_scatter(df, x='Age', y='MonthlyIncome', color='Attrition', size='TotalWorkingYears'):
    fig = px.scatter(df, x=x, y=y, color=color, size=size, title='Employee Monthly Income vs Age', hover_name='JobRole', hover_data=['Department'])
    return fig

# correlation matrix
def viz_correlation_matrix(df):
    fig = px.imshow(df.corr(), title='Correlation Matrix', width=800, height=800)
    return fig


# 3d scatter plot

def viz_employee_3d_scatter(df, x='Age', y='MonthlyIncome', z='TotalWorkingYears', color='Attrition'):
    fig = px.scatter_3d(df, x=x, y=y, z=z, color=color, title='Employee Monthly Income vs Age vs Total Working Years', hover_name='JobRole', hover_data=['Department'], height=800, width=800)
    return fig

def load_basics():
    df = load_data('dataset.csv')
    fig1 = viz_employee_attrition(df, graph='pie')
    fig2 = viz_department(df, graph='funnel')
    fig3 = viz_travel(df, graph='area')
    fig4 = viz_education_field(df, graph='violin')
    fig5 = viz_job_role(df, graph='box', color='MaritalStatus')
    fig6 = viz_job_satisfaction(df, graph='bar')
    fig7 = viz_job_level(df, graph='bar')
    fig8 = viz_job_involvement(df, graph='bar')
    fig9 = viz_performance_rating(df, graph='bar')
    fig10 = viz_relationship_satisfaction(df, graph='bar')
    fig11 = viz_work_life_balance(df, graph='bar')
    fig12 = viz_environment_satisfaction(df, graph='bar')
    fig13 = viz_employee_distribution(df, graph='hist')
    fig14 = viz_employee_income(df, graph='hist')
    fig15 = viz_income(df, graph='box')
    fig16 = viz_sunburst(df)
    fig17 = viz_employee_scatter(df)
    fig18 = viz_correlation_matrix(df)
    fig19 = viz_employee_3d_scatter(df)
    return {'fig1':fig1, 'fig2':fig2, 'fig3':fig3, 'fig4':fig4, 'fig5':fig5, 'fig6':fig6, 'fig7':fig7, 'fig8':fig8, 'fig9':fig9, 'fig10':fig10, 'fig11':fig11, 'fig12':fig12, 'fig13':fig13, 'fig14':fig14, 'fig15':fig15, 'fig16':fig16, 'fig17':fig17, 'fig18':fig18, 'fig19':fig19}