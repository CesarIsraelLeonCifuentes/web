# -*- encoding:utf-8 -*-

{
    'name': 'Web Widget Remaining Days Disable',
    "version": "16.0.1.0.0",
    "category": "web",
    'description': '''
        Allows you to disable the remaining_days widget
    ''',
    'author': 'Trescloud, Odoo Community Association (OCA)',
    'maintainer': 'TRESCLOUD',
    "website": "https://github.com/OCA/web",
    'summary': 'The widget is removed for the specified models.',
    'license': 'OEEL-1',
    'depends': [
        'web',
    ],
    "assets": {
        "web.assets_backend": [
            "web_widget_remaining_days_disable/static/src/js/**/*",
        ],
    },
    'installable': True,
    'auto_install': False,
}
