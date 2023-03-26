import PyPDF2
import tkinter as tk
from tkinter import ttk, filedialog

def merge_pdf():
    # Ask user to select PDF files to merge
    pdFiles = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    
    # Create a PdfFileMerger object
    merger = PyPDF2.PdfFileMerger()

    # Append each selected PDF to the merger object
    for filename in pdFiles:
        with open(filename, 'rb') as pdfFile:
            merger.append(PyPDF2.PdfFileReader(pdfFile))

    # Merge the PDFs and save the output file
    with open('merged.pdf', 'wb') as outputFile:
        merger.write(outputFile)

if __name__ == '__main__':
    # Create the GUI window
    window = tk.Tk()
    window.title("PDF Merger")

    # Set window size and center on screen
    window_width = 500
    window_height = 200
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)
    window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")

    # Add a style to the window and widgets
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabel", font=("Arial", 14), foreground="#333333")
    style.configure("TButton", font=("Arial", 14), foreground="#ffffff", background="#4CAF50", relief="raised", bd=3)

    # Create a label to display instructions
    instructions_label = ttk.Label(window, text="Select the PDF files you want to merge")
    instructions_label.pack(pady=20)

    # Create a button to initiate the file selection and merging process
    merge_button = ttk.Button(window, text="Merge PDFs", command=merge_pdf)
    merge_button.pack(pady=10)

    # Start the GUI loop
    window.mainloop()   