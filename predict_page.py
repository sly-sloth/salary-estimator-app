import streamlit as st
import pickle
import numpy as np
import requests
import sklearn



def load_model():
    with open("saved_mod.pkl", "rb") as file:
        data = pickle.load(file)

    return data


data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_ed = data["le_ed"]
le_industry = data["le_industry"]


countries_and_currency_codes = {
    'India': 'INR',
    'United States of America': 'USD',
    'United Kingdom and Northern Ireland': 'GBP',
    'Netherlands': 'EUR',
    'Germany': 'EUR',
    'France': 'EUR',
    'Spain': 'EUR',
    'Italy': 'EUR',
    'Canada': 'CAD',
    'Brazil': 'BRL',
    'Sweden': 'SEK',
    'Poland': 'PLN',
    'Australia': 'AUD'
}


countries_and_currency_symbols = {
    'India': '₹',
    'United States of America': '$',
    'United Kingdom and Northern Ireland': '£',
    'Netherlands': '€',
    'Germany': '€',
    'France': '€',
    'Spain': '€',
    'Italy': '€',
    'Canada': 'CAD',
    'Brazil': 'BRL',
    'Sweden': 'kr',
    'Poland': 'zł',
    'Australia': 'AUD'
}

@st.cache_data
def api_call():
    r = requests.get(url="https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_8O1MhUePV3qZRWQf22Rmv0bfzxMYaOamCQTCJwDK&currencies=CAD%2CAUD%2CINR%2CBRL%2CUSD%2CEUR%2CSEK%2CPLN%2CGBP")
    r.raise_for_status()

    return r.json()

conversion_data = api_call()
conversion_data = conversion_data["data"]
# print(conversion_data)
# print(r.json())


def show_predict_page():
    st.title("Software Dev Salary Predictor")

    st.write("""### We need some info to predict the salary""")


    countries = (
        'India',
        'United States of America',
        'United Kingdom and Northern Ireland',
        'Netherlands',
        'Germany',
        'France',
        'Spain',
        'Italy',
        'Canada',
        'Brazil',
        'Sweden',
        'Poland',
        'Australia'
    )

    ed_lvl = (
        "Bachelor's Degree",
        "Less than a Bachelor's",
        "Master's Degree",
        "Post Grad"
    )

    industries = (
        'Information Services, IT, Software Development, or other Technology',
        'Other',
        'Financial Services',
        'Manufacturing, Transportation, or Supply Chain',
        'Retail and Consumer Services',
        'Higher Education',
        'Insurance',
        'Healthcare',
        'Wholesale',
        'Oil & Gas',
        'Advertising Services',
        'Legal Services'
    )


    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", ed_lvl)
    industry = st.selectbox("Industry", industries)

    experience = st.slider("Years of Experience", 0, 50, 3)

    
    ok = st.button("Calculate")
    if ok:
        x = np.array([[country, education, experience, industry]])

        x[:, 0] = le_country.transform(x[:, 0])
        x[:, 1] = le_ed.transform(x[:, 1])
        x[:, 3] = le_industry.transform(x[:, 3])
        x = x.astype(float)

        salary = regressor.predict(x)
        salary = salary[0]
        formatted_salary = "{:,.2f}".format(salary)

        native_salary = round(salary * conversion_data[countries_and_currency_codes[country]], 2)
        native_c = countries_and_currency_symbols[country]
        formatted_native_salary = "{:,.2f}".format(native_salary)

        if country != "United States of America":
            st.subheader(f"The estimated salary is $ {formatted_salary} or {native_c} {formatted_native_salary}")
        else:
            st.subheader(f"The estimated salary is $ {formatted_salary}")
