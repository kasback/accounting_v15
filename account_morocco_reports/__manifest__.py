# pylint: disable=missing-docstring, manifest-required-author
{
    'name': "Account Morocco Reports",
    'summary': "Account Morocco Reports Updates",
    'author': "CORE B.P.O",
    'website': "http://www.core-bpo.com",
    'category': 'account',
    'version': '13.0.1.0.0',
    'license': 'OPL-1',
    'depends': [
        'account',
        'account_accountant',
        'account_reports',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/assets_group.xml',
        'views/equity_group.xml',
        'views/profit_group.xml',
        'views/loss_group.xml',
        'views/partner_share.xml',
        'views/account_account.xml',
        'views/menuitem.xml',
        'templates/morocco_template.xml',
        'report/account_report_assets.xml',
        'report/account_report_equity.xml',
        'report/account_report_profit.xml',
        'report/partner_share_report.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'account_morocco_reports/static/src/scss/account_reports.scss',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}
