# Cloning Export/Import Chatbot

## Part 1: 

### Setting up Dialogflow

Visit the [Dialogflow console](https://dialogflow.cloud.google.com/) to set up the agent. Remember, you need to have a google account to be able to login.

![dialogflow console](https://cloud-9x2pb85rb.vercel.app/screenshot7.png)

Upload the all intents json files to Dialogflow in the "Intent" folder.

## Part 2: 

### Setting up a webhook webserver

Deploy all the files in "Chatbot" folder to Heroku.

## Part 3: 

### Enable webhook fulfilment in Dialogflow

![dialogflow fulfilment](https://task3.yukcheong.ml/wp-content/uploads/2021/07/DialogflowFulfilmet.png)

Place the link of the heroku app in the fulfilment section with "/webhook" behind.

## Part 4: 

### Enable webhook call for "Import/Export Requirements" intent.

![intent fulfilment](https://task3.yukcheong.ml/wp-content/uploads/2021/07/IntentFulfilment.png)

Toggle "Enable webhook call for this intent" under fulfilment section.
