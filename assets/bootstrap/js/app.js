Dropzone.options.myUpload = {
  init: function() {

    this.on("queuecomplete", function(file) {
      alert("All files have uploaded");
    });

    this.on("complete", function(file) {
      alert("Its complete");
    });

}};
