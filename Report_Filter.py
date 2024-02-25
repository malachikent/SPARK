import os
import pdfplumber

def ensure_pdf_files(input_folder):
    pdf_files = []
    other_files = []

    # Iterate through files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            pdf_files.append(filename)
        else:
            print(f"Skipping non-PDF file: {filename}")
            continue

    return pdf_files, other_files

if __name__ == "__main__":
    input_folder = "C:\\Users\\Malachi\\OneDrive\\Desktop\\PHD\\SPRING_2024\\Machine_Learing\\SPARK\\lab_reports"

    # Ensure that the folder exists
    if os.path.exists(input_folder):
        pdf_files, other_files = ensure_pdf_files(input_folder)
    else:
        print(f"The folder '{input_folder}' does not exist.")

    # Ensure that the folder exists
    if os.path.exists(input_folder):
        pdf_files, other_files = ensure_pdf_files(input_folder)
        
        if len(other_files) == 0:
            print("All files in 'lab_reports' folder are PDF files.")
        else:
            print("The following files in 'lab_reports' folder are not PDF files:")
            for filename in other_files:
                print(filename)
    else:
        print(f"The folder '{input_folder}' does not exist.")

def extract_discussion(pdf_path):
    discussions = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                # Example logic to find discussion section, adjust as needed
                discussion_start = text.find("Discussion")
                if discussion_start != -1:
                    discussion = text[discussion_start:]
                    discussions.append(discussion)
    except Exception as e:
        print(f"Error processing PDF file '{pdf_path}': {e}")
    return discussions

def append_to_discussion_file(discussion_list, output_file):
    with open(output_file, "a") as f:
        for i, discussion in enumerate(discussion_list):
            f.write(f"Discussion {i+1}:\n\n")
            f.write(discussion)
            f.write("\n\n")

def main(input_folder, output_file):
    # Collect discussion sections from each PDF
    discussions = []
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            filepath = os.path.join(input_folder, filename)
            discussions.extend(extract_discussion(filepath))

    # Write discussion sections to a single file
    append_to_discussion_file(discussions, output_file)

if __name__ == "__main__":
    input_folder = "C:\\Users\\Malachi\\OneDrive\\Desktop\\PHD\\SPRING_2024\\Machine_Learing\\SPARK\\lab_reports"
    output_file = "Discussion.txt"
    main(input_folder, output_file)

