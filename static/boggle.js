//to post the JSON object to server to be fetched by Flask 
async function dup() {
    let data= {"data" : e.target.value }
    let resp = await axios.post('http://127.0.0.1:5000/game', JSON.parse(data))
return resp}
    
function add(){
    let bttn= document.getElementById('enter')
    console.log(bttn)
    bttn.addEventListener('click', function(e) {e.preventDefault(); 
    let lis=document.createElement('li')
    lis.append(e.target.value)
    })}

dup()
add()
