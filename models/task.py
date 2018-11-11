from odoo import models, fields, api
from odoo.exceptions import ValidationError


class task(models.Model):
    _name = 'training.task'
    _rec_name = 'name'

    name = fields.Char()
    duration = fields.Integer()
    training_id = fields.Many2one(comodel_name="training.training")
    parent_id = fields.Many2one(string="Depend on", comodel_name="training.task",
        domain="[('training_id', '=', training_id)]")
    state = fields.Selection(selection=[('draft', 'Draft'), ('in_progress', 'In progress'),('done','Done')])
    approved = fields.Boolean()
    color = fields.Integer()

    @api.multi
    @api.depends('parent_id')
    def create(self,vals):
        res=self.env['training.task'].search([('id', '=', vals['parent_id'])])
        if res.approved == False:
            print("task not approved")
            print(vals['state'])
            if vals['state'] == 'in_progress' or vals['state'] == 'done':
                raise ValidationError("sorry the parent task not approved")
        rec = super(task, self).create(vals)
        return True