function addRow() {
    var markup = '<input type="url" class="form-control" placeholder="Add image URL" name="imageURL"><br>';
    $('#imageForm').find("table tbody tr td").append(markup);
}

function submitImageForm() {
    var data = [];
    $("input[name*='imageURL']").each(function () {
        var url = $(this).val();
        if (url) {
            data.push(url);
        }
    });
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.post(API_URL + 'dashboard/', {data: JSON.stringify(data), csrfmiddlewaretoken: csrf})
        .done(function (response) {
            cleanFormData('imageForm');
        });
}