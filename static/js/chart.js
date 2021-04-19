let url = "http://127.0.0.1:8000/api/v1/data/"



function get_temperature_data(url) {
    fetch(url)
    .then(response => response.json())
    .then(function(data) {
        let chart_data = {"labels": [],
        "series": [[]]
        }
      for (var i in data) {
        // chart_data["labels"].push(    {x: new Date(data[i]["timestamp"]), y: data[i]["measure"]}     )
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

// anim = mainChart.on('draw', function(data) {
//     if (data.type === 'line' || data.type === 'area') {
//         data.element.animate({
//             d: {
//                 begin: 1000 * data.index,
//                 dur: 1000,
//                 from: data.path.clone().scale(1, 0).translate(0, data.chartRect.height()).stringify(),
//                 to: data.path.clone().stringify(),
//                 easing: Chartist.Svg.Easing.easeOutQuint
//             }
//         });
//     }
// });


// let mainChart = new Chartist.Line('#chart1', {
    
//     labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
//     series: [
//         [1, 5, 2, 5, 4, 15],
//     ]
// }, {
//     low: 0,
//     showArea: true,
//     showPoint: false,
//     fullWidth: true
// });







