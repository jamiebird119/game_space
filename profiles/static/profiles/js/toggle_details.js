
function toggleDetails(id){
    var x = document.getElementById(id)
    var button_id = `button_${id}`
    var a = document.getElementById(button_id)
    x.classList.toggle("d-none");
    if(x.classList.contains("d-none")){
        a.innerHTML = `View details <i class="fas fa-arrow-down">`
    }else{
        a.innerHTML = `Close details <i class="fas fa-arrow-up">`
    }
  }