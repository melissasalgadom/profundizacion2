# -*- coding: utf-8 -*-
{
    'name': 'Estacion metereologica',
    'version': '12.0.1.0.1',
    'summary': 'Módulo para la creacion de una estacion metereologica',
    'category': 'Cobros',
    'author': 'JWLM',
    'maintainer': 'JWLM',
    'company': 'Universidad de Manizales',
    'website': 'https://www.umanizales.edu.co',
    'depends': [],
    'data': [
        # 'views/gotagota_prestamo_view.xml',
        'security/estacion_security.xml',
        'security/ir.model.access.csv',
        'views/estacion_clientes_view.xml',
        'views/estacion_estacion_view.xml',
        'views/estacion_eventos_view.xml',
        'views/estacion_menu.xml',

        #'views/product_label.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
