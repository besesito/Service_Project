const rdata = JSON.parse(data.replace(/&quot;/g, '"'))
const input = document.getElementById('search_field')
let = filtered = []
input.addEventListener('keyup', (e)=> {
    table.innerHTML = ""
    console.log(rdata)
    filtered = rdata.filter(customer=> customer['name'].toLowerCase().includes(e.target.value.toLowerCase()))
    if (filtered.length > 0){
        filtered.map(customer=>{
            if  (customer['phone_number'] == null) {
                customer['phone_number'] = "brak"
            } else {}
            if  (customer['alias'] != null) {
                customer['name'] = customer['alias']
            } else {}
            if  (customer['email'] == null) {
                customer['email'] = "brak"
            } else {}
            table.innerHTML +=`
            <tr>
                <td>
                    <a href="http://127.0.0.1:8000/klienci/${customer['id']}"><img class="icon-size-p" src="/static/img/icons/loupe.png"></a>
                    <a href="http://127.0.0.1:8000/klienci/${customer['id']}/edytuj"><img class="icon-size-p" src="/static/img/icons/pencil.png"></a>
                    <a href="http://127.0.0.1:8000/klienci/${customer['id']}/usun"><img class="icon-size-p" src="/static/img/icons/bin.png"></a>
                </td>
                <td>${customer['name']}</td>
                <td>${customer['phone_number']}</td>
                <td>${customer['email']}</td>
            </tr>
            `
        })
    } else {
        table.innerHTML = "<br/><b>Nie znaleziono...</b>"
    }
})