import os
import time
from slackclient import SlackClient

BOT_NAME = 'snnbot'

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

if __name__ == "__main__":
    api_call = slack_client.api_call("users.list",presence=1,limit=1000)
    while True:
        if api_call.get("ok"):
            #get all users so we can find our bot
            users = api_call.get('members')
            for user in users:
                if 'name' in user and user.get('name') == BOT_NAME:
                    print("Bot ID for'" + user['name'] + "' is " + user.get('id'))
                    exit()
        else:
            print("could not find bot user with the name " + BOT_NAME)
            break
        Uid=user.get('id')
        print( Uid )
        time.sleep(3)
        api_call = slack_client.api_call("users.list",presence=1,limit=1000,offset=Uid)
