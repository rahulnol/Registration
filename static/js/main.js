function showLoadingState(elementId)
{
    $('#' + elementId).find('.loaded-state').addClass('element-hide');
    $('#' + elementId).find('.loading-state').removeClass('element-hide');
}

function showLoadedState(elementId)
{
    $('#' + elementId).find('.loaded-state').removeClass('element-hide');
    $('#' + elementId).find('.loading-state').addClass('element-hide');
}

function cleanFormData(elementId) {
    $('#' + elementId).find("input, textarea").each(function () {
        $(this).val('');
    })
}

API_URL = 'http://localhost:8000/'