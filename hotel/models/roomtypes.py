# -*- coding: utf-8 -*-

from odoo import models, fields

class RoomTypes(models.Model):
    _name = 'hotel.roomtypes'
    _description = 'Hotel Room Types Master List'
    _order = "name"

    name = fields.Char(string="Room Type Name")
    description = fields.Char(string="Room Type Description")
    imageroom = fields.Image(string="Room")
    imagebathroom = fields.Image(string="Bathroom")
    dailycharges_ids = fields.One2many('hotel.dailycharges', 'roomtype_id', string='Daily Charges')
    room_ids = fields.One2many('hotel.rooms', 'roomtype_id', string='Rooms')


class DailyCharges(models.Model):
    _name = 'hotel.dailycharges'
    _description = 'Hotel Room Type Daily Charges List'

    charge_id = fields.Many2one('hotel.charges', string="Charge Title")
    amount = fields.Float(string="Daily Amount", digits=(10, 2), help="Amount charged per day")
    roomtype_id = fields.Many2one('hotel.roomtypes', string="Room Type")
    
