import PyPDF2
import os

class PdfMerger:

    def __init__(self):
        self.show_merger()
        self.show_files = []

    
    @staticmethod
    def show_merger():
        print("\n===== PDF MERGER =====")
        print("PDF files ke names do (comma se alag).")
        print("Example: mydoc.pdf, report.pdf, appendix.pdf")
    
    

    def merge_file(self):

        files = input("\nEnter the files name (example : example.pdf)").split(',')
        files = [f.strip() for f in files]

        existing = [f for f in files if os.path.exists(f)]
        missing = [f for f in files if not os.path.exists(f)]

        if missing:
            print(f"⚠️ Files not found: {missing}")
        if not existing:
            print("No valid PDF files to merge.")
            return

        output_file_name = input("\n Enter output file name (example : merge.pdf)")
        if not output_file_name.endswith('.pdf'):
            output_file_name =+ '.pdf'


        try:
            
            merger = PyPDF2.PdfFileManger()
            for f in existing:
                merge.append(f)
                print(f"➕ Added: {pdf}")

                merger.writer(output_file_name)
                merger.close()
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    pdfmerge = PdfMerger()
    pdfmerge.merge_file()


