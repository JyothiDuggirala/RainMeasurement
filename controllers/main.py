# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime
import logging
from odoo import http

_logger = logging.getLogger(__name__)


class RainRecorder(http.Controller):

    @http.route('/rain/measure/<int:height>', type='http', auth="public", website=True)
    def recordRain(self, height, **kwargs):
        _logger.info('saving rain measuerment')
        # assert height is not null, "Incorrect rating"
        obj = http.request.env['rain.measurement'].create({
            'date': datetime.now,
            'rainQuantity': height,
        })
        return obj
