# -*- coding: utf-8 -*-

from odoo import fields, models, api
import json
import requests
import logging

_logger = logging.getLogger(__name__)

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
    blacklist = fields.Boolean(string="Encender", default=False)

    @api.onchange('blacklist')
    def onchange_blacklist(self):
        _logger.info('Entro al blacklist')
        if self.blacklist == True:
            dato = 1
        else:
            dato = 0

        headers = {
            'Authorization': 'Basic b2RvbzoxNjQzMTU2OTUzNTE2ODQ1MzUxNjg0NTY4NA==',
            'Content-Type': 'application/json'
        }
        #data = {'enable': dato}
        url = 'https://home.juxn3.com:8100'
        #datajson = json.dumps(data)
        #_logger.info(datajson)
        payload = {"enable": dato}
        datajson = json.dumps(payload)
        _logger.info(payload)
        #response = requests.request("POST", url, headers=headers, data=datajson)
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        _logger.info(response)


