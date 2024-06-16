import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")   

    return df


df = load_data()

@st.cache_data
def show_explore_page():
    st.title("Explore Software Engineer Salaries")
    
    st.write("""
             ## Stack Overflow Developer Survey 2023
             """)
            
    data = df["Country"].value_counts()

    explode = [0] * len(data)
    explode[0] = 0.05
    explode[4] = 0.2
    fig1, ax1 = plt.subplots()
    patches, texts, autotexts = ax1.pie(data, labels=data.index, explode=explode, radius=1.2, autopct="%1.1f%%", pctdistance=0.8, textprops={'fontsize':6}, startangle=90)
    # ax1.set_facecolor('#000000')

    for autotext in autotexts:
        autotext.set_horizontalalignment('center')
        autotext.set_fontstyle('italic')

    ax1.axis("equal")


    st.write("""### Number of data from different countries""")
    st.pyplot(fig1)

    st.divider()

    st.write("""### Mean Salary based on Country""")

    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    data = data.rename(index={
        "United Kingdom and Northern Ireland": "United Kingdom",
        "United States of America": "United States"
    })


    st.bar_chart(data, height=500)

    st.divider()

    st.write("""### Mean Salary based on Experience""")

    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data, height=450, color="#4338ca")

