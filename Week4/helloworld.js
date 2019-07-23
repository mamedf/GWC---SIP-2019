var adjectives = ["brave","nice"]
var pos = 0;
var loc = document.getElementsByID('adjective')

function changeadj(){
  loc.innerHTML = adjectives[pos];
  pos ++;
  if (pos >= adjectives.length){
    pos = 0;
  }
}
var x = document.getElementsByTagName('body')[0]
function colorfulbackground
