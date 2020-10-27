# -*- coding: utf-8 -*-

from odoo import fields, models


class Estacion(models.Model):
    _name = 'estacion.estacion' # exaflow_documento
    _description = 'Estacion'
    _order = 'name asc'
    name = fields.Char(string='Nombre Finca', required=True, size=150)
    serial = fields.Char(string='Serial', required=True, size=150)
    latitud = fields.Char(string='Latitud', required=True, size=150)
    longitud = fields.Char(string='Longitud', required=True, size=150)
    fecha_instalacion = fields.Date(string='Fecha Instalacion', required=True)
    cliente_id = fields.Many2one('estacion.clientes', 'Cliente', required=True)
    _sql_constraints = {('cobrador_uniq', 'unique(serial)', 'El serial debe ser unico')}