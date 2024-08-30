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

healthcare-assistant/ │ ├── src/ │ ├── app.py # Main application file │ ├── model.py # Model and RAG implementation │ └── vector_store/ # Directory containing vector database files │ ├── frontend/ │ ├── index.html # HTML file for the user interface │ ├── styles.css # CSS file for styling the user interface │ └── script.js # JavaScript file for client-side functionality │ └── README.md # Project documentation
