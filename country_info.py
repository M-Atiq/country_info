# country_info
this is a country card all information country here e.g currency time region nd other
import streamlit as st
import requests

def get_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}?fullText=true"
    response = requests.get(url)
    
    if response.status_code == 200:
        countries = response.json()
        country_data = []
        for data in countries:
            country_data.append({
                "Name": data.get("name", {}).get("common", "N/A"),
                "Official Name": data.get("name", {}).get("official", "N/A"),
                "Capital": ", ".join(data.get("capital", ["N/A"])),
                "Population": f"{data.get('population', 'N/A'):,}",
                "Region": data.get("region", "N/A"),
                "Subregion": data.get("subregion", "N/A"),
                "Currency": ", ".join([f"{v['name']} ({k})" for k, v in data.get("currencies", {}).items()]),
                "Languages": ", ".join(data.get("languages", {}).values()),
                "Timezones": ", ".join(data.get("timezones", [])),
                "Flag": data.get("flags", {}).get("png", ""),
                "Borders": ", ".join(data.get("borders", ["None"]))
            })
        return country_data
    else:
        return None

st.title("🌍 Country Information Card")

country_name = st.text_input("Enter full country name:", "United Arab Emirates")

if st.button("Get Info"):
    country_info_list = get_country_info(country_name.strip())
    
    if country_info_list:
        for country_info in country_info_list:
            st.image(country_info["Flag"], caption=country_info["Name"], width=150)
            st.write(f"**Official Name:** {country_info['Official Name']}")
            st.write(f"**Capital:** {country_info['Capital']}")
            st.write(f"**Population:** {country_info['Population']}")
            st.write(f"**Region:** {country_info['Region']}")
            st.write(f"**Subregion:** {country_info['Subregion']}")
            st.write(f"**Currency:** {country_info['Currency']}")
            st.write(f"**Languages:** {country_info['Languages']}")
            st.write(f"**Timezones:** {country_info['Timezones']}")
            st.write(f"**Neighboring Countries:** {country_info['Borders']}")
            st.write("---")
    else:
        st.error("Country not found! Please enter the exact name and try again.")
