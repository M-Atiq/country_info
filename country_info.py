# country_info
# this is a country card all information country here e.g currency time region nd other
import streamlit as st
import requests

def get_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}?fullText=true"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            country = data[0]
            name = country.get("name", {}).get("common", "N/A")
            capital = country.get("capital", ["N/A"])[0]
            population = country.get("population", "N/A")
            region = country.get("region", "N/A")
            subregion = country.get("subregion", "N/A")
            flag = country.get("flags", {}).get("png", "")
            
            return {
                "Name": name,
                "Capital": capital,
                "Population": population,
                "Region": region,
                "Subregion": subregion,
                "Flag": flag
            }
        else:
            return None
    else:
        return None

st.title("Country Information Finder")

country_name = st.text_input("Enter country name:", "United States")

if st.button("Search"):
    country_name = country_name.strip().title()  # Normalize input
    result = get_country_info(country_name)
    
    if result:
        st.image(result["Flag"], width=150)
        st.write(f"**Name:** {result['Name']}")
        st.write(f"**Capital:** {result['Capital']}")
        st.write(f"**Population:** {result['Population']}")
        st.write(f"**Region:** {result['Region']}")
        st.write(f"**Subregion:** {result['Subregion']}")
    else:
        st.error("Invalid country name. Please enter a valid country.")
