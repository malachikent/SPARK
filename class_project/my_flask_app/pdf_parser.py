import pdfplumber

def parse_pdf_sections(pdf_path):
    # Dictionary to hold content of each section
    sections = {
        "Introduction": "",
        "Materials and Methods": "",
        "Results": "",
        "Calculations": "",
        "Discussion": "",
        "References": ""
    }

    # Keywords to identify sections
    keywords = list(sections.keys())

    # Variable to keep track of the current section
    current_section = None

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                for word in text.split():
                    # Check if the word is a section keyword
                    if word in keywords:
                        current_section = word
                    elif current_section:
                        # Append text to the current section
                        sections[current_section] += f"{word} "

    return sections

# Test the function (uncomment for testing)
#sections = parse_pdf_sections("/Users/devinfico/Desktop/SPARK/my_flask_app/sample_reports/ochem 2 lab report- experiment 6.pdf")
#print(sections)

