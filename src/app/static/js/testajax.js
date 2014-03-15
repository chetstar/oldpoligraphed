  $(function() {
    var submit_form = function(e) {
      var dates = [];
      var more_dates = [];
      $.getJSON($SCRIPT_ROOT + '/_search_api', {
        a: $('input[name="a"]').val(),
        b: $('input[name="b"]').val()
      }, function(data) {

        $("#result").empty();

        for (var a in data.keywords) {
          for (var b in data.keywords[a].results) {
            $('#result').append("<li>" + a + " said " +
            data.keywords[a].results[b].count +
            " times by politicians on " +
            data.keywords[a].results[b].day +"</li>");
            if (a === "0") {
              dates.push([data.keywords[a].results[b].day, data.keywords[a].results[b].count]);
            } else {
              more_dates.push([data.keywords[a].results[b].day, data.keywords[a].results[b].count]);
            }
          }
        }
            $("#keyword").text($('input[name="a"]').val() + " vs. " + $('input[name="b"]').val());

            $.plot($("#placeholder"), [dates, more_dates], {xaxis: {
                mode: "time",
                timeformat: "%d"
            }}
          );
        $('#result').text(data.user);
        $('input[name=a]').focus().select();
      });
      return false;
    };

    $('a#calculate').bind('click', submit_form);

    $('input[type=text]').bind('keydown', function(e) {
      if (e.keyCode == 13) {
        submit_form(e);
      }
    });

    $(window).resize(submit_form);

    $('input[name=a]').focus();


  });
