document.addEventListener('DOMContentLoaded', function() {
  var trace1 = {
    x: JSON.parse(document.getElementById('dates').textContent),
    close: JSON.parse(document.getElementById('close').textContent),
    decreasing: { line: { color: '#D33F49' } },
    high: JSON.parse(document.getElementById('high').textContent),
    increasing: { line: { color: '#88D18A' } },
    line: { color: 'rgba(31,119,180,1)' },
    low: JSON.parse(document.getElementById('low').textContent),
    open: JSON.parse(document.getElementById('open').textContent),
    type: 'candlestick',
    xaxis: 'x',
    yaxis: 'y'
  }

  var data = [trace1]

  var layout = {
    dragmode: 'zoom',
    margin: {
      r: 10,
      t: 25,
      b: 40,
      l: 60
    },
    showlegend: false,
    paper_bgcolor: 'black',
    plot_bgcolor: 'black',
    xaxis: {
      autorange: true,
      domain: [0, 1],
      range: [
        document.getElementById('last').textContent,
        document.getElementById('first').textContent
      ],
      rangeslider: {
        range: [
          document.getElementById('last').textContent,
          document.getElementById('first').textContent
        ]
      },
      title: 'Date',
      type: 'date'
    },
    yaxis: {
      autorange: true,
      domain: [0, 1],
      range: [
        document.getElementById('lowStock').textContent,
        document.getElementById('highStock').textContent
      ],
      type: 'linear'
    }
  }

  Plotly.newPlot('candlestick_stock', data, layout)
})
