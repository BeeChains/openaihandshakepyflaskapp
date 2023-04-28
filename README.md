# openaihandshakepyflaskapp | dns-to-image | innerigpt

Open AI Handshake Python Flask App - Flask app for generating images based on prompts for Handshake domains

This Flask app uses the OpenAI API to generate images based on prompts for Handshake domains. It requires a Handshake resolver set up and running on http://localhost:8080, and a valid OpenAI API key. This app uses the pyhandshake library to interact with a local Handshake resolver and get the address for the SLD. You would need to make sure that your local resolver is set up and running on http://localhost:8080, and that the innerigpt SLD is registered on the Handshake blockchain.

To run this app, you would also need to install the pyhandshake library in addition to Flask. You can then send a POST request to dns like, http://sld.tld/generate_image with a form field named domain_name containing the SLD you want to generate an image for using OpenAI and dalle

# Installation:
<ul>Install Python 3.6 or later if it is not already installed.

Clone this repository ``` git clone https://github.com/BeeChains/openaihandshakepyflaskapp.git ``` or download the ZIP file and extract it. 

Open a terminal or command prompt in the project directory.

Create a virtual environment with ``` python -m venv venv ```

Activate the virtual environment with ``` source venv/bin/activate ``` on macOS/Linux or ``` venv\Scripts\activate ``` on Windows.

Install the required Python packages with ``` pip install -r requirements.txt ```</ul>

# Configuration:

Before running the app, you need to set your OpenAI API key. You can do this by setting the OPENAI_API_KEY environment variable to your API key, like this:
    ``` export OPENAI_API_KEY=<your API key>
    ```

If you are on Windows, you can set the environment variable using the command:
    ``` set OPENAI_API_KEY=<your API key>
    ```
    
# Usage:
  To start the app, run the following command in the project directory:
    ``` 
    flask run 
    ```
    
This will start the app on http://localhost:5000
    
To generate an image based on a prompt for a Handshake domain, send a POST request to http://sld.tld/generate_image, where sld is the second-level domain you want to generate an image for, and tld is your Handshake top-level domain. For example, if you own the domain example/, you could send a request to http://generateimg.example/generate_image with the following json:
 
    
     {
     "prompt": "Create an image that captures the essence of your Handshake domain",
     "size": "512x512"
     } 
     
This will generate an image based on the prompt and return a message indicating success and the filename of the generated image.
Note that you need to have registered the Handshake domain and set up a Handshake resolver to use this app. You also need to configure your DNS settings to point your Handshake domain to your app.

# Installation and set-up instructions for a Handshake resolver on http://localhost:8080
The hsd daemon is a full node implementation of the [Handshake protocol](https://handshake.org/), and it can be used to participate in the Handshake network. If you want to use hsd to register your Handshake domain and run a resolver on your local machine, you will need to install and run the hsd daemon.

# Installation: 
1. Install Node.js and npm (the Node.js package manager) if they are not already installed. You can download the installer from the official website at https://nodejs.org/.

2. Open a terminal or command prompt and run the following command to install the hsd package globally:
    ``` 
     npm install -g hsd 
    ```

# Set-up
1. Generate a new Handshake configuration with the following command:
   ``` 
    hsd --prefix ~/.hsd create

   ```
2. Open the ~/.hsd/handshake.conf file in a text editor and add the following lines:  
   ```
    network: testnet
    prune: false
    rpc: true
    index-tx: true
    index-address: true
    api-key: <your API key>
   ```
 Replace <your API key> with a secure and random string of your choice, which will be used to authenticate API requests to your resolver.  
 Start the Handshake daemon with the following command:
    ```
    hsd --prefix ~/.hsd
    ```
 This will start the daemon in the foreground. If you want to run it in the background, you can use a process manager like pm2 or systemd.
 
 4. Register a new Handshake domain using the hs-client command-line tool:
    ```
    hs-client --prefix ~/.hsd name --register <name>
    ```
Replace <name> with the name of the domain you want to register. Note that you will need to have some HNS coins to register a domain.

Configure your DNS settings to point your Handshake domain to your resolver. You can do this by adding a DNS record of type NS for your domain, with the value localhost. (including the trailing dot). For example, if you registered the domain example/, you would add the following DNS record:
   ```
    example/ IN NS localhost.
   ```

6. Test your resolver by making an API request to it. For example, you can use the curl command to retrieve the list of Handshake names:
   ```
    curl -u <your API key>: http://localhost:8080/api/names
   ```
   
   Replace <your API key> with your API key, and you should see a JSON response with the list of names registered on your resolver.
   
   # 🤝 Your Handshake resolver is now set up and running on http://localhost:8080. You can use it to resolve Handshake domains and serve content from your local machine.
   
 Once you have set your API key, you can use it to authenticate requests to your resolver API by including it in the Authorization header of your HTTP requests. For example, you can use the following curl command to retrieve the list of Handshake names from your resolver:
   ```
   curl -u <your API key>: http://localhost:8080/api/names
   ```
The -u option specifies the user name and password (separated by a colon) to use for authentication. In this case, the user name is your API key, and the password is empty.
   
## To generate a UUID or hash, you can use Python's built-in uuid and hashlib modules;
# Generate a UUID   
   ``` 
    import uuid

    api_key = str(uuid.uuid4())
    print(api_key)
  ```
This will generate a unique API key using the uuid4() method from the uuid module.

# Generate a SHA-256 hash in Python:
  ```
   import hashlib

   api_key = hashlib.sha256(b'MY_SECRET_KEY').hexdigest()
   print(api_key)
 ```
This will generate a SHA-256 hash of the string 'MY_SECRET_KEY' using the sha256() method from the hashlib module. You can replace 'MY_SECRET_KEY' with any string of your choice to generate a different hash.

## another example of registering a Handshake sld.tld/
 ``` 
  hs-client --prefix ~/.hsd name --register generateimg.innerigpt
 ```
 This will register the generateimg.innerigpt domain with the Handshake network, using the ~/.hsd directory as the data directory for the Handshake node. Note that you will need to have a Handshake node running and configured to use the ~/.hsd directory for this to work.
 
 Once you have registered your domain, you can use it as the hostname for your resolver, and you can configure your DNS settings to point your domain to the IP address of your resolver.
   
