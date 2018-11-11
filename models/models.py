# -*- coding: utf-8 -*-

from odoo import models, fields, api


class training(models.Model):
    _name = 'training.training'

    name = fields.Char()
    color = fields.Integer()
    employee_id = fields.Many2one(comodel_name="res.users")
    task_ids = fields.One2many(comodel_name="training.task", inverse_name="training_id")

