[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/TSrfnk?referralCode=ZTYsGf)


## Telegrambot-with-GPT4free
🤖 A Telegram bot powered by ChatGPT using the Aiogram API.       

ℹ️ Note: The Hugging Face token is only required for image captioning.      
      

✨ Features:           
  
- Supports OCR with Tesseract in addition to [salesforce blip image captioning.](https://huggingface.co/Salesforce/blip-image-captioning-large)
- Easy to translate to your own language with multi-language support.
- Internet access using  [duckduckgo_search.](https://github.com/deedy5/duckduckgo_search)
- Supports voice transcription with [speech_recognition](https://github.com/Uberi/speech_recognition)
- Image generation using Stability Diffusion and DALL-E.     
- Plugin support for DuckDuckGo search and news (under testing).    
        
       

## Installation Steps

### Linux    

Download or clone this repository  
Go to the directory

```
git clone https://github.com/noes14155/Telegrambot-with-GPT4free
cd Telegrambot-with-GPT4free
```


Copy example.env file to .env

```
cp example.env .env
```

Change environment variables in .env file [Environment Variables](#environment-variables)   

```
nano .env
```


Create virtual environment for this project/directory     

```
python3 -m venv venv
source venv/bin/activate
```


Install the requirements    
```
apt install -y flac ffmpeg tesseract-ocr
wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/script/Devanagari.traineddata -P /usr/share/tesseract-ocr/4.00/tessdata/script/
EXPORT TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata

pip install -r requirements.txt
```
Run the bot
```
python main.py
```

### Windows    

1. Download or clone this repository:    
```
git clone https://github.com/noes14155/Telegrambot-with-GPT4free
cd Telegrambot-with-GPT4free
```

2. Copy the example.env file to .env
3. Change the environment variables in the .env file using a text editor of your choice.

4. Create a virtual environment for this project/directory:

```
python -m venv venv
venv\Scripts\activate
```

5. Install the required dependencies:    
```
pip install -r requirements.txt
```
6. Install additional dependencies:

+ Install Tesseract OCR:
    - Install using single command 'choco install tesseract' or manually using the following steps.
    - Download the Windows installer from the  [Tesseract OCR GitHub page](https://github.com/UB-Mannheim/tesseract/wiki).
    - Run the installer and make sure to check download Additional script data option in the installation options.
    - Add the Tesseract installation directory to the system's PATH environment variable.
+ Install FFmpeg:
    - Install using single command 'choco install ffmpeg' or manually using the following steps.
    - Download the latest static build of FFmpeg for Windows from the  [official FFmpeg website](https://ffmpeg.org/download.html#build-windows) 
    - Extract the downloaded ZIP file to a location of your choice.
    - Add the FFmpeg bin directory to the system's PATH environment variable.
    
7. Run the bot:
```
python main.py
```

## Docker
Build (change environment variables before build)

Uncomment this section (If yu want to use gpt4free)
```bash
  g4f_server:
    container_name: g4f_server
    ports:
      - '1337:1337'
    environment:
      - PYTHONUNBUFFERED=1
    build:
      context: ./interference
      dockerfile: Dockerfile
    restart: always
```
Build containers
```bash
docker-compose up --build -d
```



## Environment Variables

To run this project, you will need to create a .env file or rename the existing example.env to .env and add the following environment variables   


- `BOT_TOKEN`
Get this by messaging @botfather Refer to [📖 Telegram Bot Tutorial](https://core.telegram.org/bots/tutorial#obtain-your-bot-token)

- `HG_TOKEN`
Optional(Required for image captioning). Sign up on hugging face and get the token from  [🔗 Hugging Face](https://huggingface.co/settings/tokens).      

- `HG_img2text`
Required for image captioning. If you wnat to use another model for image captioning. change it here.   
Default value HG_img2text = 'https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large'     

- `DEFAULT_LANG`
Change to your language default english. If you want to translate to your own language please do so in the language_files folder make your own language.yml file and add the language to languages.yml file.        

- `Plugins`
Enable or disable plugins. Default value True.    

- `BOT_OWNER_ID`
Add your userid from telegram. If empty DM enable or disable option will be disabled.     

- `GPT_KEY`
To use GPT4free GPT_KEY = '' (Only working in docker)
Key from the provider (including openai). Whichever api base you want use the key provided.
For Naga AI, Get this by messaging run the /key get command in th bot channel in [Naga AI Discord](https://discord.gg/JxRBXBhabu) , [Naga AI Telegram](https://t.me/chimer_ai)     

- `API_BASE`
To use GPT4free API_BASE = 'http://g4f_server:1337' (Only working in docker)
You can use any provider. I have included Naga AI api base. Use the key for the same.

- `MAX_HISTORY`
Number of conversation history to be sent with each request. Default value 10. Don't put more than 20.      

- `ENABLED_PLUGINS`
List of enabled plugins. Only wolfram is disabled by default. Add Worlframalpha api key before adding wolfram to this list.     

- `WOLFRAM_APP_ID`
Wolframalpha api key

- `DUCKDUCKGO_SAFESEARCH`
Valid values are 'safe', 'moderate', 'off'

- `WORLDTIME_DEFAULT_TIMEZONE`
Timezone should be in the format Asia/Dubai or Europe/Rome
      


      
🎉 You're all set! Enjoy using the Telegram bot with ChatGPT!        

## Contributors
<a href = "https://github.com/noes14155/Telegrambot-with-GPT4free/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo=noes14155/Telegrambot-with-GPT4free"/>
</a>
