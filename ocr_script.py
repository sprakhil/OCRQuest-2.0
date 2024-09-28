import streamlit as st
from PIL import Image
import torch
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from colpali_engine.models import ColPali, ColPaliProcessor

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_colpali = ColPali.from_pretrained("vidore/colpali-v1.2", torch_dtype=torch.bfloat16).to(device)
processor_colpali = ColPaliProcessor.from_pretrained("google/paligemma-3b-mix-448")

model_qwen = Qwen2VLForConditionalGeneration.from_pretrained("Qwen/Qwen2-VL-7B-Instruct").to(device)
processor_qwen = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-7B-Instruct")

st.title("OCR and Document Search Web Application")
st.write("Upload an image containing text in both Hindi and English for OCR processing and keyword search.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")

        conversation = [{"role": "user", "content": [{"type": "image"}, {"type": "text", "text": "Describe this image."}]}]
        text_prompt = processor_qwen.apply_chat_template(conversation, add_generation_prompt=True)
        inputs = processor_qwen(text=[text_prompt], images=[image], padding=True, return_tensors="pt").to(device)

        with torch.no_grad():
            output_ids = model_qwen.generate(**inputs, max_new_tokens=128)
            generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(inputs.input_ids, output_ids)]
            output_text = processor_qwen.batch_decode(generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True)

        st.write("Extracted Text:")
        st.write(output_text)

        keyword = st.text_input("Enter a keyword to search in the extracted text:")
        if keyword:
            if keyword.lower() in output_text[0].lower():
                st.write(f"Keyword '{keyword}' found in the text.")
            else:
                st.write(f"Keyword '{keyword}' not found in the text.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    st.write("Deploying the web application...")
