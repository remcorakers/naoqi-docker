# This example is fetched from the IBM Cloud docs on IBM Watson Assistant
# For more information: https://console.bluemix.net/docs/services/conversation/develop-app.html#building-a-client-application

import watson_developer_cloud  # The library used to connect to IBM Watson assistant. Install it using PIP.
import time

# Set up Conversation service.
conversation = watson_developer_cloud.ConversationV1(
  username = 'USERNAME',  # Replace with username from service key
  password = 'PASSWORD',  # Replace with password from service key
  version = '2017-05-26'
)
workspace_id = 'WORKSPACE'  # Replace with workspace ID

# Initialize with empty value to start the conversation.
user_input = ''
context = {}
current_action = ''

# Main input/output loop
while current_action != 'end_conversation':

  # Send message to Conversation service.
  response = conversation.message(
    workspace_id = workspace_id,
    input = {
      'text': user_input
    },
    context = context
  )

  # Print the output from dialog, if any.
  if response['output']['text']:
    print(response['output']['text'][0])

  # Update the stored context with the latest received from the dialog.
  context = response['context']
  # Check for action flags sent by the dialog.
  if 'action' in response['output']:
    current_action = response['output']['action']
  # User asked what time it is, so we output the local system time.
  if current_action == 'display_time':
    print('The current time is ' + time.strftime('%I:%M:%S %p'))
  # If we're not done, prompt for next round of input.
  if current_action != 'end_conversation':
    user_input = input('>> ')
