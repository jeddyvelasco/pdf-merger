import os
import customtkinter as ctk
from tkinterdnd2 import TkinterDnD, DND_FILES
from pypdf import PdfWriter

# Set appearance mode and color theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class PDFMergerApp(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()

        self.title("PDF Merger")
        self.geometry("500x450")
        self.resizable(False, False)

        self.pdf_files = []

        # --- UI Components ---
        self.title_label = ctk.CTkLabel(
            self, 
            text="PDF Merger", 
            font=ctk.CTkFont(size=22, weight="bold")
        )
        self.title_label.pack(pady=(20, 10))

        # Drop Zone Frame
        self.drop_frame = ctk.CTkFrame(self, width=440, height=180, corner_radius=10)
        self.drop_frame.pack(pady=10, padx=20)
        self.drop_frame.pack_propagate(False)

        self.drop_label = ctk.CTkLabel(
            self.drop_frame, 
            text="Drag & Drop PDF files here\n\n(or click 'Add PDFs')", 
            font=ctk.CTkFont(size=14)
        )
        self.drop_label.place(relx=0.5, rely=0.5, anchor="center")

        # Enable Drag and Drop on the frame directly
        self.drop_frame.drop_target_register(DND_FILES)
        self.drop_frame.dnd_bind("<<Drop>>", self.handle_drop)

        # File List Status Label
        self.status_label = ctk.CTkLabel(
            self, 
            text="0 files selected", 
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        self.status_label.pack(pady=(5, 10))

        # Button Frame
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(pady=10)

        self.add_btn = ctk.CTkButton(
            self.btn_frame, 
            text="Add PDFs", 
            command=self.browse_files,
            width=120
        )
        self.add_btn.grid(row=0, column=0, padx=10)

        self.clear_btn = ctk.CTkButton(
            self.btn_frame, 
            text="Clear", 
            fg_color="#D9534F", 
            hover_color="#C9302C", 
            command=self.clear_files,
            width=100
        )
        self.clear_btn.grid(row=0, column=1, padx=10)

        # Merge Button
        self.merge_btn = ctk.CTkButton(
            self, 
            text="Merge & Save PDF", 
            font=ctk.CTkFont(size=15, weight="bold"),
            height=40,
            width=260,
            command=self.merge_pdfs
        )
        self.merge_btn.pack(pady=(15, 20))

    # --- Functions ---
    def add_pdf(self, file_path):
        """Helper to add PDF path if valid."""
        clean_path = file_path.strip("{}")  # Remove TkinterDnD curly braces
        if clean_path.lower().endswith(".pdf") and clean_path not in self.pdf_files:
            self.pdf_files.append(clean_path)

    def handle_drop(self, event):
        """Processes dropped files."""
        files = self.splitlist(event.data)
        for f in files:
            self.add_pdf(f)
        self.update_status()

    def browse_files(self):
        """File dialog selector fallback."""
        files = ctk.filedialog.askopenfilenames(
            title="Select PDF Files", 
            filetypes=[("PDF Files", "*.pdf")]
        )
        if files:
            for f in files:
                self.add_pdf(f)
            self.update_status()

    def clear_files(self):
        """Resets selected file list."""
        self.pdf_files.clear()
        self.update_status()

    def update_status(self):
        """Updates counter label text."""
        count = len(self.pdf_files)
        if count == 0:
            self.status_label.configure(text="0 files selected", text_color="gray")
        else:
            self.status_label.configure(
                text=f"{count} PDF file(s) ready to merge", 
                text_color="#2ECC71"
            )

    def merge_pdfs(self):
        """Merges PDFs and prompts location to save output."""
        if not self.pdf_files:
            self.status_label.configure(text="Please add PDFs first!", text_color="#E74C3C")
            return

        save_path = ctk.filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF File", "*.pdf")],
            title="Save Merged PDF As"
        )

        if save_path:
            try:
                merger = PdfWriter()
                for pdf in self.pdf_files:
                    merger.append(pdf)
                merger.write(save_path)
                merger.close()

                self.status_label.configure(
                    text="Successfully saved merged PDF!", 
                    text_color="#2ECC71"
                )
            except Exception as e:
                self.status_label.configure(
                    text=f"Error: {str(e)}", 
                    text_color="#E74C3C"
                )


if __name__ == "__main__":
    app = PDFMergerApp()
    app.mainloop()