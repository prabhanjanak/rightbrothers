import streamlit as st

# Define the links
links = {
    "Rental Agreement": "https://rightbrothersrental.streamlit.app/",
    "Trust Deed": "https://rightbrotherstrust.streamlit.app/",
    "MoU": "https://rightbrothersmou.streamlit.app/"
}

# Set the page title
st.set_page_config(page_title="Right Brothers Document Generation")

# Display the title with the logo
st.title("Objective 1 Right Brothers Document Generation")

# Display the logo
st.image("pes.png", width=100)  # Adjust width as needed

# Create a sidebar with links to different documents
st.sidebar.title("Documents")
selection = st.sidebar.radio("Choose a document type", list(links.keys()))

# Redirect to the chosen link
st.write(f"Redirecting to the {selection}...")
st.markdown(f"[Click here to open {selection}]({links[selection]})", unsafe_allow_html=True)

# You can also use the following approach to open the link in a new tab
# import webbrowser
# webbrowser.open(links[selection])
