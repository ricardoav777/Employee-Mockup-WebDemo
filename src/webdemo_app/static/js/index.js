const
  table = document.getElementById("employeeTable"),
  checkboxes = table.querySelectorAll('input[type="checkbox"]') ,
  deleteBtn = document.getElementById("multipleDelete");

deleteBtn.addEventListener("click", multipleDelete);

function multipleDelete(event){
    var checked = []

    for (const checkbox of checkboxes){
        if (checkbox.checked) {
            checked.push(checkbox.value);
        }
    }
    if(checked.length === 0) {
     alert("Seleccione al menos un empleado")
    }
    else{
        checked_array = JSON.stringify(checked)

        $.ajax({
            type: 'POST',
            url: multiple_delete_url,
            headers: {
                'Accept': 'application/json',
                'X-CSRFToken': csrftoken,
            },
                data: {checked_array},
                error: function (response) {
                    alert('Hubo un error, no se pudieron borrar las personas seleccionadas');
                },
                success: function (response) {
                    console.log("llegue")
                    $("#employeeTable tr").remove();
                    var table_obj = []
                    response.employees.forEach(el => {
                        table_tr =
                        `<tr>
                            <td input="checkbox"> value= ${el.pk}</td>
                            <td> ${el.first_name} ${el.last_name} </td>
                            <td> ${el.email} </td>
                            <td> ${el.email} </td>
                            <td>
                            <a class="link" type="button" data-toggle="tooltip" data-placement="top" title="Editar" href="{% url 'employee-update'pk="+${el.pk}+" %}">
                                <i class="fa-solid fa-user-pen" ></i>
                            </a>
                            <a class="link" type="button" data-toggle="tooltip" data-placement="top" title="Borrar" href="{% url 'employee-delete'pk=" +${el.pk}+" %}">
                                <i class="fa-solid fa-trash"></i>
                            </a>
            </td>
                        </tr>`
                        table_obj.push(table_tr)
                        })
                    $("#employeeTable").append(table_obj)
                }})
        }
    }