import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import tkinter as tk
from tkinter import scrolledtext
import warnings
warnings.filterwarnings('ignore')

# Load and process your dataset
data = pd.read_csv("dailogs2.csv", encoding='ISO-8859-1')

vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(data['Input'])
y = data['Output']

# Train the Logistic Regression model
model = LogisticRegression()
model.fit(x, y)


# Function to get chatbot response
def chatbot_response(user_input):
    user_input_vec = vectorizer.transform([user_input])
    score = cosine_similarity(user_input_vec, x)
    closest_match = score.argmax()
    return data['Output'][closest_match]


# Function to handle sending a message
def send_message():
    user_input = user_input_entry.get()

    if user_input.strip() == "":
        return

    # Display user input in the chat window
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, "You: " + user_input + "\n", 'user')

    # Get chatbot response and display it
    response = chatbot_response(user_input)
    chat_display.insert(tk.END, "Bot: " + response + "\n", 'bot')
    chat_display.config(state=tk.DISABLED)
    chat_display.yview(tk.END)

    # Clear the input field
    user_input_entry.delete(0, tk.END)



root = tk.Tk()
root.title("ChatBot")
root.geometry("340x440")
root.configure(bg='#333333')


chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, bg="#ffffff", fg="#000000",
                                         font=("Arial", 12))
chat_display.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

#to add colours
chat_display.tag_config('user', foreground='#FF3399', font=("Arial", 12, 'bold'))
chat_display.tag_config('bot', foreground='#00C851', font=("Arial", 12, 'italic'))


input_frame = tk.Frame(root, bg='#333333')
input_frame.pack(padx=10, pady=10, fill=tk.X)

user_input_entry = tk.Entry(input_frame, width=50, font=("Arial", 12), bd=2, relief=tk.RAISED)
user_input_entry.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

#send button
send_button = tk.Button(input_frame, text="Send", command=send_message, bg="#FF3399", fg="#ffffff",
                        font=("Arial", 12, 'bold'), bd=2, relief=tk.RAISED)
send_button.pack(side=tk.RIGHT, padx=5, pady=5)


user_input_entry.bind("<Return>", lambda event: send_message())

root.mainloop()
