# OCRQuest-2.0

# OCR and Document Search Web Application

This web application allows users to upload images containing text in both Hindi and English for OCR processing and keyword search. The application uses models from Hugging Face's `transformers` library and is built with Streamlit.

## Table of Contents
- Prerequisites
- Installation
- Running the Application Locally
- Deployment
- Usage
- Contributing
- License

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- CUDA-compatible GPU (optional but recommended for faster processing)

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/sprakhil/OCRQuest-2.0.git
    cd OCRQuest-2.0
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application Locally
1. **Start the Streamlit server**:
    ```bash
    streamlit run ocr_script.py
    ```

2. **Access the application**:
    Open your web browser and go to `http://localhost:8501`.

## Deployment
To deploy the application on Streamlit, follow these steps:

1. **Create a Streamlit account**:
    - Sign up at Streamlit.

2. **Prepare your repository**:
    - Ensure all dependencies are listed in `requirements.txt`.
    - Include a `Procfile` with the following content:
        ```plaintext
        web: streamlit run ocr_script.py
        ```

3. **Deploy to Streamlit**:
    - Push your code to a GitHub repository.
    - Go to your Streamlit dashboard and click on "New app".
    - Connect your GitHub repository and select the branch and file (`ocr_script.py`) to deploy.
    - Click "Deploy" and Streamlit will handle the rest.

4. **Access your deployed app**:
    - Once deployed, you will receive a URL to access your application.
    
## Usage
1. **Upload an Image**:
    - Click on the "Choose an image..." button and select an image file (jpg, jpeg, png).

2. **View Extracted Text**:
    - The application will process the image and display the extracted text.

3. **Keyword Search**:
    - Enter a keyword in the text input box to search within the extracted text.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
