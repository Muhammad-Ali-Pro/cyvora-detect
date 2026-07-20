from datetime import datetime
import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
)

from backend.app.config import (
    APP_NAME,
    APP_VERSION,
    REPORT_TITLE,
    REPORT_FOOTER,
    LOGO_PATH,
)


def section_heading(title, styles):
    return Paragraph(
        f"<b>{title}</b>",
        styles["Heading2"],
    )



def generate_pdf_report(report_data, output_path):

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER

    heading_style = styles["Heading2"]

    normal = styles["BodyText"]

    doc = SimpleDocTemplate(
        output_path,
        leftMargin=40,
        rightMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    elements = []

    rule = report_data["rule"]
    validation = report_data["validation"]
    score = report_data["score"]
    mitre = report_data["mitre"]
    review = report_data["review"]

    generated_date = datetime.now().strftime(
        "%d %B %Y %H:%M"
    )

    

    
    # =====================================================
    # Logo
    # =====================================================

    if os.path.exists(LOGO_PATH):

        logo = Image(
            LOGO_PATH,
            width=0.85 * inch,
            height=0.85 * inch,
        )

        logo.hAlign = "CENTER"

        elements.append(logo)

        elements.append(
            Spacer(1, 0.15 * inch)
        )

    # =====================================================
    # Title
    # =====================================================

    elements.append(
        Paragraph(
            APP_NAME.upper(),
            title_style,
        )
    )

    elements.append(
        Paragraph(
            REPORT_TITLE,
            heading_style,
        )
    )

    elements.append(
        Spacer(1, 0.20 * inch)
    )

    elements.append(
        Paragraph(
            f"<b>Generated:</b> {generated_date}",
            normal,
        )
    )

    elements.append(
        Spacer(1, 0.35 * inch)
    )


    # =====================================================
    # Executive Summary
    # =====================================================

    elements.append(
        section_heading("Executive Summary", styles)
    )

    if validation["valid"]:
        validation_status = "VALID"
    else:
        validation_status = "INVALID"

    production_ready = (
        "YES"
        if review["quality"]["score"] >= 80
        else "NO"
    )

    summary = f"""
This Sigma rule was analysed using
<b>{APP_NAME}</b>.

<br/><br/>

Validation Status:
<b>{validation_status}</b>

<br/>

Production Ready:
<b>{production_ready}</b>

<br/>

Overall Grade:
<b>{review['quality']['grade']}</b>
"""
    elements.append(
        Paragraph(summary, normal)
    )

    elements.append(Spacer(1, 0.30 * inch))

    # =====================================================
    # Rule Information
    # =====================================================

    elements.append(
        section_heading("Rule Information", styles)
    )

    rule_table = Table(
        [
            ["Title", rule.get("title", "-")],
            ["Platform", rule.get("product", "-")],
            ["MITRE Technique", mitre.get("technique", "-")],
            ["MITRE Name", mitre.get("name", "-")],
            ["MITRE Tactic", mitre.get("tactic", "-")],
        ],
        colWidths=[150, 300],
    )

    rule_table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
                ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )

    elements.append(rule_table)

    elements.append(Spacer(1, 0.30 * inch))

    # =====================================================
    # Risk Assessment
    # =====================================================

    elements.append(
        section_heading("Risk Assessment", styles)
    )

    risk_table = Table(
        [
            ["Risk Score", str(score["risk"])],
            ["Severity", score["severity"]],
        ],
        colWidths=[150, 300],
    )

    risk_table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )

    elements.append(risk_table)

    elements.append(Spacer(1, 0.35 * inch))

    # ===== Part 2 continues below =====

        # =====================================================
    # Quality Assessment
    # =====================================================

    elements.append(
        section_heading("Quality Assessment", styles)
    )

    quality_table = Table(
        [
            ["Quality Score", f"{review['quality']['score']}/100"],
            ["Grade", review["quality"]["grade"]],
            ["Review Status", review["status"]],
        ],
        colWidths=[150, 300],
    )

    quality_table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )

    elements.append(quality_table)

    elements.append(Spacer(1, 0.30 * inch))

    # =====================================================
    # Strengths
    # =====================================================

    elements.append(
        section_heading("Strengths", styles)
    )

    if review["strengths"]:
        for item in review["strengths"]:
            elements.append(
                Paragraph(f"✓ {item}", normal)
            )
    else:
        elements.append(
            Paragraph("No strengths identified.", normal)
        )

    elements.append(Spacer(1, 0.25 * inch))

    # =====================================================
    # Missing Fields
    # =====================================================

    elements.append(
        section_heading("Missing Fields", styles)
    )

    if review["missing"]:
        for item in review["missing"]:
            elements.append(
                Paragraph(f"✗ {item}", normal)
            )
    else:
        elements.append(
            Paragraph("No missing fields.", normal)
        )

    elements.append(Spacer(1, 0.25 * inch))

    # =====================================================
    # Recommendations
    # =====================================================

    elements.append(
        section_heading("Recommendations", styles)
    )

    recommendation_data = [["Field", "Recommendation"]]

    for rec in review["recommendations"]:
        recommendation_data.append(
            [
                rec["field"],
                rec["recommendation"],
            ]
        )

    recommendation_table = Table(
        recommendation_data,
        colWidths=[120, 330],
    )

    recommendation_table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ]
        )
    )

    elements.append(recommendation_table)

    elements.append(Spacer(1, 0.40 * inch))

    # =====================================================
    # Footer
    # =====================================================

    footer = f"""
<b>Generated by {APP_NAME} v{APP_VERSION}</b>

<br/><br/>

{REPORT_FOOTER}

<br/><br/>

This report is intended to assist security analysts
in reviewing Sigma detection rules and identifying
opportunities for improvement before deployment.
"""

    elements.append(
        Paragraph(footer, normal)
    )

    # =====================================================
    # Build PDF
    # =====================================================

    doc.build(elements)