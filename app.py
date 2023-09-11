from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from flask import Flask, request, render_template, send_file
from datetime import date
from reportlab.lib.enums import TA_RIGHT

app = Flask(__name__)

month_names = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}

date_today = date.today()
time = date_today.strftime("%d-%m-%Y")
day = date_today.strftime("%d")
month = date_today.strftime("%m")
months = month_names.get(month)

namesdict = {
    'Akanksh M': ['URK22DS1003', 'Akanksh M', 'Angelina Residence'],
    'Nidhin Paul': ['URK22CS1094', 'Nidhin Paul', 'Hepzibah Residence'],
    'Steeve P P': ['URK22C02024', 'Steeve P P', 'Angelina Residence'],
    'Benjamin George': ['URK22CS1141', 'Benjamin George', 'Hepzibah Residence'],
    'Shalom Mathew': ['URK22CS7026', 'Shalom Mathew', 'Hepzibah Residence'],
    'Christine': ['URK22CS1205', 'Christine', 'Hepzibah Residence'],
    'Chris Joseph George': ['URK22CS5118', 'Chris Joseph George', 'Hepzibah Residence'],
    'Stephen Thomas': ['URK22CS1110', 'Stephen Thomas', 'Hepzibah Residence'],
    'Aldrin G': ['URK22EC1019', 'Aldrin G', 'Hepzibah Residence'],
    'Evalt D': ['URK22CS1200', 'Evalt D', 'Angelina Residence'],
    'Anish Ramesh': ['URK21EC3008', 'Anish Ramesh', 'Bobraj Residence'],
    'Reuben Reny': ['URK21CS1024', 'Reuben Reny', 'Jerry Manuel Residence'],
    'Ishan Chaskar': ['URK21CS1181', 'Ishan Chaskar', 'Jerry Manuel Residence'],
    'Paul Isiah': ['URK21CS1153', 'Paul Isiah', 'Jerry Manuel Residence'],
    'Kevin Jojo': ['URK21CS7004', 'Kevin Jojo', 'Jerry Manuel Residence'],
    'Melvin Sajith': ['URK22CS5021', 'Melvin Sajith', 'Hepzibah Residence'],
    'Gifton Paul Immanuel': ['URK21CS5054', 'Gifton Paul Immanuel', 'Jerry Manuel Residence'],
    'Razeek': ['URK20CS2081', 'Razeek', 'Johnson Victor Residence'],
    'Fabine Bobby': ['URK22CS5035', 'Fabine Bobby', 'Hepzibah Residence']
    
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    selected_names = request.form.getlist('names')

    # Generate PDF
    pdf_filename = f'permission_request_boys_{time}.pdf'
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    elements = []

    # Add permission request letter content
    styles = getSampleStyleSheet()
    content = []

    # Add the date
    # content.append(Paragraph(f"Date: {time}", styles['Normal'],alignment=TA_RIGHT))
    # content.append(Spacer(1, 12))
    date_line = f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Date: {time}"
    date_paragraph = Paragraph(date_line, styles['Normal'])
    date_paragraph.alignment = TA_RIGHT  # Set right alignment for the paragraph
    content.append(date_paragraph)
    content.append(Spacer(1, 12))
    
    # Add the sender information
    content.append(Paragraph(f"From: ", styles['Normal']))
    content.append(Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;Head CTC", styles['Normal']))
    content.append(Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;Karunya Institute of Technology and Sciences", styles['Normal']))
    content.append(Spacer(1, 12))  # Add space

    # Add the recipient information
    content.append(Paragraph(f"To:", styles['Normal']))
    content.append(Paragraph(f"&nbsp;&nbsp;&nbsp;&nbsp;The Chief Warden (Boys Hostel)", styles['Normal']))
    content.append(Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;Karunya Institute of Technology and Sciences,", styles['Normal']))
    content.append(Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;Coimbatore-641114.", styles['Normal']))
    content.append(Spacer(1, 12))  # Add space

    # Add the subject
    content.append(Paragraph("Subject:,", styles['Normal']))
    content.append(Paragraph("&nbsp;&nbsp;&nbsp;&nbsp; Permission for late residence entry", styles['Normal']))
    content.append(Spacer(1, 12)) 
    

    # Add the salutation
    content.append(Paragraph("Respected Madam,", styles['Normal']))
    content.append(Spacer(1, 12))  # Add space

    # Add the main content
    content.append(Paragraph(f"The following students were working late at CTC on {day} {months} 2023 from 8:30 PM to 11 PM.", styles['Normal']))
    content.append(Paragraph("Kindly permit them to enter the hostel.", styles['Normal']))
    content.append(Spacer(1, 12))  # Add space

    # Create a table header
    header = ['Register Number', 'Name', 'Residence']
    table_data = [header]

    for name in selected_names:
        if name in namesdict:
            data = namesdict[name]
            table_data.append(data)

    # Create a table style without colors
    table_style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align for all cells
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header bottom padding
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),  # Table grid
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),  # Data font
        ('FONTSIZE', (0, 0), (-1, 0), 10),  # Header font size
        ('FONTSIZE', (0, 1), (-1, -1), 10),  # Data font size
        ('TOPPADDING', (0, 0), (-1, -1), 5),  # Top padding for all cells
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Bottom padding for all cells
    ])

    # Create the table and apply the table style
    table = Table(table_data)
    table.setStyle(table_style)

    # Add content and table to the document
    content.append(table)
    content.append(Spacer(1, 12))  # Add space
    content.append(Paragraph("Thank You.", styles['Normal']))
    content.append(Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HEAD(CTC)", styles['Normal']))

    elements.extend(content)

    doc.build(elements)

    return send_file(pdf_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
