const input = document.getElementById('search_field')
let = filtered = []
input.addEventListener('keyup', (e)=> {
table.innerHTML = ""
filtered = data.filter(service => service['fields']['customer'].toLowerCase().includes(e.target.value.toLowerCase()))
if (filtered.length > 0){
    filtered.map(service=>{
        if  (service['fields']['date'] == null) {
            service['fields']['date'] = "do ustalenia"
        } else {}
        table.innerHTML +=`
        <tr>                
            <td>
                <a href="http://127.0.0.1:8000/uslugi/${service['pk']}"><img class="icon-size-p"
                                                                        src="/static/img/icons/loupe.png"></a>
                <a href="http://127.0.0.1:8000/uslugi/${service['pk']}/edytuj"><img class="icon-size-p"
                                                                        src="/static/img/icons/pencil.png"></a>
                <a href="http://127.0.0.1:8000/uslugi/${service['pk']}/usun"><img class="icon-size-p"
                                                                        src="/static/img/icons/bin.png"></a>
            </td>
            <td>
                ${service['fields']['customer']}
            </td>
            <td>
                ${service['fields']['date']}
            </td>
            <td>
                ${service['fields']['kind']}
            </td>
            <td>
                ${service['fields']['status']}
            </td>

        </tr>
        `
    })
} else {
    table.innerHTML = "<br/><b>Nie znaleziono...</b>"
    }
})