# Healthcare Assistant using Retrieval-Augmented Generation (RAG)

## Overview

This project is a prototype of a Healthcare Assistant using Retrieval-Augmented Generation (RAG). The assistant is designed to provide users with primary health suggestions based on their queries. It fetches relevant information stored in a vector database and, if necessary, searches the internet to provide answers in the style of a professional doctor. 

**Please note:** This assistant is a prototype and should not be relied upon for serious medical decisions. Always consult a doctor for severe cases.

## Features

- **Data Retrieval**: The assistant retrieves information from a pre-stored vector database for relevant answers.
- **Internet Search**: If an answer isn't found in the vector database, the assistant performs an internet search to provide information as a professional doctor.
- **Primary Health Suggestions**: Provides basic health information and suggestions based on user queries.
- **User-Friendly Interface**: Simple and intuitive interface for users to interact with the assistant.

## Project Structure
- Main application file: app.py
- Model file: model.py
- Vector Database for RAG: vectorstore.py
- Output text cleaning steps: preprocessing.py

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/healthcare-assistant.git
   cd healthcare-assistant
   ```
   
