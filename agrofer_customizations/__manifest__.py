# -*- coding: utf-8 -*-
{
    'name': 'Personalizaciones Agrofer',
    'summary': """
        Personalizaciones generales y Acceso a la información de los costos del producto en vistas.
    """,
    'description': "Personalizaciones generales y Acceso a la información de los costos del producto en vistas",
    'version': '15.0.0.1',
    'category': 'Customizations',
    'complexity': 'easy',
    'author': 'Proyectos Agiles, S.A. - Inteligos',
    'company': 'Proyectos Agiles, S.A. - Inteligos',
    'maintainer': 'Proyectos Agiles, S.A. - Inteligos',
    'depends': ['base', 'sale', 'product', 'pos_inteligos_fel'],
    'data': [
        'security/groups.xml',
        'views/product_views.xml',
        'views/sale_order_form_inherited.xml'
    ],
    "assets": {
        'point_of_sale.assets': [
            'agrofer_customizations/static/src/js/*.js',
        ],
        'web.assets_qweb': [
            'agrofer_customizations/static/src/xml/**/*',
        ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False
}
