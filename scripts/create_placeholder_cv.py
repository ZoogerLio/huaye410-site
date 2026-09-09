from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


OUTPUT = Path(__file__).resolve().parents[1] / "public" / "cv" / "cv.pdf"


def build_cv() -> None:
    styles = getSampleStyleSheet()
    ink = HexColor("#3A3A3A")
    muted = HexColor("#60656A")
    accent = HexColor("#9A6A28")

    name = ParagraphStyle(
        "Name", parent=styles["Title"], fontName="Helvetica-Bold",
        fontSize=25, leading=29, textColor=ink, spaceAfter=5,
    )
    role = ParagraphStyle(
        "Role", parent=styles["Normal"], fontName="Helvetica",
        fontSize=10.5, leading=15, textColor=muted, spaceAfter=18,
    )
    heading = ParagraphStyle(
        "Heading", parent=styles["Heading2"], fontName="Helvetica-Bold",
        fontSize=12, leading=15, textColor=accent, spaceBefore=11,
        spaceAfter=7, uppercase=True,
    )
    item = ParagraphStyle(
        "Item", parent=styles["Normal"], fontName="Helvetica",
        fontSize=9.5, leading=14, textColor=muted, spaceAfter=7,
    )

    doc = SimpleDocTemplate(
        str(OUTPUT), pagesize=A4,
        leftMargin=24 * mm, rightMargin=24 * mm,
        topMargin=22 * mm, bottomMargin=20 * mm,
        title="Your Name - Curriculum Vitae",
        author="Your Name",
    )

    story = [
        Paragraph("Your Name", name),
        Paragraph(
            "Doctoral Researcher in Human-Centered Computing | Example University<br/>"
            "your.name@example.edu | Hong Kong",
            role,
        ),
        Paragraph("Research Interests", heading),
        Paragraph(
            "Human-centered AI; responsible technology; computational social science; "
            "data visualization.", item,
        ),
        Paragraph("Education", heading),
        Paragraph(
            "<b>PhD in Information Studies</b>, Example University, 2023-present<br/>"
            "Research focus: human-centered and responsible artificial intelligence.", item,
        ),
        Paragraph(
            "<b>MSc in Computational Social Science</b>, Metropolitan Institute of Technology, "
            "2021-2023", item,
        ),
        Paragraph("Selected Publications", heading),
        Paragraph(
            "Your Name, Maya Chen, and Daniel Ortiz. \"Adaptive Explanations for Human-AI "
            "Decision Making.\" ACM CHI, 2026.", item,
        ),
        Paragraph(
            "Your Name and Priya Raman. \"Public-Interest AI: Institutional Practices for "
            "Accountable Deployment.\" Journal of Responsible Technology, 2025.", item,
        ),
        Paragraph(
            "Jordan Lee, Your Name, and Amara Wilson. \"Visualizing Uncertainty in Community "
            "Data Platforms.\" IEEE VIS, 2025.", item,
        ),
        Paragraph("Research Experience", heading),
        Paragraph(
            "<b>Research Associate</b>, Center for Public-Interest Technology, 2022-2023<br/>"
            "Supported mixed-method research and public-facing data projects.", item,
        ),
        Paragraph(
            "<b>Visiting Researcher</b>, Digital Society Lab, Summer 2024", item,
        ),
        Spacer(1, 8),
        Paragraph(
            "This is placeholder content. Replace public/cv/cv.pdf with your own PDF when ready.",
            ParagraphStyle("Note", parent=item, fontSize=8.5, textColor=HexColor("#8A8D90")),
        ),
    ]
    doc.build(story)


if __name__ == "__main__":
    build_cv()
