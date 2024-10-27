{
    'name': 'Clinic System',
    'version': '1.0',
    'description': '''
        A module for managing patients in a clinic, including patient records,
        appointments, billing, and medical history.
    ''',
    'summary': 'Manage clinic patients and appointments',
    'author': 'James Michael Ortiz',
    'license': 'LGPL-3',
    'category': 'Healthcare',
    'depends': [
        'base','contacts'
    ],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'data/appointment_seq.xml',
        'views/patient.xml',
        'views/appointment.xml',
        'views/doctor.xml'
    ],
    'auto_install': False,
    'application': True,
}