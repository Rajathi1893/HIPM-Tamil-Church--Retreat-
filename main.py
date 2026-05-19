import streamlit as st
import csv
import os
from datetime import datetime

# Page Config
st.set_page_config(
    page_title="HIPM Tamil Retreat",
    page_icon="🕊️",
    layout="centered"
)

# Title
st.title("HIPM Tamil Church Retreat")
st.subheader("Retreat Registration Form")

# Registration Form
with st.form("registration_form"):

    name = st.text_input("Full Name *")

    phone = st.text_input("Phone Number *")

    address = st.text_area("Address *")

    location = st.selectbox(
        "Choose Your Location",
        ["Bedford", "Dartmouth", "Downtown", "Others"]
    )

    submit = st.form_submit_button("Submit Registration")


# Save Data
if submit:

    # Validation
    if not name.strip() or not phone.strip() or not address.strip():
        st.error("Please fill all required fields.")
    else:

        file_name = "registrations.csv"

        file_exists = os.path.isfile(file_name)

        try:
            with open(file_name, mode="a", newline="", encoding="utf-8") as file:

                writer = csv.writer(file)

                # Write header only once
                if not file_exists:
                    writer.writerow([
                        "Name",
                        "Phone",
                        "Address",
                        "Location",
                        "Registered Time"
                    ])

                # Save registration
                writer.writerow([
                    name.strip(),
                    phone.strip(),
                    address.strip(),
                    location,
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ])

            st.success("Registration Submitted Successfully!")
            st.balloons()

        except Exception as e:
            st.error(f"Error saving registration: {e}")
