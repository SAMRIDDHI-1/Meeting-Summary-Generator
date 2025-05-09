import streamlit as st
import pandas as pd
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

# Load the model and tokenizer
@st.cache_resource
def load_model():
    tokenizer = T5Tokenizer.from_pretrained("t5-small")
    model = T5ForConditionalGeneration.from_pretrained("t5-small")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    return tokenizer, model, device

tokenizer, model, device = load_model()

# Summarize function
def summarize_text(text, max_len=128):
    input_ids = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True).to(device)
    summary_ids = model.generate(input_ids, max_length=max_len, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Streamlit UI
st.title("📋 Meeting Summary Generator")

option = st.radio("Choose input method:", ("📝 Paste transcript", "📁 Upload CSV/TXT file"))

if option == "📝 Paste transcript":
    user_input = st.text_area("Paste your meeting transcript below:", height=300)
    if st.button("Generate Summary"):
        if user_input.strip():
            with st.spinner("Generating summary..."):
                summary = summarize_text(user_input)
            st.success("Summary:")
            st.write(summary)
        else:
            st.warning("Please enter some text.")

elif option == "📁 Upload CSV/TXT file":
    uploaded_file = st.file_uploader("Upload .csv or .txt file", type=['csv', 'txt'])
    if uploaded_file:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
            if 'transcript' not in df.columns:
                st.error("CSV must contain a 'transcript' column.")
            else:
                st.write("🧾 Preview of Uploaded Transcripts:")
                st.dataframe(df.head())

                if st.button("Generate Summaries for First 5 Entries"):
                    summaries = []
                    for i, row in df.head(5).iterrows():
                        summary = summarize_text(row['transcript'])
                        summaries.append(summary)

                    df_summary = df.head(5).copy()
                    df_summary['Generated Summary'] = summaries
                    st.write("✅ Generated Summaries:")
                    st.dataframe(df_summary[['transcript', 'Generated Summary']])
        else:  # .txt file
            text = uploaded_file.read().decode('utf-8')
            if st.button("Generate Summary from TXT"):
                summary = summarize_text(text)
                st.success("Summary:")
                st.write(summary)
