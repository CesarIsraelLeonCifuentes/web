/** @odoo-module **/
import {RemainingDaysField} from "@web/views/fields/remaining_days/remaining_days_field";
import { patch } from "@web/core/utils/patch";

patch(RemainingDaysField.prototype, 'custom_remaining_days_field', {
    get diffString() {
        //The widget is removed for the following models
        var models_to_skip_widget = [
            'mrp.production',
        ];
        if (models_to_skip_widget.includes(this.props.record.resModel)) {
            return this.formattedValue;
        }
        return this._super(...arguments);
    }
 });