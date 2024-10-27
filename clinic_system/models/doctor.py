from odoo import models, fields,api

class ClinicDoctor(models.Model):
    _name = 'clinic.doctor'
    _description = 'Clinic Doctor'

    partner_id = fields.Many2one('res.partner', string='Related Partner', ondelete='cascade')
    name = fields.Char(related='partner_id.name', store=True, readonly=False)
    license_number = fields.Char(string='License Number')
    specialization = fields.Char(string='Specialization')
    years_of_experience = fields.Integer(string='Years of Experience')
    availability = fields.Selection([
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
    ], string='Availability', default='full_time')


    
    @api.model
    def create(self, vals):
        if 'partner_id' not in vals:
            partner_vals = {
                'name': vals.get('name', 'Unnamed Doctor'),
                'is_company': False,
            }
            partner = self.env['res.partner'].create(partner_vals)
            vals['partner_id'] = partner.id
        return super(ClinicDoctor, self).create(vals)