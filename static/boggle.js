
async function dup() {
    let data= {"data" : e.target.value }
    let resp = await axios.post('http://127.0.0.1:5000/game', JSON.parse(data))
    console.log(resp)

    let bttn= document.getElementsByTagName('button')
    console.log(bttn)
    bttn.addEventListener('click', function(e){e.preventDefault(); 
    let uls= document.querySelector('ul')
    let lis=document.createElement('li')
    console.log("hello")
    uls.appendChild(lis)
    lis.append(e.target.value)
    console.log(e.target.value)
    })}
dup()