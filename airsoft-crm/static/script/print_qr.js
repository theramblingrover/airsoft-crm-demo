<script>
  window.onload = function () {
    var printBut = document.getElementById('printBut');
    printBut.onclick = function () {
      var win = window.open();
      win.document.write('<img src={% url "players:get_qr" player.id %}>');
      win.print();
      win.close()
    }
  }
</script>