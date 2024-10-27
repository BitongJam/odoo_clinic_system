from odoo import models, fields, api

class ClinicAppointment(models.Model):
    _name = 'clinic.appointment'
    _description = 'Clinic Appointment'

    name = fields.Char(string='Appointment Reference', required=True, copy=False, readonly=True, default='New')
    patient_id = fields.Many2one('clinic.patient', string='Patient', required=True)
    appointment_date = fields.Datetime(string='Appointment Date', required=True)
    doctor_id = fields.Many2one('res.partner', string='Doctor')
    status = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    ], string='Status', default='scheduled')
    notes = fields.Text(string='Notes')
    medical_history_ids = fields.One2many('clinic.medical.history', 'appointment_id', string='Medical History')
    appointment_type = fields.Selection([
        ('consultation', 'Consultation'),
        ('follow_up', 'Follow-up'),
        ('emergency', 'Emergency'),
    ], string='Appointment Type')
    duration = fields.Float(string='Duration (Hours)')
    invoice_id = fields.Many2one('account.move', string='Invoice')
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('clinic.appointment') or 'New'
        return super(ClinicAppointment, self).create(vals)
