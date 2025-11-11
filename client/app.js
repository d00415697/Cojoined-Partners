console.log("connected")


let editID = null

const message_div = document.querySelector("#message_reviews")

function load(){
    message_div.innerHTML = ""

    fetch(`/messages`)
        .then(function(response){
            response.json()
                .then(function(data){
                    console.log(data)
                    data.forEach(message => load_message(message))
                }) 
        })
}



function load_message(message){
    let div = document.createElement("article")
    let h3 = document.createElement("h3")
    let p = document.createElement("p")
    let p2 = document.createElement("p")

    h3.textContent = message.name
    p.textContent = "Description: " + message.description;
    p2.textContent = "Age: " + message.age + " | Rank: " + message.rank + " | Kills: " + message.kills
    
    let delButton = document.createElement("button")
    delButton.innerHTML = "&times;"
    delButton.classList.add("delete-btn")
    delButton.onclick = function() { delete_message(message.id)}
    const art = document.createElement("article")
    art.classList.add("message-card")


    let editButton = document.createElement("button")
    editButton.textContent = "Edit"
    editButton.classList.add("edit-btn")
    editButton.onclick = function() { do_edit(message) }

    div.append(h3, p, p2, editButton, delButton)
    message_div.append(div)

}

function addNewmessage(){
    let name = document.querySelector('#message_input_name').value
    let description = document.querySelector('#message_input_description').value
    
    let age = document.querySelector('#message_input_age').value
    let kills = document.querySelector('#message_input_kills').value
    
    let rankEl = document.querySelector('input[name="rank"]:checked')
    let rank = rankEl ? rankEl.value : ""

    console.log("Submitting:", {name, description, rank})

    // send to api

    let data = "name="+encodeURIComponent(name)
    data += "&description="+encodeURIComponent(description)
    data += "&age="+encodeURIComponent(age)
    data += "&rank="+encodeURIComponent(rank)
    data += "&kills="+encodeURIComponent(kills) 
    console.log(data)

    let submit_method = "POST"
    const button_text = document.querySelector("#message_submit_button").innerHTML
    let url = "/messages"
    if (button_text == "SAVE"){
        submit_method = "PUT"
        url = "/messages/"+ editID
    }

    fetch(url, {
        method: submit_method,
        body: data,
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    })
    .then(function (response){
            if(response.status === 201){
                console.log("Saved")
                document.querySelector("#message_form").reset()
                load()
            } else{
                console.error("Failed to save message:", response.status)
            }
        })
        .catch(function (err){
            console.error("Error saving message", err)
        })
}

function delete_message(id){
    console.log("Deleting Predator: ", id)
    fetch(`/messages/${id}`, { method: "DELETE" })

        .then(function(response){
            if(response.status === 200){
                console.log("Predator Eliminated")
                load()
            } else if (response.status === 404){
                console.warn("Predator not found")
            } else{
                console.error("Failed to Eliminate:", response.status)
            }
        })
        .catch(function(err){
            console.error("Error deleting Predator", err)
        })
}

let button = document.querySelector("#message_submit_button")
button.onclick = addNewmessage
load()

function reset_form() {
    document.querySelector('#message_input_name').value = ""
    document.querySelector('#message_input_description').value = ""
    document.querySelector('#message_input_age').value = ""
    document.querySelector('#message_input_kills').value = ""

    // Uncheck rank radios
    document.querySelectorAll('input[name="rank"]').forEach(r => r.checked = false)

    // Reset button and edit state
    const btn = document.querySelector('#message_submit_button')
    btn.innerHTML = "Submit Message"
    editID = null
}

function do_edit(message){
    console.log("You are going to edit messages:", message.id)
    document.querySelector('#message_input_name').value = message.name
    document.querySelector('#message_input_description').value = message.description
    document.querySelector('#message_input_age').value = message.age
    document.querySelector('#message_input_kills').value = message.kills
    let rankEl = document.querySelector(`input[name="rank"][value="${message.rank}"]`)
    if(rankEl){
        rankEl.checked = true
    }
    document.querySelector('#message_submit_button').innerHTML = "SAVE"
    editID = message.id
}

// create a delete button to delete. we need an eventhandler to wait for the user to click on the button.

// delButton.innerhtml = "del"
// delButton.onclick = function(){
        // do_delete = (messages.id)
// }

// function do_delete(id){
//     console.log("You are deleting messages: ", id)
//      fetch("http://localhost:5000/messages/"+id, )
//         .then(function(response){
//             response.json()
//                 .then(function(data){
//                     console.log(data)
//                     data.forEach(message => load_message(message))
//                 }) 
//         })
// }
// console.log("You're deleting this messages: ")
// we're not importing cors library

// fetch("http://localhost:5000/messages", {
    //     method: "POST",
    //     body: data,
    //     headers: {
    //         "Content-Type": "application/x-www-form-urlencoded"
    //     }
    // })