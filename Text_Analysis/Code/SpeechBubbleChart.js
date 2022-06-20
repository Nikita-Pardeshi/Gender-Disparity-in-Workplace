// !preview r2d3 data = read.csv("./datasets/SpeechWordFrequency.csv"), d3_version = 4

// Based on https://bl.ocks.org/mbostock/4063269

// Initialization

// Setting font and background
svg.attr("font-family", 'Georgia')
  .attr("text-anchor", "middle")
  .style("fill", "white");
  
// Setting size
var svgSize = 600;

// Color scheme
var color = d3.scaleOrdinal(["#cb2729","#cc2929","#ce2b2a","#d02d2a","#d12f2b",
"#d3312b","#d4332c","#d6352c","#d7382d","#d93a2e","#da3c2e","#dc3e2f","#dd4030",
"#de4331","#e04532","#e14733","#e24a33","#e34c34","#e44e35","#e55136","#e75337",
"#e85538","#e95839","#ea5a3a","#eb5d3c","#ec5f3d","#ed613e","#ed643f","#ee6640",
"#ef6941","#f06b42","#f16e43","#f17044","#f27346","#f37547","#f37848","#f47a49",
"#f57d4a","#f57f4b","#f6824d","#f6844e","#f7864f","#f78950","#f88b51","#f88e53",
"#f89054","#f99355","#f99557","#f99858","#fa9a59","#fa9c5b","#fa9f5c","#fba15d",
"#fba35f","#fba660","#fba862","#fcaa63","#fcad65","#fcaf66","#fcb168","#fcb369",
"#fcb56b","#fdb86d","#fdba6e","#fdbc70","#fdbe72","#fdc073","#fdc275","#fdc477",
"#fdc678","#fdc87a","#fdca7c","#fecc7e","#fecd80","#fecf81","#fed183","#fed385",
"#fed587","#fed689","#fed88a","#feda8c","#fedb8e","#fedd90","#fede92","#fee094",
"#fee196","#fee397","#fee499","#fee69b","#fee79d","#fee89f","#feeaa1","#feeba3",
"#feeca4","#feeda6","#feeea8","#fef0aa","#fef1ac","#fdf2ae","#fdf2b0","#fdf3b2",
"#fdf4b4","#fcf5b6","#fcf6b8","#fbf6ba","#fbf7bc","#faf7be","#faf8c0","#f9f8c2",
"#f9f8c4","#f8f9c6","#f7f9c8","#f7f9ca","#f6f9cc","#f5f9ce","#f4f9d0","#f3f9d2",
"#f2f9d4","#f1f8d6","#f0f8d8","#eff8da","#edf8dc","#ecf7dd"])


var pack = d3.pack()
  .size([svgSize, svgSize])
  .padding(1.5);
    
var format = d3.format(",d");

var group = svg.append("g");

// Resize
r2d3.onResize(function(width, height) {
  var minSize = Math.min(width, height);
  var scale = minSize / svgSize;
  
  group.attr("transform", function(d) {
    return "" +
      "translate(" + (width - minSize) / 2 + "," + (height - minSize) / 2 + ")," +
      "scale(" + scale + "," + scale + ")";
  });
});

// Rendering
r2d3.onRender(function(data, svg, width, height, options) {
  var root = d3.hierarchy({children: data})
    .sum(function(d) { return d.value; })
    .each(function(d) {
      if (id = d.data.id) {
        var id, i = id.lastIndexOf(".");
        d.id = id;
        d.package = id.slice(0, i);
        d.class = id.slice(i + 1);
      }
    });

 var node = group.selectAll(".node")
		.data(pack(root).leaves())
		.enter().append("g")
			.attr("class", "node")
			.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
			
  node.append("circle")
			.attr("id", function(d) { return d.id; })
			.attr("r", function(d) { return d.r; })
			.style("fill", function(d) { return color(d.id); });


  node.append("clipPath")
      .attr("id", function(d) { return "clip-" + d.id; })
    .append("use")
      .attr("xlink:href", function(d) { return "#" + d.id; });
      
node.append("text")
			.attr("clip-path", function(d) { return "url(#clip-" + d.id + ")"; })
		.append("tspan")
			.attr("x", 0)
			.attr("y", function(d) { return d.r/8; })
			.attr("font-size", function(d) { return d.r/2; })
			.text(function(d) { return d.id; });
  node.append("title")
      .text(function(d) { return d.id + "\n" + format(d.value); });
  r2d3.resize(width, height);
});

 