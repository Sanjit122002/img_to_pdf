import streamlit as st
from PIL import Image
from io import BytesIO

# Inject custom CSS to change background and text colors


# Function to convert images to PDF
def convert_images_to_pdf(image_files):
    images = []
    for image_file in image_files:
        image = Image.open(image_file)
        if image.mode == 'RGBA':  # Convert PNG with alpha to RGB
            image = image.convert('RGB')
        images.append(image)
    
    # Save images as a PDF in memory
    pdf_bytes = BytesIO()
    images[0].save(pdf_bytes, format='PDF', save_all=True, append_images=images[1:])
    pdf_bytes.seek(0)  # Reset the buffer position to the beginning

    return pdf_bytes

# Streamlit Web App
st.title("Image to PDF Converter")

# File uploader to accept multiple image files
uploaded_images = st.file_uploader("Upload Images", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

# Button to trigger the PDF conversion
if uploaded_images and st.button("Convert to PDF"):
    # Convert images to PDFc
    pdf_file = convert_images_to_pdf(uploaded_images)
    
    # Download link for the generated PDF
    st.success("Conversion successful! Download your PDF below.")
    st.download_button("Download PDF", data=pdf_file, file_name="converted_images.pdf", mime="application/pdf")

# Footer or additional information
st.write("Upload your images in PNG, JPG, or JPEG format and click 'Convert to PDF' to generate a PDF file.")
