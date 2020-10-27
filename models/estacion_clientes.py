# -*- coding: utf-8 -*-

from odoo import fields, models


class Clientes(models.Model):
    _name = 'estacion.clientes' # exaflow_documento
    _description = 'Clientes'
    _order = 'name asc'
    name = fields.Char(string='Nombre cliente', required=True, size=150)
    tipodocumento = fields.Selection(
    [('1','Cedula de ciudadania'),
     ('2', 'NIT'),
     ('3', 'Cedula de extranjeria'),
     ('4', 'Pasaporte'),
    ], string='Tipo de Documento', required=True, index=True, track_visibility='onchange', track_sequence=3, default="1")
    documento = fields.Char(string='Serial', required=True, size=150)
    correo_electronico = fields.Char(string='Correo electronico', required=True, size=150)
    fecha_nacimiento = fields.Date(string='Fecha Nacimiento', required=True)
    _sql_constraints = {('cobrador_uniq', 'unique(documento)', 'El numero de documento debe ser unico')}
