import os
from slackclient import SlackClient

BOT_NAME = 'snnbot'

slack_token = os.environ["SLACK_BOT_TOKEN"]
#slack_token='xoxb-197158873254-ch2IZ1vIH16MpmQSbIMziP2f'
print("slack_token " + slack_token)
sc = SlackClient(slack_token)
sc.api_call("users.list")
# sc.api_call(
#   "chat.postMessage",
#   channel="#mmmc-test",
#   text="Hello from snnbot! :tada:"
# )

# sc.api_call(
#     "users.info"
#     )
# sc.api_call(
#   user="U1234567890",
# )
