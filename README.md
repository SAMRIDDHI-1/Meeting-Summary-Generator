# Meeting-Summary-Generator


📋 Meeting Summary Generator
A Streamlit-based web app that uses the T5 Transformer model to generate concise summaries from meeting transcripts. The app supports both pasted text and CSV/TXT file uploads for summarization.

🚀 Features
📄 Paste meeting transcripts directly.

📁 Upload .csv (with a transcript column) or .txt files.

🧠 Summarize using Hugging Face's t5-small model.

🧾 Preview and generate summaries for multiple entries.

📦 Dependencies
  Python ≥ 3.7
  
  Streamlit
  
  pandas
  
  torch
  
  transformers

Install with:

pip install -r requirements.txt

🛠️ How to Run

streamlit run app.py

🖼️ Interface Overview
Paste transcript – enter long meeting text and get summarized.

Upload CSV/TXT – bulk process transcripts from files.

📁 Example
Sample usage:

Copy code
transcript: "Today we discussed the quarterly goals..."
summary: "Team discussed quarterly objectives and plans."


📑 File Structure

├── app.py                    # Streamlit app
├── test_df.csv               # Test data (optional)
├── validation_df.csv         # Validation data (optional)
├── Meeting Summary Generator.ipynb  # Notebook version (optional)

📌 Notes
CSV files must have a column named 'transcript'.

Summarization is limited to first 5 entries for performance.
