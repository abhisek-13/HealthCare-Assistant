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
   git clone https://github.com/abhisek-13/Healthcare-Assistant.git
   cd healthcare-assistant
   ```
2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application**:

   ```bash
   python app.py
   ```

## Usage
- Enter your health-related query into the search bar on the webpage.
- The assistant will first check the vector database for relevant information.
- If no information is found in the database, it will perform an internet search to provide an answer.
- Note: This assistant is for primary health suggestions only. For serious health concerns, please consult a professional doctor.

## Limitations
- This is a prototype and may not always provide accurate or up-to-date medical information.
- It should not be used as a substitute for professional medical advice, diagnosis, or treatment.

## Future Improvements
- Enhancing the accuracy and relevance of information retrieval from the vector database.
- Improving the natural language understanding capabilities of the assistant.
- Adding support for more comprehensive health databases.

## Contributing
- Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

## License
- This project is licensed under the MIT License - see the LICENSE file for details.
   
