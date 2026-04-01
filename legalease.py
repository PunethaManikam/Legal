
   

import PyPDF2

# List of common legal risk words
risk_words = ["penalty", "liability", "breach", "obligation", "indemnity", "termination", "fine"]

# Function to read PDF file
def read_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text()
    return text

# Function to summarize text (simple method)
def summarize_text(text):
    sentences = text.split(".")
    summary = ".".join(sentences[:3])
    return summary

# Function to find risk words
def find_risks(text):
    found = []
    for word in risk_words:
        if word.lower() in text.lower():
            found.append(word)
    return list(set(found))

# Main program
file_path = input("Enter the path of your legal document (PDF or TXT): ")

# Read file
if file_path.lower().endswith(".pdf"):
    content = read_pdf(file_path)

elif file_path.lower().endswith(".txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

else:
    print("Only PDF or TXT files are supported!")
    exit()

# Generate output
summary = summarize_text(content)
risks = find_risks(content)

print("\n--- Plain-Language Summary ---")
print(summary)

print("\n--- Legal Risk Flags ---")
if risks:
    for r in risks:
        print("-", r)
else:
    print("No obvious risk words found.")
