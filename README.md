
# ImageGen-OpenAI
*Empower Your Creativity with AI-Generated Images*

[Screencast.webm](https://github.com/Laban254/ImageGen-OpenAI/assets/64686919/dbcae23c-48aa-47f4-bf25-6f2253de1b4a)

## Table of Contents
1. [Description](#description)
2. [Features](#features)
3. [Getting Started](#getting-started)
    - [Installation](#installation)
    - [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)
6. [Additional Information](#additional-information)

## Description
ImageGen-OpenAI is a web application built using Django and the OpenAI API. It allows users to generate images based on textual descriptions they provide. The application sends the user's input to the OpenAI API, which then generates an image corresponding to the description. The generated image is displayed on the webpage, and users have the option to download it directly. ImageGen-OpenAI is designed with simplicity and user-friendliness in mind, featuring a clean interface and straightforward functionality.

## Features
- **Text-to-Image Generation:** Users can input text descriptions, which are then used to generate images.
- **Image Variations:** The application can produce multiple variations of an image based on the same input text, providing different visual interpretations.
- **User Interface:** A clean and intuitive interface enables users to input text and view the generated images seamlessly.
- **Image Display and Download:** Generated images are displayed on the webpage for immediate viewing, and users can download them with ease.
- **Customization:** Users have the option to customize the style or theme of the generated images by providing specific instructions or prompts.

## Getting Started

### Installation

To leverage ImageGen locally, follow these steps:

```bash
# Clone the repository
$ git clone https://github.com/Laban254/ImageGen-OpenAI.git

# Navigate to the project directory
$ cd ImageGen-OpenAI

# Install dependencies
## If you're using pipenv, run:
$ pipenv install

## Alternatively, if you prefer using pip, you can install the dependencies listed in the `Pipfile` manually

# Apply Migrations
$ python manage.py migrate

# Start the Server
$ python manage.py runserver

# After running this command, you can access the application by navigating to `http://localhost:8000` in your web browser
```

### Usage

- **Generate an Image**: Enter your text description in the input field on the homepage and click "Generate" to create an image.
- **Download Image**: Once the image is generated, you can download it by clicking the "Download Image" button.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues on GitHub.

## License

ImageGen is open-source software licensed under the MIT License.

