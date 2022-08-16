$(document).ready(function(){
  get_star_info();
})

function get_star_info(){
  $.ajax({
    type: "GET",
    url: "/star",
    data: {},
    success: function(res) {
      // console.log(res.data[0].image)
      create_card(res);
    },
    error: function(res) {
      console.log(res)
    }
  })
}

function like(id){
  $.ajax({
    type: "POST",
    url: "/star",
    data:{
      "id" : id
    },
    success: function(res){
      console.log(res)
      window.location.reload();
    }
  })
}
function delete_card(){
  alert("delete")
}

function create_card(res){
  for(i = 0; i < res.data.length; i++){
    console.log(res)
    card = `
      <div>
        <div class="col">
          <div class="card">
            <img src="${res.data[i].image}" class="card-img-top" alt="${res.data[i].name}_photo">
            <span> 인기순위 ${i+1}번째 </span>
            <div class="card-body">
              <h5 class="card-title">${res.data[i].name} (좋아요: ${res.data[i].like})</h5>
              <footer>
                <a href="#" class="card-text" onclick="like(${res.data[i].id})">좋아요</a>
                <a href="#" class="card-text" onclick="delete_card()">삭제</a>
              </footer>
            </div>
          </div>
        </div>
      </div>
      `
    $(".profile").append(card)
  }
}