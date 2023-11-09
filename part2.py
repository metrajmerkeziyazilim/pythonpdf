# ilgili kütüphaneden FPDF modülünün import edilmesi
from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # logo
        self.image("2023-10-08_23-14-35.png", 10, 8, 25)
        self.image("2023-10-08_23-14-35.png", 170, 8, 25)

        self.set_font("helvetica", "B", 20)

        self.cell(80)

        self.cell(30, 10, "Title", border=True, ln=1, align="C")

        self.ln(20)

    def footer(self):
        self.set_y(-15)

        self.set_font("helvetica", "I", 10)

        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


# FPDF Modülünden ölçülerin ve sayfa boyutunun tanımlanması
pdf = PDF("P", "mm", "A4")

# get total pages numbers

pdf.alias_nb_pages()

# set auto page break

pdf.set_auto_page_break(
    auto=True, margin=15
)  # sayfanın alt kısmından kaç mm yukarıda başlayacağını ayarlıyor.


#  FPDF Modülünden yeni sayfa eklenmesi
pdf.add_page()

# yazı fontunun ayarlanması
pdf.set_font("courier", "", 14)

# bir döngü ile 1-41 arası satırların oluşturulması
for i in range(1, 41):
    pdf.cell(10, 10, f"Bu Döngünün {i}. Satiridir.", ln=True)


pdf.output("pythonpdf_part2.pdf")
