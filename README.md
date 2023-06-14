![image](https://github.com/DaeSikWoo/LLM-chat-system/assets/35883117/c2d91600-ac8f-4739-ab58-e764f35c926f)# LLM-chat-system

This is a code to implement a chat system based on LLM (Language Model) using the localGPT model developed by PromptEngineer (https://github.com/PromtEngineer/localGPT). The original code has been modified to include a conversational interface accessible through port 5000. Cribl solution documentation manual in PDF format has been loaded in the SOURCE_DOCUMENT to provide the necessary data.

### Note
The chat system is built using the vicuna-7B language model and the Flask framework. The system is currently configured to use CPU due to the environment, but it can be modified to utilize GPU if desired. Please refer to the original code repository at https://github.com/PromtEngineer/localGPT if any additional settings are required and for further instructions.

# Prerequisite

Ensure that all the required dependencies are installed before running the app.

```
pip install -r requirements.txt
```

# Running the app

Execute the app.py file to run the application. The application will be hosted on port 5000 by default but can be modified according to the specific working environment.

```
python app.py
```

# Interface

The system's user interface is displayed below. You can enter different queries to receive responses from the system.

![image](https://github.com/DaeSikWoo/LLM-chat-system/assets/35883117/ed65c0c5-d397-4a40-b380-7ebec77606e1)
![image](https://github.com/DaeSikWoo/LLM-chat-system/assets/35883117/3070e5ba-0eb7-404c-b1c3-751d14a2b6ed)

To interact with the system, simply enter your query or message in the chat input field. Each query will generate a response from the system. Feel free to ask various questions or provide different inputs to engage with the system and receive relevant responses.
