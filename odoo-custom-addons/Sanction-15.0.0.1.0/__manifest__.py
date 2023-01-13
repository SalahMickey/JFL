-*- coding: utf-8 -*-
##############################################################################
#    Copyright (C) 2020 AtharvERP (<http://atharverp.com/>). All Rights Reserved
# Odoo Proprietary License v1.0
#
# This software and associated files (the "Software") may only be used (executed,
# modified, executed after modifications) if you have purchased a valid license
# from the authors, typically via Odoo Apps, atharverp.com or you have written agreement from
# author of this software owner.
#
# You may develop Odoo modules that use the Software as a library (typically
# by depending on it, importing it and using its resources), but without copying
# any source code or material from the Software. You may distribute those
# modules under the license of your choice, provided that this license is
# compatible with the terms of the Odoo Proprietary License (For example:
# LGPL, MIT, or proprietary licenses similar to this one).
#
# It is forbidden to publish, distribute, sublicense, or sell copies of the Software
# or modified copies of the Software.
#
# The above copyright notice and this permission notice must be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
##############################################################################
{
    'name': 'Sanction',
    'summary': """Manage employee's sanctions""",
    'version': '15.0.0.1.0',
    'category': 'hr',
    'author': 'Twisted Business solution',

    'website': 'http://www.twisted-sd.com',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/sanction.xml',
        'views/employee.xml',

    ],
    'license': 'AGPL-3',
    'application': True,
    'installable': True,
    'auto_install': False,
    'price': 'free',
}