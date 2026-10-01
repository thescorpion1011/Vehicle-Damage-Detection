import streamlit as st
from model_helper import predict
import tempfile
from pathlib import Path

st.title("Vehicle Damage Detection")

uploaded_file = st.file_uploader(
    "Upload the file",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    # Get original file extension
    suffix = Path(uploaded_file.name).suffix

    # Create temporary file with correct extension
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    ) as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        image_path = temp_file.name

    st.image(
        uploaded_file,
        caption="Uploaded File",
        width="stretch"
    )

    prediction = predict(image_path)

    st.info(f"Predicted Class: {prediction}")