import re

# Clean the text output
def clean_text(text_list):
    # Filter out empty lines
    cleaned_lines = [line for line in text_list if line.strip()]

    # Remove markdown formatting (**bold**)
    cleaned_lines = [re.sub(r'\*\*(.*?)\*\*', r'\1', line) for line in cleaned_lines]

    # Format the list items for better readability
    cleaned_lines = [line.replace("1. ", "\n1. ").replace("2. ", "\n2. ").replace("3. ", "\n3. ").replace("4. ", "\n4. ") for line in cleaned_lines]

    return cleaned_lines