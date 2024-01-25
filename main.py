from config import LICENCE_KEY
from ironpdf import License as License
from ironpdf import *


License.LicenseKey = LICENCE_KEY


renderer = ChromePdfRenderer()
 
# Create a PDF from a HTML string using Python
pdf = renderer.RenderHtmlAsPdf("<h1>Hello World</h1>")
 
# Export to a file or Stream
pdf.SaveAs("output1.pdf")

# myAdvancedPdf = renderer.RenderHtmlAsPdf("<img src='icons/iron.png'>", r"C:\site\assets")
# myAdvancedPdf.SaveAs("html-with-assets.pdf")