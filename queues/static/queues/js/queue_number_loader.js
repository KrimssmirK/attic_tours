const state = {
  "received_data": null,
  "previous_data": null
}

function updateQueueNumber(endpoint, interval, DomID) {
  var intervalId = window.setInterval(function () {
    getCurrentQueueNumber(endpoint)
  }, interval)

  function getCurrentQueueNumber(endpoint) {
    const xhttp = new XMLHttpRequest()
    xhttp.onload = function () {
      // What to do when the response is ready
      const received_data = JSON.parse(xhttp.responseText)
      state.received_data = received_data
  
      // update UI
      if (!_.isEqual(received_data, state.previous_data)) {
        updateTargetDOM(DomID)
        callCustomer()
      }
      state.previous_data = received_data
    }
    xhttp.open('GET', endpoint)
    xhttp.send()
  }

  function updateTargetDOM(DomID) {
    const targetDOM = document.getElementById(DomID)
    targetDOM.innerText = state.received_data.current_queue_number
  }

  function callCustomer() {
    const templateSpeach = "japan visa applicant number"
    let utterance = new SpeechSynthesisUtterance(templateSpeach + state.received_data.current_queue_number)
    speechSynthesis.speak(utterance)
  }
}










