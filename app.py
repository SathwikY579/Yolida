import streamlit as st
from database import create_tables, get_session, Document, User, QueryHistory
from document_processor import extract_text
from security import encrypt_data, decrypt_data
from sqlalchemy.orm import sessionmaker

# Create tables if not exist
create_tables()

def upload_document(session, file):
    content = extract_text(file)
    encrypted_content = encrypt_data(content)
    document = Document(filename=file.name, content=encrypted_content)
    session.add(document)
    session.commit()
    st.success(f"Document '{file.name}' uploaded successfully.")

def handle_query(session, query):
    results = []
    documents = session.query(Document).all()
    for doc in documents:
        decrypted_content = decrypt_data(doc.content)
        if query.lower() in decrypted_content.lower():
            results.append((doc.filename, decrypted_content))
    
    return results

def save_query_history(session, user_id, query, response):
    history = QueryHistory(user_id=user_id, query=query, response=response)
    session.add(history)
    session.commit()

def download_history(session, user_id):
    history = session.query(QueryHistory).filter(QueryHistory.user_id == user_id).all()
    history_text = "\n".join([f"Query: {h.query}\nResponse: {h.response}" for h in history])
    
    st.download_button("Download History", history_text, file_name="history.txt")

def main():
    st.title("Document Query Application")

    session = get_session()

    menu = ["Upload Document", "Query Documents", "View History"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Upload Document":
        st.subheader("Upload Document")
        file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"])
        if file is not None:
            upload_document(session, file)

    elif choice == "Query Documents":
        st.subheader("Query Documents")
        query = st.text_input("Enter your query")
        if st.button("Search"):
            results = handle_query(session, query)
            if results:
                for filename, content in results:
                    st.write(f"**{filename}**")
                    st.write(content)
                    save_query_history(session, user_id=1, query=query, response=content)  # Replace with actual user ID
            else:
                st.write("No matching documents found.")

    elif choice == "View History":
        st.subheader("View and Download History")
        download_history(session, user_id=1)  # Replace with actual user ID

if __name__ == '__main__':
    main()
