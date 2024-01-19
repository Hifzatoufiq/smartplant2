import streamlit as st
import pandas as pd

# Set page config to change background color
st.set_page_config(
    page_title="Your App Title",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(
    """
    <style>
        body {
            background-color: #080707;
            color: #f4fbfb;
            font-family: serif;
            primaryColor=#7b2828;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Add custom CSS for styling
custom_css = """
    <style>
        body {
            background-color: white;
            color: white;
        }
        .sidebar .sidebar-content {
            background-color: gray;
        }
        .stTable {
            color: white;
            margin-bottom: 10px; /* Add margin between table rows */
        }
        /* Style anchor tag for yashkawa schedule */
        .sidebar a[href="#yashkawa-schedule"] {
            color: white;
            text-decoration: none;
        }
        .sidebar .css-15ziabu {
            margin: 0 !important;
            padding: 0 !important;
        }
    </style>
"""


st.markdown(custom_css, unsafe_allow_html=True)


st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url('https://res.cloudinary.com/asadullahkhan/image/upload/c_pad,b_auto:predominant,fl_preserve_transparency/v1705583102/RE-removebg-preview_kp4ymg.jpg?_s=public-apps');

               background-repeat: no-repeat;
               background-size: 120px;
                padding-top: 120px;
                background-position: 20px 20px;
            }
           
           
        </style>
        """,
        unsafe_allow_html=True,
    )

# Main content
st.subheader(" Parts  list")

# First DataFrame
data1 = {
    'Father Component': [
        '<a href="" style="color: white; text-decoration: none;">PICKUP FRAME</a>',
        '<a href="" style="color: white; text-decoration: none;">V6 TAIL GATE</a>',
        '<a href="" style="color: white; text-decoration: none;">HD TAIL GATE</a>'
    ]
}


df1 = pd.DataFrame(data1)

styled_df1 = df1.style.hide(axis="index").set_table_styles([
{'selector': '', 'props': [('background-color', '#7b7f89'), ('color', 'white')]},
        {'selector': 'th', 'props': [('background-color', '#7b7f89'), ('color', 'white')]},
])

st.markdown(styled_df1.to_html(escape=False), unsafe_allow_html=True)

# Add a horizontal rule with black color
st.markdown("<hr style='border: 2px solid #0E1117;'>", unsafe_allow_html=True)


data2 = {
    'Part description<br>(father)': ['PICKUP FRAME', 'PICKUP FRAME', 'PICKUP FRAME'],
    'Item name(children)': ['FANCANTINE-A40-ST1', 'COCLE-A-40-ST1', 'RACCOGLITORE_V6_DX-K56790'],
    'Quantity needed per order': ['1', '1', '1'],
}

df2 = pd.DataFrame(data2)

styled_df2 = df2.style.hide(axis="index").set_table_styles([
{'selector': '', 'props': [('background-color', '#7b7f89'), ('color', 'white')]},
        {'selector': 'th', 'props': [('background-color', '#7b7f89'), ('color', 'white')]},
])

# Convert the styled DataFrame to HTML
html_code = styled_df2.to_html(escape=False)

# Manipulate the HTML string to include the width property
html_code = html_code.replace('<table', '<table style="width:1000px;"')

st.markdown(html_code, unsafe_allow_html=True)
