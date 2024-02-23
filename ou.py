import streamlit as st
import requests
import re

def extract_mp4_urls(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            mp4_urls = re.findall(r'(https?://\S+\.mp4)', html_content)
            return mp4_urls
        else:
            st.error("Failed to fetch the webpage. Status code:", response.status_code)
            return None
    except Exception as e:
        st.error("An error occurred:", str(e))
        return None

st.title("MP4 URL Extractor")

url = st.text_input("Enter URL:")
if st.button("Extract MP4 URLs"):
    if url:
        mp4_urls = extract_mp4_urls(url)
        if mp4_urls:
            st.success("MP4 URLs found:")
            for mp4_url in mp4_urls:
                st.write(mp4_url)
        else:
            st.warning("No MP4 URLs found.")
    else:
        st.warning("Please enter a URL.")
