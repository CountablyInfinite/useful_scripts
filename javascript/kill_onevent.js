javascript: (function() {
  
    var onevents = ["paste", "copy"],
        Z = [],
        s = "",
        j;

    function disable_onevents(doc, a) {
      	while (doc[a]) {
            Z[a] = Z[a] ? Z[a] + 1 : 1;
            N[a] = null;
        }
    }

    function iterate_onevents(doc) {
        var i, C;
        for (an_event in onevents) disable_onevents(doc, "on" + onevents[an_event]);
        C = doc.childNodes;
        for (i = 0; i < C.length; ++i) iterate_onevents(C[i]);
    }
  
    iterate_onevents(document);
    for (j in Z) s += j + " (" + Z[j] + ")\n";
    if (s) alert("Disabled onevent:\n\n" + s);
    else alert("No onevents found.");
})();