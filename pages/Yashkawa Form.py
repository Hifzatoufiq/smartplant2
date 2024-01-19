import streamlit as st
import pandas as pd






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

class Person:
    def __init__(self, name, email, person_type, parent=None):
        self.name = name
        self.email = email
        self.person_type = person_type
        self.parent = parent

def register_person(name, email, person_type, parent=None):
    data_key = f"{person_type}_data"

    if data_key not in st.session_state:
        st.session_state[data_key] = pd.DataFrame(columns=["Name", "Email", "Parent"])

    new_data = pd.DataFrame({"Name": [name], "Email": [email], "Parent": [parent]})
    st.session_state[data_key] = pd.concat([st.session_state[data_key], new_data], ignore_index=True)

def edit_person(name, person_type):
    data_key = f"{person_type}_data"

    if data_key in st.session_state and not st.session_state[data_key].empty:
        selected_person = st.selectbox(f"Select {person_type} to edit:", st.session_state[data_key]['Name'])

        index = st.session_state[data_key][st.session_state[data_key]['Name'] == selected_person].index[0]

        st.session_state[data_key].at[index, 'Name'] = st.text_input(f"Edit {person_type}'s name:", value=selected_person)
        st.session_state[data_key].at[index, 'Email'] = st.text_input(f"Edit {person_type}'s email:",
                                                                     value=st.session_state[data_key].at[index, 'Email'])

        if person_type == 'child':
            fathers = st.session_state.father_data['Name'].tolist()
            selected_father = st.selectbox("Select Father:", fathers,
                                           index=fathers.index(st.session_state[data_key].at[index, 'Parent']))
            st.session_state[data_key].at[index, 'Parent'] = selected_father

        st.success(f"{person_type.capitalize()} Details Edited Successfully")

def prefill_registration_form(person_type, name):
    data_key = f"{person_type}_data"
    person_data = st.session_state[data_key]

    if not person_data.empty:
        person_row = person_data[person_data['Name'] == name].iloc[0]

        form_key = f"{person_type}_registration_form_{name}"
        with st.form(form_key):
            st.text_input(f"Enter {person_type}'s name:", value=person_row['Name'], key=f"{form_key}_name")
            st.text_input(f"Enter {person_type}'s email:", value=person_row['Email'], key=f"{form_key}_email")

            if person_type == 'child':
                fathers = st.session_state.father_data['Name'].tolist()
                selected_father = st.selectbox("Select Father:", fathers,
                                               index=fathers.index(person_row['Parent']),
                                               key=f"{form_key}_parent")
            else:
                selected_father = None

            submit_button = st.form_submit_button(f"Update {person_type.capitalize()}")

        if submit_button:
            update_person_data(person_type, name, form_key)
            st.experimental_set_query_params()  # Force rerun to update the table
            st.success(f"{person_type.capitalize()} Details Updated Successfully")

def update_person_data(person_type, name, key_prefix):
    data_key = f"{person_type}_data"
    person_data = st.session_state[data_key]

    if not person_data.empty:
        index = person_data[person_data['Name'] == name].index[0]

        person_data.at[index, 'Name'] = st.session_state[key_prefix + f"_name"]
        person_data.at[index, 'Email'] = st.session_state[key_prefix + f"_email"]

        if person_type == 'child':
            person_data.at[index, 'Parent'] = st.session_state[key_prefix + f"_parent"]

def display_person_registration_form(person_type):
    st.subheader(f"{person_type.capitalize()} Registration")
    data_key = f"{person_type}_data"

    with st.form(f"{person_type}_registration_form"):
        name = st.text_input(f"Enter {person_type}'s name:")
        email = st.text_input(f"Enter {person_type}'s email:")

        if person_type == 'child':
            fathers = st.session_state.father_data['Name'].tolist()
            selected_father = st.selectbox("Select Father:", fathers)
        else:
            selected_father = None

        submit_button = st.form_submit_button(f"Register {person_type.capitalize()}")

    if submit_button:
        register_person(name, email, person_type, selected_father)
        st.success(f"{person_type.capitalize()} Registered Successfully")

def display_person_table(person_type):
    st.subheader(f"Registered {person_type.capitalize()}s:")
    data_key = f"{person_type}_data"

    if not st.session_state[data_key].empty:
        # Display the table without the 'Edit' column
        st.dataframe(st.session_state[data_key][['Name', 'Email', 'Parent']], height=300)

        # Add a multiselect for selecting persons to edit (excluding fathers for simplicity)
        selected_persons = st.multiselect(f"Select {person_type}s to Edit:",
                                          st.session_state[data_key]['Name'],
                                          key=f"{person_type}_multiselect")

        # Display the editing form for selected persons
        if selected_persons:
            for selected_person in selected_persons:
                prefill_registration_form(person_type, selected_person)

    else:
        st.info(f"No {person_type.capitalize()}s registered.")

# Display data in a Streamlit app
st.title("Father and Child Form")

if 'father_data' not in st.session_state:
    st.session_state.father_data = pd.DataFrame(columns=["Name", "Email", "Parent"])

if 'child_data' not in st.session_state:
    st.session_state.child_data = pd.DataFrame(columns=["Name", "Email", "Parent"])

selected_form = st.sidebar.radio("Select Form:", ["Father", "Child"])

if selected_form == "Father":
    display_person_registration_form("father")
    display_person_table("father")
elif selected_form == "Child":
    display_person_registration_form("child")
    display_person_table("child")
