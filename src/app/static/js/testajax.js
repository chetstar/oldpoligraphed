$(function() {

    var date_value_input = function(input, days_back) {
        var now = new Date();
        now.setDate(now.getDate() - days_back);
        var day = ("0" + now.getDate()).slice(-2);
        var month = ("0" + (now.getMonth() + 1)).slice(-2);
        var today = now.getFullYear()+"-"+(month)+"-"+(day) ;
        input.val(today);
    };

    var submit_form = function(e) {
      var dates = [];
      var more_dates = [];

      //Set timeformat based on granularity
      if ($('select[name="granularity"]').val() == 'Day'){
        timeformat = "%m/%d";
      } else if($('select[name="granularity"]').val() == 'Month'){
        timeformat = "%m/%y";
      } else if($('select[name="granularity"]').val() == 'Year'){
        timeformat = "%y";
      }

      $('.hidden-container').show();

      $.getJSON($SCRIPT_ROOT + '/_search_api', {

        keyword_1: $('input[name="keyword_1"]').val(),
        keyword_2: $('input[name="keyword_2"]').val(),
        date_low: $('input[name="date_low"]').val(),
        date_high: $('input[name="date_high"]').val(),
        granularity: $('select[name="granularity"]').val()

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
            $("#keyword").text($('input[name="keyword_1"]').val() + " vs. " + $('input[name="keyword_2"]').val());

            $.plot($("#placeholder"),
              [ { label: $('input[name="keyword_1"]').val(), data: dates },
                { label: $('input[name="keyword_2"]').val(), data: more_dates }
              ],
              { xaxis: {
                  mode: "time",
                  timeformat: timeformat
                },
                lines: {
                  show: true
                },
                points: {
                  show: true
                },
              grid: {
                hoverable: true,
                clickable: true
              },
              legend: {
                  show: true,
                  // labelFormatter: null or (fn: string, series object -> string)
                  // labelBoxBorderColor: #000,
                  // noColumns: number
                  position: "ne",
                  // margin: number of pixels or [x margin, y margin]
                  backgroundColor: "white",
                  backgroundOpacity: .5
                  // container: null or jQuery object/DOM element/jQuery expression
                  // sorted: null/false, true, "ascending", "descending", "reverse", or a comparator
              }
            }
          );

        $('.hidden-container').hide();
        $('#result').text(data.user);
        $('input[name=a]').focus().select();
      });
      return false;
    };

    $('#calculate').bind('click', submit_form);

    $('input[type=text]').bind('keydown', function(e) {
      if (e.keyCode == 13) {
        submit_form(e);
      }
    });

    $(window).resize(submit_form);

    $('input[name=a]').focus();

    $.plot($("#placeholder"), [[0,0]]);

   date_value_input($('#date_low'), 30);
   date_value_input($('#date_high'), 0);

  });
