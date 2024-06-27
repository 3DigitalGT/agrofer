odoo.define("dimona_customizations.models", function (require) {
    "use strict";

    var models = require("point_of_sale.models");
    var core = require("web.core");

    models.load_fields("res.company", ["legal_name"]);
    models.load_fields("pos.config", ["pos_address_complete"]);
    let _super_order = models.Order.prototype;

    models.Order = models.Order.extend({
        export_for_printing: function () {
            let self = this;
            let company_legal_name = this.pos.company.legal_name || '';
            let pos_address_complete = this.pos.config.pos_address_complete || '';
            let receipt = _super_order.export_for_printing.apply(this, arguments);
            receipt = _.extend(receipt, {
                'company_legal_name': company_legal_name,
                'pos_address_complete': pos_address_complete,
            });
            return receipt;
        }
    });

});
