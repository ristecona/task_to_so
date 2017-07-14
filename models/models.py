# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import logging
from odoo.exceptions import UserError
_logger = logging.getLogger(__name__)

class nebiz_task_to_so(models.Model):
    
    _inherit = 'project.task'

    @api.multi
    def convert_to_so(self):
    	self.ensure_one()
    	so_data = {}
    	if self.partner_id:
    		so_data['partner_id'] = self.partner_id.id 
    	else:
    		raise UserError(_('No Partner set on the TASK'))
    	product = self.env['product.product'].search([('default_code', '=', '123456789')])
    	if not product:
    		product = self.env['product.product'].create({'name' : "Programming Hours",'type' : 'service', 'default_code' : '123456789'})

    	new_order = self.env['sale.order'].create(so_data)

    	_logger.info("SALE ORDER HAS BEEN CREATED %s" %new_order.id)
    	for t in self.timesheet_ids:
    		_logger.info("TIME NAME : %s" %t.name)
    		sol = self.env['sale.order.line'].create({'order_id' : new_order.id,'product_id' : product.id, 'product_uom_qty' : t.unit_amount, 'name' : t.name})
    	base_url   =  self.env['ir.config_parameter'].sudo().get_param('web.base.url')
    	self.message_post(body="This task has been billed at: " '%s/web#id=%s&amp;view_type=form&amp;model=sale.order' % (base_url, new_order.id))

#http://localhost.odoo10/web#id=16&view_type=form&model=sale.order&action=263&menu_id=88

    	return True
