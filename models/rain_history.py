from odoo import fields,models

class Rainhistory(models.Model):
    _name = "rain.history"
    _description = "contains historical data of rain"

    id = fields.Char("unique id",required=True)
    date = fields.Datetime("rain measurement date",required=True)
    rainQuantity = fields.Integer("rain measurment in mm",required=True)