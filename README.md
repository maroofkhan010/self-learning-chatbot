# Self-Learning Chatbot Using Python

## About the Project
A simple Python-based interactive chatbot that answers user queries, including technical abbreviations and their full forms. It allows users to teach new responses when the chatbot does not know an answer.

## Features
- Answers predefined questions and technical abbreviations.
- Asks users to teach it when an answer is unavailable.
- Stores newly learned questions and answers in a JSON file.
- Retrieves previously learned responses in future interactions.
- Maintains learned data even after restarting the program.

## Technologies Used
- Python
- JSON
- File Handling

## Project Files
- `chatbot_version0.2.py` – Chatbot implementation.
- `full_forms01.json` – Stores questions and their answers.
- `chatbot_version01` – Additional project file.

## How It Works
1. User enters a question.
2. Chatbot checks whether the answer is available.
3. If the answer is unknown, it asks the user to teach it.
4. The new response is saved in the JSON file.
5. The chatbot can retrieve that response in future sessions.

## Author
Maroof Khan
