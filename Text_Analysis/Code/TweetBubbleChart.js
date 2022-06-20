// !preview r2d3 data = read.csv("./datasets/TweetWordFrequency.csv"), d3_version = 4

// Based on https://bl.ocks.org/mbostock/4063269

// Initialization

// Setting font and background
svg.attr("font-family", "Georgia")
  .attr("text-anchor", "middle")
  .style("fill", "white");
  
// Setting size
var svgSize = 600;

// Color scheme
var color = d3.scaleOrdinal(["#a1d0e4","#9fcee3","#9dcde2","#9bcbe1","#99c9e1",
"#96c8e0","#94c6df","#92c4de","#90c3dd","#8ec1dc","#8cbfdb","#8abeda","#88bcd9",
"#86bad8","#84b8d7","#82b6d6","#7fb5d5","#7db3d4","#7bb1d3","#79afd2","#77add1",
"#75abd0","#73a9cf","#71a7ce","#6fa5cd","#6da3cc","#6ca1cb","#6a9fca","#689dc9",
"#669bc8","#6499c7","#6297c5","#6094c4","#5f92c3","#5d90c2","#5b8ec1","#598cc0",
"#5889bf","#5687be","#5485bc","#5383bb","#5180ba","#507eb9","#4e7cb8","#4d7ab7",
"#4c77b5","#4a75b4","#4973b3","#4870b2","#466eb1","#456cb0","#4469ae","#4367ad",
"#4264ac","#4162ab","#4060aa","#3f5da8","#3e5ba7","#3d58a6","#3c56a5","#3b54a4",
"#3a51a2","#394fa1","#384ca0","#374a9f","#37479e","#36459c","#35429b","#34409a",
"#333d99","#333b97","#323896","#313695"])


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

// Plot was saved using export on RStudio