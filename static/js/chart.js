let url = "http://www.simteiva.fr/api/v1/data/"



function get_temperature_data(url) {
    fetch(url)
    .then(response => response.json())
    .then(function(data) {
        let chart_data = {"labels": [],
        "series": [[]]
        }
      for (var i in data) {
        console.log(new Date(data[i]["timestamp"]))
        chart_data["series"][0].push({x: new Date(data[i]["timestamp"]), y: data[i]["measure"]})
      }

      let mainChart = new Chartist.Line('#chart1', chart_data, {
        showPoint: false,
        fullWidth: true,
        axisX: {
          type: Chartist.FixedScaleAxis,
          divisor: 6,
          labelInterpolationFnc: function(value) {
            return moment(value).format('DD/MM HH:mm:ss');
          }
              },
    })
  });}



get_temperature_data(url);








