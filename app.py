import streamlit as st
import os
from PIL import Image

# Set up upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Use session state to store uploaded data
if "festival_data" not in st.session_state:
    st.session_state.festival_data = {}

st.title("🎉 Festival Image Uploader")

# Ask for festival name first
festival_name = st.text_input("Enter the festival name")

# Upload section
uploaded_file = st.file_uploader("Upload a festival image", type=["jpg", "jpeg", "png"])
description = st.text_area("Write a description about the festival image")

if st.button("Submit"):
    if festival_name and uploaded_file and description:
        # Save the image
        file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Store in session_state
        if festival_name not in st.session_state.festival_data:
            st.session_state.festival_data[festival_name] = []

        st.session_state.festival_data[festival_name].append({
            "filename": uploaded_file.name,
            "description": description
        })

        st.success(f"Image added to {festival_name} gallery!")
    else:
        st.error("Please enter festival name, upload an image, and add a description.")

# ---------------------------
# 📸 Festival Gallery Section
# ---------------------------
st.markdown("---")
st.header("📸 Festival Gallery")

if st.session_state.festival_data:
    for fest, items in st.session_state.festival_data.items():
        st.subheader(f"✨ {fest}")  # Festival name at top
        for item in items:
            img_path = os.path.join(UPLOAD_FOLDER, item["filename"])
            img = Image.open(img_path)
            st.image(img, width=400, caption=item["description"])
        st.markdown("---")
else:
    st.info("No festival images uploaded yet.")