
# CHATBOT APPLICATION

This is a simple chatbot application built with Python using Tkinter for the graphical user interface and scikit-learn for the machine learning model. The chatbot provides responses based on user input using a pre-trained Logistic Regression model and cosine similarity for response matching.



## Features

- Interactive Chat Interface
- Text Input and Response
- Simple GUI




## Requirements
- Python 3.x
- pandas
- scikit-learn
- tkinter

You can install the required libraries using pip:



```http
  pip install pandas scikit-learn
```
Note: Tkinter comes pre-installed with Python, so no additional installation is needed for it.





## Setup

1.Prepare the Dataset

Make sure you have the dataset file dailogs2.csv in the same directory as the script. The CSV file should contain two columns:

- Input: User input dialogues.
- Output: Corresponding chatbot responses.

2.Run the Application

Execute the script to launch the chatbot application:

```http
  python chatbot.py
```




## Usage

- Chatting with the Bot: Type your message in the input field and press Enter or click the "Send" button to receive a response from the chatbot.
- Ending the Chat: You can close the application window to exit the chatbot.
## Customization
- Dataset: Update dailogs2.csv with your own dialogues and responses to customize the chatbot's behavior.
- Appearance: Modify the Tkinter widget properties and colors in the code to customize the appearance of the chat window.
## Acknowledgements

 - Tkinter: For the graphical user interface.
- scikit-learn: For the machine learning model.

