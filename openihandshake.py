from flask import Flask, request
import openai
import requests
import pyhandshake

app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = "MY OPENAI API"

# Set up Handshake resolver
resolver = pyhandshake.HandshakeResolver("http://localhost:8080")

# Define a route for generating an image based on a prompt
@app.route('/generate_image', methods=['POST'])
def generate_image():
    # Get the domain name from the request
    domain_name = request.form['domain_name']
    
    # Get the Handshake address for the SLD
    sld_address = resolver.get_address(f"{domain_name}.")
    
    # Generate an image based on the prompt
    prompt = f"Create an image that captures the essence of consciousness for the Handshake name {domain_name}."
    response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")

    # Retrieve the URL of the generated image
    image_url = response['data'][0]['url']

    # Download the image
    image_data = requests.get(image_url).content

    # Save the image to a file with the domain name as the filename
    filename = f"{domain_name}_image.png"
    with open(filename, "wb") as f:
        f.write(image_data)

    # Return a message indicating success and the filename of the generated image
    return f"Generated image for {domain_name} ({sld_address}) and saved as {filename}"

if __name__ == '__main__':
    app.run()
