var FaceletDirective = function () {

    // Directive object
    var directive = { };

    // Setting properties (template and model)
    directive.templateUrl = 'views/partials/facelet.html';
    directive.scope = {
        colors: '=colors',
        values: '=values'
    };

    return directive;
};
