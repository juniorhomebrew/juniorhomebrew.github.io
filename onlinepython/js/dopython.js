$(document).ready(function () {

  function scrollDown() {                                 // Automatic scroll down to show newest code  (like terminal)
    var height = $('.output')[0].scrollHeight;
    $('.output').scrollTop(height);
  }

  function outf(text) {
    $(".output").append('<pre>' + text + '</pre>');    // Putting text as pre means new line by default
    scrollDown();
  }

  function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined){
      throw "File not found: '" + x + "'";
    }
    return Sk.builtinFiles["files"][x];
  }

  $("#run").click(function() {
    var pyth = $("#yourcode").val();
    var outputwidth = $(".output").width();


    $(".output").html('<div id="mycanvas"></div>');

    Sk.python3 = true;

    Sk.configure({output:outf, read:builtinRead});
    (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'mycanvas';
    Sk.TurtleGraphics.target.width = outputwidth;                               //// FINISHED HERE!!!!

    var myPromise = Sk.misceval.asyncToPromise(function() {
                      return Sk.importMainWithBody("<stdin>", false, pyth, true);
                    });

    myPromise.then(function(mod) {
        console.log('Success');
    },
        function(err) {
        $(".output").append("<pre style ='color: red;'>>> " + err + "</pre>")
        scrollDown();
        console.log(err.toString());
    });
  });

});
