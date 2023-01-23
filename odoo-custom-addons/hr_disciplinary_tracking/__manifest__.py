{
    'name': 'Enter Price Open HRMS Disciplinary Tracking',
    'version': '15.0.1.0.1',
    'summary': """Employee Disciplinary Tracking Management""",
    'live_test_url': 'https://youtu.be/LFuw2iY4Deg',
    'author': 'Cybrosys Techno solutions,Open HRMS',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'category': 'Generic Modules/Human Resources',
    'website': "https://www.openhrms.com",
    'depends': ['base', 'mail', ],
    'data': ['views/disciplinary_action.xml',
             'views/disciplinary_sequence.xml',
             'views/category_view.xml',
             'security/ir.model.access.csv',
             'security/security.xml'],
    'demo': ['data/demo_data.xml'],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}