# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class Media(models.Model):
    _name = 'publisher.media'
    _order = 'name'

    name = fields.Char(string='Name', copy=False, index=True, required=True)

    format_needed = fields.Boolean(string="Format Needed", required=True)
    location_needed = fields.Boolean(string="Location Needed", required=True)
    color_needed = fields.Boolean(string="Color Needed", required=True)
    date_start_needed = fields.Boolean(string="Publication Date Needed", required=True)
    date_end_needed = fields.Boolean(string="End Date Needed", required=True)