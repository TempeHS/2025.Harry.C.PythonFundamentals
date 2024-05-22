from fpdf import FPDF

pdf = FPDF()

with open("jharvard.pdf") as file:
    pdf.add_page()
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(40, 10, "Hello World!")
    pdf.output("jharvard.pdf")
