from fpdf import FPDF
import webbrowser

fileNameBase = "test10"


def get_file_content():
    text = ""
    with open('test.txt', "r", encoding="utf-8") as f:
        for line in f:
            text += line
    return text


def add_image(image_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(image_path)
    pdf.set_font("Arial", size=12)
    pdf.ln(85)  # move 85 down
    pdf.cell(200, 10, txt="{}".format(image_path), ln=1)
    pdf.output(fileNameBase + "2.pdf", "F")


class PDF(FPDF):

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        pdf.set_font('dejavu-mono', '', 11)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="R")


# Instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.add_font("dejavu-mono", style="", fname="font/DejaVuSansMono.ttf")
pdf.set_font('dejavu-mono', '', 10)
add_image("rivt01.png")
text = get_file_content()
pdf.multi_cell(w=210, h=6, txt=text, border=0, align='L', fill=False)
pdf.output(fileNameBase + ".pdf", "F")
