# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PosConfigInherited(models.Model):
    _inherit = "pos.config"

    pos_address_complete = fields.Char(compute='_compute_complete_address', store=True)

    @api.depends('street', 'county_id', 'state_id')
    def _compute_complete_address(self):
        for record in self:
            record.pos_address_complete = ''
            if record.street:
                record.pos_address_complete += record.street + ', '
            if record.county_id:
                record.pos_address_complete += record.county_id.name + ', '
            if record.state_id:
                record.pos_address_complete += record.state_id.name
            record.pos_address_complete = record.pos_address_complete.strip().strip(',')