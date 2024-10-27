from odoo import models, fields, api, _

class ClinicPatient(models.Model):
    _name = 'clinic.patient'
    _description = 'Clinic Patient'

    partner_id = fields.Many2one('res.partner', string='Related Partner', ondelete='cascade')

    name = fields.Char(related='partner_id.name', store=True, readonly=False)


    # Basic Information
    date_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')

    # Contact Information
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')

    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict', domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    country_code = fields.Char(related='country_id.code', string="Country Code")

    # Medical Information
    medical_history = fields.Text(string='Medical History')
    allergies = fields.Text(string='Allergies')
    medications = fields.Text(string='Current Medications')

    # Dental Information
    last_dental_visit = fields.Date(string='Last Dental Visit')
    preferred_dentist = fields.Many2one('res.users', string='Preferred Dentist')
    dental_notes = fields.Text(string='Dental Notes')

    # Status and Other Details
    active = fields.Boolean(string='Active', default=True)
    photo = fields.Binary(string='Photo')
    emergency_contact = fields.Char(string='Emergency Contact')
    emergency_phone = fields.Char(string='Emergency Phone')

    medical_history_ids = fields.One2many('clinic.medical.history', 'patient_id', string='Medical History')


    @api.model
    def create(self, vals):
        if 'partner_id' not in vals:
            partner_vals = {
                'name': vals.get('name', 'Unnamed Patient'),
                'is_company': False,
            }
            partner = self.env['res.partner'].create(partner_vals)
            vals['partner_id'] = partner.id
        return super(ClinicPatient, self).create(vals)



from odoo import models, fields, api

class ClinicMedicalHistory(models.Model):
    _name = 'clinic.medical.history'
    _description = 'Medical History'

    patient_id = fields.Many2one('clinic.patient', string='Patient', required=True, ondelete='cascade')
    appointment_date = fields.Datetime(string='Appointment Date', required=True)
    medical_condition = fields.Text(string='Medical Condition')
    treatment_given = fields.Text(string='Treatment Given')
    medications_prescribed = fields.Text(string='Medications Prescribed')
    notes = fields.Text(string='Notes')
    appointment_id = fields.Many2one(comodel_name='clinic.appointment', string='')
    

    @api.model
    def create_history_entry(self, patient_id, appointment_date, medical_condition, treatment_given, medications_prescribed, notes):
        """Create a new medical history record for a patient."""
        self.create({
            'patient_id': patient_id,
            'appointment_date': appointment_date,
            'medical_condition': medical_condition,
            'treatment_given': treatment_given,
            'medications_prescribed': medications_prescribed,
            'notes': notes,
        })

    