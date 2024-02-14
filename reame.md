
---

# Project Name: Coolify Your Image

## Description

This Flask application detects faces in uploaded images, blurs the faces, and overlays sunglasses on them. It utilizes MTCNN for face detection, OpenCV for image processing, and PIL (Python Imaging Library) for image manipulation.

## Installation

### Prerequisites

- Python 3.6 or later
- pip

### Steps

1. **Clone the repository**

    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2. **Set up a virtual environment** (optional but recommended)

    - For Unix/macOS:

        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

    - For Windows:

        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3. **Install the required dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **TensorFlow Installation Note**

    The project uses MTCNN, which depends on TensorFlow. The `requirements.txt` includes the CPU version of TensorFlow. If you need TensorFlow with GPU support, please install `tensorflow-gpu` instead by running:

    ```bash
    pip install tensorflow-gpu==2.6.0
    ```

## Running the Application

1. **Start the Flask application**

    ```bash
    python app.py
    ```

    The application will start running on `http://localhost:5000`.

2. **Using the application**

    - The application provides an endpoint `/process-image` which expects a POST request with an image file.
    - You can use Postman or any other API testing tool to send a request to this endpoint.
    - Postman collection have been included so make sure to attach an image while calling this endpoint
    - Since this is running locally a postman desktop agent is preferred 

3. **Postman Collection**

    - A Postman collection is included in the root folder of the project (`Coolify_Your_Image.postman_collection.json`). Import this collection into Postman to easily test the application.
    - Make sure to attach the image you want to process with the request under the form-data section with the key `image`.
    - The image is already present in the postman collection and the output of the processed image "update_image.png" at the project root

## Endpoint Details

**POST** `/process-image`

- **Description**: Processes the uploaded image, detects faces, blurs them, and overlays sunglasses.
- **Body**: `multipart/form-data` with a key of `image` and the value being the file you wish to upload.


---

