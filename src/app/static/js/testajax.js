  $(function() {
    var submit_form = function(e) {
      $.getJSON($SCRIPT_ROOT + '/_search_api', {
        a: $('input[name="a"]').val(),
        // b: $('input[name="b"]').val()
      }, function(data) {
        $("#result").empty();
        for (var i in data.results) {
          $('#result').append("<li>Was said " +
            data.results[i].count +
            " times by politicians on " +
            data.results[i].day +"</li>");
        }
        $("#keyword").text("The keyword " + $('input[name="a"]').val());
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

    $('input[name=a]').focus();
  });
