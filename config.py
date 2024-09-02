import os, time, re
id_pattern = re.compile(r'^.\d+$')



class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "23578854")
    API_HASH  = os.environ.get("API_HASH", "3257596471c6d08212b3c0a47cc815ea")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7255149716:AAEuWpRWIy9uETfiuyyYVZgNTPrLILOFXS4") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","cluster0")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://zoey611870:5ErfLUWPKH44hkqK@cluster0.7doyqob.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://telegra.ph/file/ed13414eb379f31aae9bc.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1302933634').split()]

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "Nameless_Botz") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002177962671"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """Hello {} 👋 

➻ This Is An Advanced And Yet Powerful Rename Bot.

➻ Using This Bot You Can Rename And Change Thumbnail Of Your Files.

➻ You Can Also Convert Video To File And File To Video.

➻ This Bot Also Supports Custom Thumbnail And Custom Caption.

<b>Bot Is Owned By :</b> @Nameless_Being"""

    ABOUT_TXT = """
╭───────────────⍟
├<b>🤖 My Name</b> : {}
├<b>🖥️ Developer</b> : <a href=https://t.me/Nameless_Botz>Nameless Botz</a> 
├<b>👨‍💻 Real Programer</b> : <a href=https://t.me/MadflixOfficials>Jishu Developer</a>
├<b>📕 Library</b> : <a href=https://github.com/pyrogram>Pyrogram</a>
├<b>✏️ Language</b> : <a href=https://www.python.org>Python 3</a>
├<b>💾 Database</b> : <a href=https://cloud.mongodb.com>Mongo DB</a>
├<b>📊 Build Version</b> : <a href=https://instagram.com/jishu.editz>Rename v4.5.0</a></b>     
╰───────────────⍟
"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

✏️ <b><u>How To Rename A File</u></b>

➪ Send Any File And Type New File Name And Select The Format [ Document, Video, Audio ].           

𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/Nameless_being>Bot Owner</a>
"""

    PROGRESS_BAR = """\n
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>🛍 UPI ID:</b> `628706468@axl`
"""


    SEND_METADATA = """<b><u>🖼️  HOW TO SET CUSTOM METADATA</u></b>

For Example :-

<code>-map 0 -c:s copy -c:a copy -c:v copy -metadata title="Encoded By :- @Nameless_Botz" -metadata author="@Namesless_being" -metadata:s:s title="Subtitled By :- @Nameless_Botz" -metadata:s:a title="By :- @Nameless_Botz" -metadata:s:v title="Encoded By :- @Nameless_Botz"</code>

💬 For Any Help Contact @Nameless_being
"""








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper
