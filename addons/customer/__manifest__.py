# Copyright 2016-2017 LasLabs Inc.
# Copyright 2017-2018 Tecnativa - Jairo Llopis
# Copyright 2018-2019 Tecnativa - Alexandre Díaz
# Copyright 2021 ITerra - Sergey Shebanin
# Copyright 2023 Onestein - Anjeel Haria
# Copyright 2023 Taras Shabaranskyi
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Master Customer",
    "summary": "Comprehensive management of customer data, including contact details, segmentation, and integration with other modules.",
    "version": "17.0.1.0.1",
    "category": "Sales",
    "website": "https://github.com/OCA/web",
    "author": "LasLabs, Tecnativa, ITerra, Onestein, "
    "Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "installable": True,
    "depends": ["web", "mail"],
    "development_status": "Production/Stable",
    "maintainers": ["Yajo", "Tardo", "SplashS"],
    "excludes": ["web_enterprise"],
    "data": 
    [
        "security/ir.model.access.csv",
        "views/customer_menu.xml",
    ],
    "assets": {
    },
    "sequence": 1,
    "application": True,

}
