$(function() {

    $("#placeholder").bind("plotclick", function (event, pos, item) {
        alert(item.datapoint + ' ' + item.series.label);
        submit_form();
    });

    var submit_form = function() {

        $.getJSON($SCRIPT_ROOT + '/_search_cr_api', {
            keyword_1: keyword_1_value,
            keyword_2: keyword_2_value,
            date_low: date_low_value,
            date_high: date_high_value,

        }, function( data ) {
            for (var a in data.keywords) {
                for (var b in data.keywords[a].results) {
                    alert(data.keywords[a].results[b].title);
                }
            }
        });

    };

});
