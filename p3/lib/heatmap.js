

const heatmapChart = function(data) {
  const margin = { top: 50, right: 0, bottom: 100, left: 120 },
    width = 960 - margin.left - margin.right,
    height = 430 - margin.top - margin.bottom,
    gridSize = Math.floor(width / 24),
    legendElementWidth = gridSize*2,
    buckets = 9,
    colors = ["#ffffd9","#edf8b1","#c7e9b4","#7fcdbb","#41b6c4","#1d91c0","#225ea8","#253494","#081d58"], // alternatively colorbrewer.YlGnBu[9]
    days = ["Primary", "Secondary", "Some Secondary", "Some College", "Some Graduate", "College", "Graduate"],
    times = ["16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"];


  const svg = d3.select("#rightFly")
      .append("svg")
      .attr("width", "90%")
      .attr("height", "90%")
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  const dayLabels = svg.selectAll(".dayLabel")
      .data(days)
      .enter().append("text")
        .text(function (d) { return d; })
        .attr("x", 0)
        .attr("y", (d, i) => i * gridSize)
        .style("text-anchor", "end")
        .attr("transform", "translate(-6," + gridSize / 1.5 + ")")
        .attr("class", (d, i) => ((i >= 0 && i <= 4) ? "dayLabel mono axis axis-workweek" : "dayLabel mono axis"));

  const timeLabels = svg.selectAll(".timeLabel")
      .data(times)
      .enter().append("text")
        .text((d) => d)
        .attr("x", (d, i) => i * gridSize)
        .attr("y", 0)
        .style("text-anchor", "middle")
        .attr("transform", "translate(" + gridSize / 2 + ", -6)")
        .attr("class", (d, i) => ((i >= 7 && i <= 16) ? "timeLabel mono axis axis-worktime" : "timeLabel mono axis"));

  const colorScale = d3.scaleQuantile()
    .domain([0, buckets - 1, d3.max(data, (d) => d.value)])
    .range(colors);

  const cards = svg.selectAll(".hour")
      .data(data, (d) => d.day+':'+d.hour);

  cards.append("title");

  cards.enter().append("rect")
      .attr("x", (d) => (d.hour - 1) * gridSize)
      .attr("y", (d) => (d.day - 1) * gridSize)
      .attr("rx", 4)
      .attr("ry", 4)
      .attr("class", "hour bordered")
      .attr("width", gridSize)
      .attr("height", gridSize)
      .style("fill", colors[0])
    .merge(cards)
      .transition()
      .duration(1000)
      .style("fill", (d) => colorScale(d.value));

  cards.select("title").text((d) => d.value);

  cards.exit().remove();

  const legend = svg.selectAll(".legend")
      .data([0].concat(colorScale.quantiles()), (d) => d);

  const legend_g = legend.enter().append("g")
      .attr("class", "legend");

  legend_g.append("rect")
    .attr("x", (d, i) => legendElementWidth * i)
    .attr("y", height)
    .attr("width", legendElementWidth)
    .attr("height", gridSize / 2)
    .style("fill", (d, i) => colors[i]);

  legend_g.append("text")
    .attr("class", "mono")
    .text((d) => "≥ " + Math.round(d))
    .attr("x", (d, i) => legendElementWidth * i)
    .attr("y", height + gridSize);

  legend.exit().remove();
};

//heatmapChart(datasets[0]);
