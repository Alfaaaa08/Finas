class FinancialPlanning {
    static onChangeCategoryField() {
        const category_field = $('#category-field');

        const category = (category_field.val()).trim();
        
        if(!category) {
            return alert('Insert a category');
        }

        this.addNewCategory(category);
    }

    static addNewCategory(category) {
        
    }
}