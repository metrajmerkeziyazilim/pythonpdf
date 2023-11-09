from fpdf import FPDF


# Create FPDF Object
# Layout ("P","L")
# Unit ("mm","cm","in")
# format ("A3","A4" (Default), "A5","Letter","Legal",(100,150))
pdf = FPDF("P", "mm", "A4")

# Add a page
pdf.add_page()

# specify font
# fonts("times","courier","helvetica","symbol","zpfdingbats")
# "B" (BOLD), "U" (UNDERLINE),"I" (ITALIC),"" (REGULAR), Combination (i.e., ("BU"))


pdf.set_font("courier", "", 14)


# Add text
# w=width
# h=height

# pdf.cell(W, H, "Hello World", ln=1)
pdf.cell(120, 100, "Hello World", ln=1, border=True)
pdf.cell(80, 10, "Goodbye World")

pdf.output("pythonpdf_part1.pdf")
