const state = {
  "received_data": null,
  "previous_data": {
    "current_queue_number": 0
  }
}

function updateQueueNumber(endpoint, interval, DomID, hasCallVoice, audioID) {
  var intervalId = window.setInterval(function () {
    getCurrentQueueNumber(endpoint, audioID)
  }, interval)

  function getCurrentQueueNumber(endpoint, audioID) {
    const xhttp = new XMLHttpRequest()
    xhttp.onload = function () {
      // What to do when the response is ready
      const received_data = JSON.parse(xhttp.responseText)
      state.received_data = received_data

      // update UI
      if (!_.isEqual(received_data, state.previous_data)) {
        updateTargetDOM(DomID)
        if (hasCallVoice) {
          // call ring
          ring(audioID)
          // call customer
          // callCustomer()
        }
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

  function ring(audioID) {
    const targetAudio = document.getElementById(audioID)
    targetAudio.play()
    targetAudio.setAttribute("onended", "callCustomer()")
  }

  
}
function callCustomer() {
  const templateSpeach = "japan visa applicant number"
  let utterance = new SpeechSynthesisUtterance(templateSpeach + state.received_data.current_queue_number)
  speechSynthesis.speak(utterance)
}









