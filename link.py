import streamlit as st

# Set up the page configuration
st.set_page_config(
    page_title="Document Generator",
    page_icon=":page_facing_up:",
    layout="wide"
)

# Display the logo and title
st.title("Document Generator")

# Display the logo
st.image("pes.png", width=100)

# Navigation
st.sidebar.title("Navigation")
option = st.sidebar.radio("Select a Document:", ["Rental Agreement", "Trust Deed", "MoU"])

if option == "Rental Agreement":
    st.write("### Rental Agreement Generator")
    st.write("Click [here](rental.py) to generate a Rental Agreement.")
elif option == "Trust Deed":
    st.write("### Trust Deed Generator")
    st.write("Click [here](trust.py) to generate a Trust Deed.")
elif option == "MoU":
    st.write("### MoU Generator")
    st.write("Click [here](mou.py) to generate a MoU.")

# Footer
st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
        font-size: 12px;
        color: #555;
    }
    </style>
    <div class="footer">
        Developed by Right Brothers, Dept of AIML PESITM Shivamogga
    </div>
    """, unsafe_allow_html=True)
