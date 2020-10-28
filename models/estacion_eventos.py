# -*- coding: utf-8 -*-

from odoo import fields, models


class Estacion(models.Model):
    _name = 'estacion.eventos' # exaflow_documento
    _description = 'Eventos'
    _order = 'name asc'
    name = fields.Char(string='Nombre evento', required=True, size=150)
    pluviosidad = fields.Char(string='Pluviosidad', required=True, size=150)
    sensor1 = fields.Char(string='Sensor 1', required=True, size=150)
    sensor2 = fields.Char(string='Sensor 2', required=True, size=150)
    fecha_creacion = fields.Date(string='Fecha Creacion', required=True)
    estacion_id = fields.Many2one('estacion.estacion', 'Estacion', required=True)
   #_sql_constraints = {('cobrador_uniq', 'unique(documento)', 'El numero de documento debe ser unico')}